import requests
from bs4 import BeautifulSoup

url = 'https://oxylabs.io/blog'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
blog_titles = soup.select('h5')
for count, title in enumerate(blog_titles):
    if count != 0:
        print(f'#{count}:', title.text)
