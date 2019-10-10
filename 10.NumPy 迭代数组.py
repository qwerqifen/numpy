'''
NumPy 迭代数组
    NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
    迭代器最基本的任务的可以完成对数组元素的访问。
'''

#实例1
import numpy as np

a = [[1,2,3],[3,4,5],[4,5,6]]
print('原始数组是：')
print(a)
print('\n')
print('迭代输出元素：')
for x in np.nditer(a): # 0, 1, 2, 3, 4, 5,
    print(x, end=", ")
print('\n')

# 实例2
a = np.arange(6).reshape(2, 3) # 0, 1, 2, 3, 4, 5,
for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

for x in np.nditer(a.T.copy(order='C')): # 0, 3, 1, 4, 2, 5, 按行输出
    print(x, end=", ")
print('\n')

# 实例3
'''
控制遍历顺序
        for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
        for x in np.nditer(a.T, order='C'):C order，即是行序优先；
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('原始数组的转置是：')
b = a.T
print (b)
print ('\n')
print ('以 C 风格顺序排序：')
c = b.copy(order='C') #按行存储方式
print (c)
for x in np.nditer(c):
    print (x, end=", " )
print  ('\n')
print  ('以 F 风格顺序排序：')
c = b.copy(order='F')
print (c)
for x in np.nditer(c):
    print (x, end=", " )

#实例4  可以通过显式设置，来强制 nditer 对象使用某种顺序：
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('以 C 风格顺序排序：')
for x in np.nditer(a, order =  'C'):
    print (x, end=", " )
print ('\n')
print ('以 F 风格顺序排序：')
for x in np.nditer(a, order =  'F'):
    print (x, end=", " )

    '''
    这些例子显示 行优先 按行输出；列优先 按列输出；默认值则是按大小排序输出
    '''


# 实例5
'''
修改数组中元素的值
        nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
        为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print ('修改后的数组是：')
print (a)
print('\n')


# 实例6
'''
使用外部循环
        c_index
        f_index
        multi-index
        external_loop  #给出的值是具有多个值的一维数组，而不是零维数组
        前三个不懂
'''

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('修改后的数组是：')
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'): #给出的值是具有多个值的一维数组，而不是零维数组
   print (x, end=", " )


'''
如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 
假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。
'''

a = np.arange(0,60,5)
a = a.reshape(3,4)
print  ('第一个数组为：')
print (a)
print  ('\n')
print ('第二个数组为：')
b = np.array([1,  2,  3,  4], dtype =  int)
print (b)
print ('\n')
print ('修改后的数组为：')
for x,y in np.nditer([a,b]):# a与b 对应元素的访问 输出结果以：连接
    print ("%d:%d"  %  (x,y), end=", " ) # 0:1, 5:2, 10:3, 15:4, 20:1, 25:2, 30:3, 35:4, 40:1, 45:2, 50:3, 55:4,