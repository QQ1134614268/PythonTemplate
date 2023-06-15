from pyiter import iterate as it
from tqdm import tqdm

# 把列表里的小写变成大写并存于新列表中
text = ["hello", "world"]
text_upper = []
for i in text:
    text_upper.append(i.upper())
print(text_upper)

text_upper1 = it(text).map(str.upper).to_list()
text_upper2 = it(text).map(lambda x: x.upper()).to_list()
print(text_upper1)
print(text_upper2)

# use tqdm
# 使用进度条
it(range(10)).map(lambda x: str(x)).progress(lambda x: tqdm(x, total=x.len)).parallel_map(lambda x: x,
                                                                                          max_workers=5).to_list()
