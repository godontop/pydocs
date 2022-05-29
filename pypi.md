* [PyPI](#pypi)
    * [aiohttp](#aiohttp)
    * [Beautiful Soup](#beautiful-soup)
    * [chardet](#chardet)
    * [Django](#django)
        * [settings.py](#settingspy)
    * [Flask](#flask)
    * [Gerapy](#gerapy)
    * [IPython](#ipython)
        * [Installation](#installation)
            * [安装IPython内核](#安装ipython内核)
                * [Kernels for Python 2 and 3](#kernels-for-python-2-and-3)
    * [lxml](#lxml)
    * [matplotlib](#matplotlib)
    * [mitmproxy](#mitmproxy)
    * [MySQL-python](#mysql-python)
    * [NumPy](#numpy)
    * [openpyxl](#openpyxl)
    * [pandas](#pandas)
        * [索引与选择数据](#索引与选择数据)
        * [选项和设置](#选项和设置)
        * [Pandas API 参考](#pandas-api-参考)
            * [输入/输出](#输入输出)
            * [通用函数](#通用函数)
            * [Series](#series)
            * [DataFrame](#dataframe)
    * [pip](#pip)
    * [PyMongo](#pymongo)
    * [PyMySQL](#pymysql)
    * [pyquery](#pyquery)
    * [pyspider](#pyspider)
    * [redis-py](#redis-py)
    * [Requests](#requests)
    * [SciPy](#scipy)
    * [Scrapy](#scrapy)
    * [Scrapy-Redis](#scrapy-redis)
    * [Scrapy-Splash](#scrapy-splash)
    * [Scrapyd](#scrapyd)
    * [Scrapyd API](#scrapyd-api)
    * [Scrapyd-Client](#scrapyd-client)
    * [Scrapyrt](#scrapyrt)
    * [Selenium](#selenium)
    * [tesserocr](#tesserocr)
    * [Tornado](#tornado)
    * [tushare](#tushare)


## PyPI
### aiohttp
用于 [asyncio](https://aiohttp.readthedocs.io/en/stable/glossary.html#term-asyncio) 和 Python 的异步 HTTP 客户端/服务器。  

官方文档：[https://aiohttp.readthedocs.io/en/stable/](https://aiohttp.readthedocs.io/en/stable/)  
GitHub：[https://github.com/aio-libs/aiohttp](https://github.com/aio-libs/aiohttp)  

**库安装**

```sh
$ pip install aiohttp
```

你可能想安装可选的 [cchardet](https://aiohttp.readthedocs.io/en/stable/glossary.html#term-cchardet) 库替换 [chardet](https://aiohttp.readthedocs.io/en/stable/glossary.html#term-chardet) ，因为 [cchardet](https://aiohttp.readthedocs.io/en/stable/glossary.html#term-cchardet) 更快：

```sh
$ pip install cchardet
```

为了通过客户端 API 加速DNS解析你也可以安装 [aiodns](https://aiohttp.readthedocs.io/en/stable/glossary.html#term-aiodns)。高度推荐这个选择：

```sh
$ pip3 install aiodns
```

### Beautiful Soup
官方文档：[https://www.crummy.com/software/BeautifulSoup/bs4/doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
中文文档：[https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)  

安装Beautiful Soup  

```sh
$ pip3 install beautifulsoup4
```

**注意**  
这里我们虽然安装的是 beautifulsoup4 这个包，但是在引入的时候却是 bs4。这是因为这个包源代码本身的库文件夹名称就是 bs4，所以安装完成之后，这个库文件夹就被移入到本机 Python3 的 lib 库（/usr/local/lib/python3.6/site-packages）里，所以识别到的库文件名就叫作 bs4。

因此，包本身的名称和我们使用时导入的包的名称并不一定是一致的。  

### 安装解析器
Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 [lxml](http://lxml.de/) .根据操作系统不同,可以选择下列方法来安装lxml:  

$ apt-get install Python-lxml  

$ easy_install lxml  

$ pip install lxml  

另一个可供选择的解析器是纯Python实现的 [html5lib](http://code.google.com/p/html5lib/) , html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:  

$ apt-get install Python-html5lib  

$ easy_install html5lib  

$ pip install html5lib  

下表列出了主要的解析器,以及它们的优缺点:  

解析器        |使用方法                               |优势  |劣势  
-------------|--------------------------------------|------|------
Python标准库  |BeautifulSoup(markup, "html.parser")  |<ul><li>Python的内置标准库</li><li>执行速度适中</li><li>文档容错能力强</li></ul>  |Python 2.7.3 或 3.2.2 以前的版本中文档容错能力差  
lxml HTML 解析器  |BeautifulSoup(markup, "lxml")  |<ul><li>速度快</li><li>文档容错能力强</li></ul>  |<ul><li>需要安装C语言库</li></ul>  
lxml XML 解析器  |BeautifulSoup(markup, ["lxml-xml"])<br><br>BeautifulSoup(markup, "xml")  |<ul><li>速度快</li><li>唯一支持XML的解析器</li></ul>  |<ul><li>需要安装C语言库</li></ul>  
html5lib  |BeautifulSoup(markup, "html5lib")  |<ul><li>最好的容错性</li><li>以浏览器的方式解析文档</li><li>生成HTML5格式的文档</li></ul>  |<ul><li>速度慢</li><li>不依赖外部扩展</li></ul>  

推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.  

提示: 如果一段HTML或XML文档格式不正确的话,那么在不同的解析器中返回的结果可能是不一样的。  

从文档中获取所有文字内容  

```python
>>> from bs4 import BeautifulSoup
>>> html_doc = """
... <div bdsfid="72" class="answer_2AM9f">动词加ed的读音主要有三种：<br bdsfid="73">以清辅音结尾的读t,如worked<br bdsfid="74">以浊辅音结尾的读d,如rained.<br bdsfid="75">以t和d结尾的读id.如needed.</div>
... """
>>> soup = BeautifulSoup(html_doc, 'html.parser')
>>> print(soup)

<div bdsfid="72" class="answer_2AM9f">动词加ed的读音主要有三种：<br bdsfid="73"/>以清辅音结尾的读t,如worked<br bdsfid="74"/>以浊辅音结尾的读d,如rained.<br bdsfid="75"/>以t和d结尾的读id.如needed.</div>

>>> print(soup.get_text())

动词加ed的读音主要有三种：以清辅音结尾的读t,如worked以浊辅音结尾的读d,如rained.以t和d结尾的读id.如needed.
              
>>> html_doc2 = soup.prettify()
>>> print(html_doc2)
<div bdsfid="72" class="answer_2AM9f">
 动词加ed的读音主要有三种：
 <br bdsfid="73"/>
 以清辅音结尾的读t,如worked      
 <br bdsfid="74"/>
 以浊辅音结尾的读d,如rained.                                                                                  
 <br bdsfid="75"/>                                                              
 以t和d结尾的读id.如needed.
</div>                                           
                   
>>> soup2 = BeautifulSoup(html_doc2, 'html.parser')                                                            
>>> print(soup2.get_text())

 动词加ed的读音主要有三种：                                                                              

 以清辅音结尾的读t,如worked    
                   
 以浊辅音结尾的读d,如rained.
                                                                                                                         
 以t和d结尾的读id.如needed.                                                 

   
>>>         
```

## chardet
官方文档：[https://chardet.readthedocs.io/en/latest/index.html](https://chardet.readthedocs.io/en/latest/index.html)

```python
>>> import urllib
>>> rawdata = urllib.urlopen('http://yahoo.co.jp/').read()
>>> import chardet
>>> chardet.detect(rawdata)
{'encoding': 'EUC-JP', 'confidence': 0.99}
```

```python
import urllib.request
import chardet


proxy_handler = urllib.request.ProxyHandler(proxies={'https': 'https://127.0.0.1:11824'})
opener = urllib.request.build_opener(proxy_handler)
page = opener.open('https://www.google.com')
print(chardet.detect(page.read()))
```

上面代码的运行结果为：

```
{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
```

## Django
Django官网  
[https://www.djangoproject.com](https://www.djangoproject.com)

### 安装Django  
pip3 install Django

#### settings.py
**ALLOWED_HOSTS**

默认值：[]（空列表）

一个表示 Django 站点可以服务的主机/域名名称的字符串列表。

当 **DEBUG** 为 True 且 **ALLOWED_HOSTS** 为空时，针对列表 **['localhost', '127.0.0.1', '[::1]']** 中的主机是有效的。
<br><br>

**TIME_ZONE**

默认值： **'America/Chicago'**

一个表示时区的字符串。看[时区列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)。

**注解**

自从 Django 第一版发布将 **TIME_ZONE** 设置为 **'America/Chicago'** 以来，全局设置 (如果你的项目的 **settings.py** 中什么都没定义则使用) 保持 **'America/Chicago'** 是为了向后兼容。新项目模板默认为 **'UTC'**。

### django.contrib.auth
django.contrib.auth 是 Django 开发的认证框架，它提供 “组和用户” 相关功能。  

### 创建项目
创建一个名为mysite的项目  
$ django-admin startproject mysite  

#### 创建一个应用
创建一个名为web的应用  
$ python3 manage.py startapp web  

创建应用后需要修改项目的urls.py文件，将新应用添加到urlpatterns中。  

{% 和 {{ 标签是 Django 模板语言的一部分。

### Flask
GitHub：[https://github.com/pallets/flask](https://github.com/pallets/flask)  
官方文档：[http://flask.pocoo.org](http://flask.pocoo.org)  
中文文档：[http://docs.jinkan.org/docs/flask](http://docs.jinkan.org/docs/flask/)  

安装Flash

```sh
$ pip3 install flask
```

### Gerapy
GitHub：[https://github.com/Gerapy/Gerapy](https://github.com/Gerapy/Gerapy)  
PyPI：[https://pypi.org/project/gerapy/](https://pypi.org/project/gerapy/)  

**安装Gerapy**

```sh
pip3 install gerapy
```

## IPython
官方文档：[https://ipython.readthedocs.io/en/stable/index.html](https://ipython.readthedocs.io/en/stable/index.html)

### Installation
#### 安装IPython内核
##### Kernels for Python 2 and 3
If you’re running Jupyter on Python 3, you can set up a Python 2 kernel like this:

```
python2 -m pip install ipykernel
python2 -m ipykernel install --user
```

**On Windows:**  

```
py -2 -m pip install ipykernel
py -2 -m ipykernel install --user
```

If you’re running Jupyter on Python 2 and want to set up a Python 3 kernel, follow the same steps, replacing `2` with `3`.

The last command installs a [kernel spec](https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernelspecs) file for the current python installation. Kernel spec 文件是JSON文件，可以被普通文本编辑器浏览和修改。

### 教程
#### 内置魔法命令
**注意**

To Jupyter users: Magics are specific to and provided by the IPython kernel. Whether Magics are available on a kernel is a decision that is made by the kernel developer on a per-kernel basis. 为了正确地工作，Magics 必须使用一个在底层语言中无效的语法元素。例如，the IPython kernel uses the `%` syntax element for Magics as `%` is not a valid unary operator in Python. 然而，`%` 可能在其它语言中有意义。

**%load**  
加载代码到当前的前端。

用法：  
%load [options] source

其中 source 可以是一个文件名，URL，输入历史范围，宏，或者用户命名空间中的元素

用法举例：  

```
%load myfile.txt
%load temp.py
```

### lxml
官方网站：[https://lxml.de](https://lxml.de)  
GitHub：[https://github.com/lxml/lxml](https://github.com/lxml/lxml)  

安装lxml

```sh
$ pip3 install lxml
```

## matplotlib
PyPI链接：[https://pypi.org/project/matplotlib/](#https://pypi.org/project/matplotlib/)  

### 安装matplotlib
pip install matplotlib

引用 matplotlib API 通常使用标准约定：  

```python
import matplotlib.pyplot as plt

# 如果你正在使用 Jupyter Notebook，你可能也想运行下面这行代码，以便在你的 notebook 中显示你的代码：

%matplotlib inline
```

### 用法
简单的折线图  

```python
>>> import matplotlib.pyplot as plt
>>> x_data = ['01', '02', '03', '04', '05']
>>> y_data = [1.1, 1.5, 1.7, 2.0, 2.5]
>>> plt.plot(x_data, y_data)
>>> plt.xlabel('month')  # 设置x轴的标签
>>> plt.ylabel('ratio')  # 设置y轴的标签
>>> plt.title('600031')  # 设置绘图的标题
>>> plt.show()
>>>
```

![简单的折线图](./img/simple_matplotlib_1.png)  

### matplotlib.pyplot.plot
Plot y versus x as lines and/or markers.

Call signatures:  
plot([x], y, [fmt], \*, data=None, \*\*kwargs)  

可选参数 *fmt* 是一种用于定义基本格式如颜色，标记及线条样式的简单方式。

#### 格式化字符串
格式字符串由颜色，标记及线条的一部分组成：

`fmt = '[marker][line][color]'`

**标记**  

字符 |描述
-----|----
'.'  |点标记
'o'  |圆标记

**线条风格**  

字符 |描述
-----|-----
'-'  |实线风格
'--' |虚线风格

**颜色**  

支持的颜色缩写是单个字母代码

字符 |颜色
-----|-----
'b'  |blue
'g'  |green
'r'  |red
'c'  |cyan
'm'  |magenta
'y'  |yellow
'k'  |black
'w'  |white

### mitmproxy
GitHub：[https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)  
官方网站：[https://mitmproxy.org](https://mitmproxy.org)  
官方文档：[https://docs.mitmproxy.org/stable/](https://docs.mitmproxy.org/stable/)  
mitmdump：[https://docs.mitmproxy.org/stable/tools-mitmdump/](https://docs.mitmproxy.org/stable/tools-mitmdump/)  
下载地址：[https://github.com/mitmproxy/mitmproxy/releases](https://github.com/mitmproxy/mitmproxy/releases)  
DockerHub：[https://hub.docker.com/r/mitmproxy/mitmproxy](https://hub.docker.com/r/mitmproxy/mitmproxy)  

#### 安装mitmproxy  

**Windows平台**  
到 [https://github.com/mitmproxy/mitmproxy/releases](https://github.com/mitmproxy/mitmproxy/releases) 页面下载 mitmproxy-4.0.1-windows-installer.exe 文件，之后双击即可安装。

**Linux平台**  
CentOS 7.6.1810  
到 [https://github.com/mitmproxy/mitmproxy/releases](https://github.com/mitmproxy/mitmproxy/releases) 页面下载 mitmproxy-3.0.3-linux.tar.gz 文件，因为 mitmproxy 3.0.3 以上的版本要求glibc的版本为2.18，而CentOS 7.6的glibc版本为2.17，所以无法使用更新版本的mitmproxy。

```sh
$ cd /usr/local/bin
$ wget https://github.com/mitmproxy/mitmproxy/releases/download/v3.0.3/mitmproxy-3.0.3-linux.tar.gz
$ tar zxvf mitmproxy-3.0.3-linux.tar.gz
$ rm -f mitmproxy-3.0.3-linux.tar.gz
```

`tar zxvf mitmproxy-3.0.3-linux.tar.gz` 命令会将 mitmproxy-3.0.3-linux.tar.gz 文件中的三个可执行文件解压到当前目录，这三个可执行文件分别是mitmproxy、mitmdump和mitmweb。

**macOS平台**  

```sh
$ brew install mitmproxy
```

#### 配置mitmproxy证书
运行mitmdump命令以产生CA证书（产生的CA证书在用户的HOME目录下的.mitmproxy目录，Windows为 `%USERPROFILE%\.mitmproxy`，Linux及macOS为 `~/.mitmproxy`），并启动mitmdump；

证书及其说明

名称                    |描述
-----------------------|------------------------------------
mitmproxy-ca-cert.p12  |PKCS12 格式的证书，适用于Windows平台
mitmproxy-ca-cert.pem  |PEM 格式证书，适用于大多数非Windows平台

**Windows平台**  
1. 双击 mitmproxy-ca-cert.p12，之后“下一步”即可，在“私钥保护”界面不用设置密码，直接“下一步”；
2. 在“证书存储”界面选择“将所有的证书都放入下列存储”——“受信任的根证书颁发机构”；

**macOS平台**  
1. 双击 mitmproxy-ca-cert.pem 文件，之后点击“添加”；
2. 在“钥匙串访问”窗口中找到“mitmproxy”，之后双击该证书，然后展开“信任”，在“使用此证书时”后面的下拉选项框中选择“始终信任”即可。

**Android平台**  
在移动设备上配置正确的代理设置（配置代理前要在PC上启动mitmdump），然后访问 http://mitm.it 。之后点击Android图标下载证书，下载完成后会提示安装，填好证书名称再点确定即可。


## MySQL-python
简介：Python interface to MySQL  
官方主页：[https://pypi.org/project/MySQL-python/](https://pypi.org/project/MySQL-python/)  
这个包（最新的发布日期是2014-01-03）至今都不支持 Python 3，且这个库需要编译安装，安装前需要安装 MySQL 和 Python 的开发包，MySQL 的 Python 接口不建议使用这个库。  

### 项目描述

MySQLdb is an interface to the popular [MySQL](http://www.mysql.com/) database server for Python. 设计目标是：

* Compliance with Python database API version 2.0 [[PEP-0249](http://www.python.org/peps/pep-0249.html)]  
* Thread-safety  
* Thread-friendliness (threads will not block each other)  

当前支持 MySQL-3.23 到 5.5 以及 Python-2.4 到 2.7 。未来的版本将支持 Python-3.0 。支持 PyPy 。

安装 MySQL-python  
`pip install MySQL-python`  

**用法**  

```python
>>> import MySQLdb
>>>
```

**注意：** 安装 MySQL-python 库以后，导入的模块名是 **MySQLdb**。

## NumPy
习惯上，我们按以下方式导入numpy：

```python
import numpy as np
```

### NumPy: 初学者的绝对基础
#### 欢迎来到 NumPy!
NumPy (**Numerical Python**) 是一个开源的 Python 库，它几乎用于科学与工程学的每一个领域。NumPy API 广泛用于 Pandas, SciPy, Matplotlib, scikit-learn, scikit-image 以及大多数其它数据科学及与科学有关的 Python 包。

**ndarray** —— a homogeneous n-dimensional array（一个同类型的N维数组）

#### 关于 arrays 的更多信息
NumPy **ndarray** 类被用于表示矩阵及向量。一个**向量**是一个一维数组 (行向量和列向量之间没有区别)，而一个**矩阵**指的是一个二维数组。对于 **3-D** 或 更高维度的数组，通常使用术语张量。  

在 NumPy 中，维被称为**坐标轴**。   

**ndarray.ndim** 将高速你数组的坐标轴或者维的个数。  

**ndarray.shape** 将显示一个整型数元组用以表明数组的每个维所存储的元素的个数。例如，如果你有一个2行3列的2维数组，则你的数组的形状是 (2, 3)。  


### numpy.arange
numpy.**arange**([*start*, ]*stop*, [*step*, ]*dtype=None*)  
在指定的区间内返回等间距的值。

```python
>>> np.arange(3)
array([0, 1, 2])
>>> type(np.arange(3))
<class 'numpy.ndarray'>
>>>
```

返回值：  
类型：*ndarray*  

### numpy.ndarray.reshape
方法  

ndarray.**reshape**(*shape, order='C'*)  
返回一个包含相同数据的新的形状的数组。

完整的文档请参考 [numpy.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape)。

**另请参考：**  
[numpy.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape) 等价函数

**注意**  
与自由函数 [numpy.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape) 不同，这个 [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray) 方法允许形状参数的元素作为单独的参数被传递。例如，`a.reshape(10, 11)` 等同于 `a.reshape((10, 11))`。

```python
>>> a = np.arange(6)
>>> type(a)
<class 'numpy.ndarray'>
>>> a.reshape(3, 2)
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> np.arange(6).reshape(3, 2)
array([[0, 1],
       [2, 3],
       [4, 5]])
>>>
```

### numpy.random.randn
numpy.random.**randn**(*d0, d1, ..., dn*)  
如果没有指定参数则返回一个随机的浮点数。  

**参数：**  
整型数，可选的

**返回值：**  
浮点数或者 ndarray 类型的数组  

```python
>>> np.random.randn()
-1.2479550666117432
```

```python
>>> np.random.randn(2, 3)
array([[ 2.19473825,  1.1897689 , -0.27926663],
       [ 0.16774206,  0.05763704,  0.54997363]])
>>> type(np.random.randn(2, 3))
<class 'numpy.ndarray'>
>>> df =pd.DataFrame(np.random.randn(2, 3), columns=list('ABC'))
>>> df
          A         B         C
0 -0.150573 -0.545417  0.112082
1 -0.238589  1.684458  0.141182
>>>
```

`pd.DataFrame(np.random.randn(2, 3), columns=list('ABC'))` 返回的是一个2行3列的 DataFrame。  

```python
>>> np.random.randn(3)
array([-1.00131874, -1.56444553, -0.44134847])
>>> np.random.randn(3, 1)
array([[1.22019482],
       [0.47821871],
       [2.00688915]])
>>> pd.DataFrame(np.random.randn(3))
          0
0  1.348695
1 -0.592470
2 -2.501976
>>> pd.DataFrame(np.random.randn(3, 1))
          0
0 -2.009443
1  1.227551
2  0.116526
>>>
```

通过 np.random.randn() 来构建 DataFrame 时，np.random.randn() 的第一个参数表示行数，第二个参数表示列数，如果第二个没有，则表示列数为 1。  

```python
>>> s1 = pd.Series(np.random.randn(3), index=list('abc'))
>>> s1
a   -0.276098
b    0.571327
c   -0.605284
dtype: float64
>>>
```

构建 Series 的数据必须是一维的，所以通过 np.random.randn() 来构建 Series 对象时只能使用一个参数。  

### numpy.reshape
numpy.**reshape**(*a, newshape, order='C'*)  
在不改变数组数据的前提下给出一个新的数组形态。

**参数：**  
**a：** **_array_like_**  
需要被改造的数组。  

**newshape：**  
*整型数或者整型数元组*  
新的形状应该与原始的形状相兼容。  

**返回值：**  
**reshaped_array：** **_ndarray_** 类型  

**另请参考：**  
[ndarray.reshape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape) 等价方法。

```python
>>> a = np.arange(6).reshape((3, 2))
>>> a
array([[0, 1],
       [2, 3],
       [4, 5]])
>>>
```

### 术语表
**along an axis**  
参考链接：[https://docs.scipy.org/doc/numpy-1.10.0/glossary.html](https://docs.scipy.org/doc/numpy-1.10.0/glossary.html)  
轴被用于定义超过一维的数组。一个 2 维的数组有两个对应的轴：第一个垂直向下穿过行 (axis 0)，而第二个水平运行穿过列 (axis 1)。  

许多操作可以沿着一个轴发生。例如，we can sum each row of an array, in which case we operate along columns, or axis 1:  

```python
>>> x = np.arange(12).reshape((3, 4))
>>> x
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> x.sum(axis=1)
array([ 6, 22, 38])
>>>
```

**along an axis**  
参考链接：[https://numpy.org/doc/stable/glossary.html](https://numpy.org/doc/stable/glossary.html)  
沿着数组 **a** 的*轴 n* 的一个操作的行为就好像它的参数是数组 **a** 的分片，并且每个分片都有一个连续的轴 *n* 索引。    

例如，如果 **a** 是一个 3 x *N* 数组，一个沿轴 0 的操作行为就好像它的参数是一个包含每一行分片的数组一样：  

```python
>>> np.array((a[0,:], a[1,:], a[2,:]))
```

为使它更具体，我们可以选择操作数组逆转的函数 [numpy.flip](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip)，它接受一个 **axis** 参数。我们构造一个 3 x 4 的数组 **a**：  

```python
>>> a = np.arange(12).reshape(3, 4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> 
```

沿轴 0 反转 (the row axis)   

```python
>>> np.flip(a, axis=0)
array([[ 8,  9, 10, 11],
       [ 4,  5,  6,  7],
       [ 0,  1,  2,  3]])
>>> 
```

回顾沿一个轴的定义，沿轴 0 翻转对待它的参数就好像它是  

```python
>>> np.array((a[0,:], a[1,:], a[2,:]))
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
```

而 **np.flip(a,axis=0)** 的结果是反转分片：  

```python
>>> np.array((a[2,:], a[1,:], a[0,:]))
array([[ 8,  9, 10, 11],
       [ 4,  5,  6,  7],
       [ 0,  1,  2,  3]])
>>> 
```

三维数组  

```python
>>> a = np.arange(27).reshape(3, 3, 3)                                                            
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
>>> a[0,:,:]
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> a[:,0,:]
array([[ 0,  1,  2],
       [ 9, 10, 11],
       [18, 19, 20]])
>>> a[:,:,0]
array([[ 0,  3,  6],
       [ 9, 12, 15],
       [18, 21, 24]])
>>> a.sum(axis=0)     
array([[27, 30, 33],
       [36, 39, 42],
       [45, 48, 51]])
>>> a[0,:,:] + a[1,:,:] + a[2,:,:]   
array([[27, 30, 33],
       [36, 39, 42],
       [45, 48, 51]])
>>> a.sum(axis=1)
array([[ 9, 12, 15],
       [36, 39, 42],
       [63, 66, 69]])
>>> a[:,0,:] + a[:,1,:] + a[:,2,:]      
array([[ 9, 12, 15],
       [36, 39, 42],
       [63, 66, 69]])
>>> a.sum(axis=2)
array([[ 3, 12, 21],
       [30, 39, 48],
       [57, 66, 75]])
>>> a[:,:,0] + a[:,:,1] + a[:,:,2]     
array([[ 3, 12, 21],
       [30, 39, 48],
       [57, 66, 75]])
>>> 
```

## openpyxl
介绍：openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.  

**安装**  

```sh
pip install openpyxl
```

如果需要将 pandas DataFrame 数据导出为 Excle 文件，则必须安装 openpyxl。  

## pandas
官方网站：[https://pandas.pydata.org](https://pandas.pydata.org)  
PyPi主页：[https://pypi.org/project/pandas/](https://pypi.org/project/pandas/)  
pandas 参考手册：[https://pandas.pydata.org/pandas-docs/stable/reference/index.html](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)  

### 安装pandas
$ pip install pandas  

习惯上，我们按以下方式导入：  

```python
import pandas as pd
```

### 索引与选择数据
#### 索引的不同选择
为了支持更明确的位置，对象选择已经添加了一些用户要求的基本索引。Pandas 现在支持三种类型的多轴索引。

* .loc 主要是基于标签，但是也可以和一个布尔数组一起使用。当元素没有找到时 .loc 将抛出 KeyError 。允许的输入是： 

    * 一个单一的标签，例如 5 或者 'a' (注意 5 被解释为一个索引标签。这种用法 **不是** 沿着索引位置的一个整型数。)。

    * 一个列表或标签数组 ['a', 'b', 'c']。

    * 一个标签分片对象 `'a':'f'` (注意与通常的 python 分片相反，当起点（'a'）和终点（'f'）都在索引中出现时，它们将都被包含！参见 [标签分片](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-slicing-with-labels) 及 [端点被包含](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-endpoints-are-inclusive)。)

    * 一个布尔数组 (所有 NA 值都将被当作 False)。

    * A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).

  更多信息参见 [通过标签选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label)。

* .iloc 主要是基于位置的整型数 (从 0 到 轴的长度减1)，但也可以和一个布尔数组一起使用。如果请求的索引在界外，则 .iloc 将抛出 IndexError，除了分片索引，因为分片索引允许界外索引。 (这与 Python/NumPy 的 *分片* 语义一致)。允许的输入是：

    * 一个整型数，例如 5。

    * 一个整型数列表或数组 [4, 3, 0]。

    * 一个整型数分片对象 1:7。

    * 一个布尔数组 (所有 NA 值都将被作为 False)。

    * A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).

  更多信息请参考 [根据位置选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-integer)，[高级索引](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced) 和 [高级层次结构](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-advanced-hierarchical)。

* .loc，.iloc，以及 [] 索引可以接受一个可调用对象作为索引。更多信息参见 [通过可调用对象选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-callable)。

用多轴筛选从一个对象中获取值使用下面的记法 (以 .loc 为例，但下面的例子也适用于 .iloc)。任何轴存取器都可以是空分片 `:`。忽略轴的规格会假定轴为 `:`，例如 `p.loc['a']` 等同于 `p.loc['a', :]`。

对象类型   |索引  
----------|------
Series    |s.loc[indexer]  
DataFrame |df.loc[row_indexer,column_indexer]  

```python
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.DataFrame(np.arange(16).reshape(4, 4), columns=list('ABCD'), index=list('1234'))
>>> df
    A   B   C   D
1   0   1   2   3
2   4   5   6   7
3   8   9  10  11
4  12  13  14  15
>>> df.loc['1']              # 获取第'1'行的数据
A    0
B    1
C    2
D    3
Name: 1, dtype: int32
>>> df.loc['1', :]           # 获取第'1'行的数据
A    0
B    1
C    2
D    3
Name: 1, dtype: int32
>>> df.loc['1', 'B':]        # 获取第'1'行从'B'列开始的数据
B    1
C    2
D    3
Name: 1, dtype: int32
>>> df.loc['1', ['B', 'D']]  # 获取第'1'行'B'列和'D'列的数据
B    1
D    3
Name: 1, dtype: int32
>>>
```

#### 基础
就像在[上一节](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics)中介绍数据结构时提到的那样，`[]` 索引 (对于那些熟悉在 Python 中实现类行为的人来说，这亦称 `__getitem__`) 的主要功能是选出低维切片。下表展示的是当使用 `[]` 索引 pandas 对象时返回值的类型：

对象类型    |选择           |返回值类型  
-----------|---------------|-----------
Series     |series[label]  |scalar value  
DataFrame  |frame[colname] |`Series` corresponding to colname  

你可以给 `[]` 传递一个关于列的列表，然后按该列表中的顺序选择列。多列也可以通过这种方式来设置：  

```python
>>> df = pd.DataFrame(np.arange(16).reshape(4, 4), columns=list('ABCD'), index=list('1234'))
>>> df
    A   B   C   D
1   0   1   2   3
2   4   5   6   7
3   8   9  10  11
4  12  13  14  15
>>> df[['D', 'B']]
    D   B
1   3   1
2   7   5
3  11   9
4  15  13
>>>
```

#### 属性访问
你可以直接访问 Series 的一个索引或者 DataFrame 的一个列，就像访问一个属性一样：  

```python
>>> sa = pd.Series([1, 2, 3], index=list('abc'))
>>> sa.b
2
>>>
```

```python
>>> dfa = df.copy()
>>> dfa.A
1     0
2     4
3     8
4    12
Name: A, dtype: int32
>>>
```

**警告**  
* 如果一个属性与一个已存在的方法名冲突了，则该属性将不可用，例如 `s.min` 是不被允许的，但 `s['min']` 是可以的。  

你也可以将一个字典赋值给 DataFrame 的一个行：  

```python
>>> x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
>>> x.iloc[1] = {'x': 9, 'y': 99}
>>> x
   x   y
0  1   3
1  9  99
2  3   5
>>>
```

你可以使用属性访问来修改一个已存在的 Series 元素或者 DataFrame 列，但是要小心；如果你尝试使用属性访问来创建一个新列，它将创建一个新属性而不是一个新列。在 0.21.0 及更新的版本中，这将抛出一个 `UserWarning`：  

```python
>>> df = pd.DataFrame({'one': [1., 2., 3.]})
>>> df.two = [4, 5, 6]
__main__:1: UserWarning: Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access
>>> df
   one
0  1.0
1  2.0
2  3.0
>>>
```

#### 切片范围
沿任意轴切片范围的最稳健及一致的方式在 [按位置选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-integer) 章节的 `.iloc` 方法的详述中描述。从现在起，我们解释使用 `[]` 运算符分片的语法。

对于 Series，当使用一个 ndarray 时，句法正确地工作，返回一个值切片及对应的标签：  

```python
In [945]: s[:5]              
Out[945]: 
2000-01-01    0.934894
2000-01-02   -1.052417
2000-01-03   -1.239888
2000-01-04   -1.125825
2000-01-05   -0.768745
Freq: D, Name: A, dtype: float64

In [946]: s[::2]             
Out[946]: 
2000-01-01    0.934894
2000-01-03   -1.239888
2000-01-05   -0.768745
2000-01-07    0.593572
Freq: 2D, Name: A, dtype: float64

In [947]: s[::-1]            
Out[947]: 
2000-01-08   -0.868615
2000-01-07    0.593572
2000-01-06   -1.268688
2000-01-05   -0.768745
2000-01-04   -1.125825
2000-01-03   -1.239888
2000-01-02   -1.052417
2000-01-01    0.934894
Freq: -1D, Name: A, dtype: float64
```

对于 DataFrame，`[]` 中的切片切割行。这大大提高了便利性，因为这是一个如此常用的操作。

```python
In [949]: df[:3]             
Out[949]: 
                   A         B         C         D
2000-01-01  0.934894  1.246335  1.000530  0.468386
2000-01-02 -1.052417 -0.121034  0.004829  2.353777
2000-01-03 -1.239888  0.839079  0.449671  0.404814

In [950]: df[::-1]           
Out[950]: 
                   A         B         C         D
2000-01-08 -0.868615 -0.824368 -0.488416  0.450658
2000-01-07  0.593572 -0.265830 -1.508893 -1.381523
2000-01-06 -1.268688  0.597614  0.618702  1.465065
2000-01-05 -0.768745  0.179232 -1.804884  0.522359
2000-01-04 -1.125825 -0.065592  0.461488  0.886664
2000-01-03 -1.239888  0.839079  0.449671  0.404814
2000-01-02 -1.052417 -0.121034  0.004829  2.353777
2000-01-01  0.934894  1.246335  1.000530  0.468386
```

#### 按标签选择
**警告**  
用于设置操作而返回的，不管是一个副本还是一个引用，可能依赖于上下文。这有时被成为链式赋值且应该被避免。参考 [返回一个视图 vs 副本](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-view-versus-copy)。

```python
In [1234]: df = pro.fund_daily(ts_code='512760.SH', start_date='20200825', end_date='20200901', fields='ts_code, trade_date, amount')                                                            

In [1235]: df                                   
Out[1235]: 
     ts_code trade_date      amount
0  512760.SH   20200901  301999.161
1  512760.SH   20200831  499673.933
2  512760.SH   20200828  457668.061
3  512760.SH   20200827  800757.929
4  512760.SH   20200826  850562.865
5  512760.SH   20200825  414941.116

In [1236]: df1 = df.head(1)                     

In [1237]: df1                                  
Out[1237]: 
     ts_code trade_date      amount
0  512760.SH   20200901  301999.161

In [1238]: df1['average_amoount'] = df.amount.mean()                                            
/usr/bin/ipython:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  #!/usr/bin/python

In [1239]: df1                                  
Out[1239]: 
     ts_code trade_date      amount  average_amoount
0  512760.SH   20200901  301999.161      554267.1775
```

通过上面的例子可以看出，当给一个 DataFrame 切片的副本添加列，并赋值时，弹出了警告。对于上述问题，有两种解决办法，一是可以先对原 DataFrame 进行操作，之后再进行切片。二是先创建一个空的 DataFrame（使其与原 DataFrame 既无引用关系，也无复制关系），再对其进行赋值。  

方法一：  

```python
In [1254]: df['average_amount'] = df.amount.mean()                                              

In [1255]: df                                   
Out[1255]: 
     ts_code trade_date      amount  average_amount
0  512760.SH   20200901  301999.161     554267.1775
1  512760.SH   20200831  499673.933     554267.1775
2  512760.SH   20200828  457668.061     554267.1775
3  512760.SH   20200827  800757.929     554267.1775
4  512760.SH   20200826  850562.865     554267.1775
5  512760.SH   20200825  414941.116     554267.1775

In [1256]: df1 = df.head(1)                     

In [1257]: df1                                  
Out[1257]: 
     ts_code trade_date      amount  average_amount
0  512760.SH   20200901  301999.161     554267.1775
```

方法二：

```python
In [1303]: df                                   
Out[1303]: 
     ts_code trade_date      amount
0  512760.SH   20200901  301999.161
1  512760.SH   20200831  499673.933
2  512760.SH   20200828  457668.061
3  512760.SH   20200827  800757.929
4  512760.SH   20200826  850562.865
5  512760.SH   20200825  414941.116

In [1304]: df1 = pd.DataFrame(columns=df.columns)                                               

In [1305]: df1                                  
Out[1305]: 
Empty DataFrame
Columns: [ts_code, trade_date, amount]
Index: []

In [1306]: df1.loc[0] = df.loc[0]               

In [1307]: df1                                  
Out[1307]: 
     ts_code trade_date      amount
0  512760.SH   20200901  301999.161

In [1308]: df1['average_amount'] = df.amount.mean()                                             

In [1309]: df1                                  
Out[1309]: 
     ts_code trade_date      amount  average_amount
0  512760.SH   20200901  301999.161     554267.1775
```

**警告**  

当你提交的分片与索引类型不兼容（或者不可转换）时，.loc 是严格的。例如在一个 `DatetimeIndex` 中使用整型数。这将抛出一个 `TypeError`。

```python
In [1310]: df1 = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'), index=pd.date_range('20130101', periods=5)) 

In [1311]: df1               
Out[1311]: 
                   A         B         C         D
2013-01-01  0.687998  0.286866 -2.024732  0.221790
2013-01-02 -0.313433  1.907409 -1.874109  1.530983
2013-01-03 -0.853349 -0.028631 -1.125664  2.389619
2013-01-04  0.089914  0.762910 -0.781565 -0.445401
2013-01-05 -0.488538 -0.221172  0.645656 -0.131853

In [1312]: df1.loc[2:3]      
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.datetimes.DatetimeIndex'> with these indexers [2] of <class 'int'>
```

对于 DatetimeIndex，分片中的类字符串可以被转换成 DatetimeIndex 类型的索引并获得正常的切片。

```python
In [1313]: df1.loc['20130102':'20130104']                  
Out[1313]: 
                   A         B         C         D
2013-01-02 -0.313433  1.907409 -1.874109  1.530983
2013-01-03 -0.853349 -0.028631 -1.125664  2.389619
2013-01-04  0.089914  0.762910 -0.781565 -0.445401
```

为了拥有**纯粹基于标签的索引**pandas 提供了一整套方法。这是一种基于协议的严格包含。每一个请求的标签都必须在索引中，否则将抛出一个 `KeyError`。当切片时，起始边界**和**终止边界都将被包含，如果它们出现在索引中的话。整型数是有效的标签，但它们指的是标签**而不是位置**。

`.loc` 属性是主要的访问方法。下面的是有效输入：  

* 一个单一的标签，例如 5 或者 'a' (注意 5 被解释为一个索引标签。这种用法**不是**一个沿着索引的整型数位置。)。

* 一个列表或者一个标签数组 `['a', 'b', 'c']`。

* 一个标签分片对象 `'a':'f'` (注意与通常的 python 分片相反，当它们出现在索引中时，开始索引（'a'）和结束索引（'f'）都将被包含！参见 [标签分片](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-slicing-with-labels)。

* 一个布尔数组。

* 一个可调用对象，参见 [通过可调用对象选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-callable)。  

```python
In [1993]: s1 = pd.Series(np.random.randn(6), index=list('abcdef'))                            

In [1994]: s1                
Out[1994]: 
a   -1.395686
b    0.424361
c   -0.258070
d   -0.868951
e   -1.274847
f   -1.050252
dtype: float64

In [1995]: s1.loc['c':]      
Out[1995]: 
c   -0.258070
d   -0.868951
e   -1.274847
f   -1.050252
dtype: float64

In [1996]: s1.loc['b']       
Out[1996]: 0.42436116596528517
```

For getting a cross section using a label (等同于 `df.xs('a')`):

```python
In [2269]: df1.loc['a']      
Out[2269]: 
A    0.088747
B    0.561819
C    0.331591
D    0.355395
Name: a, dtype: float64

In [2270]: df1.xs('a')       
Out[2270]: 
A    0.088747
B    0.561819
C    0.331591
D    0.355395
Name: a, dtype: float64
```

当 DataFrame 的列超过了一屏时，可以通过 df.loc[row label] 或 df.xs(row label) 命令来将指定的行按纵向的方式来展示：

```python
In [2284]: df = pro.fund_basic(status='L', market='E')     

In [2285]: df.head(1)        
Out[2285]: 
   ts_code    name            management  custodian  fund_type  ...    type        trustee purc_startdate redm_startdate market
0  502056.SH  医疗基金(LOF)    广发基金     北京银行    股票型     ...  契约型开放式    None       20200831       20200831      E

[1 rows x 25 columns]

In [2286]: df.loc[0]         
Out[2286]: 
ts_code                               502056.SH
name                                  医疗基金(LOF)
management                                 广发基金
custodian                                  北京银行
fund_type                                   股票型
found_date                             20200826
due_date                                   None
list_date                              20150731
issue_date                             20200826
delist_date                                None
issue_amount                             0.5931
m_fee                                       0.5
c_fee                                      0.15
duration_year                              None
p_value                                       1
min_amount                                  NaN
exp_return                                 None
benchmark         中证医疗指数收益率*95%+银行活期存款利率(税后)*5%
status                                        L
invest_type                               被动指数型
type                                     契约型开放式
trustee                                    None
purc_startdate                         20200831
redm_startdate                         20200831
market                                        E
Name: 0, dtype: object
```

#### 用标签分片
当使用 `.loc` 分片时，如果起始标签和终止标签都出现在索引中，则它们两者之间的元素 (包括它们自身) 被返回：  

```python
In [2033]: s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])                                                         

In [2034]: s.loc[3:5]        
Out[2034]: 
3    b
2    c
5    d
dtype: object
```

#### 按位置选择
**警告**  
为了一个设置操作而返回的，不管是一个副本还是一个引用，有可能依赖于上下文。这有时被称为 `链式赋值` 且应该被禁止。参见 [返回一个视图 vs 副本](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-view-versus-copy)。  

为了获得**完全基于整型数的索引** Pandas 提供了一整套方法。语法接近 Python 和 NumPy 分片。有基于 0 的索引。当分片时，会包含起始边界，但不会包含终止边界。当尝试使用一个非整型数时，即使是一个**有效的**标签也将抛出一个 `IndexError`。

`.iloc` 属性是主要的访问方法。下面是有效的输入：

* 一个整型数，例如：`5`。

* 一个整型数列表或者数组 `[4, 3, 0]`。

* 一个整型数分片对象 `1:7`。

* 一个布尔数组。

* 一个可调用对象，参见 [按可调用对象选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-callable)。

For getting a cross section using an integer position (等同于 `df.xs(1)`):  
df.xs() 的 key 参数只能为标签或标签元组。  

```python
In [2287]: df1 = pd.DataFrame(np.random.randn(6, 4), index=list(range(0, 12, 2)), 
                              columns=list(range(0, 8, 2)))        

In [2288]: df1.iloc[1]       
Out[2288]: 
0    0.163863
2    0.948425
4   -0.035419
6   -0.183619
Name: 2, dtype: float64
```

当 DataFrame 的列太多时，可以通过 df.iloc[row position] 或 df.xs(row position) 命令来将指定行中的列按纵向展示，以便查看完整的列数据。  

超出范围的分片索引会被优雅地处理，就像 Python/Numpy 中一样。  

```python
# these are allowed in python/numpy.
In [2300]: x = list('abcdef')

In [2301]: x                 
Out[2301]: ['a', 'b', 'c', 'd', 'e', 'f']

In [2302]: x[4:10]           
Out[2302]: ['e', 'f']

In [2303]: x[8:10]           
Out[2303]: []

In [2304]: s = pd.Series(x)  

In [2305]: s                 
Out[2305]: 
0    a
1    b
2    c
3    d
4    e
5    f
dtype: object

In [2306]: s.iloc[4:40]      
Out[2306]: 
4    e
5    f
dtype: object

In [2307]: s.iloc[8:10]      
Out[2307]: Series([], dtype: object)
```

一个超出范围的单一索引将抛出一个 `IndexError`。一个索引列表中任何一个元素超出范围都将抛出一个 `IndexError`。

```python
>>> df1 = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))
>>> df1.iloc[[4, 5, 6]]
IndexError: positional indexers are out-of-bounds

>>> df1.iloc[:, 4]
IndexError: single positional indexer is out-of-bounds
```

#### 按可调用对象选择
`.loc`, `.iloc`, 和 `[]` 索引可以接受一个可调用对象作为索引。The callable must be a function with one argument (the calling Series or DataFrame) that returns valid output for indexing.

#### 重建索引
实现选择可能找不到的元素的惯用方式是通过 `.reindex()`。另请参考关于 [重建索引](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-reindexing) 的章节。

```python
In [2338]: s = pd.Series([1, 2, 3])                        

In [2339]: s                 
Out[2339]: 
0    1
1    2
2    3
dtype: int64

In [2340]: s.reindex([1, 2, 3])                            
Out[2340]: 
1    2.0
2    3.0
3    NaN
dtype: float64
```

另一种选择是，如果你想仅选择*有效的*键，下面的方法是惯用且有效的；它确保保护选择的数据的类型。

```python
In [2343]: labels = [1, 2, 3]

In [2344]: s.loc[s.index.intersection(labels)]             
Out[2344]: 
1    2
2    3
dtype: int64
```

#### 扩大设置
当设置一个不存在的键时，`.loc/[]` 操作可以为相应的轴执行扩大设置。

对于 `Series` 这等效于附加操作。  

```python
In [2358]: se = pd.Series([1, 2, 3])                       

In [2359]: se                
Out[2359]: 
0    1
1    2
2    3
dtype: int64

In [2360]: se[5] = 5         

In [2361]: se                
Out[2361]: 
0    1
1    2
2    3
5    5
dtype: int64

In [2362]: se.loc[6] = 6

In [2363]: se
Out[2363]:
0    1
1    2
2    3
5    5
6    6
dtype: int64
```

#### 快速地获取及设置标量值
因为 `[]` 索引必须处理一些情况 (单标签访问，分片，布尔索引，等等。)，为了计算出你正在问什么它有一定的开销。如果你仅仅想访问一个标量值，最快的方式是使用 `at` 和 `iat` 方法，这两个方法在所有数据结构上都实现了。

与 `loc` 类似，`at` 提供基于标签的标量查找，与此同时，`iat` 提供类似于 `iloc` 基于整型数的查找  

```python
In [2395]: s = pd.Series([0, 1, 2, 3, 4, 5])               

In [2396]: s.iat[5]          
Out[2396]: 5

In [2397]: dates = pd.date_range('1/1/2000', periods=8)    

In [2398]: df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])                         

In [2399]: df                
Out[2399]: 
                   A         B         C         D
2000-01-01  0.532947 -0.265345  2.131531 -1.060020
2000-01-02  0.318499  1.453165  1.650231 -0.193968
2000-01-03  1.406332  0.452542  0.027695  0.333423
2000-01-04 -0.903745  1.229573 -0.265945  0.700144
2000-01-05  0.097685  0.049682 -0.150477 -0.622863
2000-01-06  1.005626  1.778057 -0.873678 -1.065244
2000-01-07 -0.524694  1.234492 -0.220565 -1.095799
2000-01-08 -1.158843 -0.239093 -0.188501  0.061266

In [2400]: df.at[dates[5], 'A']                            
Out[2400]: 1.0056264261667067

In [2401]: df.iat[3, 0]      
Out[2401]: -0.903744648864624
```

#### 布尔索引
另一种常用操作是使用布尔向量过滤数据。这些操作符是：`|` for `or`, `&` for `and`, and `~` for `not`。这些必须使用圆括号分组，因为默认情况下 Python 将一个表达式如 `df['A'] > 2 & df['B'] < 3` 计算为 `df['A'] > (2 & df['B']) < 3`，而期望的计算顺序是 `(df['A'] > 2) & (df['B'] < 3)`。

使用一个布尔向量索引一个 Series 能正确地工作就像在一个 NumPy ndarray 中一样：

```python
In [2402]: s = pd.Series(range(-3, 4))                     

In [2403]: s                 
Out[2403]: 
0   -3
1   -2
2   -1
3    0
4    1
5    2
6    3
dtype: int64

In [2404]: s[s > 0]          
Out[2404]: 
4    1
5    2
6    3
dtype: int64
```

列表包含以及 Series 的 `map` 方法也可以用来创作更复杂的条件：  

```python
In [2469]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'], 
      ...:                     'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'], 
      ...:                     'c': np.random.randn(7)})   

# only want 'two' or 'three'
In [2470]: criterion = df2['a'].map(lambda x: x.startswith('t'))                                                       
In [2471]: df2[criterion]    
Out[2471]: 
       a  b         c
2    two  y -0.151329
3  three  x -0.574711
4    two  y  0.763878

# equivalent but slower
In [2472]: df2[[x.startswith('t') for x in df2['a']]]      
Out[2472]: 
       a  b         c
2    two  y -0.151329
3  three  x -0.574711
4    two  y  0.763878

# Multiple criteria
In [2473]: df2[criterion & (df2['b'] == 'x')]              
Out[2473]: 
       a  b         c
3  three  x -0.574711

```

对于可供选择的方法 [按标签选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label)，[按位置选择](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-integer)，以及 [高级索引](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced)，你可能会使用布尔向量结合其它索引表达式沿多个轴选择数据。

```python
In [2474]: df2.loc[criterion & (df2['b'] == 'x'), 'b':'c'] 
Out[2474]: 
   b         c
3  x -0.574711

```

#### 用 isin 方法索引
考虑到 Series 的 [isin()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin) 方法，它返回一个布尔向量，如果 Series 的元素存在于传递的列表中，则相应的布尔值为 true。这个方法允许你选择那些一列或者多列中包含你想要的值的行：

```python
In [15]: s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')                           

In [16]: s                   
Out[16]: 
4    0
3    1
2    2
1    3
0    4
dtype: int64

In [17]: s.isin([2, 4, 6])   
Out[17]: 
4    False
3    False
2     True
1    False
0     True
dtype: bool

In [18]: s[s.isin([2, 4, 6])]
Out[18]: 
2    2
0    4
dtype: int64

```

这个方法也适用于 Index 对象，当你不知道哪些被寻找的标签实际存在时很有用：

```python
In [44]: s[s.index.isin([2, 4, 6])]                        
Out[44]: 
4    0
2    2
dtype: int64

# compare it to the following
In [45]: s.reindex([2, 4, 6])
Out[45]: 
2    2.0
4    0.0
6    NaN
dtype: float64
```

DataFrame 也有一个 [isin()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin) 方法。当调用 `isin` 时，传递一个数组或字典的值的集合。如果值是一个数组，`isin` 返回一个与原始 DataFrame 形状相同的布尔值 DataFrame，只要元素在值的序列中则相应的布尔值为 True。

```python
In [233]: df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'], 'ids2': ['a', 'n', 'c', 'n']})         

In [234]: values = ['a', 'b', 1, 3]                        

In [235]: df.isin(values)    
Out[235]: 
    vals    ids   ids2
0   True   True   True
1  False   True  False
2   True  False  False
3  False  False  False
```

你常常想在确定的列中匹配确定的值。只需将一个字典作为值，其中键是列名，而值是你想检查的项的列表。

```python
In [236]: values = {'ids': ['a', 'b'], 'vals': [1, 3]}     

In [237]: df.isin(values)    
Out[237]: 
    vals    ids   ids2
0   True   True  False
1  False   True  False
2   True  False  False
3  False  False  False
```

结合 DataFrame 的 isin 和 any() 及 all() 方法可以快速地从你的数据中筛选出符合指定条件的子集。选择每一列都符合它自己的条件的行：

```python
In [252]: values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}                               

In [253]: row_mask = df.isin(values).all(1)                

In [254]: df[row_mask]       
Out[254]: 
   vals ids ids2
0     1   a    a
```

### where() 方法及 Masking  
通过布尔向量从一个 Series 中选择值通常返回一个原始数据的子集。为了保证筛选的输出与原始数据的形状相同，你可以在 Series 和 DataFrame 中使用 where 方法。  

仅返回被选择的行：  

```python
In [264]: s[s > 0]           
Out[264]: 
3    1
2    2
1    3
0    4
dtype: int64
```

返回一个和原始 Series 形状相同的 Series：

```python
In [265]: s.where(s > 0)     
Out[265]: 
4    NaN
3    1.0
2    2.0
1    3.0
0    4.0
dtype: float64
```

现在通过布尔规范从一个 DataFrame 中选择值也将保持输入数据的形状。背后的实现是通过 where 。下面的代码等同于 `df.where(df < 0)`。  

```python
In [271]: df[df < 0]         
Out[271]: 
                   A         B         C         D
2000-01-01       NaN -1.254982       NaN -0.016761
2000-01-02       NaN -0.656100 -2.003315       NaN
2000-01-03 -1.211283       NaN -1.021318 -0.181545
2000-01-04 -1.093566 -0.267235       NaN -0.393395
2000-01-05 -1.479570 -0.924544 -0.380941       NaN
2000-01-06 -0.190404 -0.212619       NaN       NaN
2000-01-07       NaN       NaN -1.721793       NaN
2000-01-08       NaN       NaN -0.067199       NaN
```

另外，`where` 带有一个可选的 `other` 参数用于替换条件为假的值，并就地返回相应的副本。

```python
In [273]: df.where(df < 0, -df)                            
Out[273]: 
                   A         B         C         D
2000-01-01 -1.027261 -1.254982 -0.347028 -0.016761
2000-01-02 -0.959209 -0.656100 -2.003315 -1.678398
2000-01-03 -1.211283 -2.775171 -1.021318 -0.181545
2000-01-04 -1.093566 -0.267235 -0.211445 -0.393395
2000-01-05 -1.479570 -0.924544 -0.380941 -0.046379
2000-01-06 -0.190404 -0.212619 -1.470182 -0.710863
2000-01-07 -1.620551 -1.852458 -1.721793 -1.036632
2000-01-08 -0.148211 -2.144672 -0.067199 -1.913107
```

默认情况下，`where`返回一个数据副本的修改版本。有一个可选参数 `inplace` 可以在不创建副本的情况下直接修改原始数据：

```python
In [285]: df_orig = df.copy()

In [286]: df_orig.where(df > 0, -df, inplace=True)         

In [287]: df_orig            
Out[287]: 
                   A         B         C         D
2000-01-01  1.027261  1.254982  0.347028  0.016761
2000-01-02  0.959209  0.656100  2.003315  1.678398
2000-01-03  1.211283  2.775171  1.021318  0.181545
2000-01-04  1.093566  0.267235  0.211445  0.393395
2000-01-05  1.479570  0.924544  0.380941  0.046379
2000-01-06  0.190404  0.212619  1.470182  0.710863
2000-01-07  1.620551  1.852458  1.721793  1.036632
2000-01-08  0.148211  2.144672  0.067199  1.913107
```

**注意**

[DataFrame.where()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where) 的签名不同于 [numpy.where()](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where)。虽然 `df1.where(m, df2)` 大体上等同于 `np.where(m, df1, df2)`。

```python
In [294]: df.where(df < 0, -df) == np.where(df < 0, df, -df)                                                           
Out[294]: 
               A     B     C     D
2000-01-01  True  True  True  True
2000-01-02  True  True  True  True
2000-01-03  True  True  True  True
2000-01-04  True  True  True  True
2000-01-05  True  True  True  True
2000-01-06  True  True  True  True
2000-01-07  True  True  True  True
2000-01-08  True  True  True  True
```

**对齐**

而且，`where` 使输入的布尔条件对齐 (ndarray 或者 DataFrame)，因此设置部分数据是可能的。这类似于通过 `.loc` 设置部分数据 (但这是通过内容而不是轴标签)。  

```python
In [295]: df2 = df.copy()    

In [296]: df2[df2[1:4] > 0] = 3                            

In [297]: df2                
Out[297]: 
                   A         B         C         D
2000-01-01  1.027261 -1.254982  0.347028 -0.016761
2000-01-02  3.000000 -0.656100 -2.003315  3.000000
2000-01-03 -1.211283  3.000000 -1.021318 -0.181545
2000-01-04 -1.093566 -0.267235  3.000000 -0.393395
2000-01-05 -1.479570 -0.924544 -0.380941  0.046379
2000-01-06 -0.190404 -0.212619  1.470182  0.710863
2000-01-07  1.620551  1.852458 -1.721793  1.036632
2000-01-08  0.148211  2.144672 -0.067199  1.913107
```

当执行 `where` 时，Where 也能接受 `axis` 和 `level` 参数使输入对齐。

```python
In [299]: df2 = df.copy()    

In [300]: df2.where(df2 > 0, df2['A'], axis='index')       
Out[300]: 
                   A         B         C         D
2000-01-01  1.027261  1.027261  0.347028  1.027261
2000-01-02  0.959209  0.959209  0.959209  1.678398
2000-01-03 -1.211283  2.775171 -1.211283 -1.211283
2000-01-04 -1.093566 -1.093566  0.211445 -1.093566
2000-01-05 -1.479570 -1.479570 -1.479570  0.046379
2000-01-06 -0.190404 -0.190404  1.470182  0.710863
2000-01-07  1.620551  1.852458  1.620551  1.036632
2000-01-08  0.148211  2.144672  0.148211  1.913107
```

这等同于下面的代码（但比下面的更快）。

```python
In [301]: df2 = df.copy()    

In [302]: df.apply(lambda x, y: x.where(x > 0, y), y=df['A'])                                                          
Out[302]: 
                   A         B         C         D
2000-01-01  1.027261  1.027261  0.347028  1.027261
2000-01-02  0.959209  0.959209  0.959209  1.678398
2000-01-03 -1.211283  2.775171 -1.211283 -1.211283
2000-01-04 -1.093566 -1.093566  0.211445 -1.093566
2000-01-05 -1.479570 -1.479570 -1.479570  0.046379
2000-01-06 -0.190404 -0.190404  1.470182  0.710863
2000-01-07  1.620551  1.852458  1.620551  1.036632
2000-01-08  0.148211  2.144672  0.148211  1.913107
```

**Mask**

[mask()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask) 是 `where` 的反向布尔操作。

```python
In [310]: s.mask(s >= 0)     
Out[310]: 
4   NaN
3   NaN
2   NaN
1   NaN
0   NaN
dtype: float64
```

### query() 方法
[DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) 对象有一个 query() 方法，该方法允许筛选使用一个表达式。

```python
In [320]: n = 10             

In [321]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))                                                 
In [322]: df                 
Out[322]: 
          a         b         c
0  0.322170  0.380921  0.571703
1  0.951441  0.335061  0.146904
2  0.245722  0.686748  0.609397
3  0.230059  0.531634  0.924360
4  0.749230  0.862731  0.882803
5  0.490591  0.138896  0.666389
6  0.699899  0.453408  0.537391
7  0.383800  0.440843  0.381102
8  0.214088  0.200563  0.919920
9  0.327337  0.507083  0.887235

# pure python      
In [324]: df[(df['a'] < df['b']) & (df['b'] < df['c'])]    
Out[324]: 
          a         b         c
0  0.322170  0.380921  0.571703
3  0.230059  0.531634  0.924360
4  0.749230  0.862731  0.882803
9  0.327337  0.507083  0.887235

# query            
In [326]: df.query('(a < b) & (b < c)')                    
Out[326]: 
          a         b         c
0  0.322170  0.380921  0.571703
3  0.230059  0.531634  0.924360
4  0.749230  0.862731  0.882803
9  0.327337  0.507083  0.887235
```

### 重置索引
为方便起见，DataFrame 有一个新的函数叫作 [reset_index()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index)，它将索引值转换为 DataFrame 的列并设置一个简单的整型数索引。这是 [set_index()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index) 的反向操作。

```python
In [503]: data               
Out[503]: 
         c    d
a   b          
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0

In [504]: data.reset_index() 
Out[504]: 
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0
```

### 返回一个视图 vs 一个副本
当给 pandas 对象设置值时，必须小心一种称之为 **链索引** 的情况。这里有一个例子。

```python
In [516]: dfmi = pd.DataFrame([list('abcd'), list('efgh'), list('ijkl'), list('mnop')], 
     ...: columns=pd.MultiIndex.from_product([['one', 'two'], ['first', 'second']]))      

In [517]: dfmi               
Out[517]: 
    one          two       
  first second first second
0     a      b     c      d
1     e      f     g      h
2     i      j     k      l
3     m      n     o      p
```

比较这两种访问方法：

```python
In [518]: dfmi['one']['second']                            
Out[518]: 
0    b
1    f
2    j
3    n
Name: second, dtype: object

In [519]: dfmi.loc[:, ('one', 'second')]                   
Out[519]: 
0    b
1    f
2    j
3    n
Name: (one, second), dtype: object
```

方法2比方法1（chained []）更好。方法2不仅更快，而且还允许同时索引两个轴。  

参考链接：  
[https://pandas.pydata.org/docs/user_guide/indexing.html](https://pandas.pydata.org/docs/user_guide/indexing.html)  

### 选项和设置
#### 概述
pandas 有一个选项系统，可以让你自定义其行为的某些方面，与显示相关的选项是用户最有可能调整的选项。  

选项有一个完整的“dotted-style”，不区分大小写的名称（例如 display.max_rows）。 您可以直接获取/设置选项作为顶层 **options** 属性的属性：  

```python
In [602]: pd.options.display.max_rows                      
Out[602]: 60

In [603]: pd.options.display.max_rows = 999                

In [604]: pd.options.display.max_rows                      
Out[604]: 999
```

这个 API 由 5 个相关函数组成，可直接从 pandas 命名空间获得：  

* [get_option()](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option) / [set_option()](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option) - 获取/设置一个单一选项的值。  
* [reset_option()](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option) - 将一个或多个选项重置为其默认值。  
* [describe_option()](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option) - 打印一个或多个选项的描述。  
* [option_context()](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context) - 使用一组选项执行代码块，这些选项在执行后恢复为先前的设置。  
**注意：**开发者可以查看 [pandas/core/config_init.py](https://github.com/pandas-dev/pandas/blob/master/pandas/core/config_init.py) 以了解更多信息。  

#### Unicode 格式
**警告：**  
启用此选项将影响打印 DataFrame 和 Series 的性能（大约慢 2 倍）。仅在实际需要时使用。  

一些东亚国家使用 Unicode 字符，其宽度对应于两个拉丁字符。如果 DataFrame 或 Series 包含这些字符，则默认输出模式可能无法正确对齐它们。  

```python
>>> df = pd.read_excel('E:/Downloads/2021-10-13.xlsx').head(1)
>>> df
        股票代码  股票简称 最新户均持股市值(元) 最新户均持股数量(股) 最新户均持股比例(%) 股东人数变动公告日2021.10.13    holders
0  601728.SH  中国电信     6204.72      1453.1           0            20210819  303.1684万
```

![默认设置](./img/display.unicode.east_asian_width-1.png)  

启用 **display.unicode.east_asian_width** 允许 pandas 检查每个字符的“东亚宽度”属性。通过将此选项设置为 True，可以正确对齐这些字符。但是，这将导致比标准 **len** 函数更长的渲染时间。  

```python
>>> pd.set_option("display.unicode.east_asian_width", True)
>>> df
    股票代码   股票简称   最新户均持股市值(元)  最新户均持股数量(股)   最新户均持股比例(%)  股东人数变动公告日2021.10.13  holders
0  601728.SH  中国电信              6204.72               1453.1                   0                     20210819  303.1684万
```

![display.unicode.east_asian_width-with-True](./img/display.unicode.east_asian_width-2.png)  

参考链接：  
[https://pandas.pydata.org/docs/user_guide/options.html](https://pandas.pydata.org/docs/user_guide/options.html)  

## Pandas API 参考
### 输入/输出
#### pandas.read_csv
__pandas.read_csv(*filepath_or_buffer, sep=NoDefault.no_default, delimiter=None, header='infer', names=NoDefault.no_default, index_col=None, usecols=None, squeeze=None, prefix=NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None*)__  

将逗号分隔值 (csv) 文件读入 DataFrame。  

还支持可选地将文件迭代或分解成块。  

更多帮助可以在 [IO Tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) 的在线文档中找到。  

**参数：**  
**skiprows:** __*list-like, int or callable, 可选的*__  
文件开头要跳过的行号（0-indexed）或要跳过的行数（int）。  

**thousands:** __*str, 可选的*__  
千位分隔符。  

**decimal:** __*str, 默认为 ‘.’*__  
识别为小数点的字符（例如，对欧洲数据使用“,”）。   

**注意： 如果数值列中出现了字符串（如空格），则整个列都无法应用 decimal 选项。**  

**encoding:** __*str, 可选的*__  
读取/写入时用于 UTF 的编码（例如“utf-8”）。 [Python 标准编码列表](https://docs.python.org/3/library/codecs.html#standard-encodings)。  

#### pandas.read_excel
**pandas.read_excel(*io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, decimal='.', comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None*)**  

pandas.**read_excel**(\*args, \*\*kwargs)  
将一个 Excel 文件读取到一个 pandas DataFrame 中。  

**参数：**  
**io：** *__str, bytes, ExcelFile, xlrd.Book, path object, or file-like object__*  
任何有效的字符串路径都是可接受的。  

**sheet_name： *str, int, list, or None, 默认值 0***  
字符串用于工作表名称。 整数用于零索引工作表位置（图表工作表不计为工作表位置）。 字符串/整数列表用于请求多张工作表。 指定 None 以获取所有工作表。  

可用实例：  
* 默认为 0： 第一张工作表作为一个 *DataFrame*  
* 1： 第二张工作表作为一个 *DataFrame*  
* “Sheet1”： 加载名为“Sheet1”的工作表  
* [0, 1, "Sheet5"]: 加载第一个、第二个和名为“Sheet5”的工作表作为一个 *DataFrame* 的字典  
* None： 所有工作表。  

**index_col：** *__int, list of int, default None__*  
用作 DataFrame 行标签的列 (0-indexed)。  

例子：  

```python
>>> pd.read_excel('SZ.xlsx')
   Unnamed: 0   code  trade_date    ts_code  name         vol  ratio exchange
0           0  70001    20200522  000001.SZ  平安银行  1647348155   8.48       SZ
1           1  70002    20200522  000002.SZ  万 科A   482338018   4.96       SZ
2           2  70005    20200522  000005.SZ  世纪星源        2010   0.00       SZ
>>> pd.read_excel('SZ.xlsx', index_col=0)
    code  trade_date    ts_code  name         vol  ratio exchange
0  70001    20200522  000001.SZ  平安银行  1647348155   8.48       SZ
1  70002    20200522  000002.SZ  万 科A   482338018   4.96       SZ
2  70005    20200522  000005.SZ  世纪星源        2010   0.00       SZ
>>>
``` 

**thousands： *str, 默认值 None***  
千位分隔符用于将字符串列解析为数字。请注意，此参数仅对在 Excel 中存储为 TEXT 的列是必需的，无论显示格式如何，任何数字列都会被自动解析。  

**decimal： *str, 默认值 ‘.’***  
将字符串列解析为数字时识别为小数点的字符。请注意，此参数仅对在 Excel 中存储为 TEXT 的列是必需的，任何数字列都将自动被解析，无论显示格式如何。（例如，对于欧洲数据使用“,”）。  

***1.4.0 版中的新功能。***  

**Returns： DataFrame 或 DataFrames 字典**  
来自传入的 Excel 文件的 DataFrame。 有关何时返回 DataFrames 字典的更多信息，请参阅 sheet_name 参数中的注释。  

#### pandas.DataFrame.to_excel
**DataFrame.to_excel(*excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None*)**  

将对象写入 Excel 工作表。  

要将单个对象写入 Excel .xlsx 文件，只需指定目标文件名。 要写入多个工作表，需要创建一个具有目标文件名的 *ExcelWriter* 对象，并在文件中指定要写入的工作表。  

通过指定唯一的 *sheet_name* 可以写入多个工作表。 将所有数据写入文件后，有必要保存更改。请注意，使用已存在的文件名创建 *ExcelWriter* 对象将导致现有文件的内容被删除。

**参数：**  
**excel_writer：** **_path-like, file-like, or ExcelWriter 对象_**  
文件路径或者已存在的 ExcelWriter。  

**sheet_name：** **_str, 默认为 ‘Sheet1’_**  
将包含 DataFrame 的工作表的名称。  

**header：** **_bool or list of str, 默认为 True_**  
写出列名。 如果给出字符串列表，则假定它是列名的别名。  

**index：** **_bool, 默认为 True_**  
写行名称（索引）。  

**例子**  
创建、写入和保存工作簿：  

```python
>>> df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
>>> df1.to_excel("output.xlsx", sheet_name='Sheet_name_1')
```

如果您希望写入工作簿中的多个工作表，则需要指定一个 ExcelWriter 对象：  

```python
>>> df2 = df1.copy()
>>> with pd.ExcelWriter('output.xlsx') as writer:
...     df1.to_excel(writer, sheet_name='Sheet_name_1')
...     df2.to_excel(writer, sheet_name='Sheet_name_2')
```

ExcelWriter 也可用于附加到现有的 Excel 文件：  

```python
>>> with pd.ExcelWriter('output.xlsx', mode='a') as writer:
...     df.to_excel(writer, sheet_name='Sheet_name_3')
```

#### pandas.ExcelWriter  
**class pandas.ExcelWriter(*path, engine=None, date_format=None, datetime_format=None, mode='w', storage_options=None, if_sheet_exists=None, engine_kwargs=None, \*\*kwargs*)**  

用于将 DataFrame 对象写入 Excel 工作表的类。  

默认使用：* xlwt 用于 xls，* xlsxwriter 用于 xlsx，如果安装了 xlsxwriter 否则 openpyxl，* odf 用于 ods。有关典型用法，请参阅 DataFrame.to_excel。  

writer 应该用作上下文管理器。否则，调用 *close()* 保存并关闭任何打开的文件句柄。  

**参数：**  
**path：** **_str or typing.BinaryIO_**  
xls 或 xlsx 或 ods 文件的路径。  

**mode：** **_{‘w’, ‘a’}, 默认值 ‘w’_**  
要使用的文件模式（写入或附加）。 附加不适用于 fsspec URLs。  

### 通用函数
#### pandas.concat  
pandas.**concat**_(objs: Union[Iterable[‘DataFrame’], Mapping[Label, ‘DataFrame’]], axis='0', join: str = "'outer'", ignore_index: bool = 'False', keys='None', levels='None', names='None', verify_integrity: bool = 'False', sort: bool = 'False', copy: bool = 'True') → ’DataFrame’_  

**参数：**  
**objs：** a sequence or mapping of Series or DataFrame objects

**axis：** _{0/’index’, 1/’columns’}, default 0_  
指定沿哪一个轴合并，默认是按横轴合并。  

**例子**  

合并两个具有相同列的 DataFrame 对象。

```python
>>> df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
>>> df1
  letter  number
0      a       1
1      b       2
>>> df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
>>> df2
  letter  number
0      c       3
1      d       4
>>> pd.concat([df1, df2])
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
>>>
```

#### pandas.to_numeric
pandas.**to_numeric**(*arg, errors='raise', downcast=None*)  
将参数转换为数字类型。  

默认返回数据类型为 *float64* 或 *int64*，具体取决于提供的数据。使用 *downcast* 参数获取其它数据类型。  

```python
>>> df = pd.DataFrame({"股票简称": ["中国电信", "京东方A", "华润材料"], "holders": ["303.1684万", "141.0821万", 3]})
>>> df
   股票简称    holders
0  中国电信  303.1684万
1  京东方A  141.0821万
2  华润材料          3
>>> df.holders = df.holders.replace('万', 'E4', regex=True)
>>> df
   股票简称     holders
0  中国电信  303.1684E4
1  京东方A  141.0821E4
2  华润材料           3
>>> df.holders = pd.to_numeric(df.holders, downcast="integer")
>>> df
   股票简称  holders
0  中国电信  3031684
1  京东方A  1410821
2  华润材料        3
```

参考链接：  
[https://pandas.pydata.org/docs/reference/general_functions.html](https://pandas.pydata.org/docs/reference/general_functions.html)  

### Series
#### pandas.Series.all
**Series.all(*axis=0, bool_only=None, skipna=True, level=None, \*\*kwargs*)**  

返回是否所有元素都为真，可能在一个轴上。  


返回 True 除非在 Series 中或沿 Dataframe 轴至少有一个元素为 False 或等效（例如零或空）。  

**参数：**  
**axis： *{0 or ‘index’, 1 or ‘columns’, None}, 默认值 0***  
指示应减少哪个轴或哪些轴。  

* 0 / ‘index’ : 减少索引，返回一个索引为原始列标签的 Series。  
* 1 / ‘columns’ : 减少列，返回一个索引为原始索引的 Series。  
* None : 减少所有轴，返回一个标量。  

#### pandas.Series.astype  
**Series.astype(*dtype, copy=True, errors='raise')***  

将 pandas 对象转换为指定的 dtype ***dtype***。  

**参数：**  
**dtype： *data type, or dict of column name -> data type***  
使用 numpy.dtype 或 Python 类型将整个 pandas 对象转换为相同类型。或者，使用 {col: dtype, ...}，其中 col 是列标签，dtype 是 numpy.dtype 或 Python 类型，将 DataFrame 的一个或多个列转换为特定于列的类型。  

**Returns：**  
**casted： *与调用者相同的类型***  

```python
>>> df1
   id  sku name
0   1  NaN   aa
>>> df2
   id    sku name
0   1    NaN   aa
1   2    NaN   bb
2   3  HH-Y6   cc
3   4  HH-Y7   dd
>>> type(df1.sku)
<class 'pandas.core.series.Series'>
>>> type(df2.sku)
<class 'pandas.core.series.Series'>
>>> try:
...     df1['sku'] = df1.sku.str.extract(r'(\w+)')
... except AttributeError as e:
...     print(e)
...
Can only use .str accessor with string values!
>>> try:
...     df2['sku'] = df2.sku.str.extract(r'(\w+)')
... except AttributeError as e:
...     print(e)
...
>>> df2
   id  sku name
0   1  NaN   aa
1   2  NaN   bb
2   3   HH   cc
3   4   HH   dd
>>> try:
...     df1['sku'] = df1.sku.astype(str).str.extract(r'(\w+)')
... except AttributeError as e:
...     print(e)
...
>>> df1
   id  sku name
0   1  nan   aa
>>> type(df1.sku.astype(str))
<class 'pandas.core.series.Series'>
>>>
```

#### pandas.Series.isin
Series.**isin**(*self, values*)  
Check whether *values* are contained in Series.

Return a boolean Series showing whether each element in the Series matches an element in the passed sequence of *values* exactly.

**参数：**  
**values：** *必须是集合或类列表*    
The sequence of values to test. 传递一个单字符串将抛出一个 TypeError. 将一个单字符串变成一个单元素的列表代替。

**返回值：** **Series**  
Series of booleans indicating if each element is in values.

```python
>>> df
  trade_date   ggt_ss   ggt_sz      hgt      sgt  north_money  south_money
0   20200515   871.53  1206.17  -111.53  1305.91      1194.38      2077.70
1   20200514  2471.56  1604.79 -1650.19   325.38     -1324.81      4076.35
2   20200513  1478.46  1915.81    26.09  -230.73      -204.64      3394.27
3   20200512   752.76  1075.14   561.87  1188.07      1749.94      1827.90
4   20200511 -2296.58   659.60  1071.89  1575.67      2647.56     -1636.98
>>> s = df['north_money']
>>> type(s)
<class 'pandas.core.series.Series'>
>>> s
0    1194.38
1   -1324.81
2    -204.64
3    1749.94
4    2647.56
Name: north_money, dtype: float64
>>> a = s.isin(['2647.56'])
>>> type(a)
<class 'pandas.core.series.Series'>
>>> a
0    False
1    False
2    False
3    False
4     True
Name: north_money, dtype: bool
>>> df[a]
  trade_date   ggt_ss  ggt_sz      hgt      sgt  north_money  south_money
4   20200511 -2296.58   659.6  1071.89  1575.67      2647.56     -1636.98
>>>
```

#### pandas.Series.isna
**Series.isna()**  

检测缺失值。

返回一个相同大小的布尔值对象，表明值是否为 NA。 NA 值，例如 None 或 **numpy.NaN**，被映射到 True 值。 其他所有内容都映射到 False 值。空字符串 '' 或 **numpy.inf** 等字符不被视为 NA 值（除非您设置 **pandas.options.mode.use_inf_as_na = True**）。  

**Returns：** **Series**  
Series 中每个元素的布尔值掩码，表明元素是否为 NA 值。  

#### pandas.Series.isnull
**Series.isnull()**  

Series.isnull 是 Series.isna 的别名。  

检测缺失值。

返回一个相同大小的布尔值对象，表明值是否为 NA。 NA 值，例如 None 或 **numpy.NaN**，被映射到 True 值。 其他所有内容都映射到 False 值。空字符串 '' 或 **numpy.inf** 等字符不被视为 NA 值（除非您设置 **pandas.options.mode.use_inf_as_na = True**）。  

**Returns：** **Series**  
Series 中每个元素的布尔值掩码，表明元素是否为 NA 值。  

#### pandas.Series.replace
Series.**replace**(*to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad'*)  

用 *value* 替换 *to_replace* 中给出的值。  

Series 的值被动态地替换为其它值。  

**参数：**  
**to_replace：** **_str, regex, list, dict, Series, int, float, or None_**  
如何找到将被替换的值。  
* 数值，字符串或正则表达式：  
    * 数值：等于 *to_replace* 的数值将被替换为 *value*  
    * 字符串：与 *to_replace* 完全匹配的字符串将被替换为 *value*  
    * 正则表达式：匹配 *to_replace* 的正则表达式将被替换为 *value*  

**value：** **_scalar, dict, list, str, regex, 默认值 None_**  
替换与 *to_replace* 匹配的任何值的值。对于 DataFrame，可以使用值的字典来指定每列使用哪个值（不在字典中的列将不会被填充）。 正则表达式、字符串和列表或此类对象的字典也是被允许的。  

**inplace：** **_bool, 默认值 False_**  
如果为 True，则就地执行操作并返回 None。  

**regex：** **_bool or same types as to_replace, 默认值 False_**  
是否将 *to_replace* 和/或 *value* 解释为正则表达式。如果这是 **True** 那么 *to_replace 必须*是一个字符串。 或者，这可以是正则表达式或正则表达式列表、字典或数组，在这种情况下 *to_replace* 必须为 **None**。  

**Returns：** **Series**  
替换后的对象。  

```python
>>> df = pd.DataFrame({"股票简称": ["中国电信", "京东方A", "华润材料"], "holders": ["303.1684万", "141.0821万", 3]})
>>> df
   股票简称    holders
0  中国电信  303.1684万
1  京东方A  141.0821万
2  华润材料          3
>>> df.holders.replace('万', 'E4', inplace=True, regex=True)
>>> df
   股票简称     holders
0  中国电信  303.1684E4
1  京东方A  141.0821E4
2  华润材料           3
```

#### pandas.Series.str.extract  
**Series.str.extract(*pat, flags=0, expand=True*)**  

将正则表达式 *pat* 中的捕获组提取为 DataFrame 中的列。  

对于 Series 中的每个主题字符串，从正则表达式 *pat* 的第一个匹配项中提取组。  

**参数：**  
**pat：** ***str***  
带有捕获组的正则表达式模式。  

**Returns：** **DataFrame 或 Series 或 Index**  
一个 DataFrame，每个主题字符串一行，每组一列。正则表达式 pat 中的任何捕获组名称都将用于列名称；否则将使用捕获组编号。每个结果列的 dtype 始终是 object，即使没有找到匹配项。如果 **expand=False** 并且 pat 只有一个捕获组，则返回一个 Series （如果主题是系列）或索引（如果主题是索引）。  

### DataFrame
#### pandas.DataFrame.all
DataFrame.all(*axis=0, bool_only=None, skipna=True, level=None, \*\*kwargs*)  
返回至少一个轴上的所有元素是否为真。  

返回真，如果在一个 series 中或者沿 Dataframe 的一个轴上至少有一个元素为假或等价（例如：0或者空）则返回假。

**参数：**  
**axis：** **_{0 or ‘index’, 1 or ‘columns’, None}, default 0_**  
表明哪一个轴（or axes）应该被缩减。

* 0/‘index’: 缩减索引，返回一个 Series，其索引是原来的列标签。  
* 1/‘columns’: 缩减列，返回一个 Series，其索引是原来的索引。  
* None: 缩减所有轴，返回一个标量。  

**返回值**  
**Series 或者 DataFrame**  
如果指定了 level 则返回 DataFrame；否则返回 Series。  

**例子**  
**DataFrames**  
通过字典构建一个 dataframe。

```python
>>> df = pd.DataFrame({'col1': [True, True, True], 'col2': [True, True, False], 'col3': [True, False, False]})
>>> df
   col1   col2   col3
0  True   True   True
1  True   True  False
2  True  False  False
```

默认行为检查列式的值是否都返回真。

```python
>>> df.all()
col1     True
col2    False
col3    False
dtype: bool
>>>
```

指定 axis='columns'（或者 axis=1）以检查是否行式的值都返回真。

```python
>>> df.all(axis='columns')
0     True
1    False
2    False
dtype: bool
>>> df.all(axis=1)
0     True
1    False
2    False
dtype: bool
```

或者指定 axis=None 以检查是否所有值都为真。

```python
>>> df.all(axis=None)
False
```

#### pandas.DataFrame.drop
**DataFrame.drop(*labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')***  

从行或列中删除指定的标签。  

通过指定标签名称和相应的轴，或直接指定索引或列名称来删除行或列。使用多索引时，可以通过指定级别来移除不同级别的标签。 有关现在未使用的级别的更多信息，请参阅*用户指南 <advanced.shown_levels>*。  

**参数：**  
**labels： *single label or list-like***  
要删除的索引或列标签。 元组将用作单个标签，而不被视为一个类似列表。  

**axis： *{0 or ‘index’, 1 or ‘columns’}, 默认值 0***  
是否从索引（0 或“index”）或列（1 或“columns”）中删除标签。  

**index： *single label or list-like***  
替代指定轴（labels，axis=0 相当于 index=labels）。  

**columns： *single label or list-like***  
替代指定轴（labels，axis=1 相当于 columns=labels）。  

**inplace： *bool, 默认值 False***  
如果为 False，则返回一个副本。 否则，就地执行操作并返回 None。  

**Returns： DataFrame or None**  
无已删除索引或列标签的 DataFrame，如果 `inplace=True`，则为 None。  

**Raises： KeyError**  
如果在所选轴中有任何标签未找到。  

#### pandas.DataFrame.index
DataFrame.**index**: *Index*  
返回 DataFrame 的索引（行标签）。  

```python
In [1435]: df                                  
Out[1435]: 
       ts_code     name         management    fund_type list_date invest_type
905  163801.SZ     中银中国       中银基金       混合型  20050223         稳定型
906  510050.SH    上证50ETF       华夏基金       股票型  20050223       被动指数型
907  160105.SZ     南方积配       南方基金       混合型  20041220         混合型

In [1436]: df[df['ts_code'] == '510050.SH']    
Out[1436]: 
       ts_code     name          management   fund_type list_date invest_type
906  510050.SH    上证50ETF       华夏基金       股票型  20050223       被动指数型

In [1437]: df[df['ts_code'] == '510050.SH'].index                                              
Out[1437]: Int64Index([906], dtype='int64')
```

#### pandas.DataFrame.merge  
**DataFrame.merge(*right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)***  

用数据库风格的 join 将 DataFrame 或命名的 Series 对象合并。  

一个命名的 Series 对象被视为具有单个命名列的 DataFrame。  

连接是在列或索引上完成的。 如果在列上连接列，则 DataFrame 索引*将被忽略*。否则，如果合并索引上的索引或列上的索引，则索引将被传递。 执行交叉合并时，不允许合并列规范。  

**参数：**  
**right： *DataFrame or named Series***  
要合并的对象。  

**how： *{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, 默认值 ‘inner’***  
要执行的合并类型。  

* left: 仅使用左帧中的键，类似于 SQL 左外连接；保留键的顺序。  
* right: 仅使用右帧中的键，类似于 SQL 右外连接；保留键的顺序。  
* outer: 使用两个帧中键的并集，类似于 SQL 全外连接；按字典顺序对键进行排序。  
* inner: 使用来自两个帧的键的交集，类似于 SQL 内连接；保留左键的顺序。  
* cross: 从两个帧创建笛卡尔积，保留左键的顺序。  

***版本 1.2.0 中的新功能。***  

**Returns： DataFrame**  
两个合并对象的 DataFrame。  

```python
>>> df1
     type             order id             sku  ... selling fees  fba fees  total
0   Order  702-1138646-9141825   HT-CWSBLE8BKS  ...        -7.37       0.0  41.78
2   Order  701-0152570-2531474   HT-CWSBLD9BKS  ...        -4.42      -8.7  16.36
3   Order  701-5837171-7378639  HT-CWSBLD9BKXL  ...        -4.54      -8.7  17.02
4   Order  701-2584669-0129845  HT-CWSBLD9PPXL  ...        -5.34       0.0  30.25
5   Order  701-2584669-0129845  HT-CWSBLD9WTXL  ...        -5.34       0.0  30.25
7   Order  701-6310582-5160205   HT-CWSBLD9BKS  ...        -4.42      -8.7  16.36
8   Order  701-0200508-1054662   HT-CWSBLV8ORS  ...        -5.85       0.0  33.14
9   Order  701-0909993-5240234   HT-CWSBLD9BKS  ...        -4.42      -8.7  16.36
10  Order  702-1107566-1984247   HT-CWSBLD9BES  ...        -5.34       0.0  30.25
12  Order  701-0787880-4570618   HT-CWSBLD9BKM  ...        -4.54      -8.7  17.02

[10 rows x 10 columns]
>>> df2
                 sku        采购成本
0        HT-TWTWG4SG    7.350000
1       HT-TWTWG4SBE    7.350000
2        HT-TWTWG4CG    6.700000
3       HT-TWTWG4CBE    7.350000
4         HT-TWTSR2R   11.750000
...              ...         ...
7179  HT-CWSBLH8BK10   41.333333
7180    HT-BCPWP2LGY   18.910000
7181  HT-DWTSWBPD22D   20.200000
7182   HT-ACANHA10CB   30.000000
7183     HT-DWTC20BK  135.000000

[7184 rows x 2 columns]
>>> df1 = df1.merge(df2)
>>> df1
    type             order id             sku  ... fba fees  total       采购成本
0  Order  702-1138646-9141825   HT-CWSBLE8BKS  ...      0.0  41.78  34.560000
1  Order  701-0152570-2531474   HT-CWSBLD9BKS  ...     -8.7  16.36  39.000000
2  Order  701-6310582-5160205   HT-CWSBLD9BKS  ...     -8.7  16.36  39.000000
3  Order  701-0909993-5240234   HT-CWSBLD9BKS  ...     -8.7  16.36  39.000000
4  Order  701-5837171-7378639  HT-CWSBLD9BKXL  ...     -8.7  17.02  39.000000
5  Order  701-2584669-0129845  HT-CWSBLD9PPXL  ...      0.0  30.25  39.640288
6  Order  701-2584669-0129845  HT-CWSBLD9WTXL  ...      0.0  30.25  39.640288
7  Order  701-0200508-1054662   HT-CWSBLV8ORS  ...      0.0  33.14  40.793333
8  Order  702-1107566-1984247   HT-CWSBLD9BES  ...      0.0  30.25  40.666667
9  Order  701-0787880-4570618   HT-CWSBLD9BKM  ...     -8.7  17.02  39.492500

[10 rows x 11 columns]
>>>
```

#### pandas.DataFrame.sort_values
DataFrame.**sort_values**(*by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None*)  
沿任一轴按值排序。

**参数：**  
**by：** *__字符串或字符串列表__*

**axis：** *__{0 or ‘index’, 1 or ‘columns’}, default 0__*  
按指定轴排序。

**ascending：** *__布尔值或布尔值列表，默认为真__*  
按升序或降序排序。多重排序请使用列表。如果这是一个布尔值列表，则它必须匹配 *by* 参数的长度。

**inplace：** *__布尔值，默认为假__*  
如果为真，则就地执行。

**na_position：** *__{‘first’, ‘last’}, default ‘last’__*  
如果为 *first* 则将 NaNs 放在开头；如果为 *last* 则将 NaNs 放在末尾。

**例子**

```python
>>> df = pd.DataFrame({
...     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2': [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
...     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
... })
>>> df
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
>>>
```

按 col1 列排序

```python
>>> df.sort_values(by=['col1'])
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
>>>
```

按多列排序

```python
>>> df.sort_values(by=['col1', 'col2'])
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
>>>
```

降序排列

```python
>>> df.sort_values(by='col1', ascending=False)
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D
>>>
```

将 NAs 放在最前面

```python
>>> df.sort_values(by='col1', ascending=False, na_position='first')
  col1  col2  col3 col4
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
>>>
```  
<br/>

参考链接：  
[https://pandas.pydata.org/docs/reference/frame.html](https://pandas.pydata.org/docs/reference/frame.html)  

#### pandas 修改列名
修改所有列名  

```python
>>> df = pd.DataFrame({"A1": [1, 2], "B2": [3, 4], "C3": [5, 6], "D4": [7, 8]})
>>> df
   A1  B2  C3  D4
0   1   3   5   7
1   2   4   6   8
>>> df.columns = ["A", "B", "C", "D"]
>>> df
   A  B  C  D
0  1  3  5  7
1  2  4  6  8
```

修改指定列名  

```python
>>> df.rename(columns={"C": "c", "D": "d"}, inplace=True)
>>> df
   A  B  c  d
0  1  3  5  7
1  2  4  6  8
```

### pandas例子
pandas 示例   
1.选择DateFrame中的特定行及列  

```python
>>> import tushare as ts
>>> pro = ts.pro_api()
>>> df = pro.moneyflow_hsgt(start_date='20200511', end_date='20205015')
>>> df
  trade_date   ggt_ss   ggt_sz      hgt      sgt  north_money  south_money
0   20200515   871.53  1206.17  -111.53  1305.91      1194.38      2077.70
1   20200514  2471.56  1604.79 -1650.19   325.38     -1324.81      4076.35
2   20200513  1478.46  1915.81    26.09  -230.73      -204.64      3394.27
3   20200512   752.76  1075.14   561.87  1188.07      1749.94      1827.90
4   20200511 -2296.58   659.60  1071.89  1575.67      2647.56     -1636.98
>>> df['hgt']    # 选择'hgt'列，使用类字典属性，返回的是Series类型
0    -111.53
1   -1650.19
2      26.09
3     561.87
4    1071.89
Name: hgt, dtype: float64
>>> type(df['hgt'])
<class 'pandas.core.series.Series'>
>>> df.hgt       # 选择'hgt'列，使用点属性，返回的是Series类型
0    -111.53
1   -1650.19
2      26.09
3     561.87
4    1071.89
Name: hgt, dtype: float64
>>> type(df.hgt)
<class 'pandas.core.series.Series'>
>>> df[['hgt']]  # 选择'hgt'列，返回的是DataFrame类型
       hgt
0  -111.53
1 -1650.19
2    26.09
3   561.87
4  1071.89
>>> type(df[['hgt']])
<class 'pandas.core.frame.DataFrame'>
>>> df[['hgt', 'sgt']]  # 选择'hgt'和'sgt'列
       hgt      sgt
0  -111.53  1305.91
1 -1650.19   325.38
2    26.09  -230.73
3   561.87  1188.07
4  1071.89  1575.67
>>> df[0:2]             # 返回前两行
  trade_date   ggt_ss   ggt_sz      hgt      sgt  north_money  south_money
0   20200515   871.53  1206.17  -111.53  1305.91      1194.38      2077.70
1   20200514  2471.56  1604.79 -1650.19   325.38     -1324.81      4076.35
>>> df[1:2]             # 返回第2行，返回的是单行，如果使用 df[1] 则报错
  trade_date   ggt_ss   ggt_sz      hgt     sgt  north_money  south_money
1   20200514  2471.56  1604.79 -1650.19  325.38     -1324.81      4076.35
>>> 
```

2.查询DataFrame的总行数  

```python
>>> df = pro.income(ts_code='600031.SH', period='20191231', fields='ts_code, end_date, n_income_attr_p, update_flag')
>>> df
     ts_code  end_date  n_income_attr_p update_flag
0  600031.SH  20191231     1.120666e+10           0
1  600031.SH  20191231     1.120666e+10           1
>>> len(df)
2
>>> len(df.index)
2
>>>
```

```python
In [125]: df = pro.income(ts_code='600031.SH', start_date='20160101', end_date='20200531', 
     ...:                fields='ts_code, ann_date, end_date, n_income_attr_p, update_flag')                   

In [126]: df1 = df[df['end_date'].isin(['20161231', '20171231', '20181231', '20191231'])]                      

In [127]: df1              
Out[127]: 
      ts_code  ann_date  end_date  n_income_attr_p update_flag
1   600031.SH  20200424  20191231     1.120666e+10           1
2   600031.SH  20200424  20191231     1.120666e+10           0
9   600031.SH  20190401  20181231     6.116288e+09           1
13  600031.SH  20180417  20171231     2.092253e+09           1
17  600031.SH  20170428  20161231     2.034570e+08           0

In [128]: timeit df1.shape 
1.49 µs ± 483 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [129]: timeit len(df1)  
738 ns ± 91.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [130]: timeit len(df1.index)                        
548 ns ± 91.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

可以看到，在效率上 len(df1.index) > len(df1) > df1.shape ，如果要计算DataFrame的总行数，df.index 是更好的选择。  

3. 计算 DataFrame 指定列的列值之和  
计算前三行 north_money 列的列值之和

```python
>>> df
  trade_date      hgt       sgt  north_money
0   20200716 -2371.68  -4548.68     -6920.36
1   20200715 -1474.22  -1231.40     -2705.62
2   20200714 -4995.06 -12389.09    -17384.15
3   20200713  3342.22   3508.13      6850.35
4   20200710 -1703.96  -2689.16     -4393.12
5   20200709  3327.99   4623.42      7951.41
>>> df.north_money[0:3].sum()
-27010.13
>>>
```

## pip
## 安装
### 我需要安装pip吗？
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from [python.org](https://www.python.org/) or if you are working in a [Virtual Environment](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments) created by [virtualenv](https://packaging.python.org/key_projects/#virtualenv) or [pyvenv](https://packaging.python.org/key_projects/#venv). Just make sure to [upgrade pip](https://pip.pypa.io/en/latest/installing/#upgrading-pip).

### 升级pip
On Linux or macOS:  
`pip install -U pip`

On Windows:  
`python -m pip install -U pip`

## 参考指南
### pip install
#### 描述
Install packages from:

* PyPI (and other indexes) using requirement specifiers.
* VCS project urls.
* Local project directories.
* Local or remote source archives.

pip also supports installing from “requirements files”, which provide an easy way to specify a whole environment to be installed.

##### 概述
Pip 安装有几个阶段：

1. Identify the base requirements. The user supplied arguments are processed here.
2. 解决依赖。什么将被安装是在这里决定的。
3. 构建 wheels. All the dependencies that can be are built into wheels.
4. 安装指定的包 (and uninstall anything being upgraded/replaced).

##### VCS 支持
pip 支持从 Git, Mercurial, Subversion 和 Bazaar 安装，并使用 URL 前缀：`git+`, `hg+`, `svn+`, 和 `bzr+` 来检测 VCS 的类型。

pip 要求你的路径中存在一个有效的 VCS 命令： `git`, `hg`, `svn`, 或 `bzr`。

VCS 项目可以在 [可编辑模式](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) (使用 [--editable](https://pip.pypa.io/en/stable/reference/pip_install/#install-editable) 选项) 下被安装，也可以不使用可编辑模式。

* 对于可编辑模式安装，在虚拟环境下默认的克隆位置是 `<venv path>/src/SomeProject`，而全局安装的默认克隆位置是 `<cwd>/src/SomeProject`。[--src](https://pip.pypa.io/en/stable/reference/pip_install/#install-src) 选项可以被用来修改这个位置。  
* 对于非可编辑模式安装，项目在本地的一个临时目录中构建，然后被正常地安装。注意如果一个符合要求的包的版本已经被安装了，没有一个 `--upgrade` 标志 VCS 源将不会覆盖它。VCS requirements pin the package version (specified in the `setup.py` file) of the target commit, not necessarily the commit itself.  
* 当且仅当使用可编辑选项安装完成时，[pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/#pip-freeze) 子命令将记录 VCS 要求说明符 (引用一个特定的提交)。

URL 后缀的 “project name” 组件 `egg=<project name>` 被 pip 用于它的依赖逻辑以在 pip 下载及分析元数据前确认项目。对于 `setup.py` 不在项目根目录的项目，“subdirectory” 组件被使用。“subdirectory” 组件的值应该是一个从项目的根目录开始到 `setup.py` 所在位置的一个路径。

所以如果你的仓库布局是：

* pkg_dir/  
    * setup.py # 包 `pkg` 的 setup.py  
    * some_module.py  
* other_dir/  
    * some_file  
* some_other_file  

你必须使用 `pip install -e vcs+protocol://repo_url/#egg=pkg&subdirectory=pkg_dir`.

**Git**  
pip 现在支持通过 `git`, `git+http`, `git+https`, `git+ssh`, `git+git` 和 `git+file` 进行克隆：

下面是支持的形式：

```sh
[-e] git://git.example.com/MyProject#egg=MyProject  
[-e] git+http://git.example.com/MyProject#egg=MyProject  
[-e] git+https://git.example.com/MyProject#egg=MyProject  
[-e] git+ssh://git.example.com/MyProject#egg=MyProject  
[-e] git+git://git.example.com/MyProject#egg=MyProject  
[-e] git+file:///home/user/projects/MyProject#egg=MyProject  
-e git+git@git.example.com:MyProject#egg=MyProject  
```

传递一个分支名称，一个提交哈希值，a tag name or a git ref is possible like so:

```sh
[-e] git://git.example.com/MyProject.git@master#egg=MyProject  
[-e] git://git.example.com/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject  
[-e] git://git.example.com/MyProject.git@v1.0#egg=MyProject  
[-e] git://git.example.com/MyProject.git@refs/pull/123/head#egg=MyProject  
```

当传递一个提交哈希值时，指定一个完整的哈希值比一个部分的哈希值更好，因为一个完整的哈希值允许 pip 更高效地操作 (例如： 通过创建更少的网络调用)。

#### 选项
--user  
Install to the Python user install directory for your platform. 通常是 `~/.local/`，或者 Windows 平台的 %APPDATA%\Python 。 (See the Python documentation for site.USER\_BASE for full details.)

-U, --upgrade  
升级所有指定的包到最新的可用版本。依赖的处理依赖于使用的升级策略。

### PyMongo
GitHub：[https://github.com/mongodb/mongo-python-driver](https://github.com/mongodb/mongo-python-driver)  
官方文档：[https://api.mongodb.com/python/current](https://api.mongodb.com/python/current/)  

安装PyMongo  

```sh
$ pip3 install pymongo
```

使用 [find_one()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one) 获取一个单一的文档

在MongoDB中可以被执行的最基本的查询类型是 [find_one()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one)。这个方法返回一个匹配查询的单一的文档 (或者 `None` 如果没有文档被匹配)。这很有用当你知道那里仅有一个匹配文档，或者仅对第一个匹配有兴趣。

**find_and_modify**(*query={}, update=None, upsert=False, sort=None, full_response=False, manipulate=False, \*\*kwargs*)  
更新并返回一个对象。

**弃用** - 使用 [find_one_and_delete()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_delete), [find_one_and_replace()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_replace), 或者 [find_one_and_update()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_update) 代替。

### PyMySQL
GitHub：[https://github.com/PyMySQL/PyMySQL](https://github.com/PyMySQL/PyMySQL)  
官方文档：[https://pymysql.readthedocs.io/en/latest/](https://pymysql.readthedocs.io/en/latest/)  

安装PyMySQL  

```sh
$ pip3 install pymysql
```

### pyquery
GitHub：[https://github.com/gawel/pyquery](https://github.com/gawel/pyquery)  
官方文档：[https://pyquery.readthedocs.io/en/latest/](https://pyquery.readthedocs.io/en/latest/)  

**安装pyquery**  

```sh
$ pip3 install pyquery
```

### pyspider
官方文档：[http://docs.pyspider.org/en/latest/](http://docs.pyspider.org/en/latest/)  
GitHub：[https://github.com/binux/pyspider](https://github.com/binux/pyspider)  
官方教程：[http://docs.pyspider.org/en/latest/tutorial/](http://docs.pyspider.org/en/latest/tutorial/)  

pyspider需要用到PhantomJS，所以在安装pyspider前，需要先安装好PhantomJS。  
pyspider还依赖于pycurl、WsgiDAV以及其它第三方Python库，且不支持最新版的WsgiDAV 3.0.0，需要安装2.4.1版本的WsgiDAV（因为3.0.0版本的WsgiDAV改变了一些选项的名称，而pyspider中引用的依旧是老版本中的选项名称）。    

pycurl PyPI：[https://pypi.org/project/pycurl/](https://pypi.org/project/pycurl/)  
pycurl 下载地址：[https://pypi.org/project/pycurl/#files](https://pypi.org/project/pycurl/#files)  

pycurl支持的Python版本：  
Python2： 2.7  
Python3： 3.4-3.6  

**Windows平台**  
Windows平台建议直接到 [https://pypi.org/project/pycurl/#files](https://pypi.org/project/pycurl/#files) 下载Wheel文件安装（如 pycurl-7.43.0.2-cp36-cp36m-win_amd64.whl）。  

```
C:\Users\Administrator\Downloads>pip3 install pycurl-7.43.0.2-cp36-cp36m-win_amd64.whl
```

如果此处直接使用 `pip3 install pycurl` 编译安装pycurl，通常会出现类似下面的报错信息：

```
Command "python setup.py egg_info" failed with error code 10 in C:\Users\YWH\AppData\Local\Temp\pip-install-v7jh2bj2\pycurl\
```

安装WsgiDAV 2.4.1和pyspider

```
C:\Users\Administrator\Downloads>pip3 install wsgidav==2.4.1
C:\Users\Administrator\Downloads>pip3 install pyspider
```

运行pyspider

```
C:\Users\Administrator\Downloads>pyspider all
```

**Linux平台安装pyspider**  
Ubuntu 18.04.1 LTS  

安装PhantomJS  

```sh
# apt install libfontconfig1
# wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
# tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
# cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
```

安装pip3

```sh
# apt install python3-pip
```

安装编译pycurl需要的包  
libcurl4-openssl-dev包提供/usr/bin/curl-config文件  
libssl-dev包提供/usr/include/openssl/ssl.h文件

```sh
# apt install libcurl4-openssl-dev
# apt install libssl-dev
```

安装pycurl

```sh
# pip3 install pycurl
```

安装WsgiDAV 2.4.1  

```sh
# pip3 install wsgidav==2.4.1
```

如果不指定版本，会安装最新版的WsgiDAV 3.0.0，如果安装最新版的WsgiDAV，启动pyspider会报下面的错误：

```
ValueError: Invalid configuration:
  - Deprecated option 'domaincontroller': use 'http_authenticator.domain_controller' instead.
```

这是因为3.0.0版的WsgiDAV重命名了之前版本中的某些选项名，而pyspider中引用的仍旧是之前的选项名。

安装pyspider

```sh
# pip3 install pyspider
```

运行pyspider

```sh
# pyspider all
```

**CentOS Linux release 7.6.1810 (Core)**  
**安装pycurl**  
1. 安装libcurl-devel  

```sh
# yum install libcurl-devel  
```

libcurl-devel包提供/usr/bin/curl-config文件，若不安装此包，安装pycurl时会出现下面的错误提示：

```
FileNotFoundError: [Errno 2] No such file or directory: 'curl-config': 'curl-config'
```

2. 指定编译pycurl时所使用的SSL后端

```sh
export PYCURL_SSL_LIBRARY=nss
```

若不指定编译pycurl时所使用的SSL后端，则安装pycurl时会出现下面的错误提示：

```
__main__.ConfigurationError: Curl is configured to use SSL, but we have not been able to determine w
hich SSL backend it is using. Please see PycURL documentation for how to specify the SSL backend manuall
y.
```

3. 安装pycurl

```sh
# pip3 install pycurl
```

**安装2.4.1版本的WsgiDAV**  

```sh
# pip3 install wsgidav==2.4.1
```

**安装pyspider**

```sh
# pip3 install pyspider
```

**启动pyspider**

```sh
# pyspider all
```

**注意：**  
如果为pycurl指定了错误的SSL后端（`export PYCURL_SSL_LIBRARY=openssl`），则在运行pyspider时，会出现下面的错误提示：

```py
ImportError: pycurl: libcurl link-time ssl backend (nss) is different from compile-time ssl backend (ope
nssl)
```

**macOS平台安装pyspider**  
安装pycurl  

```sh
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS="-L/usr/local/opt/openssl/lib”
export CPPFLAGS="-I/usr/local/opt/openssl/include"
python3.6 -m pip install pycurl
```

安装WsgiDAV 2.4.1  

```sh
python3.6 -m pip install wsgidav==2.4.1
```

安装pyspider，之后启动pyspider  

```sh
python3.6 -m pip install pyspider
pyspider
```

通过Homebrew安装openssl时，在安装完成之后会有一个类似下面的提示：

```
For compilers to find openssl you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl/include”
```

### redis-py
GitHub：[https://github.com/andymccurdy/redis-py](https://github.com/andymccurdy/redis-py)  
官方文档：[https://redis-py.readthedocs.io/en/latest/](https://redis-py.readthedocs.io/en/latest/)  

安装redis-py  

```sh
$ pip3 install redis
```

### Requests
GitHub地址：[https://github.com/kennethreitz/requests](https://github.com/kennethreitz/requests)  
Pypi地址：[https://pypi.org/project/requests/](https://pypi.org/project/requests/)  
官方文档：[https://2.python-requests.org/en/master/](https://2.python-requests.org/en/master/)  
中文文档：[http://docs.python-requests.org/zh_CN/latest/](http://docs.python-requests.org/zh_CN/latest/)  

**安装requests**  

```sh
$ pip3 install requests
```

#### 快速上手
##### 定制请求头
如果你想为请求添加 HTTP 头部，只要简单地传递一个 `dict` 给 `headers` 参数就可以了。

```python
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> r = requests.get(url, headers=headers)
>>>
```

#### SOCKS
版本 2.10.0 中新增。

除了基本的 HTTP 代理，Requests 也支持使用 SOCKS 协议的代理。这是一个可选的特性，在使用以前它要求已安装额外的第三方库。

这个特性的相关依赖你可以通过 `pip` 获取：

```sh
$ pip install requests[socks]
```

一旦你安装好那些依赖，使用一个 SOCKS 代理和使用一个 HTTP 代理一样简单：

```python
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
```

使用 `socks5` 方案会导致 DNS 解析发生在客户端，而不是在代理服务器上。这和 curl 是一致的，curl 使用协议方案来决定是在客户端还是在代理上做 DNS 解析。如果你想在代理服务器上做域名解析，使用 `socks5h` 作为协议方案。

### SciPy 
官方网站：[https://scipy.org](https://scipy.org)  

SciPy 是一个基于 Python 的用于数学，科学以及工程学的开源软件生态系统。特别地，这些是一些核心包：  
* **NumPy** 基于N维数组的包  
* **SciPy 库** 用于科学计算的基础库  
* **Matplotlib** 全面的 2-D 绘图库  
* **IPython** 增强的交互式控制台  
* **SymPy** 符号数学  
* **pandas** 数据结构与分析  

### Scrapy
官方网站：[https://scrapy.org](https://scrapy.org)  
官方文档：[https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)  
PyPI：[https://pypi.org/project/Scrapy](https://pypi.org/project/Scrapy/)  
GitHub：[https://github.com/scrapy/scrapy](https://github.com/scrapy/scrapy)  
中文文档：[http://scrapy-chs.readthedocs.io](http://scrapy-chs.readthedocs.io)  

**Windows平台**  
1. 安装好Visual Studio Community 2017（需要安装编译器及Windows SDK组件）；
2. 通过 `pip3 install scrapy` 命令安装。

**Linux及macOS平台**  

```sh
$ pip3 install scrapy
```

#### scrapy命令用法
用法：

```
  scrapy <command> [options] [args]
```

可用命令：

```
  runspider     运行一个自包含的蜘蛛 (不创建项目)
```

关于一个命令的更详细信息请使用 "scrapy <command> -h" 查看

##### scrapy crawl
用法  

```
  scrapy crawl [options] <spider>
```

运行一个蜘蛛

选项  

```
-a NAME=VALUE           设置蜘蛛参数 (可以重复)
```

##### scrapy runspider
用法  

```
  scrapy runspider [options] <spider_file>
```

选项    

```
--output=FILE, -o FILE  转储爬取的元素到 FILE 中 (标准输出使用 - )
```

设置一个新的Scrapy项目  

```
scrapy startproject tutorial
```

### Scrapy-Redis
GitHub：[https://github.com/rmax/scrapy-redis](https://github.com/rmax/scrapy-redis)  
PyPI：[https://pypi.org/project/scrapy-redis](https://pypi.org/project/scrapy-redis)  
官方文档：[https://scrapy-redis.readthedocs.io/en/stable/](https://scrapy-redis.readthedocs.io/en/stable/)  
**安装Scrapy-Redis**  

```sh
pip3 install scrapy-redis
```

### Scrapy-Splash
GitHub：[https://github.com/scrapy-plugins/scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)  
PyPI：[https://pypi.org/project/scrapy-splash](https://pypi.org/project/scrapy-splash/)  
使用说明：[https://github.com/scrapy-plugins/scrapy-splash#configuration](https://github.com/scrapy-plugins/scrapy-splash#configuration)  
Splash官方文档：[https://splash.readthedocs.io/en/stable/](https://splash.readthedocs.io/en/stable/)  

**安装Splash**  
建议直接通过Docker安装并启动。

```sh
docker run --name splash -p 8050:8050 scrapinghub/splash
```

或者以后台运行的方式启动容器

```sh
docker run --name splash -d -p 8050:8050 scrapinghub/splash
```

**安装Scrapy-Splash**  

```sh
pip3 install scrapy-splash
```

### Scrapyd
GitHub：[https://github.com/scrapy/scrapyd](https://github.com/scrapy/scrapyd)  
PyPI：[https://pypi.org/project/scrapyd](https://pypi.org/project/scrapyd)  
官方文档：[https://scrapyd.readthedocs.io/en/stable/](https://scrapyd.readthedocs.io/en/stable/)  

**安装Scrapyd**  

```sh
pip3 install scrapyd
```

**配置Scrapyd**  
配置文件  
Scrapyd 在下列位置搜索配置文件，并按顺序分析它们，最上面的优先级最高：

* `/etc/scrapyd/scrapyd.conf` (Unix)  
* `c:\scrapyd\scrapyd.conf` (Windows)  
* `/etc/scrapyd/conf.d/*` (按字母顺序，Unix)  
* `scrapyd.conf`  
* `~/.scrapyd.conf` (用户Home目录)  

配置文件支持下面的选项 (默认值参见示例配置)。

**示例配置文件**  
这是一个带所有默认值的示例配置文件：

```
[scrapyd]
eggs_dir    = eggs
logs_dir    = logs
items_dir   =
jobs_to_keep = 5
dbs_dir     = dbs
max_proc    = 0
max_proc_per_cpu = 4
finished_to_keep = 100
poll_interval = 5.0
bind_address = 127.0.0.1
http_port   = 6800
debug       = off
runner      = scrapyd.runner
application = scrapyd.app.application
launcher    = scrapyd.launcher.Launcher
webroot     = scrapyd.website.Root

[services]
schedule.json     = scrapyd.webservice.Schedule
cancel.json       = scrapyd.webservice.Cancel
addversion.json   = scrapyd.webservice.AddVersion
listprojects.json = scrapyd.webservice.ListProjects
listversions.json = scrapyd.webservice.ListVersions
listspiders.json  = scrapyd.webservice.ListSpiders
delproject.json   = scrapyd.webservice.DeleteProject
delversion.json   = scrapyd.webservice.DeleteVersion
listjobs.json     = scrapyd.webservice.ListJobs
daemonstatus.json = scrapyd.webservice.DaemonStatus
```

CentOS 7配置Scrapyd  

```sh
# mkdir /etc/scrapyd
# cp /usr/local/lib/python3.6/site-packages/scrapyd/default_scrapyd.conf /etc/scrapyd/scrapyd.conf
# vim /etc/scrapyd/scrapyd.conf
```

修改 `/etc/scrapyd/scrapyd.conf` 文件，将 `max_proc_per_cpu` 和 `bind_address` 的值修改为如下即可：

```
max_proc_per_cpu = 10
bind_address = 0.0.0.0
```

配置访问认证  

1. 安装nginx

```sh
# yum install nginx
```

2. 修改 `/etc/nginx/nginx.conf` 文件，在 `http` 块下面添加一个 `server` 块，内容如下：

```
    server {
        listen 6801;
        location / {
            proxy_pass    http://127.0.0.1:6800/;
            auth_basic    "Restricted";
            auth_basic_user_file    /etc/nginx/conf.d/.htpasswd;
        }
    }
```

3. 为Scrapyd创建一个名为admin的认证用户，并将 `.htpasswd` 文件放在 `/etc/nginx/conf.d` 目录下；

```sh
# cd /etc/nginx/conf.d
# htpasswd -c .htpasswd admin
```

4. 允许Nginx绑定到6801端口

```sh
# semanage port -a -t http_port_t -p tcp 6801
```

5. 允许Nginx连接到网络端口6800

```sh
# semanage port -a -t http_port_t -p tcp 6800
```

6. 启动nginx

```sh
# systemctl start nginx
```

### Scrapyd API
GitHub：[https://github.com/djm/python-scrapyd-api](https://github.com/djm/python-scrapyd-api)  
PyPI：[https://pypi.org/project/python-scrapyd-api](https://pypi.org/project/python-scrapyd-api)  
官方文档：[http://python-scrapyd-api.readthedocs.io/en/latest/usage.html](https://python-scrapyd-api.readthedocs.io/en/latest/usage.html)  

**安装Scrapyd API**  

```sh
pip3 install python-scrapyd-api
```

### Scrapyd-Client
GitHub：[https://github.com/scrapy/scrapyd-client](https://github.com/scrapy/scrapyd-client)  
PyPI：[https://pypi.org/project/scrapyd-client](https://pypi.org/project/scrapyd-client)  
使用说明：[https://github.com/scrapy/scrapyd-client#scrapyd-deploy](https://github.com/scrapy/scrapyd-client#scrapyd-deploy)  

**安装Scrapyd-Client**  

```sh
pip3 install scrapyd-client
```

### Scrapyrt
GitHub：[https://github.com/scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt)  
PyPI：[https://pypi.org/project/scrapyrt](https://pypi.org/project/scrapyrt/)  
官方文档：[https://scrapyrt.readthedocs.io/en/latest/](https://scrapyrt.readthedocs.io/en/latest/)  

**安装Scrapyrt**  

```sh
pip3 install scrapyrt
```

### Selenium
官方网站：[https://www.seleniumhq.org](https://www.seleniumhq.org)  
GitHub地址：[https://github.com/SeleniumHQ/selenium/tree/master/py](https://github.com/SeleniumHQ/selenium/tree/master/py)  
PyPI：[https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)  
官方文档：[https://selenium-python.readthedocs.io](https://selenium-python.readthedocs.io)  
中文文档：[https://selenium-python-zh.readthedocs.io/en/latest/](https://selenium-python-zh.readthedocs.io/en/latest/)  

**安装selenium**  

```sh
$ pip3 install selenium  
```

### tesserocr
tesserocr 是 Python 的一个 OCR 识别库，但其实它是对 tesseract 做的一层 Python API 封装，所以它的核心是 tesseract。因此，在安装 tesserocr 之前，我们需要先安装 tesseract。

tesserocr GitHub：[https://github.com/sirfz/tesserocr](https://github.com/sirfz/tesserocr)  
tesserocr PyPI：[https://pypi.org/project/tesserocr/](#https://pypi.org/project/tesserocr/)  
tesseract 下载地址：[https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/)  
tesseract GitHub：[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)  
tesseract 语言包：[https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata)  
tesseract 文档：[https://github.com/tesseract-ocr/tesseract/wiki/Documentation](https://github.com/tesseract-ocr/tesseract/wiki/Documentation)  

**Windows平台**  
安装tesseract  

1. 到 [https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/) 页面下载 tesseract-ocr-w64-setup-v4.0.0.20181030.exe 文件；
2. 双击下载的 tesseract-ocr-w64-setup-v4.0.0.20181030.exe 文件，在安装的过程中可以勾选“Additional language data (download)”选项来安装 OCR 识别支持的语言包，这样 OCR 便可以识别多国语言。
3. 安装完成后需要把tesseract安装目录下的tessdata目录复制到Python的安装目录下，否则调用时会出现类似下面的错误提示：

```python
RuntimeError: Failed to init API, possibly an invalid tessdata path: d:\program files\python37\/tessdata/
```

安装tesserocr  
通过pip安装  
从 [simonflueckiger/tesserocr-windows_build/releases](https://github.com/simonflueckiger/tesserocr-windows_build/releases) 下载对应你的Windows平台和Python版本的 wheel 文件，并通过下面的方式安装：

```
> pip install <package_name>.whl
```

tesserocr 的安装方法请参考：[tesserocr 的PyPI主页](https://pypi.org/project/tesserocr/)

**Linux平台**  
CentOS和Red Hat  
安装tesseract  

```sh
# yum install tesseract -y
```

列出支持的语言列表  

```sh
$ tesseract --list-langs  
List of available languages (1):
```

如果想要支持多国语言，还需要安装语言包，官方叫作 tessdata。

```sh
$ git clone https://github.com/tesseract-ocr/tessdata.git
# mv tessdata/* /usr/share/tesseract/tessdata/
```

再次查看tesseract支持的语言列表

```sh
$ tesseract --list-langs
List of available languages (129):
```

安装tesserocr  
安装必要的依赖包  

```sh
# yum install python36-devel leptonica-devel tesseract-devel
```

安装tesserocr  

```sh
$ pip3 install tesserocr
```

**macOS平台**  
系统环境：  
macOS High Sierra (10.13.6)  
Python 3.7.2  
Python 2.7.10  

通过Homebrew安装tesseract  

```sh
$ brew install tesseract
$ brew install tesseract-lang
```

默认安装的是tesseract的最新版，版本是4.0.0。

安装tesserocr  
通过pip3安装tesserocr  

```sh
$ pip3 install tesserocr
```

安装tesseract 4.0.0后，在Python 3.7.2中导入tesserocr模块时会出现如下错误（Python 2.7.10中可以正常导入）：

```python
>>> import tesserocr
!strcmp(locale, "C"):Error:Assert failed:in file baseapi.cpp, line 209
[1]    5249 illegal hardware instruction  python3
```

解决办法一  
导入tesserocr前，将LC_ALL的值设为'C'。

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL,'C')
'C'
>>> import tesserocr
```

解决办法二  
安装tesseract 3.05.02  

1. 从 [https://raw.githubusercontent.com/Homebrew/homebrew-core/5df6eb919506a097b2efb1df34a16e3a147c8731/Formula/tesseract.rb](https://raw.githubusercontent.com/Homebrew/homebrew-core/5df6eb919506a097b2efb1df34a16e3a147c8731/Formula/tesseract.rb) 下载 tesseract.rb 文件，之后修改 tesseract.rb 文件，将文件中第65行的 “needs :cxx11” 删掉，之后保存，如果不修改 tesseract.rb 文件，安装时会报如下错误：

```
Error: tesseract: "cxx11" is not a recognized standard
```

2. 切换到刚才下载的 tesseract.rb 文件所在的目录，执行如下命令：

```sh
$ brew install tesseract.rb --with-all-languages
$ pip3 install tesserocr
$ pip3 install pillow
```

### Tornado
GitHub：[https://github.com/tornadoweb/tornado](https://github.com/tornadoweb/tornado)  
官方文档：[http://www.tornadoweb.org/en/stable/](http://www.tornadoweb.org/en/stable/)  

安装Tornado

```sh
$ pip3 install tornado
```

## tushare
Tushare官方网站：[https://tushare.pro](https://tushare.pro)  
Tushare官方文档：[http://tushare.org](http://tushare.org)  

### 安装tushare  
tushare依赖于lxml、requests

```sh
$ pip3 install --user lxml requests tushare
```

### 初始化pro接口
**导入tushare**

```python
import tushare as ts
```

**设置token**

```python
ts.set_token('your token here')
```

以上方法只需要在第一次或者token失效后调用，完成调取tushare数据凭证的设置，正常情况下不需要重复设置。也可以忽略此步骤，直接用pro_api('your token')完成初始化

**初始化pro接口**

```python
pro = ts.pro_api()
```

如果上一步骤ts.set_token('your token')无效或不想保存token到本地，也可以在初始化接口里直接设置token:

```python
pro = ts.pro_api('your token')
```

### 利润表
接口：income  
权限：用户需要至少800积分才可以调取  

income 接口可以查询股票的净利润

**输入参数**  

名称         |类型  |必选  |描述
------------|------|------|-----
ts_code     |str   |Y     |TS股票代码  
start_date  |str   |N     |公告开始日期  
end_date    |str   |N     |公告结束日期  
period      |str   |N     |报告期(每个季度最后一天的日期，比如20171231表示年报)  

**输出参数**  

名称             |类型    |默认显示  |描述
-----------------|-------|---------|-----
ts_code          |str    |Y        |TS代码  
ann_date         |str    |Y        |公告日期  
end_date         |str    |Y        |报告期  
n_income_attr_p  |float  |Y        |净利润(不含少数股东损益)  
update_flag      |str    |N        |更新标识，0未修改1更正过  

n_income_attr_p 对应的就是同花顺财务报表中的净利润  

获取三一重工2016 ~ 2019年度的年报中的净利润数据  

```python
>>> df = pro.income(ts_code='600031.SH', start_date='20160101', end_date='20200531', fields='ts_code, ann_date, end_date, n_income_attr_p, update_flag')
>>> df_year = df[df['end_date'].isin(['20161231', '20171231', '20181231', '20191231'])]
>>> df_year_dup = df_year.drop_duplicates(subset=['end_date'])  # subset 参数表示仅考虑 end_date 列
>>> df_year_dup
      ts_code  ann_date  end_date  n_income_attr_p update_flag
1   600031.SH  20200424  20191231     1.120666e+10           1
9   600031.SH  20190401  20181231     6.116288e+09           1
13  600031.SH  20180417  20171231     2.092253e+09           1
17  600031.SH  20170428  20161231     2.034570e+08           0
>>>
```

### 财务指标数据
#### 资产负债表
接口：balancesheet  
权限：每分钟最多访问200次  

**输出参数**  

名称                        |类型    |默认显示  |描述  
----------------------------|-------|----------|----
ts_code                     |str    |Y         |TS股票代码  
ann_date                    |str    |Y         |公告日期  
end_date                    |str    |Y         |报告期  
total_cur_assets            |float  |Y         |流动资产合计  
goodwill                    |str    |Y         |商誉  
total_nca                   |float  |Y         |非流动资产合计  
total_assets                |float  |Y         |资产总计  
total_liab                  |float  |Y         |负债合计  
total_hldr_eqy_exc_min_int  |float  |Y         |股东权益合计（不含少数股东权益）  
update_flag                 |str    |N         |更新标识  

total_assets 对应同花顺中的“资产合计”。  
total_hldr_eqy_exc_min_int 对应的即是同花顺中的“净资产”概念。  
资产负债率 = 负债合计/资产合计 * 100%  

#### 财务指标数据
接口： fina_indicator  
权限： 用户需要至少800积分才可以调取，每分钟最多可访问该接口200次  

fina_indicator 接口可以查询股票的ROE  
fina_indicator 不包括“业绩预告”  

**输入参数**  

名称         |类型  |必选  |描述
------------|------|------|-----
ts_code     |str   |Y     |TS股票代码,e.g. 600001.SH/000001.SZ  
start_date  |str   |N     |报告期开始日期  
end_date    |str   |N     |报告期结束日期  

**输出参数**

名称               |类型  |默认显示  |描述
-------------------|------|---------|-------
ts_code            |str   |Y        |TS代码  
ann_date           |str   |Y        |公告日期  
end_date           |str   |Y        |报告期  
extra_item         |float |Y        |非经常性损益  
profit_dedt        |float |Y        |扣除非经常性损益后的净利润  
netprofit_margin   |float |Y        |销售净利率  
grossprofit_margin |float |Y        |销售毛利率  
profit_to_gr       |float |Y        |净利润/营业总收入  
roe                |float |Y        |净资产收益率  
netprofit_yoy      |float |Y        |归属母公司股东的净利润同比增长率(%)  
update_flag        |str   |N        |更新标识  

净利润（同花顺中的净利润） = 非经常性损益（extra_item） + 扣除非经常性损益后的净利润（profit_dedt）  
netprofit_yoy 对应的是同花顺财务板块中的净利润同比增幅；  
netprofit_margin 和 profit_to_gr 对应的都是净利率；  

**常见用法**  
1.根据股票代码获取单个股票的历史交易数据  

```python
>>> import tushare as ts
>>> ts.get_hist_data('600568')
```

2.设定历史数据的时间

```python
>>> import tushare as ts
>>> ts.get_hist_data('600568', start='2019-12-18', end='2020-01-19')
```
