'''
创建一个 n维数组 只需调用 NumPy 的 array 函数即可：
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
    object  数组或嵌套的数列 如[1,2,3]
    dtype   数组元素的数据类型，可选
    copy    对象是否需要复制，可选
    order   创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
    subok   默认返回一个与基类类型一致的数组
    ndmin   指定生成数组的最小维度
'''

# 实例 1
import numpy as np
a = np.array([1,2,3])
print (a)
print('\n')
'''
[1 2 3]
'''

# 实例2
import numpy as np
a = np.array([[1,  2],  [3,  4]])
print (a)
print('\n')
'''
[[1 2]
 [3 4]]
'''

# 实例3
import numpy as np
a = np.array([1,  2,  3,4,5], ndmin =  2)
print (a)
print('\n')
'''
[[1 2 3 4 5]] 二维数组
'''

# 实例4
import numpy as np
a = np.array([1,  2,  3], dtype = complex)
print (a)
print('\n')
'''
[1.+0.j 2.+0.j 3.+0.j]
'''

#实例5
import numpy as np
a = np.array([1,2,3],dtype =complex,copy = True,order = None,ndmin = 5)
print(a)