import numpy as np


# 1) Создать матрицу 5х5 со значениями 1,2,3,4 чуть ниже диагонали.
# Для начала давайте посмотрим, что мы должны получить.
# Как видно есть главная диагональ матрицы и снизу её стоят нужные значения.


# matrix = np.zeros(shape=(5, 5))
# matrix[0][0] = 0
# matrix[1][1] = 1
# matrix[2][2] = 2
# matrix[3][3] = 3
# matrix[4][4] = 4
# print(matrix)


# 2)Создать матрицу 8х8 и заполните ее шахматным рисунком


# matrix = np.zeros((8, 8), dtype=int)
# matrix[1::2, ::2] = 1
# # matrix[::2, 1::2] = 1
# print(matrix)


# 3) Найти общие значения между двумя массивам


# array1 = np.array([1, 2, 3, 4, 5])
# array2 = np.array([4, 5, 6, 7, 8])
# common_values = np.intersect1d(array1, array2)
# print(common_values)


# 4)Есть одномерный массив, сделать отрицательными все элементы, которые находятся между 3 и 9.


# array = [i for i in range(1, 10)]
# for i in range(len(array)):
#     if array[i] > 3 and array[i] < 9:
#         array[i] *= -1
#
# print(array)


# 5)Создать вектор размера 10, заполненный числом 2.5


# vector = np.full(10, 2.5)
# print(vector)


# 6)Найти индексы ненулевых элементов в [1,2,0,0,4,0]


# index = [1, 2, 0, 0, 4, 0]
#
# for i in range(len(index)):
#     if index[i] != 0:
#         print(i)


# 7)Преобразовать массив из float в int
# в дз вложить файл с кодом


# int_type = [1, 2, 0, 0, 4, 0]
# float_type = [float(i) for i in int_type]
# print(float_type)

