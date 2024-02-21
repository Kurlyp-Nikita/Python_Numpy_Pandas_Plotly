import plotly
import numpy as np
import pandas as pd
import plotly.express as px  # для быстрого рисования графиков
import plotly.graph_objs as go  #


frame = px.data.carshare()  # таблицы на которых рисуют графики
new_frame = frame.groupby('peak_hour').sum()

fig = px.bar(x=new_frame.index, y=new_frame.car_hours, title='cars',
             color_continuous_scale=['red', 'green', 'blue'],
             color=new_frame.car_hours)
# fig.show()


# другая таблица которая, для обучения есть в plotly

frame = px.data.election()
new_frame = frame.groupby('winner').sum()
fig = px.pie(new_frame, names=new_frame.index, values=new_frame.total, title='vibory')
fig.show()


