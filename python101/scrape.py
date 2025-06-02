# Example: getting links from a page
import requests
from bs4 import BeautifulSoup

response = requests.get("https://es.finance.yahoo.com/quote/NVDA/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGCx0IKCND-0-pz0mS606LrEoluxUaUU24T_K45EHsZFd0xOqx81foE9hfz08pGXzjFALgzOL5N-R30x5IC2nxIi3AR14PyIMKhAc5os-0WTtXOVuU62gXwDSaChEhVNJu5R-3kYWOQK-q5Zxb65GhKT2igEwG9SoXJ3bzcdaPBy")
soup = BeautifulSoup(response.text, "html.parser")

# Print first 10 <a> tags
links = soup.find_all("a")
print("First 10 links on the page:")
for tag in links[:10]:
    href = tag.get("href")
    text = tag.get_text().strip()
    print(f"• {text} → {href}")

