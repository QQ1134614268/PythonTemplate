# -*- coding:utf-8 -*-
"""
@Time: 2022/8/11
@Description:
"""
import json
from os import path

import yaml

from conf.config import DATA_DIR
from conf.json_config import MyJsonEncoder


def get_data_dir(file_path):
    return path.join(DATA_DIR, file_path)


class JsonFileUtil:
    @staticmethod
    def to_file(data, file_path):
        content = json.dumps(data, ensure_ascii=False, cls=MyJsonEncoder, indent=2)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write(content)

    @staticmethod
    def to_dict(file_path):
        return json.load(file_path)


class YamlFileUtil:

    @staticmethod
    def to_file(dict_value, save_path):
        """dict保存为yaml"""
        with open(save_path, mode='w', encoding="utf-8") as file:
            file.write(yaml.dump(dict_value, allow_unicode=True))

    @staticmethod
    def to_dict(yaml_path):
        with open(yaml_path) as file:
            dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
            return dict_value


class PropFileUtil:
    # TODO 暂不支持list
    @staticmethod
    def to_file(data: dict, file_path):
        ret_list = PropFileUtil.__dict_to_prop(data)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write("\n".join(ret_list))

    @staticmethod
    def to_dict(file_path):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        new_list = []
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() != "":
                new_list.append(line)
        root = {}
        for line in new_list:
            pos_num = line.find("=")
            arr = line[:pos_num].split(".")
            curr = root
            # 模拟文件夹, 根据路径,从根目录开始, 切换当前目录. 不存在时就创建
            for index, name in enumerate(arr):
                if index == len(arr) - 1:
                    curr[name] = line[pos_num + 1:]
                else:
                    curr = root.setdefault(name, {})
        return root

    @staticmethod
    def __dict_to_prop(data: dict, full_path="", ret=None) -> list:
        if ret is None:
            ret = []
        if full_path:
            full_path += "."
        #  todo 优化 拼接 .
        for k, v in data.items():
            if isinstance(v, dict):
                PropFileUtil.__dict_to_prop(v, f"{full_path}{k}", ret)
            else:
                ret.append(f"{full_path}{k}={v}")
        return ret


class XmindFileUtil:
    # 只有值, 类似xmind, 目录结构
    @staticmethod
    def to_file(data, file_path, key):
        ret_list = XmindFileUtil._handel_data(data, key=key)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write("\n".join(ret_list))

    @staticmethod
    def _handel_data(data_list, level=0, ret=None, key="value"):
        if ret is None:
            ret = []
        if isinstance(data_list, dict):
            data_list = [data_list]

        for dic in data_list:
            line = level * "  " + dic.get(key)
            ret.append(line)
            if dic.get("children"):
                XmindFileUtil._handel_data(dic.get("children"), level + 1, ret, key=key)
        return ret

    @staticmethod
    def to_dict(file_path):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        vos = []
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() != "":
                vos.append({
                    "value": line.lstrip(),
                    "space": len(line) - len(line.lstrip()),
                    "children": []
                })
        root = list(filter(lambda x: x.get("space") == 0, vos))
        for i in range(len(vos) - 1, -1, -1):
            vo = vos[i]
            for j in range(i - 1, -1, -1):
                vo2 = vos[j]
                if vo.get("space") > vo2.get("space"):
                    vo2.get("children").insert(0, vo)
                    break

        return root
