selenium
====================================================
对于动态渲染类页面，如果能通过ajax直接获取数据那是最好的， 如果ajax处理的数据还需要浏览器的js相关复杂处理，那可能就需要selenium了。
做到可见即可爬。对于一些 JavaScript 动态渲染的页面来说，此种抓取方式非常有效。

入门selenium
----------------------------------------------------------

.. code-block:: python

    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()

基本操作
----------------------------------------------------------
通过selenium启动一个浏览器，我们需要进行元素查找，进行交换操作（点击、填充、拖拽）。甚至可以执行自定义的javascript脚本。
