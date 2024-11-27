# [节点选择器 start]
html_content="""
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
print(soup.div.ul.li.contents)
# ['Foo']
# [节点选择器 end]


# 方法选择器
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
print(soup.find_all(name="li"))



# css选择器

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
# print(soup.select("div.panel-body > ul.list"))
# print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
for li in soup.select('ul li'):
    print(li.text)

