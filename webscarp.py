import requests
from bs4 import BeautifulSoup

# Step 1: Choose a website (example: BBC News)
URL = "https://www.bbc.com/news"

# Step 2: Fetch the page
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 3: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines (check site structure; here <h2> is used)
headlines = []
for h in soup.find_all("h2"):
    text = h.get_text().strip()
    if text:  # avoid empty strings
        headlines.append(text)

# Step 5: Save to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, start=1):
        file.write(f"{i}. {headline}\n")

print(f"✅ {len(headlines)} headlines saved to headlines.txt")
