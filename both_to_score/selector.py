from selenium import webdriver
from bs4 import BeautifulSoup
import time

def select_html( day:int, month:int, year:int = 2025):
# URL сайту
    url = f"https://www.forebet.com/en/football-predictions/both-to-score/{year:04d}-{month:02d}-{day:02d}"
    print(url)
    # Ініціалізація драйвера
    driver = webdriver.Chrome()

    # Відкриваємо сайт
    driver.get(url)
    print("Website opened successfully.")

    # Натискаємо кнопку для завантаження додаткових елементів
    try:
        button = driver.find_element("xpath", "//span[contains(@onclick, 'ltodrows')]")
        time.sleep(3)  # Пауза для візуалізації
        # button = driver.find_element("xpath", "//span[contains(@onclick, 'ltodrows')]")
        button.click()
        print("Button clicked.")
    except Exception as e:
        print(f"Error clicking the button: {e}")

    # Чекаємо, поки сторінка завантажиться та стабілізується
    time.sleep(2)  # Збільште час, якщо завантаження займає більше часу

    # Отримуємо HTML-код
    html_source = driver.page_source

    # Виправлення HTML за допомогою BeautifulSoup
    soup = BeautifulSoup(html_source, "html.parser")
    formatted_html = soup.prettify()

    # Збереження виправленого HTML
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(formatted_html)
    print("Corrected HTML source code saved to 'page_source.html'.")

    # Підрахунок елементів з класами rcnt tr_0, rcnt tr_1, rcnt tr_2
    count_tr_0 = len(soup.find_all("div", class_="rcnt tr_0"))
    count_tr_1 = len(soup.find_all("div", class_="rcnt tr_1"))
    count_tr_2 = len(soup.find_all("div", class_="rcnt tr_2"))

    # Виведення результатів
    print(f"day - {year} - {month} - {day}")
    print(f"Count of 'rcnt': {count_tr_0+count_tr_1+count_tr_2}")
 
    # Закриваємо браузер
    driver.quit()


# if __name__ == "__main__":
#     select_html(12,1)
