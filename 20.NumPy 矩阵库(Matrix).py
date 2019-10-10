'''
NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。
一个 的矩阵是一个由行（row）列（column）元素排列成的矩形阵列
'''

# 实例1 matlib.empty()
'''
matlib.empty() 函数返回一个新的矩阵，语法格式为：
        numpy.matlib.empty(shape, dtype, order)
        
        shape: 定义新矩阵形状的整数或整数元组
        Dtype: 可选，数据类型
        order: C（行序优先） 或者 F（列序优先）
'''
import numpy.matlib
import numpy as np

print(np.matlib.empty((2,3)))
print('\n')
# 填充为随机数据


# 实例2 numpy.matlib.zeros()
# numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
import numpy.matlib
import numpy as np

print(np.matlib.zeros((3, 3)))
print('\n')

# 实例3 numpy.matlib.ones()
# numpy.matlib.ones()函数创建一个以 1 填充的矩阵。。

print (np.matlib.ones((2,2)))
print('\n')

# 实例4 numpy.matlib.eye()
'''
numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
        numpy.matlib.eye(n, M,k, dtype)
                n: 返回矩阵的行数
                M: 返回矩阵的列数，默认为 n
                k: 对角线的索引       就是那个1从哪里开始
                dtype: 数据类型
'''
print (np.matlib.eye(n =  3, M =  4, k =  2, dtype =  float))
print('\n')

# 实例5 numpy.matlib.identity()   函数返回给定大小的单位矩阵。
print (np.matlib.identity(5, dtype =  float))
print('\n')

# 实例6  numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
print (np.matlib.rand(3,3))
print('\n')





