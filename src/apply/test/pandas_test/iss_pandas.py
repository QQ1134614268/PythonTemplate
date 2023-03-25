import base64
import os
import re
import unittest

import pandas as pd
import numpy as np


class TestPandas(unittest.TestCase):

    def test_main(self):
        data = pd.read_excel("图码点位清单-20220512.xlsx", usecols=[2, 6])
        temp_list = np.array(data).tolist()
        map_device = {str(tmp[1]): tmp[0] for tmp in temp_list}

        path = r"D:\桌面文件夹\新建文件夹"
        files = []
        float_regx = re.compile(r"^(\d+)(\.\d+)?$")
        for main_dir, sub_dir_list, sub_file_list in os.walk(path):
            for file in sub_file_list:
                if file.endswith(".hp"):
                    files.append(os.path.join(main_dir, file))
        names = ['1', 'device_name', 'imsi', 'imei', 'captime', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        usecols = [1, 2, 4]
        sep = ','
        out_file = ''
        for index, file in enumerate(files):
            print(file)
            df = pd.read_csv(file, sep=sep, header=None, usecols=usecols, names=names, dtype=str)
            df = df.dropna()
            df = df[
                df["imsi"].apply(lambda x: re.fullmatch(float_regx, str(x)) is not None)
                & df["captime"].apply(lambda x: len(str(x)) == 14 and str(x) > "20220816000000")
                ]
            # "1056" 康健街实验幼儿园城南园借新建天网
            # & df["device_name"].apply(lambda x: x.startswith("1056"))
            df['captime'] = df['captime'].apply(lambda x: f"{x[0:4]}-{x[4:6]}-{x[6:8]} {x[8:10]}:{x[10:12]}:{x[12:14]}")
            df['device_name'] = df['device_name'].apply(lambda x: map_device.get(x[0:4]))
            df['imsi'] = df['imsi'].str.extract('([0-9]+)')
            if not df.empty:
                print()
            if index == 0:  # % 10000  _{index // 10000}
                out_file = f'小江帧码-清洗.csv'
                df.to_csv(out_file, index=False)
            else:
                df.to_csv(out_file, mode='a', index=False, header=False)

    def test_assert(self):
        index = 0
        in_file = r'小江帧码-清洗.csv'
        res = set()
        with open(in_file, 'r', encoding="utf-8") as f:
            for index, line in enumerate(f):
                if "460110505194769" in line:
                    res.add(line.split(",")[0])
                    print("目标", index, line)
        print(res)
        print(index)

    def test_filter_3(self):
        in_file = r'小江帧码-清洗.csv'
        df_iterator = pd.read_csv(in_file, chunksize=100000)
        out_file = r'小江帧码-康健街.csv'
        names = {
            '康健街实验幼儿园城南园借新建天网',
        }  # '汉安大道与西林大道交汇处（两人脸）',
        # '汉安大道 大千路（电警）4方向'

        for index, df in enumerate(df_iterator):
            df = df[df["device_name"].isin(names)]
            if index == 0:  # % 10000  _{index // 10000}
                df.to_csv(out_file, index=False)
            else:
                df.to_csv(out_file, mode='a', index=False, header=False)

    def test_base64(self):
        in_file = r'小江帧码-康健街2.csv'
        df = pd.read_csv(in_file, dtype=str)
        df["imsi"] = df['imsi'].apply(lambda x: base64.b64encode(x.encode("utf-8")).decode(encoding="utf-8"))
        # data2 = data2.loc[data2["imsi"].apply(lambda x: re.search(regex, x) is not None)]
        out_file = r'小江帧码-康健街-base64.csv'
        df.to_csv(out_file, index=False)
