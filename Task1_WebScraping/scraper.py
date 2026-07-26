import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Check if request was successful
if response.status_code != 200:
    print("Failed to fetch the website.")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Print website title
print("Website Title:")
print(soup.title.text)

# Find all book containers
books = soup.find_all("article", class_="product_pod")

print(f"\nTotal Books Found: {len(books)}\n")

# Store scraped data
data = []

# Extract book title and price
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()

    data.append({
        "Title": title,
        "Price": price
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("books.csv", index=False)

print("Data saved successfully to books.csv\n")

# Display first 5 rows
print(df.head())