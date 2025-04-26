from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Открываем страницу
driver.get('https://www.divan.ru/category/divany')

# Подождем несколько секунд, чтобы страница полностью загрузилась
time.sleep(5)

# Собираем информацию о ценах
# На сайте Divan.ru цены находятся в элементах с классом 'ui-LD-ZU KIkOH'
prices = driver.find_elements(By.CSS_SELECTOR, 'span[class*="ui-LD-ZU KIkOH"]')

# Извлекаем текст из элементов и сохраняем в список
price_list = [price.text for price in prices if price.text]

# Закрываем браузер
driver.quit()

# Создаем DataFrame из списка цен
df = pd.DataFrame(price_list, columns=['Цена'])

# Сохраняем DataFrame в CSV файл
df.to_csv('divan_prices.csv', index=False, encoding='utf-8')

print("Данные сохранены в файл 'divan_prices.csv'")

# Чтение CSV-файла
df = pd.read_csv('divan_prices.csv')

# Функция для очистки и преобразования цены
def clean_price(price_str):
    # Удаляем "руб.", пробелы и заменяем пробелы между цифрами на пустую строку
    cleaned = price_str.replace('руб.', '').replace(' ', '').strip()
    # Преобразуем в число
    return int(cleaned) if cleaned else None

# Применяем функцию к столбцу 'Цена'
df['Цена'] = df['Цена'].apply(clean_price)

# Сохраняем обработанные данные обратно в CSV
df.to_csv('divan_prices_cleaned.csv', index=False, encoding='utf-8')

print("Данные успешно обработаны и сохранены в 'divan_prices_cleaned.csv'")
print(df.head())  # Показываем первые 5 строк для проверки

# Чтение обработанного CSV-файла
df = pd.read_csv('divan_prices_cleaned.csv')

# Создаем гистограмму
plt.figure(figsize=(12, 6))

# Гистограмма с 20 корзинами (bins) для хорошей детализации
plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black')

# Настройка оформления
plt.title('Распределение цен на диваны', fontsize=16)
plt.xlabel('Цена (руб)', fontsize=12)
plt.ylabel('Количество диванов', fontsize=12)
plt.grid(axis='y', alpha=0.5)

# Автоматическая подстройка layout
plt.tight_layout()

# Показываем график
plt.show()
