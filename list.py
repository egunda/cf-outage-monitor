import requests
from bs4 import BeautifulSoup

url = "https://www.cloudflarestatus.com/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

cities = [city.text.strip() for city in soup.find_all("span", {"class": "name"})]
statuses = [status.text.strip() for status in soup.find_all("span", {"class": "component-status"})]

cities_with_partial_outage = []
for city, status in zip(cities, statuses):
    if "partial outage" in status.lower():
        cities_with_partial_outage.append(city)
        print(city)

print("Total POPs:", len(cities))
print("Total POPs Down:", len(cities_with_partial_outage))
