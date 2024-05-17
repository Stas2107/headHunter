import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/tolyatti/category/svet"

driver.get(url)

time.sleep(3)

# Ищем все элементы продуктов на странице
products = driver.find_elements(By.CLASS_NAME, 'WdR1o')

parsed_data = []

for product in products:
    try:
        # Извлекаем название продукта
        title = product.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text

        # Извлекаем цену продукта
        price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')

        # Извлекаем URL продукта
        url = product.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, price, url])

driver.quit()

# Запись данных с BOM
with open("products.csv", 'w', newline='', encoding='utf-8') as file:
    # Запись BOM в начало файла
    file.write('\ufeff')
    writer = csv.writer(file)
    writer.writerow(['Продукт', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)