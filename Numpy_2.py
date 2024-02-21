from PIL import Image
import numpy

img = numpy.array(Image.open('img/Барецкий.jpg'))
imgR = img.copy()
'''

0-red
1-green
2-blue

'''
imgR[:, :, 1] = 0
imgR[:, :, 2] = 0
img1 = Image.fromarray(imgR)
img1.save('R.png', 'PNG')
###############################################
imgG = img.copy()
imgG[:, :, 0] = 0
imgG[:, :, 2] = 0
img1 = Image.fromarray(imgG)
img1.save('G.png', 'PNG')
###############################################
imgB = img.copy()
imgB[:, :, 0] = 0
imgB[:, :, 1] = 0
img1 = Image.fromarray(imgB)
img1.save('B.png', 'PNG')
###############################################
imgGRAY = img.copy()
imgGRAY = numpy.mean(imgGRAY, axis=2).astype(numpy.uint8)
print(imgGRAY)
img1 = Image.fromarray(imgGRAY)
img1.save('GRAY.png', 'PNG')
###############################################
imgY = img.copy()
imgY[:, :, 2] = 0

img1 = Image.fromarray(imgY)
img1.save('Y.png', 'PNG')
###############################################
imgV = img.copy()
imgV[:, :, 0] = 0

img1 = Image.fromarray(imgV)
img1.save('V.png', 'PNG')
##############################################
imgF = img.copy()
imgF[:, :, 1] = 0

img1 = Image.fromarray(imgF)
img1.save('F.png', 'PNG')
##############################################
imgNew = img.copy()  #
imgNew[:200, :600, 2] = 0  # кусок делаем жёлты обнуляем blue
imgNew[:200, 600:, (0, 2)] = 0  # кусок делаем зелёным обнуляем red blue
gray = numpy.mean(imgNew[200:, :600, :], axis=2).astype(numpy.uint8)  # усреднили цвет в этой области
imgNew[200:, :600, :] = numpy.stack([gray]*3, axis=2)  # вписали в цвет axis=2 одинаковые значения 3 раза
imgNew[200:, 600:, 1] = 0  # кусок делаем фиолетовым обнуляем green
img1 = Image.fromarray(imgNew)  # матрицу в картинку
img1.save('New.png', 'PNG')  #

