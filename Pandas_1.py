import pandas as pd


data = ([[1000000, 2000000, 2500000, 3000000, 2150000],  #НН
        [1560000, 2330000, 2500000, 3990000, 2150000],  #Ас
        [2120000, 2500000, 3770000, 2650000, 4000000],  #Са
        [2589000, 2990000, 4488000, 4586000, 3500000],  #М
        [2100000, 2599000, 3100000, 2110000, 4233000],  #Во
        [1533000, 2660000, 4220000, 3500000, 2577000]])  #СП


frame_1 = pd.DataFrame(data)


data = {'Name': ['Dima', 'Zahar', 'Gosha'],
        'Age': [18, 21, 22],
        'Country': ['RU', 'RU', 'BY']}

frame_2 = pd.DataFrame(data)
frame_2.to_excel('file.xlsx', index=False)  # сохраняет в excel

frame_3 = pd.read_excel('data123.xlsx')
new_frame = frame_3.groupby(by='COUNTRY').get_group('France')
new_frame.to_csv('table.csv', index=False)

