'''
numpy的数组属性
在 NumPy中，每一个线性的数组称为是一个轴（axis），(比如[1, 2, 3])
也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，([[1, 2, 3], [4, 5, 6],[5,6,7]])
其中第一个一维数组中每个元素又是一个一维数组。第一个一维数组[[],[],[]]
所以一维数组就是 NumPy 中的轴（axis），
第一个轴相当于是底层数组，第二个轴是底层数组里的数组。
而轴的数量——秩，就是数组的维数。
'''
NumPy 的数组中比较重要 ndarray 对象属性有：
ndarray.ndim    秩，即轴的数量或维度的数量
ndarray.shape   数组的维度，对于矩阵，n 行 m 列
ndarray.size    数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype   ndarray 对象的元素类型
ndarray.itemsize    ndarray 对象中每个元素的大小，以字节为单位
ndarray.flags   ndarray 对象的内存信息
ndarray.real    ndarray元素的实部
ndarray.imag    	ndarray 元素的虚部
'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6],[5,6,7]])#这是一个二维数组
print(a.ndim)
print (a.shape)
print('\n')


#实例1
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)
print('\n')

#实例2
a = np.array([[[[1, 2, 3], [4, 5, 6]]]])
print(a.shape)
print('\n')
'''
(1, 1, 2, 3)
'''

#实例3 调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)
print('\n')

#实例4 调整数组大小 reshape
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print (b)
print('\n')

#实例5 ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。

'''
ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。

例如，一个元素类型为 float64 的数组 itemsiz 属性值为 8
(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节）
又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）。
'''
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)
print('\n')

#实例5 ndarray.flags 返回 ndarray 对象的内存信息 这个看不懂 不写了