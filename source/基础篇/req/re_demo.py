import requests
import re
url="https://quotes.toscrape.com/"
response = requests.get(url)
html_text = response.text
# print(html)
#   <a class="tag" style="font-size: 6px" href="/tag/simile/">simile</a>
pattern = r'<a class="tag" .*href="(?P<href>[^"]*?)">(?P<text>.*?)<\/a>'
matches_iter = re.finditer(pattern, html_text)
for match in matches_iter:
    href = match.group('href')
    text = match.group('text')
    print(f"href: {href}, text: {text}")
 