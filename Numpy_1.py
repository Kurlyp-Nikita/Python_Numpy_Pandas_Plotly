import numpy
from PIL import Image


num_1 = numpy.array([1, 2, 3, 4, 5])
print(num_1)

num_2 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(num_2)

num_3 = numpy.arange(0, 10, 2)
print(num_3)

num_4 = numpy.random.rand(3, 3)
print(num_4)

num_5 = numpy.zeros(shape=(4, 4))
print(num_5)

num_6 = numpy.ones(shape=(4, 4))
print(num_6)

num_7 = numpy.random.randint(low=0, high=20, size=(4, 4))
print(num_7)

summa = num_6 + num_7
print(summa)

print(numpy.max(summa))
print(numpy.min(summa))
print(numpy.sum(summa))
print(numpy.prod(summa))  # произведение
print(numpy.mean(summa))  # среднее


# img = numpy.array(Image.open('img/Барецкий.jpg'))
# print(img[0, 0])
# print(img.shape)
# print(img.size)
# print(img.ndim)
# print(img.data)
# print(img.dtype)

