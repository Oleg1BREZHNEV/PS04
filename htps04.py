
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def search_wikipedia(query):
    # Инициализация браузера
    browser = webdriver.Chrome()

    # Открытие главной страницы Википедии
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in browser.title
    time.sleep(2)

    # Поиск по запросу
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    return browser


def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.XPATH, "//p")
    for i, para in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {para.text[:200]}...")  # Выводим первые 200 символов параграфа
        if (i + 1) % 5 == 0:  # Просмотр по 5 параграфов за раз
            cont = input("Показать ещё параграфы? (да/нет): ").strip().lower()
            if cont != 'да':
                break


def list_links(browser):
    try:
        links = browser.find_elements(By.XPATH,
                                      "//a[@href and not(starts-with(@href, '#')) and not(contains(@href, 'redlink=1'))]")
        internal_links = [link.get_attribute('href') for link in links]

        for index, link in enumerate(internal_links):
            print(f"{index + 1}. {link}")

        return internal_links

    except Exception as e:
        print(f"An error occurred: {e}")
        return []





def main():
    browser = webdriver.Chrome()
    query = input("Введите запрос для поиска на Википедии: ")
    search_url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    browser.get(search_url)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        action = input("Введите номер действия: ")

        if action == '1':
            paragraphs = browser.find_elements(By.XPATH, "//p")
            for index, paragraph in enumerate(paragraphs):
                print(f"Параграф {index + 1}: {paragraph.text[:100]}...")  # Вывод первых 100 символов параграфа
                if index >= 3:  # Показывать только первые 4 параграфа
                    break

        elif action == '2':
            internal_links = list_links(browser)
            if internal_links:
                link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
                if 0 <= link_choice < len(internal_links):
                    browser.get(internal_links[link_choice])
                else:
                    print("Неверный номер ссылки.")
            else:
                print("Нет доступных ссылок.")

        elif action == '3':
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()


### Пояснения:
#1. ** search_wikipedia(query) **: Функция, которая принимает поисковый
#запрос, открывает Википедию и вводит запрос в поисковую строку.
#2. ** list_paragraphs(browser) **: Функция для листания параграфов
# текущей статьи. 3. ** list_links(browser) **: Функция для показа
# связанных страниц и выбора одной из них. 4. ** main() **: Основная
# функция, которая управляет процессом, предлагая пользователю выбор
# действий.  Программа будет работать следующим образом: 1. Запросит
# у пользователя поисковый запрос. 2. Найдет статью на Википедии по этому
# запросу. 3. Предложит пользователю три варианта действий: листать параграфы,
# переходить на связанные страницы или  выйти из программы.