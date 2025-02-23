import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://www.google.com',  # Посилання на сторінку реферера
    'DNT': '1',  # Не відстежувати
    'Cache-Control': 'max-age=0',
    'TE': 'trailers',
}
response = requests.get("https://www.oddsportal.com/matches/football/",headers=headers)
print(response.status_code)
# print(response.text)
with open("odds/page_source.html","w",encoding="utf-8") as file:
    file.write(response.text)