import numpy as np

a = np.arange(3, 15).reshape((3, 4))
print(a[0])  # 打印第0行
print(a[0][0])  # [x][y]打印第x行第y列
print(a[0, 0])  # 打印[x,y]第x行第y列
print(a[0, :])  # 打印[x,:]第x行
print(a[:, 0])  # 打印[:,x]第x列
print(a[1, 1:3])  # 打印[x,y:z] 第x行 y列到z列（不包括z列）的值

print('-----')
# for 循环打印每行
for row in a:
    print(row)
print('-----')
# for 循环打印每列
for column in a.T:
    print(column)

print(a.flatten())  # 矩阵转列表
# for item in a.flatten():  #打印每一个元素
for item in a.flat:  # 打印每一个元素
    print(item)

b = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(b[1, 0, 0])

c = b[0, 1]
print(c)
