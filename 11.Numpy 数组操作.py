#  一 ：修改数组形状

'''
修改数组形状

    reshape     不改变数据的条件下修改形状
    flat        数组元素迭代器
    flatten     返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
    ravel       返回展开数组
'''

#1. numpy.reshape
'''
# numpy.reshape
# numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
# arr：要修改形状的数组
# newshape：整数或者整数数组，新的形状应当兼容原有形状
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
'''
import numpy as np

a = np.arange(8)
print('原始数组：')
print(a)
print('\n')

b = a.reshape(4, 2) #默认是行

c = np.reshape(a,(4,2),order='C')
d = np.reshape(a,(4,2),order='F')
e = np.reshape(a,(4,2),order='A')
# f = np.reshape(a,(4,2),order='K') K 输出错误
print('修改后的数组：')
print(b)
print('\n')
print(c)
print('\n')
print(d)
print('\n')
print(e)
print('\n')

#2。numpy.ndarray.flat
'''
numpy.ndarray.flat 是一个数组元素迭代器
'''
a = np.arange(9).reshape(3, 3)
print(a)
print('\n')
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
输出a 显示的是3*3数组
'''
print('原始数组：')
for row in a:
    print(row)
print('\n')
'''
[0 1 2]
[3 4 5]
[6 7 8]
输出a 按行显示每一维
'''

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)
print('\n')
print(a)
print('\n')
'''
迭代输出
'''


# 3.numpy.ndarray.flatten
'''
numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
        ndarray.flatten(order='C')
            order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
        
            将原数组按order展开
'''
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
print('\n')

# 4.numpy.ravel
'''
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。

该函数接收两个参数：

numpy.ravel(a, order='C')
        order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
'''
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))

print('此时的a：')
print(a) # 这修改了也没影响原始数组啊



# 二：反转数组
'''
transpose       对换数组的维度
ndarray.T       与self.transpose() 相同
rollaxis        向后滚动指定的轴
swapaxes        对换数组的两个轴
'''

#1.numpy.transpose
'''
numpy.transpose 函数用于对换数组的维度，格式如下：
        numpy.transpose(arr, axes)
            arr：要操作的数组
            axes：整数列表，对应维度，通常所有维度都会对换。
'''
a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

'''

print('对换数组：')
print(np.transpose(a)) #就是转置
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]

'''


#2.numpy.ndarray.T
a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('转置数组：')
print(a.T)

#3.numpy.rollaxis    这个我不懂啊！
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 将轴 1 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 1))
# 将轴 0 滚动到轴 1：（宽度到高度）
print('\n')

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 0, 1))

'''
修改数组维度
'''