import plotly
import numpy as np
import pandas as pd
import plotly.express as px  # для быстрого рисования графиков
import plotly.graph_objs as go  #


dx = np.arange(-10, 10)  # точки для "х"

def f1(q):
    return q*q


def f2(q):
    return q**3


def f3(q):
    return q + 100

fig = go.Figure()  # Пустой график

graf_1 = go.Scatter(x=dx, y=f1(dx), name='graf_1', mode='lines')
graf_2 = go.Scatter(x=dx, y=f2(dx), name='graf_2', mode='markers')
graf_3 = go.Scatter(x=dx, y=f3(dx), name='graf_3', mode='markers')

fig.add_trace(graf_1)  # add_trace, функция добавления линии на график
fig.add_trace(graf_2)  # add_trace, функция добавления точек на график
fig.add_trace(graf_3)  # add_trace, функция добавления точек на график


fig.update_yaxes(title='точки')  # update_yaxes, функция подписать y
fig.update_xaxes(title='от -10 до 10')  # update_xaxes, функция подписать x
fig.update_layout(title='График')  # update_layout, функция подписать само название графика

fig.show()  # show, функция показа графика


