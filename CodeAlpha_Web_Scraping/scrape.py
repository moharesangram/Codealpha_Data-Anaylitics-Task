import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://quotes.toscrape.com"

# Create CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    page_url = "/page/1/"

    while page_url:
        response = requests.get(BASE_URL + page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = quote.find_all("a", class_="tag")
            tag_list = ", ".join(tag.text for tag in tags)

            writer.writerow([text, author, tag_list])

        # Go to next page
        next_btn = soup.find("li", class_="next")
        page_url = next_btn.find("a")["href"] if next_btn else None

print("Scraping completed! Data saved in quotes.csv")