import numpy_ as np

a = np.array([1,1,1])
b = np.array([2,2,2])
#数组合并
c = np.vstack((a,b)) #vstack((a,b,c...))合并 成矩阵
print(c)
d = np.hstack((a,b)) #hstack((a,b,c...))合并 成数组
print(d)
print(c.shape,d.shape)
print('------')
# 数组转矩阵
print(a.reshape(a.size,1))
print(a.reshape(-1,1))
a = a[:,np.newaxis]
print(a)
b = b[:,np.newaxis]
print(b)
print(np.c_[a,b])
print(np.concatenate((a,b,a,b),axis=1)) #横向相加
