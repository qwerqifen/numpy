import numpy as np #为了方便使用numpy 采用np简写
array = np.array([[1,2,3],[2,3,4]]) #列表转化为矩阵
print(array)
'''
[[1 2 3]
 [2 3 4]]
'''

print('number of dim:',array.ndim)
'''
number of dim: 2
'''
print('shape :',array.shape)
'''
shape : (2, 3)
'''
print('size:',array.size)
'''
size: 6
'''
