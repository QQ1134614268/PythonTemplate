import os
import re
import shutil
from unittest import TestCase

import requests


class TestNginx(TestCase):
    nginx_dir = 'D:/dev/nginx-1.17.7'
    root = os.path.join(nginx_dir, 'html')
    host = 'http://localhost:20080/proxy'
    dirs_list = ['dir1', 'dir2', 'dir3']
    file_list = ['index.html', 'index.txt']
    conf_path = os.path.join(nginx_dir, 'conf/test.conf')

    def test_init_file(self):
        """dir1 有文件, dir2 空, dir3 不存在"""
        # 创建dir
        if os.path.exists(self.root):
            shutil.rmtree(self.root)
        for level1 in self.dirs_list[:2]:
            path = os.path.join(self.root, level1)
            if not os.path.exists(path):
                os.makedirs(path)

        # 遍历dir 写入文件
        for root_dir, dirs, files in os.walk(self.root):
            if self.root == root_dir or root_dir.endswith(self.dirs_list[0]):
                for level2 in self.file_list:
                    file_path = os.path.join(root_dir, level2)
                    with open(file_path, encoding='utf-8', mode='w') as f:
                        f.write(file_path)
            # print('root:', root_dir)
            # print('dirs:', dirs)
            # print('files', files)

    def test_nginx_index(self):
        path_list = self.get_uri()

        index_files = ['/index.txt', 'index.txt']
        for index in index_files:
            proxy = '/proxy'
            tpl = f'server {{ listen 20080; location {proxy} {{ alias html; index {index}; }} }}'
            with open(self.conf_path, encoding='utf-8', mode='w') as f:
                f.write(tpl)
            os.system(f'D: && cd {self.nginx_dir} && nginx -s reload')
            #  # 访问文件, 目录; 返回结果一样,推测nginx先查文件,如果是目录,走index逻辑
            for path in path_list:
                url = f'{self.host}{path}'
                res = requests.get(url)
                print(index, url,
                      res.text.replace(self.root, '').replace("\\", '/') if res.status_code == 200 else res.status_code)

    def get_uri(self):
        path_list = []
        for l in ['', '/']:
            path_list.append(f'{l}')
            for d in self.dirs_list:
                path_list.append(f'/{d}{l}')
                for d2 in self.file_list:
                    path_list.append(f'/{d}/{d2}{l}')
        # print(all_file)
        return path_list

    def test_nginx_try_files(self):
        path_list = self.get_uri()

        try_files = ['$uri', '$uri/', '$uri/index.txt', '/index.html', 'index.html']  # todo
        for try_file in try_files:
            proxy = '/proxy'
            tpl = f'server {{ listen 20080; location {proxy} {{ alias html; try_files {try_file} index.html; }} }}'
            with open(self.conf_path, encoding='utf-8', mode='w') as f:
                f.write(tpl)
            os.system(f'D: && cd {self.nginx_dir} && nginx -s reload')
            for path in path_list:
                url = f'{self.host}{path}'  # todo /结尾
                res = requests.get(url)
                if res.status_code == 404:
                    with open(os.path.join(self.nginx_dir, 'logs/error.log'), mode='r', encoding='utf-8') as f:
                        for i, line in enumerate(f):
                            last = line
                            arr = re.findall('\"(.*?)\"', last)
                            if len(arr) == 3 and path in arr[1]:
                                print(try_file, url, arr[0], 404)
                elif res.status_code == 200:
                    print(try_file, url, res.text.replace(self.root, '').replace("\\", '/'))
                else:
                    print(try_file, url, res.status_code)

    def test_nginx_internal_location(self):
        pass
