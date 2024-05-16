from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time

#2. Заходим на главную страницу Википедии: https://ru.wikipedia.org/wiki/Заглавная_страница

#3. Щёлкаем правой кнопкой мыши на поисковой строке. Выбираем:

#в Chrome — Просмотреть код.
#4. Запоминаем название элемента в консоли.
#Если работаем в Chrome
browser = webdriver.Chrome()
#Далее одинаково для всех браузеров

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(5)
#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys("Солнечная система")
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)
#6. Запускаем код.

#7. Правой кнопкой мыши нажимаем на ссылку “Солнечная система”. Исследуем код элемента.

#8. Продолжаем работу с кодом:

a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#Добавляем клик на элемент
a.click()
time.sleep(5)
browser.quit()

