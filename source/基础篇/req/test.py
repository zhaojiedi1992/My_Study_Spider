
import urllib.request


url="http://www.ip.cn"
proxy_handler = urllib.request.ProxyHandler({"http":"91.147.221.160:41766"})
opener = urllib.request.build_opener(proxy_handler)
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]
response = opener.open(url)
html = response.read().decode('utf-8')
print(html)