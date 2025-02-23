from selenium import webdriver
from bs4 import BeautifulSoup
import time

# URL сайту
url = "https://www.forebet.com/en/football-predictions/both-to-score/2025-01-01"

# Ініціалізація драйвера
driver = webdriver.Chrome()

# Відкриваємо сайт
driver.get(url)
print("Website opened successfully.")

# Натискаємо кнопку для завантаження додаткових елементів
try:
    button = driver.find_element("xpath", "//span[contains(@onclick, 'ltodrows')]")
    time.sleep(2)  # Пауза для візуалізації
    button.click()
    print("Button clicked.")
except Exception as e:
    print(f"Error clicking the button: {e}")

# Чекаємо, поки сторінка завантажиться та стабілізується
time.sleep(5)  # Збільште час, якщо завантаження займає більше часу

# Отримуємо HTML-код
html_source = driver.page_source

# Виправлення HTML за допомогою BeautifulSoup
soup = BeautifulSoup(html_source, "html.parser")
formatted_html = soup.prettify()

# Збереження виправленого HTML
with open("page_source.html", "w", encoding="utf-8") as file:
    file.write(formatted_html)
print("Corrected HTML source code saved to 'page_source.html'.")

# Закриваємо браузер
driver.quit()
