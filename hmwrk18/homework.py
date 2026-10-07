import csv

import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/tag/life/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.select(".quote")

with open("life.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["author", "text"])
    writer.writeheader()

    for quote in quotes:
        author = quote.select_one(".author").get_text(strip=True)
        text = quote.select_one(".text").get_text(strip=True)

        writer.writerow({
            "author": author,
            "text": text,
        })

print(f"Збережено цитат: {len(quotes)}")