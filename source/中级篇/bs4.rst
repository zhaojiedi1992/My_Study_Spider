bs4
====================================================
bs4是BeautifulSoup简称，能更好的解析html和xml的。 
比如我们有如下html文档。

.. code-block:: html

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


bs4 节点选择器
----------------------------------------------------------


bs  方法选择器
----------------------------------------------------------

bs  CSS选择器
----------------------------------------------------------

.. literalinclude:: bs4_demo.py
   :encoding: utf-8
   :language: python
   :linenos:
