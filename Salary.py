import pandas as pd

df = pd.read_csv('dz.csv')  # считать информацию из файла
salary_by_city = df.groupby('City')['Salary'].mean()  # в переменной средняя зарплата по говоду
print(salary_by_city)  # вывод результата
