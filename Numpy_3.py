import numpy
import plotly
import plotly.express as px  # для быстрого рисования графиков
import plotly.graph_objs as go  #


#                       10          11      12      13       14
virushka = numpy.array([[1000000, 2000000, 2500000, 3000000, 2150000],  #НН
                    [1560000, 2330000, 2500000, 3990000, 2150000],  #Ас
                    [2120000, 2500000, 3770000, 2650000, 4000000],  #Са
                    [2589000, 2990000, 4488000, 4586000, 3500000],  #М
                    [2100000, 2599000, 3100000, 2110000, 4233000],  #Во
                    [1533000, 2660000, 4220000, 3500000, 2577000]])  #СП

total = numpy.sum(virushka)  # сумма всей матрицы
totalCity = numpy.sum(virushka, axis=1)  # сумма по городам
# print(totalCity.shape)
totalCity = totalCity.reshape(6, 1)  # сумма по городам стала вертикальной матрицей
totalDay = numpy.sum(virushka, axis=0)  # сумма по дням

print('максимальные продажи', numpy.max(totalCity), 'руб.')  #
print('максимальные продажи', numpy.argmax(totalCity))  #

goroda = ['Нижний Новгород', 'Астрахань', 'Самара', 'Москва', 'Воронеж', 'Петербург']
datas = [10, 11, 12, 13, 14]
k1 = numpy.argmax(totalCity)
print('максимальные продажи в городе', goroda[k1])
#####################################################################################################

print('максимальные продажи по датам', numpy.max(totalDay), 'руб.')
print('максимальные продажи', numpy.argmax(totalDay))
k2 = numpy.argmax(totalDay)
print('максимальные продажи в дату', datas[k2])


city_grafik = px.bar(x=goroda, y=totalCity[:, 0], title='City')
city_grafik.show()


totalDay = totalDay.reshape(5, 1)  # сумма по дням стала вертикальной матрицей
day_grafik = px.bar(x=datas, y=totalDay[:, 0], title='Day',
                    color_continuous_scale=['red', 'green', 'blue'],
                    color=totalDay[:, 0])

day_grafik.show()


