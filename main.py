from selenium import webdriver
import time
#Если мы работаем с Chrome
browser = webdriver.Chrome()

#Настраиваем возможность зайти на сайт.
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#В кавычках указываем URL сайта, на который нам нужно зайти
browser.save_screenshot("dom.png")
time.sleep(5)
#Задержка в 10 секунд
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(5)
#browser.quit()
#Закрываем браузер
#Добавляем перезагрузку страницы:
browser.refresh()
time.sleep(5)