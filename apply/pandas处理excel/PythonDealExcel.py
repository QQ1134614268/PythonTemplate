import os
import pandas as pd

os.chdir("data")
print(os.getcwd())

# name="垂钓装备.xlsx"
for name in os.listdir():
    print(name)
    data = pd.read_excel(name)

    print(data["日期"].unique())

    data["销售额"] = data["转化率"] * data["访客数"] * data["客单价"]
    print(data.head())

    data_sum = data.groupby("品牌")["销售额"].sum().reset_index()
    print(data_sum.head())
