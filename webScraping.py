import requests
from bs4 import BeautifulSoup
import pandas as pd


data = {'title     ': [], '  price ': []}

url = 'https://www.aliexpress.com/w/wholesale-laptops.html?spm=a2g0o.home.search.0'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('div', class_='multi--title--G7dOCj3')  
prices = soup.find_all('div', class_='multi--price-sale--U-S0jtj')

for title in titles:
    print(title.get_text(strip=True))
    data['title     '].append(title.get_text(strip=True))

for price in prices:
    print(price.get_text(strip=True))
    data[  '  price '].append(price.get_text(strip=True))


df = pd.DataFrame.from_dict(data)
try:
    df.to_csv('data.csv', index=False)
    print("Excel file created successfully.")
except Exception as e:
    print(f"Error creating Excel file: {e}")
