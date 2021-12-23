import numpy as np

a = np.array([5,7,9,11])
b = np.arange(1,5)
# 两个数组元素个数必须相等
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(b**2)
print(b==2) # 返回布尔值

print('----------------')
# 矩阵的运算
a = np.array([[1,2],[2,1]])
b = np.arange(4).reshape(2,2)
print(a)
print(b)
print(a*b) #单纯的对应位置数字相乘
print(np.dot(a,b)) #矩阵的乘法 行×列
print(a.dot(b))# 也是矩阵的乘法 与上面那个一样
print(a.dot(a.T))# 内积

print('------------------')
#产生随机的array
a = np.random.random((2,4))
print(a)
print(np.sum(a))#所有数求和
print(np.min(a))#求最小数
print(np.max(a))#求最大数
print(np.sum(a,axis=1)) #axis=1表示 求每行的和
print(np.sum(a,axis=0)) #axis=0表示 求每列的和
print(np.min(a,axis=1)) #求每行的最小数
print(np.max(a,axis=0)) #求每列的最大数