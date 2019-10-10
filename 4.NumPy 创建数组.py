'''
一.numpy.empty
numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
    numpy.empty(shape, dtype = float, order = 'C')
    shape   数组形状
    dtype   数据类型
    order   有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
'''
#实例1 在数据类型为int时 其输出值为0的数组；数据类型为bool时 其输出值为false；数据类型为float complex 时 输出为未初始化数
        # 疑惑
import numpy as np
x = np.empty([3,2], dtype = complex)
print (x)
print('\n')


'''
#二. numpy.zeros
创建指定大小的数组，数组元素以 0 来填充：
numpy.zeros(shape, dtype = float, order = 'C')
    shape   数组形状
    dtype   数据类型，可选
    order   'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
'''
#实例2
import numpy as np
# 默认为浮点数
x = np.zeros(5)
print(x)
# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)
# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)
print('\n')


'''
三 numpy.ones  创建指定形状的数组，数组元素以 1 来填充：
numpy.ones(shape, dtype = None, order = 'C')
    shape   	数组形状
    dtype       数组类型
    order       'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
'''
# 实例3
import numpy as np
# 默认为浮点数
x = np.ones(5)
print(x)
# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)
print('\n')
