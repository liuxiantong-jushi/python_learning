# coding=utf-8

import numpy as np

'''
Ndarray对象
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
- object 数组或嵌套的数列
- dtype  数组元素的数据类型，可选
- copy   对象是否需要复制，可选
- order  创建数组的样式，C为行方向，F为列方向，A为任意方向
- subok  默认返回一个与基类类型一致的数组
- ndmin  指定生成数组的最小唯独
'''

a = np.array([1, 2, 3])
print(a)

print("==================================")
a = np.array([[1, 2], [3, 4]])
print(a)

print("==================================")
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
a = np.array([1, 2, 3, 4, 5], ndmin=1)
print(a)

print("==================================")
a = np.array([1,2,3], dtype = complex)
print(a)

'''
Numpy数据类型
- bool_ 布尔
- int_
- intp
- int8/int16/int32/int64
- unit8/unit16/unit32/unit64
- float_
- float16/float32/float64
- complex_
- complex64/complex128
'''

'''
Numpy数组维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推
在Numpy中，每一个线性的数组称为一个轴（axis），也就是维度（dimensions）
很多时候可以声明axis，axis=0，表示沿着第0轴进行操作，
'''


'''
linear combination:
v = av1 + bv2 + cv3

linear function:
f(x + y) = f(x) + f(y)
f(ax) = af(x)

3 concepts:
- matrix/matrices
- basis
- linear transformations

matrix/matrices are representations of linear transformations.
if v = av1 + bv2 + cv3
then f(v) = af(v1) + bf(v2) + cf(v3)

once we choose a basis for both the domain and target of the linear transformation,
the columns of the matrix will represent the images of the basis vectors under the function

e.g.
we have linear transformation f which maps 3-dimension vector space to 2-dimension vector space 

v1 = [1,0,0]
v2 = [0,1,0]
v3 = [0,0,1]

w1 = [1,0]
w2 = [0,1]
 
f(v1) = 2w1 + 4w1
f(v2) = w1 -w2
f(v3) = w2

the corresponding matrix is 
M = [[2,1,0], [4,-1,1]]

the reason why this works is that matrix multiplication was designed 
so that if u multiply a matrix by the vector with all zeros except a 1 in the i-th entry
then the result is just ht i-th column of the matrix

M works correctly when applied basis vectors,
but also matrices satisfy the same properties as linear transformations
M(x + y) = Mx + My && M(ax) = aMx 

therefore M works for all vectors, so it is correct representation of f

Why does matrix multiplication work the way it does?
A = [[2,1], [4,3]], A corresponds to function f   
B = [[1,2], [1,0]], B corresponds to function g
ABx = f(g(x))

to determine what the matrix AB should look like, we can see how it affects the basis vectors 
  
'''
print("=====================================")
x = np.array([[1,0,0], [0,1,0], [0,0,1]])
M = np.array([[2,1,0],[4,-1,1]])
r = np.dot(M, x)
print(r)

A = np.array([[2,1], [4,3]])
B = np.array([[1,2], [1,0]])
w1 = np.array([1,0])

r1 = np.dot(B, w1)
print(r1)