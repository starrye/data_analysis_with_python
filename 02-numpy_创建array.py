import numpy as np

#创建array时定义类型
array = np.array([1,2,3],dtype=np.int)
print(array.dtype)
#位数越小 占用空间越小 需要精度大就需要位数较大的
array = np.array([1,2,3],dtype=np.float)
print(array.dtype)
#生成矩阵
array = np.array([[1,2,3],[4,5,6]])
print(array)
#生成全部为0的矩阵 3行4列
array = np.zeros((3,4))
print(array)
#生成1到19，步长为2的数列 arange(x,y,z) z为步长
array = np.arange(1,20,2)
print(array)
#生成1到10 4段的数组 linspace(x,y,z) 从x到y z段的数组
array = np.linspace(1,10,4)
print(array)
#生成1到12的矩阵 reshape((x,y)) 生成x行y列的矩阵
array = np.arange(1,13).reshape((3,4))
print(array)