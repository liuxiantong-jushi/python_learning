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