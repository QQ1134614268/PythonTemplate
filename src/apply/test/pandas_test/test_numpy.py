import numpy as np

arr = np.arange(1, 12, 1)  #

print({
    "arr": arr,
    "shape": arr.shape,
    "ndim": arr.ndim,
    "size": arr.size,
    "itemsize": arr.itemsize,
    "dtype": arr.dtype,
    "type(arr)": type(arr),
    "arr[2:3]": arr[2:3],  # 切片 类似Python List
    "arr[[3,2,4]": arr[[3, 2, 4]],  # 选取
}, sep="\n")

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = np.empty((2, 3))
arr = np.ones(3)
arr = np.random.random((2, 3))
arr = np.linspace(1, 10, 5)  # 1-10之间 取5个点
arr = np.full((2, 3), 5)  # 1-10之间 取5个点
# arr = np.ones_like((2, 3))
arr = np.eye(3)
arr = np.arange(1, 12, 1).reshape(3, 2, 2)  # .flat() 转一维
# 选取
print(
    {
        "arr[1][1][0]": arr[1][1][0],
        " arr[1, 1, 0]": arr[1, 1, 0],
        "arr[arr < 1]": arr[arr < 1],  # 选取
        "arr[[1, 3, 2], [2, 1, 1]]": arr[[1, 3, 2], [2, 1, 1]],  # 选取
    }
)  # 下标 条件 选取

#  flat 迭代
for item in arr.flat:
    print(item)

# 加减乘除
arr = np.arange(0, 12, 2).reshape(3, 2)  #
arr2 = np.ones((3, 2))
arr = arr + 1
arr = arr + arr2
