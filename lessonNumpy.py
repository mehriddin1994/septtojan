numbers = [18, 0, 1]
print(numbers[0])

new_num1 = [x* 2 for x in numbers]
print(new_num1)

new_num1 = [x + 2 for x in numbers]
print(new_num1)

pip install numpy

import numpy as np
arr = np.array([1, 3, 5, 7])
print("arr:", arr)
arr.shape

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("array2: ", arr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print("array3: ", arr3)
print(arr3.dtype)

arr4 = np.array([1, 2, 3, 4, 5, 6])
b = arr4.reshape(2, 3)
print("b = ", b)

z = np.zeros((2, 3))
o = np.ones((2, 3))
print("zeros: ", z)
print("ones: ", o)

a = np.array([1, 2])
print("ndim: ", a.ndim)

a = np.arange(1, 6)
print(a)

a = np.array([1, 2, 3, 4, 5, 6])
print("sum:", a.sum())
print("mean:", a.mean())
print("max:", a.max())
print("min:", a.min())

a = np.array([[1, 2], [3, 4]])
print('flatten:', a.flatten())

# T (Transpose)
a = np.array([[1, 2], [3, 4]])
print('a:', a.T)

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 3], [4, 5]])
print('dot/mulptiply:', a.dot(b))

# random.rand
a = np.random.rand(2, 3)
print("random rand:", a)

import numpy as np

a = np.array([1, 2, 3, 5, 6])
print(a)
print("*********************")

print(type(a))
print("*********************")
lst = [1, 2, 3, 4]
arr = np.array([1, 2, 3, 4])
print(lst * 2)
print(arr * 2)
print("*********************")
print("1D array")
array1 = np.array([1, 2, 3, 4])
print("2D array")
array2 = np.array([[1, 2, 5], [3, 4, 6]])
print("3D array")
array3 = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
print(array1)
print(array2)
print(array3)

print("array shape")
print(array1.shape) # qator ustun
print(array2.shape) # 2 qator 3 ustun
print(array3.shape) # 3 qator 2 ustun
print(array1.ndim) # o'lchamlar soni
print(array2.ndim)
print(array3.ndim)
print(array1.size) # elementlar soni
print(array2.size)
print(array3.size)


# amaliy ish 3*3 o'lchamli array yarating
array = np.array([[1, 2, 3],[1, 2, 3], [1, 2, 3]])
print(array.ndim)
print(array.shape)
print(array * 10)
print(array.dtype)

a = np.zeros(3)
print(a)

a = np.zeros((3, 3))
print(a)
print(np.zeros((4, 4)))

a = np.ones((2, 4))
print(a)

a = np.full((2, 4), 7)
print(a)

a = np.arange(0, 10, 2)
print(a)
b = np.arange(10)
print(b)

a = np.linspace(0, 1, 5)
print(a)

a = np.random.rand(3)
print(a)

a = np.random.randint(1, 30, size=(3, 3))
print(a)

a = np.eye(4)
print(a)

# amaliy ish
d = np.zeros((4, 3))
print(d)
f = np.arange(10, 50, 5)
print(f)
k = np.random.randint(1, 100, size=(3, 3))
print(k)

# indexlash
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 17, 18, 19])
print(a[1:3]) # 1 dan 3 gacha (3 kirmaydi)
print(a[:3]) # boshidan 3 gacha
print(a[2:]) # 2 chi indexdan oxirigacha
print(a[::2]) # har ikkinchi elementdan bittasi
print(a[::-1]) # teskari tartibda
# 2D arrayda indexlash
b = np.array([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
print(b[0, 0]) # 0-qator 0-ustun
print(b[1, 2]) # 1-qator 2-ustun
print(b[2]) # butun qator
print("*******************")
print(b[:, 1])
print(b[0, :])
print(b[0:2, 1:3])

#boolean orqali tekshirish
a = np.array([1, 2, 3, 4, 4, 5, 6, 6, 7])
maks = a > 2
print(maks)
#qisqa yozuv
print(a[a > 2])
print(a[a % 2 == 0])
print(a[a % 2 == 1])

#indexlar orqali bir nechta elementni tanlash
a = np.array([1, 2, 3, 4, 5, 6, 7])
indices = [0, 2, 5]
print(a[indices])

a = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
print(a)
# faqat 2-qator
print(a[1]) # faqat 2-qator
print(a[:, 2]) # faqat 2-ustun
print(a[a > 3])
print(a[1:3, 1:3])


#arifmetik amallar
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(a * b)
print(a + b)
print(a - b)
print(a ** 2)
print(b ** 3)

print(a + 10, b + 20)
print(a * 2, b * 3)
print(a > 2, b > 4)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
print(matrix + row)

