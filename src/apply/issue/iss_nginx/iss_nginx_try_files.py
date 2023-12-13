import os
import shutil
from unittest import TestCase

import requests


class TestNginx(TestCase):
    root = r'D:\dev\nginx-1.22.0\html'
    dirs_list = ['dir1', 'dir2', 'dir3']
    file_list = ['index.html', 'index.txt']
    conf_path = r'D:/dev/nginx-1.22.0/conf/nginx.conf'
    host = 'http://localhost:20080'

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
        path_list = ['']
        for d in self.dirs_list:
            path_list.append(f'/{d}')
            for d2 in self.file_list:
                path_list.append(f'/{d}/{d2}')
        # print(all_file)

        with open(self.conf_path, encoding='utf-8', mode='r') as f:
            lines = f.readlines()

        index_files = ['/index.html', 'index.html']
        for index in index_files:
            lines[102] = f'\t\t\tindex {index};\n'
            lines[103] = f'\t\t\t# #\n'
            with open(self.conf_path, encoding='utf-8', mode='w') as f:
                f.writelines(lines)
            os.system(r'D: && cd D:\dev\nginx-1.22.0\ && nginx -s reload')
            #  # 访问文件, 目录; 返回结果一样,推测nginx先查文件,如果是目录,走index逻辑
            for path in path_list:
                url = f'{self.host}{path}'
                res = requests.get(url)
                print(index, url,
                      res.text.replace(self.root, '').replace("\\", '/') if res.status_code == 200 else res.status_code)

    def test_nginx_try_files(self):
        path_list = ['']
        for d in self.dirs_list:
            path_list.append(f'/{d}')
            for d2 in self.file_list:
                path_list.append(f'/{d}/{d2}')

        with open(self.conf_path, encoding='utf-8', mode='r') as f:
            lines = f.readlines()

        try_files = ['$uri', '$uri/', '$uri/index.txt', '/index.html', 'index.html']  # todo
        for try_file in try_files:
            lines[102] = f'\t\t\tindex index.html;\n'
            lines[103] = f'\t\t\ttry_files {try_file} index.html;\n'  # -- todo
            with open(self.conf_path, encoding='utf-8', mode='w') as f:
                f.writelines(lines)
            os.system(r'D: && cd D:\dev\nginx-1.22.0\ && nginx -s reload')
            for path in path_list:
                url = f'{self.host}{path}'  # todo /结尾
                res = requests.get(url)
                print(try_file, url, res.headers.get("URI"),
                      res.text.replace(self.root, '').replace("\\", '/') if res.status_code == 200 else res.status_code)

    def test_nginx_internal_location(self):
        pass
