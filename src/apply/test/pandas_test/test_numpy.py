from unittest import TestCase

import numpy as np


class TestNumpy(TestCase):
    def test_np_create(self):
        print(
            {
                "np.array": np.array([[1, 2, 3], [4, 5, 6]]),
                "np.empty": np.empty((2, 3)),
                "np.ones": np.ones(3),
                "np.random": np.random.random(size=(2, 3)),
                "np.linspace": np.linspace(1, 10, 5),  # 1-10之间 取5个点
                "np.full": np.full((2, 3), 3),
                "np.eye": np.eye(3),
                "np.ones_like": np.ones_like(3),
            }
        )

    def test_np_prop(self):
        arr = np.arange(0, 12, 1)
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

    def test_np_select(self):
        arr = np.arange(0, 12, 1).reshape((3, 2, 2))
        # 选取  # 下标 条件 选取
        print(
            {
                "arr": arr,
                "arr[1]": arr[1],
                "arr[1][1]": arr[1][1],
                "arr[1][1][0]": arr[1][1][1],
                "arr[1, 1, 1]": arr[1, 1, 1],
                "arr[arr < 6]": arr[arr < 6],  # 选取
                "arr[[1, 1, 0], [1, 1, 1]]": arr[[1, 1, 0], [1, 1, 1]]  # 选取
            }
        )

    def test_np_operation(self):
        arr = np.arange(0, 12, 1).reshape(3, 4)  #
        #  flat 迭代
        for item in arr.flat:
            print(item)

        # 加减乘除
        print({
            "+ 1": arr + 1,
            "+ self": arr + arr,
            "* 3": arr * 3,
        })
