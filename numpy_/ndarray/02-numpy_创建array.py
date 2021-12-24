import numpy_ as np

# 创建array时定义类型
array = np.array([1,2,3],dtype=int)
print(array.dtype)

# 位数越小 占用空间越小 需要精度大就需要位数较大的
array = np.array([1,2,3],dtype=float)
print(array.dtype)

# 生成矩阵
array = np.array([[1,2,3],[4,5,6]])
print(array)

# 生成全部为0的矩阵 3行4列
array = np.zeros((3,4))
print(array)

# 生成1到19，步长为2的数列 arange(x,y,z) z为步长
array = np.arange(1,20,2)
print(array)

# 生成1到10 4段的数组 linspace(x,y,z) 从x到y z段的数组
array = np.linspace(1,10,4)
print(array)

# 生成1到12的矩阵 reshape((x,y)) 生成x行y列的矩阵
array = np.arange(1,13).reshape((3,4))
print(array)

# 生成以array的形状和dtype创建一个全1的数组
print(np.ones_like(array))

print(array.reshape(-1,2))# reshape(-1,x) 表示行由列决定 如果有矩阵3行4列 x是12 那就是一行 x是6 那就是两行

print(array.reshape(2,-1))

# 对角线为1 其他为0
print(np.eye(2))

# astype 类型强转 但是会创建新的数组 并非修改旧的数组
print(array.astype(np.float64))
