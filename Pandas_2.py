import pandas as pd


# frame_1 = pd.read_csv('students.csv')
# sred = frame_1[['Математика', 'Физика', 'Химия', 'Информатика', 'История']].mean(axis=1)
# print(sred)
# frame_1['Средний балл'] = sred
# frame_1 = frame_1.sort_values('Средний балл', ascending=False)

# print(frame_1.head())  # вывод 5 значений с начала по умолчанию
# print(frame_1.tail())  # вывод 5 значений с конца по умолчанию
# frame_1.to_excel('students.xlsx', index=False)


# print(frame_1.groupby('Имя').get_group('Анна Кузнецова'))
# print(frame_1.loc[4])
# print(frame_1.loc[4, 'Имя'])  # тот кто на 4-й строке, loc - для названий
# print(frame_1.loc[:, 'Имя'])  # Все студенты
# print(frame_1.iloc[0, 0])  # 1-й строка 1-й столбец,  iloc - для индексов
# print(frame_1.iloc[:, 0])  # все строки 1-го столбца
# print(frame_1.iloc[4, 0])  # 4-я строка 1-го столбца


#  Классная работа


movies = pd.read_csv('movies.csv')

genre_movies = movies[movies['Жанр'] == 'драма']
genre_movies.to_csv('genre_movies.csv')
print(genre_movies)

director_movies = movies[movies['Режиссер'] == 'Стивен Спилберг']
director_movies.to_csv('director_movies.csv')
print(director_movies)

top_rated_movies = movies.sort_values('Рейтинг', ascending=False)
top_rated_movies.to_csv('top_rated_movies.csv')
print(top_rated_movies.head(10))

year_movies = movies[movies['Год'] >= 2005]
year_movies.to_csv('year_movies.csv')
print(year_movies)

