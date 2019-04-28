# !/usr/bin/env python
# coding:utf-8

import hashlib
import json
import math
import random
import re
import time

import pyqrcode
import requests


def bytes_decode(b):
    """
    " Python3 bytes解码为str
    " Github@Chyroc
    """
    if isinstance(b, dict):
        dict_new = dict()
        for k, v in b.items():
            dict_new[bytes_decode(k)] = bytes_decode(v)
        return dict_new
    elif isinstance(b, list):
        list_new = list()
        for b_single in b:
            list_new.append(bytes_decode(b_single))
        return list_new
    elif isinstance(b, bytes):
        return b.decode()
    else:
        return b


class WxBot:

    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        self.app_id = 'wx782c26e4c19acffb'
        self.time_out = 30
        self.lang = 'zh_CN'
        self.uuid = ''
        self.conf = {'qr': 'png'}  # tty
        self.s_key = ''
        self.device_id = 'e' + repr(random.random())[2:17]  # 设备ID,以e开头加上一串15位随机数
        self.wei_xin_sid = ''
        self.pass_ticket = ''
        self.wei_xin_uin = 0
        self.base_url = ''
        self.user = {}  # 个人账号信息
        self.sync_key_dic = {}
        self.sync_key_str = ''
        self.base_request = {}
        self.s = requests.Session()
        self.friends = {}
        self.special_user = {
            'filehelper',  # 文件助手
            'weixin',  # 微信团队
        }

    '''
    ' 获取uuid
    '''

    def _get_uid(self):
        now = int(time.time() * 1000)
        url = 'https://login.wx.qq.com/jslogin?appid=%s&fun=new&lang=%s&_=%s' % \
              (self.app_id, self.lang, now)
        uid_info = requests.get(url)
        if uid_info.status_code == 200:
            uid_detail = re.match(r'window.QRLogin.code = (.*); window.QRLogin.uuid = "(.*)";', uid_info.text, re.M | re.I)
            if uid_detail.group(1) == '200':
                self.uuid = str(uid_detail.group(2))
                return True
            return False
        return False

    '''
    ' 获取随机数
    '''

    @staticmethod
    def _get_rand_num(length=10):
        if length <= 15:
            end = 2 + length
            return int(repr(random.random())[2:end])
        else:
            num = ''
            loop_times = math.floor(length / 15)
            need_more = length % 15
            for k in range(loop_times):
                num += repr(random.random())[2:17]
            end = 2 + need_more
            num += repr(random.random())[2:end]
            return int(num)

    '''
    ' 处理通讯秘钥
    '''

    def _get_sync_key_str(self):
        self.sync_key_str = ''
        for element in self.sync_key_dic['List']:
            self.sync_key_str = self.sync_key_str + str(element['Key']) + '_' + str(element['Val']) + '|'
        self.sync_key_str = self.sync_key_str[:-1]

    def _get(self, url, json_format=True):
        headers = {
            'User-Agent': self.user_agent,
            'ContentType': 'application/json; charset=UTF-8'
        }
        dic_obj = self.s.get(url, headers=headers, timeout=self.time_out, stream=False)
        dic_obj.encoding = 'utf-8'
        if json_format:
            return dic_obj.json()
        return dic_obj

    def _post(self, url, data, json_format=True):
        headers = {
            'User-Agent': self.user_agent,
            'ContentType': 'application/json; charset=UTF-8'
        }
        dic_obj = self.s.post(url, data=data, headers=headers)
        dic_obj.encoding = 'utf-8'
        if json_format:
            return dic_obj.json()
        return dic_obj

    '''
    ' 获取二维码
    ' TODO:支持二维码图片输出
    '''

    def _get_qr(self):
        url = 'https://login.weixin.qq.com/l/' + self.uuid
        qr = pyqrcode.create(url)
        if self.conf['qr'] == 'png':
            qr.png('qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        elif self.conf['qr'] == 'tty':
            print(qr.terminal(quiet_zone=1))

    '''
    ' 初始化微信
    ' 关键数据点 SyncKey、User
    '''

    def _init_wx(self):
        init_url = self.base_url + '/webwxinit?r=%i&pass_ticket=%s' % \
                                   (self._get_rand_num(), self.pass_ticket)
        params = {
            'BaseRequest': self.base_request
        }
        dic = self._post(init_url, json.dumps(params))
        self.user = dic['User']
        self.sync_key_dic = dic['SyncKey']
        self._get_sync_key_str()

    '''
    ' 开启微信状态通知
    '''

    def _status_notify(self):
        url = self.base_url + '/webwxstatusnotify?lang=' + self.lang + 'pass_ticket=' + self.pass_ticket
        param = {
            'BaseRequest': self.base_request,
            'Code': 3,
            "FromUserName": self.user['UserName'],
            "ToUserName": self.user['UserName'],
            "ClientMsgId": self._get_rand_num()
        }
        dic = self._post(url, json.dumps(param))
        if dic['BaseResponse']['Ret'] != 0:
            print("[*] 开启状态通知失败")
            exit()

    '''
    ' 获取好友列表
    '''

    def _wx_contact(self):
        url = self.base_url + '/webwxgetcontact?pass_ticket=%s&r=%i&skey=%s' % \
                              (self.pass_ticket, self._get_rand_num(), self.s_key)
        dic = self._get(url)
        if dic['BaseResponse']['Ret'] == 0:
            for member in dic['MemberList']:
                if member['UserName'][0] == '@' and member['UserName'][1] != '@':
                    self.friends[member['UserName']] = member['NickName']
        else:
            print('[*] 获取好友列表失败,错误代码:%i' % dic['BaseResponse']['Ret'])

    '''
    ' 等待用户扫码,已经用户确认登录后的相关操作
    ' 关键数据点 Sid、Skey、Uin
    '''

    def _wait_login(self):
        now = int(time.time() * 1000)
        k = 0
        while True:
            if k >= 10:
                print('[*] 二维码已经过期')
                break
            timestamp = now + k
            tip = '1'
            if k != 0:
                tip = '0'
            url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=%s&r=%s&_=%s' % \
                  (self.uuid, tip, self._get_rand_num(), timestamp)
            try:
                user_status = self._get(url, False)
            except Exception as e:
                print(e)
                continue
            login_detail = re.search(r'window.code=(\d+?);', user_status.text)
            if login_detail:
                if login_detail.group(1) == '408':
                    k += 1
                    print('[*] 系统正在等待你扫码....')
                elif login_detail.group(1) == '201':
                    k += 1
                    time.sleep(1)
                    print('[*] 请在手机上确认登录')
                elif login_detail.group(1) == '200':
                    new_url_info = re.search(r'window.redirect_uri="(\S+?)";', user_status.text)
                    new_url = new_url_info.group(1) + '&fun=new&version=v2'
                    self.base_url = new_url_info.group(1)[:new_url_info.group(1).rfind('/')]
                    important_info = self._get(new_url, False).text
                    self.wei_xin_sid = str(re.search(r'<wxsid>(\S+?)</wxsid>', important_info).group(1))
                    self.s_key = str(re.search(r'<skey>(\S+?)</skey>', important_info).group(1))
                    self.wei_xin_uin = int(re.search(r'<wxuin>(\S+?)</wxuin>', important_info).group(1))
                    self.pass_ticket = str(re.search(r'<pass_ticket>(\S+?)</pass_ticket>', important_info).group(1))
                    description = \
                        '======Login Success======\n'\
                        '[#] Web WeiXin\n'\
                        '[#] Uuid: %s\n'\
                        '[#] Uin: %i\n'\
                        '[#] DeviceID: %s\n'\
                        '[#] Sid: %s\n'\
                        '[#] s_key: %s\n'\
                        '[#] PassTicket: %s\n'\
                        '=========================' % \
                        (self.uuid, self.wei_xin_uin, self.device_id, self.wei_xin_sid, self.s_key, self.pass_ticket)
                    print(description)
                    self.base_request = {
                        'DeviceID': self.device_id,
                        'Sid': self.wei_xin_sid,
                        'Skey': self.s_key,
                        'Uin:': self.wei_xin_uin
                    }
                    break
            else:
                print('[*] 接口异常,系统正在尝试重新链接,请稍后...')
                time.sleep(3)

    '''
    ' 消息检测接口请求
    '''

    def _sync_check(self):
        now = int(time.time() * 1000)
        pre_url = 'https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin'
        url = pre_url + '/synccheck?r=%i&skey=%s&sid=%s&uin=%i&deviceid=%s&synckey=%s&_=%i' % \
                        (self._get_rand_num(), self.s_key, self.wei_xin_sid, self.wei_xin_uin, self.device_id, self.sync_key_str, now)
        try:
            res_str = self._get(url, False).text
        except Exception as e:
            print(e)
            return [-99999, 0]
        sync_status = re.search(r'retcode:"(\d+)",selector:"(\d+)"', res_str)
        return [sync_status.group(1), sync_status.group(2)]
        
    '''
    ' 消息获取接口请求
    '''

    def _wechat_sync(self):
        get_msg_url = self.base_url + '/webwxsync?sid=%s&skey=%s&pass_ticket=%s&lang=%s' % \
                                      (self.wei_xin_sid, self.s_key, self.pass_ticket, self.lang)
        params = {
            'BaseRequest': self.base_request,
            'SyncKey': self.sync_key_dic,
            'rr': self._get_rand_num()
        }
        dic = self._post(get_msg_url, json.dumps(params))
        if dic['BaseResponse']['Ret'] == 0:
            self.sync_key_dic = dic['SyncKey']
            self._get_sync_key_str()
            return dic
        else:
            print('[*] SyncKey获取失败,可能是因为上一个SyncKey过期引起的!')
            return dic

    '''
    ' 发送消息
    '''

    def _send_message(self, info, i):
        url = self.base_url + '/webwxsendmsg?pass_ticket=' + self.pass_ticket
        only_id = repr(int(time.time())) + repr(self._get_rand_num(7))
        params = {
            'BaseRequest': self.base_request,
            'Msg': {
                'Type': 1,
                'Content': info,
                'FromUserName': i['ToUserName'],
                'ToUserName': i['FromUserName'],
                'LocalID': only_id,
                'ClientMsgId': only_id,
            },
            'Scene': 0
        }
        dic = self._post(url, json.dumps(bytes_decode(params), ensure_ascii=False).encode('utf8'))
        if dic['BaseResponse']['Ret'] == 0:
            print('[-] AI 说: %s [成功]' % info)
        self._wechat_sync()

    '''
    ' 消息截取并处理
    '''

    def _handle_massage(self, i):
        if i['MsgType'] == 1:
            print('[-] %s 说: %s' % (self.friends[i['FromUserName']], i['Content']))
            ai_url = 'http://op.juhe.cn/robot/index?info=%s&userid=%s&key=823a6cc1a3326fc2cea530dbadc34a27' % \
                     (i['Content'], hashlib.md5(i['FromUserName'].encode('utf-8')).hexdigest())
            dic = requests.get(ai_url).json()
            self._send_message(dic['result']['text'], i)
        elif i['MsgType'] == 51:
            print('[*] 初始化微信聊天系统成功，等待消息输入！')
        else:
            print('[*] 目前只支持文本消息,其他消息类型暂未支持!')

    '''
    ' 消息监听
    '''

    def _listen_message(self):
        print('[*] 开启消息监听...')
        count = 1
        while True:
            [code, selector] = self._sync_check()
            if code == '0':
                count = 1
                if selector == '0':
                    print('[*] 等待消息...')
                elif selector == '2':
                    r = self._wechat_sync()
                    if r['BaseResponse']['Ret'] == 0 and len(r['AddMsgList']):
                        for i in r['AddMsgList']:
                            self._handle_massage(i)
                    time.sleep(1)
                elif selector == '7':
                    print('[*] 聊天室状态发生改变,可能是你在手机上操作了')
                else:
                    print("[*] 未知消息状态码:%s" % selector)
            elif code == '1100':
                print('[*] 你登出了 WEB 版微信，再见')
                exit()
            elif code == '1101':
                print('[*] 你在其他地方登录了 WEB 版微信，再见')
                exit()
            elif code == -99999:
                time.sleep(count * 3)
                count += 1
            else:
                count += 1
                print("[*] 未知状态码:%s" % code)

    def run(self):
        print("[*] 微信机器人开启...")
        print("[*] 正在获取UUID...")
        get_uid_result = self._get_uid()
        if get_uid_result:
            print("[*] 请扫描下方的二维码")
            self._get_qr()
            self._wait_login()
            self._init_wx()
            self._status_notify()
            self._wx_contact()
            self._listen_message()
        else:
            print('[*] 获取UUID失败')
            exit()


myWxBot = WxBot()
myWxBot.run()

