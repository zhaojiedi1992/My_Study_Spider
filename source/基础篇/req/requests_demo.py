import requests
url="https://docs.scrapy.org/en/latest/"
response = requests.get(url)
html = response.text
print(html)