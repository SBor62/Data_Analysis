import pandas as pd

df = pd.read_csv('Dow_Jones.csv')  # считать информацию из файла и сохранить её в датафрейм
print(df.head())  # первые пять строк файла
print(df.info())  # ывести информацию о данных
print(df.describe)  # статистическое описание данных
