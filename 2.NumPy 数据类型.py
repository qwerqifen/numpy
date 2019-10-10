'''
dtype 对象是使用以下语法构造的：
    numpy.dtype(object, align, copy)

    object - 要转换为的数据类型对象
    align - 如果为 true，填充字段使其类似 C 的结构体。
    copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用
'''

# 实例
import numpy as np
a = np.array([2/3,23,4],dtype=np.float32)
print(a.dtype)
print(a)
'''
float32
[ 2. 23.  4.]

'''
# dtype=np.float32 改变多维数组的数据类型 int complex bool 均正确
# 可是float出现问题 浮点数的小数部位未显示 改成除法就显示了 拿地萨嘎(显示了 右下角的那个点)