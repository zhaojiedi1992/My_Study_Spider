requests
===========================================

`官方文档 <https://requests.readthedocs.io/en/latest/>`_


获取下网页源码
---------------------------------------

.. literalinclude:: requests_demo.py
   :encoding: utf-8
   :language: python
   :linenos:


通过正则表达式进行信息提取
---------------------------------------
比如我们想提取到首页的文章的tag信息。 可以通过浏览器的debug获取到关键的信息如下。

.. code-block:: html

   <a class="tag" style="font-size: 6px" href="/tag/simile/">simile</a>


.. literalinclude:: re_demo.py
   :encoding: utf-8
   :language: python
   :linenos:


