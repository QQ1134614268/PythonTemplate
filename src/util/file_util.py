import json
from os import path

import yaml

from config.conf import DATA_DIR
from config.json_config import MyJsonEncoder


def get_data_dir(file_path):
    return path.join(DATA_DIR, file_path)


class FileUtil:
    """
    properties 文件主要用于配置简单的键值对;
        使用逗号分隔的值 eg: 1,2,3
        使用多个属性 eg: serve.id.1 = 1
        使用yml
    """

    @staticmethod
    def to_json(data, file_path):
        content = json.dumps(data, ensure_ascii=False, cls=MyJsonEncoder, indent=2)
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.write(content)

    @staticmethod
    def from_json(file_path):  # 转类
        return json.load(file_path)

    @staticmethod
    def to_yaml(dict_value, save_path):
        """dict保存为yaml"""
        with open(save_path, mode='w', encoding="utf-8") as file:
            file.write(yaml.dump(dict_value, allow_unicode=True))

    @staticmethod
    def from_yaml(yaml_path) -> dict:  # 转类
        with open(yaml_path, encoding="utf-8") as file:
            dict_value = yaml.load(file, Loader=yaml.FullLoader)
            return dict_value

    # 只有值, 类似xmind, 目录结构
    @staticmethod
    def to_xmind(data, file_path, key):
        ret_list = FileUtil._handel_data(data, key=key)
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
                FileUtil._handel_data(dic.get("children"), level + 1, ret, key=key)
        return ret

    @staticmethod
    def from_xmind(file_path):
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
