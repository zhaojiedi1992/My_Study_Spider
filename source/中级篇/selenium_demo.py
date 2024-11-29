from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq



class Huya:
    def __init__(self,url):
        self.url = url 
    def init_web(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 30)

    def do(self):
        self.init_web()
        self.index_page(self.url)
        items = list(self.parse_page())
        return items

    def parse_page(self):
        html =  self.browser.page_source
        doc = pq(html)
        for item in doc("#js-live-list .game-live-item").items(): 
              #print(pq(item).outerHtml() )
              #break
              product = {
              
                'title': item.find('.nick').text(),
                'num': item.find(".js-num").text(),
            }
              yield product
        pass

    def index_page(self,url): 
        print(f'正在爬取{url}')
        try:
            # url="https://www.huya.com/g/lol"
            self.browser.get(url)
            # 特定元素出现
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.item-mask')))
            print(f'成功爬取{url}')
        except TimeoutException:
            pass

if __name__ == '__main__':
    huya = Huya("https://www.huya.com/g/lol")
    items=huya.do()
    print(items)
        
