import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('sales_data.csv')


# 1. Круговой график по магазинам
plt.figure(figsize=(8, 8))
data['Магазин'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Продажи по магазинам')
plt.ylabel('')
plt.show()


# 2. Гистограмма для каждого магазина по товарам и количеству продаж
for store in data['Магазин'].unique():
    plt.figure(figsize=(8, 6))
    store_data = data[data['Магазин'] == store]
    store_data.groupby('Фрукт')['Количество'].sum().plot(kind='bar', color='skyblue')
    plt.title(f'Продажи товаров в магазине {store}')
    plt.xlabel('Фрукты')
    plt.ylabel('Количество продаж')
    plt.show()


# 3. Линейный график для одного магазина по товарам и цене
chosen_store = 'Фермер'  # Выбираем магазин для анализа
plt.figure(figsize=(8, 6))
chosen_store_data = data[data['Магазин'] == chosen_store]
chosen_store_data.groupby('Фрукт')['Цена'].mean().plot(kind='line', marker='o', color='green', linestyle='--')
plt.title(f'Цены на товары в магазине {chosen_store}')
plt.xlabel('Фрукты')
plt.ylabel('Цена')
plt.grid(True)
plt.show()