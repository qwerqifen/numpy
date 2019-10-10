'''
NumPy 位运算
        NumPy "bitwise_" 开头的函数是位运算函数。
        NumPy 位运算包括以下几个函数：

        bitwise_and         对数组元素执行位与操作
        bitwise_or          对数组元素执行位或操作
        invert              按位取反
        left_shift          向左移动二进制表示的位
        right_shift         	向右移动二进制表示的位
'''

# 实例1  bitwise_and() 函数对数组中整数的二进制形式执行位与运算。
import numpy as np

print('13 和 17 的二进制形式：')
a, b = 13, 15
print(bin(a), bin(b))
print('\n')

print('13 和 15 的位与：')
print(np.bitwise_and(13, 15)) # 显示的是按位与之后的二进制位所代表的十进制数


# 实例2  bitwise_or()函数对数组中整数的二进制形式执行位或运算。
a, b = 13, 17
print('13 和 17 的二进制形式：')
print(bin(a), bin(b))

print('13 和 17 的位或：')
print(np.bitwise_or(13, 17))

# 实例3 invert() 函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0。
print('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print(np.invert(np.array([13], dtype=np.uint8)))
print('\n')
# 比较 13 和 242 的二进制表示，我们发现了位的反转

print('13 的二进制表示：')
print(np.binary_repr(13, width=8))
print('\n')

print('242 的二进制表示：')
print(np.binary_repr(242, width=8))
print('\n')

# 实例4 left_shift() 函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的 0。
print('将 10 左移两位：')
print(np.left_shift(10, 5))
print('\n')

print('10 的二进制表示：')
print(np.binary_repr(10, width=8))
print('\n')

print('40 的二进制表示：')
print(np.binary_repr(320, width=16))
print('\n')
#  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。

# 实例5   right_shift() 函数将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的 0。
print('将 40 右移两位：')
print(np.right_shift(40, 2))
print('\n')

print('40 的二进制表示：')
print(np.binary_repr(40, width=8))
print('\n')

print('10 的二进制表示：')
print(np.binary_repr(10, width=8))
#  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。

