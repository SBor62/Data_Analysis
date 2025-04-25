import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(10)  # массив из 10 случайных чисел для оси x
y = np.random.rand(10)  # массив из 10 случайных чисел для оси y

# Создание диаграммы рассеяния
plt.scatter(x, y, alpha=1)

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображение графика
plt.show()
