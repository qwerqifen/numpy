'''
NumPy 提供了多种排序的方法。
这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。
        种类                          速度          最坏情况            工作空间            稳定性
        'quicksort'（快速排序）       1               O(n^2)                  0               否
        'mergesort'（归并排序）       2               O(n*log(n))             ~n/2            是
        'heapsort'（堆排序）          3               O(n*log(n))               0              否
'''

# 实例1   numpy.sort()
'''
numpy.sort() 函数返回输入数组的排序副本。函数格式如下：
        numpy.sort(a, axis, kind, order)
        
        a: 要排序的数组
        axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
        kind: 默认为'quicksort'（快速排序）
        order: 如果数组包含字段，则是要排序的字段
'''
import numpy as np

a = np.array([[3, 7], [9, 1]])
print('我们的数组是：')
print(a)
print('\n')
print('调用 sort() 函数：')
print(np.sort(a))
print('\n')
print('按列排序：')
print(np.sort(a, axis=0))
print('\n')
# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print('我们的数组是：')
print(a)
print('\n')
print('按 name 排序：')
print(np.sort(a, order='name'))
print('\n')

# 实例2 numpy.argsort()
'''
numpy.argsort() 函数返回的是数组值从小到大的索引值。
'''
x = np.array([3,  1,  2])
print ('我们的数组是：')
print (x)
print ('\n')
print ('对 x 调用 argsort() 函数：')
y = np.argsort(x)
print (y)
print ('\n')
print ('以排序后的顺序重构原数组：')
print (x[y])            # 这是个啥意思！   是索引
print ('\n')
print ('使用循环重构原数组：')
for i in y:
    print (x[i], end=" ")


# 实例3       numpy.lexsort()
'''
numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
这里举一个应用场景：小升初考试，重点班录取学生按照总成绩录取。
在总成绩相同时，数学成绩高的优先录取，在总成绩和数学成绩都相同时，按照英语成绩录取…… 
这里，总成绩排在电子表格的最后一列，数学成绩在倒数第二列，英语成绩在倒数第三列。
'''
nm =  ('raju','anil','raju','amar')
dv =  ('s.y.',  's.y.',  'f.y.',  'f.y.')
ind = np.lexsort((dv,nm))
print ('调用 lexsort() 函数：')
print (ind)
print ('\n')
print ('使用这个索引来获取排序后的数据：')
print ([nm[i]  +  ", "  + dv[i]  for i in ind])
print('\n')

# 实例4       msort、sort_complex、partition、argpartition
'''
msort(a)	数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)
sort_complex(a)     对复数按照先实部后虚部的顺序进行排序
partition(a, kth[, axis, kind, order])      指定一个数，对数组进行分区
argpartition(a, kth[, axis, kind, order])       可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
'''

np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j])

#   partition() 分区排序：
a = np.array([3, 4, 2, 1])
f = np.partition(a, 3)  # 将数组 a 中所有元素（包括重复元素）从小到大排列，
                    # 3 表示的是排序数组索引为 3 的数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
print(f)
print('\n')
print(np.partition(a, (1, 3)) )# 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间

# argpartition分区排序
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])     #找到数组的第 3 小（index=2）的值和第 2 大（index=-2）的值
b = arr[np.argpartition(arr, 2)[2]]
c = arr[np.argpartition(arr, -2)[-2]]
print(b)
print('\n')
print(c)
print('\n')

d = arr[np.argpartition(arr, [2,3])[2]]
print(d)
print('\n')
e = arr[np.argpartition(arr, [2,3])[3]]
print(e)
print('\n')

# 实例5
# numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。 二维数组按展开后的索引

a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print  ('我们的数组是：')
print (a)
print ('\n')
print ('调用 argmax() 函数：')
print (np.argmax(a)) #没给定轴则按全部排
print ('\n')
print ('展开数组：')
print (a.flatten())
print ('\n')
print ('沿轴 0 的最大值索引：')
maxindex = np.argmax(a, axis =  0)
print (maxindex)
print ('\n')
print ('沿轴 1 的最大值索引：')
maxindex = np.argmax(a, axis =  1)
print (maxindex)
print ('\n')
print ('调用 argmin() 函数：')
minindex = np.argmin(a)
print (minindex)
print ('\n')
print ('展开数组中的最小值：')
print (a.flatten()[minindex])
print ('\n')
print ('沿轴 0 的最小值索引：')
minindex = np.argmin(a, axis =  0)
print (minindex)
print ('\n')
print ('沿轴 1 的最小值索引：')
minindex = np.argmin(a, axis =  1)
print (minindex)
print('\n')

#   实例6
#   numpy.nonzero() 函数返回输入数组中非零元素的索引 这个是按二维数组索引
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 nonzero() 函数：')
print (np.nonzero (a))
print('\n')


# 实例7
# numpy.where()     函数返回输入数组中满足给定条件的元素的索引
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
print ( '大于 3 的元素的索引：')
y = np.where(x >  3)
print (y)
print ('使用这些索引来获取满足条件的元素：')
print (x[y])
print('\n')

# 实例8
# numpy.extract() 函数根据某个条件从数组中抽取元素，返回满足条件的元素
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
# 定义条件, 选择偶数元素
condition = np.mod(x,2)  ==  0
print ('按元素的条件值：')
print (condition)
print ('使用条件提取元素：')
print (np.extract(condition, x)) # 输出值位一维数组
