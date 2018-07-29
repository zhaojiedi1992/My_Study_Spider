scrapyd
=====================================================

安装
------------------------------------------------

需求环境
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- >=Python 2.6
- >=Twisted 8.0 
- >=Scrapy 0.17

通用安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    [root@102 ~]$ pip install scrapyd
    Collecting scrapyd
    Downloading scrapyd-1.2.0-py2.py3-none-any.whl
    Requirement already satisfied: six in /usr/lib/python2.7/site-packages (from scrapyd)
    Requirement already satisfied: Twisted>=8.0 in /usr/lib64/python2.7/site-packages (from scrapyd)
    Requirement already satisfied: Scrapy>=1.0 in /usr/lib64/python2.7/site-packages (from scrapyd)
    Requirement already satisfied: zope.interface>=3.6.0 in /usr/lib64/python2.7/site-packages (from Twisted>=8.0->scrapyd)
    Requirement already satisfied: constantly>=15.1 in /usr/lib/python2.7/site-packages (from Twisted>=8.0->scrapyd)
    Requirement already satisfied: incremental>=16.10.1 in /usr/lib/python2.7/site-packages (from Twisted>=8.0->scrapyd)
    Requirement already satisfied: Automat>=0.3.0 in /usr/lib/python2.7/site-packages (from Twisted>=8.0->scrapyd)
    Requirement already satisfied: hyperlink>=17.1.1 in /usr/lib/python2.7/site-packages (from Twisted>=8.0->scrapyd)
    Requirement already satisfied: PyDispatcher>=2.0.5 in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: lxml in /usr/lib64/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: service-identity in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: w3lib>=1.17.0 in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: pyOpenSSL in /usr/lib64/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: parsel>=1.1 in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: cssselect>=0.9 in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: queuelib in /usr/lib/python2.7/site-packages (from Scrapy>=1.0->scrapyd)
    Requirement already satisfied: setuptools in /usr/lib/python2.7/site-packages (from zope.interface>=3.6.0->Twisted>=8.0->scrapyd)
    Requirement already satisfied: attrs in /usr/lib/python2.7/site-packages (from Automat>=0.3.0->Twisted>=8.0->scrapyd)
    Requirement already satisfied: pyasn1 in /usr/lib/python2.7/site-packages (from service-identity->Scrapy>=1.0->scrapyd)
    Requirement already satisfied: pyasn1-modules in /usr/lib/python2.7/site-packages (from service-identity->Scrapy>=1.0->scrapyd)
    Installing collected packages: scrapyd
    Successfully installed scrapyd-1.2.0

.. note:: 如果提示python.h文件文件缺失或者gcc命令不存在，请安装开发环境yum groupinstall "development tools"。


开发工程
------------------------------------------------


API接口
------------------------------------------------

配置文件
------------------------------------------------

