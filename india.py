import requests
from bs4 import BeautifulSoup

url = "https://www.cloudflarestatus.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

count = 0
for line in soup.find_all("div", {"class": "component-inner-container"}):
    city = line.find('span', {'class': 'name'}).text.strip()
    status = line.find('span', {'class': 'component-status'}).text.strip()

    if ("bangalore" in city.lower() or "patna" in city.lower() or "ahmedabad" in city.lower() or "bhubaneswar" in city.lower() or "chandigarh" in city.lower() or "chennai" in city.lower() or "hyderabad" in city.lower() or "kanpur" in city.lower() or "kolkata" in city.lower() or "mumbai" in city.lower() or "nagpur" in city.lower() or "kochi" in city.lower() or "new delhi" in city.lower()) and status.lower() == "partial outage":
        print(f"{city} - {status}")
        count += 1

print(f"Total count of partial outage in relevant cities: {count}")

