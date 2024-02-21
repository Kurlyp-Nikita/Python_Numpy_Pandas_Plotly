import plotly
import numpy as np
import pandas as pd
import plotly.express as px  # для быстрго рисования графиков
import plotly.graph_objs as go  #


dx = [1, 2, 3, 4]
dy = [1, 4, 16, 27]
fig = px.line(x=dx, y=dy, title='Grafik')  # li график линии
fig.show()  # show показ графика

'''

line
pie
bar
scatter
area

'''

data = np.arange(0, 10, step=0.5)

def f1(q):
    return q * q

fig = px.bar(x=data, y=f1(data), title='Grafik')
fig.show()

fig = px.line(x=data, y=f1(data), title='Grafik')
fig.show()

fig = px.scatter(x=data, y=f1(data), title='Grafik')
fig.show()

fig = px.area(x=data, y=f1(data), title='Grafik')
fig.show()

