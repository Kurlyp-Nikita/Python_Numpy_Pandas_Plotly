import pandas as pd
import numpy as np


fruit_store = pd.read_csv('sales_data.csv')
#
# fruit_store['Прибыль'] = fruit_store['Количество'] * fruit_store['Цена']
# max_profit_store = fruit_store.groupby('Магазин')['Прибыль'].sum()
# profit_store = max_profit_store.idxmax()
# print(f'Прибыль магазинов: \n{max_profit_store}')
# print(f'Самый прибыльный магазин: {profit_store}')
#
#
# popular_product = fruit_store.sort_values('Фрукт', ascending=False)
#
# apple = popular_product.groupby('Фрукт').get_group('Яблоки')
# mango = popular_product.groupby('Фрукт').get_group('Манго')
# lemons = popular_product.groupby('Фрукт').get_group('Лимоны')
# grape = popular_product.groupby('Фрукт').get_group('Виноград')
# bananas = popular_product.groupby('Фрукт').get_group('Бананы')
# jus = popular_product.groupby('Фрукт').get_group('Апельсины')
#
# list_frects = [apple['Количество'].sum(),
#                mango['Количество'].sum(),
#                lemons['Количество'].sum(),
#                grape['Количество'].sum(),
#                bananas['Количество'].sum(),
#                jus['Количество'].sum()
#                ]
#
# for i in list_frects:
#     print(max(i))



# Подсчет прибыли для каждого магазина
fruit_store['Прибыль'] = fruit_store['Количество'] * fruit_store['Цена']
profit_by_store = fruit_store.groupby('Магазин')['Прибыль'].sum()
most_profitable_store = profit_by_store.idxmax()
print(f'Самый прибыльный магазин: {most_profitable_store}')

# Подсчет популярного вида фруктов
most_popular_fruit = fruit_store['Фрукт'].value_counts().idxmax()
print(f'Самый популярный вид фруктов: {most_popular_fruit}')

# Подсчет прибыли по месяцам
fruit_store['Дата'] = pd.to_datetime(fruit_store['Дата'])
fruit_store['Месяц'] = fruit_store['Дата'].dt.month
profit_by_month = fruit_store.groupby('Месяц')['Прибыль'].sum()
most_profitable_month = profit_by_month.idxmax()
print(f'Самый прибыльный месяц: {most_profitable_month}')


