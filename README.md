* [导航](#导航)
* [Markdown](#markdown)
* [HTML](#html)
* [Python](#python)
    * [Python 3 标准库](#python-3-标准库)
        * [内置函数](#内置函数)
        * [内置类型](#内置类型)
            * [数值类型 — int, float, complex](#数值类型--int-float-complex)
                * [整型数类型的按位运算](#整型数类型的按位运算)
            * [集合类型 --- set, frozenset](#集合类型-----set-frozenset)
        * [文本处理服务](#文本处理服务)
            * [string — 通用字符串操作](#string--通用字符串操作)
                * [格式化字符串语法](#格式化字符串语法)
            * [re — 正则表达式操作](#re--正则表达式操作)
                * [正则表达式语法](#正则表达式语法)
                * [模块内容](#模块内容)
                * [正则表达式对象](#正则表达式对象)
                * [匹配对象](#匹配对象)
                * [正则表达式例子](#正则表达式例子)
        * [二进制数据服务](#二进制数据服务)
            * [codecs — 编解码器注册和相关基类](#codecs--编解码器注册和相关基类)
    * [数据类型](#数据类型)
        * [collections --- 容器数据类型](#collections-----容器数据类型)
        * [collections.abc --- 容器的抽象基类](#collectionsabc-----容器的抽象基类)
    * [函数式编程模块](#函数式编程模块)
        * [itertools -- 为高效循环创建迭代器的函数](#itertools----为高效循环创建迭代器的函数)
    * [文件和目录访问](#文件和目录访问)
        * [os.path — 通用路径名操作](#ospath--通用路径名操作)
    * [通用操作系统服务](#通用操作系统服务)
        * [os --- 各种各样的操作系统接口](#os-----各种各样的操作系统接口)
            * [进程参数](#进程参数)
            * [文件和目录](#文件和目录)
            * [进程管理](#进程管理)
            * [各种各样的系统信息](#各种各样的系统信息)
        * [time — 时间的访问和转化](#time--时间的访问和转化)
            * [函数](#函数)
        * [platform --- 获取底层平台的标识数据](#platform-----获取底层平台的标识数据)
    * [并发执行](#并发执行)
        * [threading — 基于线程的并行](#threading--基于线程的并行)
            * [线程对象](#线程对象)
        * [multiprocessing — 基于进程的并行](#multiprocessing--基于进程的并行)
            * [介绍](#介绍)
                * [进程类](#进程类)
                * [上下文和启动方法](#上下文和启动方法)
            * [参考](#参考)
                * [进程和异常](#进程和异常)
                * [其它](#其它)
        * [subprocess --- 子进程管理](#subprocess-----子进程管理)
    * [网络和进程间通信](#网络和进程间通信)
        * [socket --- 底层网络接口](#socket-----底层网络接口)
    * [互联网数据处理](#互联网数据处理)
        * [json --- JSON 编码和解码器](#json-----json-编码和解码器)
    * [互联网协议与支持](#互联网协议与支持)
        * [urllib.request — 打开URLs的可扩展库](#urllibrequest--打开urls的可扩展库)
            * [OpenerDirector对象](#openerdirector对象)
        * [urllib.parse — 将URLs解析为组件](#urllibparse--将urls解析为组件)
            * [URL解析](#url解析)
        * [urllib.error — urllib.request抛出的异常类](#urlliberror--urllibrequest抛出的异常类)
        * [urllib.robotparser — 解析robots.txt](#urllibrobotparser--解析robotstxt)
    * [Python运行时服务](#python运行时服务)
        * [\_\_main\_\_ --- 顶层脚本环境](#__main__-----顶层脚本环境)
    * [Python语言参考](#python语言参考)
        * [3. 数据模型](#3-数据模型)
            * [3.3. 特殊方法名](#33-特殊方法名)
                * [3.3.1. 基本自定义](#331-基本自定义)
                * [3.3.7. 仿真容器类型](#337-仿真容器类型)
        * [5. 导入系统](#5-导入系统)
            * [5.1. importlib](#51-importlib)
            * [5.2. 包](#52-包)
            * [5.3. 搜索](#53-搜索)
            * [5.5. 基于路径的查找器](#55-基于路径的查找器)
            * [5.7. 包相对导入](#57-包相对导入)
            * [5.8. 有关 \_\_main\_\_ 的特殊事项](#58-有关-__main__-的特殊事项)
* [Python 教程](#python-教程)
    * [5. 数据结构](#5-数据结构)
        * [5.1. 列表的更多特性](#51-列表的更多特性)
    * [6. 模块](#6-模块)
        * [6.1. 有关模块的更多信息](#61-有关模块的更多信息)
        * [6.2. 标准模块](#62-标准模块)
        * [6.3. dir() 函数](#63-dir-函数)
        * [6.4. 包](#64-包)
    * [9. 类](#9-类)
        * [9.1. 名称和对象](#91-名称和对象)
        * [9.2. Python 作用域和命名空间](#92-python-作用域和命名空间)
        * [9.3. 初探类](#93-初探类)
        * [9.4. 补充说明](#94-补充说明)
        * [9.5. 继承](#95-继承)
        * [9.6. 私有变量](#96-私有变量)
        * [9.7. 杂项说明](#97-杂项说明)
        * [9.8. 迭代器](#98-迭代器)
        * [9.9. 生成器](#99-生成器)
        * [9.10. 生成器表达式](#910-生成器表达式)
* [Python安装和使用](#python安装和使用)
    * [1. 命令行与环境](#1-命令行与环境)
* [Python Wiki](#python-wiki)
    * [WindowsCompilers](#windowscompilers)
* [Python HOWTOs](#python-howtos)
    * [套接字编程指南](#套接字编程指南)
    * [如何使用urllib包获取互联网资源](#如何使用urllib包获取互联网资源)
        * [头信息](#头信息)
* [Python 打包用户指南](#python-打包用户指南)
    * [教程](#教程)
        * [安装包](#安装包)
            * [Source Distributions vs Wheels](#source-distributions-vs-wheels)
            * [Requirements files](#requirements-files)
    * [指南](#指南)
        * [打包二进制扩展](#打包二进制扩展)
* [Python 有什么新变化？](#python-有什么新变化)
    * [What's New in Python 2.3](#whats-new-in-python-23)
    * [What's New In Python 3.0](#whats-new-in-python-30)
        * [常见绊脚石](#常见绊脚石)
            * [文本 Vs. 数据代替 Unicode Vs. 8-bit](#文本-vs-数据代替-unicode-vs-8-bit)
        * [库变化](#库变化)
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
    * [numpy](#numpy)
    * [openpyxl](#openpyxl)
    * [pandas](#pandas)
        * [索引与选择数据](#索引与选择数据)
    * [pip](#pip)
    * [PyMongo](#pymongo)
    * [PyMySQL](#pymysql)
    * [pyquery](#pyquery)
    * [pyspider](#pyspider)
    * [redis-py](#redis-py)
    * [Requests](#requests)
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
* [Python Snippets](#python-snippets)
    * [proxy.py](#proxypy)
* [Python2](#python2)
    * [Python 2 语言参考](#python-2-语言参考)
        * [3. 数据模型](#3-数据模型-1)
            * [3.4. 特殊方法名](#34-特殊方法名)
                * [3.4.1. 基本自定义](#341-基本自定义)
* [数据库](#数据库)
	* [MongoDB](#mongodb)
		* [文档](#文档)
		* [mongo Shell](#mongo-shell)
			* [配置mongo Shell](#配置mongo-shell)
        * [mongo Shell方法](#mongo-shell方法)
            * [集合方法](#集合方法)
        * [mongoexport](#mongoexport)
        * [Operators](#operators)    
            * [Query and Projection Operators](#query-and-projection-operators)
            * [Update Operators](#update-operators)
                * [字段更新运算符](#字段更新运算符)
	* [MySQL](#mysql)
		* [MySQL Workbench](#mysql-workbench)
        * [LOAD DATA INFILE语法](#load-data-infile语法)
		* [UPDATE语法](#update语法)
        * [比较函数与运算符](#比较函数与运算符)
        * [4.2.5 在命令行中使用选项](#425-在命令行中使用选项)
            * [4.5.1.1 mysql 客户端选项](#4511-mysql-客户端选项)
            * [4.5.1.2 mysql 客户端命令](#4512-mysql-客户端命令)
        * [4.5.4 mysqldump — 一个数据库备份程序](#454-mysqldump--一个数据库备份程序)
        * [11.1.2 日期和时间类型概述](#1112-日期和时间类型概述)
        * [11.3.2 CHAR 和 VARCHAR 类型](#1132-char-和-varchar-类型)
        * [11.3.5 为TIMESTAMP和DATETIME自动初始化和更新](#1135-为timestamp和datetime自动初始化和更新)
        * [12.5 字符串函数](#125-字符串函数)
        * [12.7 日期和时间函数](#127-日期和时间函数)
        * [13.1.9 ALTER TABLE语法](#1319-alter-table语法)
        * [13.2.6 INSERT语法](#1326-insert语法)
        * [13.2.10 SELECT语法](#13210-select语法)
            * [13.2.10.1 SELECT ... INTO语法](#132101-select--into语法)
* [Anaconda](#anaconda)
* [Android Studio](#android-studio)
* [Appium](#appium)
* [Charles](#charles)
* [ChromeDriver](#chromedriver)
* [GeckoDriver](#geckodriver)
* [PhantomJS](#phantomjs)
* [vim](#vim)
	* [vim插件](#vim插件)
		* [YouCompleteMe](#youcompleteme)

# 导航
Anaconda  
官方网站：[https://www.anaconda.com](https://www.anaconda.com)

Anaconda Distribution  
世界上最流行的 Python/R 数据科学平台

Apache  
[Apache软件基金会SVN仓库](http://svn.apache.org/repos/asf/)

Apache Hadoop  
[https://hadoop.apache.org](https://hadoop.apache.org)

Apache Hadoop 文档  
[http://hadoop.apache.org/docs/current/](http://hadoop.apache.org/docs/current/)

Apache Subversion  
[https://subversion.apache.org](https://subversion.apache.org)

Apache Tomcat  
[http://tomcat.apache.org](http://tomcat.apache.org)

DistroWatch  
[https://distrowatch.com](https://distrowatch.com)  
Linux发行版排名统计

Eclipse  
[https://www.eclipse.org](https://www.eclipse.org)  
开源的Java IDE

IANA  
[https://www.iana.org](https://www.iana.org)  
IANA（Internet Assigned Numbers Authority）是[ICANN](https://www.icann.org)的一个职能机构，一个非营利性的美国私有公司，审核全球IP地址的分配，自治系统（AS）号的分配，DNS根域的管理，媒体类型，和其它互联网协议相关的符号及互联网地址。

IANA分配的端口号列表  
[服务名和传输协议端口号注册表](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml) 

ICANN  
[https://www.icann.org](https://www.icann.org)

Java Decompiler  
[http://jd.benow.ca](http://jd.benow.ca)  
Java反编译器

Markdonw在线编辑器  
[https://jbt.github.io/markdown-editor/](https://jbt.github.io/markdown-editor/)

MongoDB文档  
[https://docs.mongodb.com](https://docs.mongodb.com)

MongoDB Reference  
[https://docs.mongodb.com/manual/reference/](https://docs.mongodb.com/manual/reference/)

MySQL Workbench  
[https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)  

Nginx  
Nginx官网：[https://nginx.org](https://nginx.org)  

Node.js  
Node.js官网：[http://nodejs.org/](http://nodejs.org/)

Node.js 包索引网站：[https://www.npmjs.com](https://www.npmjs.com)

Visual C++ Redistributable for Visual Studio 2015是安装MySQL Workbench的前置条件。  
[Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-CN/download/details.aspx?id=48145)

Oracle数据库文档  
[https://docs.oracle.com/en/database/oracle/oracle-database/index.html](https://docs.oracle.com/en/database/oracle/oracle-database/index.html)

PyMongo  
[http://api.mongodb.com/python/current/index.html](http://api.mongodb.com/python/current/index.html)

Ruby  
官网：[https://www.ruby-lang.org/zh_cn/](https://www.ruby-lang.org/zh_cn/)  
发明者：松本行弘（Yukihiro “Matz” Matsumoto）

Ruby 经常位于全球编程语言成长和流行度指数的前十名（比如[TIOBE](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html)）。造成 Ruby 如此快速成长的原因很大程度上是因为使用 Ruby 编写的 Web 框架 [Ruby on Rails](http://rubyonrails.org/) 非常受欢迎。

**Ruby MRI**  
以 Ruby 的创造者 Yukihiro Matsumoto ("Matz") 命名的 **Matz's Ruby Interpreter** 或 **Ruby MRI** (也称 **CRuby**) 是 Ruby 程序设计语言的参考实现。直到2011年 Ruby 语言的技术规范，MRI 实现被认为是事实上的参考，特别是因为试图创建一个独立的技术规范 ([RubySpec](https://en.wikipedia.org/wiki/RubySpec)) 失败后。从 Ruby 1.9，及后续的 Ruby 2.x 及以上，官方的 Ruby 解释器已经变为 [YARV](https://en.wikipedia.org/wiki/YARV) ("Yet Another Ruby VM")。

**Ruby 的其他实现**  
作为一门语言，Ruby 有不同的实现。这里讨论的是推荐的实现，社区通常称之为 **MRI**（“Matz’s Ruby Interpreter”）或 **CRuby**（因为是用 C 语言写的）。不过，还有一些别的实现。其他实现通常在特定的场合中有用，集成了其他语言或环境，或者有 MRI 不具有的特性。

下面列出一些其他实现：

* [JRuby](http://jruby.org/) 是基于 JVM（Java Virtual Machine）的 Ruby 实现，利用了 JVM 中优秀的 JIT 编译器、垃圾回收程序、并发线程、工具生态系统和大量的库。
* [Rubinius](http://rubini.us/) 是用“Ruby 编写的 Ruby”。构建于 LLVM 之上，Rubinius 跑在一个很灵活的虚拟机上，别的语言也可以构建于这个虚拟机上。
* [MacRuby](http://www.macruby.org/) 是一个与苹果 Mac OS X 上 Cocoa 库紧密集成的实现，可以让你轻易地写出桌面应用程序。
* [mruby](http://www.mruby.org/) 是 Ruby 语言的轻量级实现，可以链接或嵌入到程序之中。mruby 由 Ruby 的创建者松本行弘（Matz）领导开发。
* [IronRuby](http://www.ironruby.net/) 是一个“与 .NET 框架紧密集成”的实现。
* [MagLev](http://maglev.github.io/) 是“一个快速、稳定的 Ruby 实现，支持集成对象持久化和分布式共享缓存”。
* [Cardinal](https://github.com/parrot/cardinal) 是一个“为 [Parrot](http://parrot.org/) 虚拟机 （Perl 6）编写的 Ruby 编译器”。

StackEdit  
[https://stackedit.io/app](https://stackedit.io/app)  
支持GFM的Markdown在线编辑器

w3schools.com  
[https://www.w3schools.com](https://www.w3schools.com)  
世界上最大的WEB开发者站点

w3school 在线教程  
[http://www.w3school.com.cn](http://www.w3school.com.cn)  
中文版的w3school

# Windows  
计算机系统硬件类  
[https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/computer-system-hardware-classes](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/computer-system-hardware-classes)

## PowerShell
### PowerShell 模块
#### Microsoft.PowerShell.Core
The Core module contains cmdlets and providers that manage the basic features of PowerShell.

[Microsoft.PowerShell.Core](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/?view=powershell-6)

#### Microsoft.PowerShell.Utility
这个模块包含用于管理 PowerShell 基本特性的命令。

[Microsoft.PowerShell.Utility](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/?view=powershell-6)

Wireshark  
[https://www.wireshark.org](https://www.wireshark.org)  
简介：开源的包分析器。也被称为网络协议分析器或抓包工具。

2018年12月中华人民共和国县以上行政区划代码  
[http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/20181201301111.html](http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/20181201301111.html)

清华大学开源软件镜像站  
[https://mirrors.tuna.tsinghua.edu.cn](https://mirrors.tuna.tsinghua.edu.cn)

时区列表  
[tz数据库时区列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

# Markdown
要在Markdown中显示`<`和`>`，必须使用使用转义字符`&lt;`和`&gt;`。

Markdown中的多个空行会被当做一个空行来处理。如果要显示多个空行，需要使用 `<br />` 标签。

如果目录中的标题同名，则在第二个同名标题的末尾加上 `-1`，在第三个同名标题的末尾加上 `-2`，如：  

* [测试标题](#测试标题)
* [测试标题](#测试标题-1)
* [测试标题](#测试标题-2)

##### 测试标题  
这是第一个同名测试标题

##### 测试标题  
这是第二个同名测试标题

##### 测试标题  
这是第三个同名测试标题

# HTML
HTML `<ul>` 标签  

```
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

无序HTML列表：

<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

# Python
## Python 3 标准库
Python 3 版本：3.6.4——3.8

[Python 语言参考](https://docs.python.org/3/reference/index.html#reference-index)描述的是 Python 语言精确的语法及语义，这个库参考手册描述的是和 Python 一起发布的标准库。它也描述一些通常包含在 Python 发行版中的可选组件。

Python 标准库包含提供访问系统功能如文件 I/O 的内置模块（C 语言所写），这些功能是 Python 程序员原本无法访问的，也包含用 Python 写的为日常编程中出现的许多问题提供标准解决方案的模块。这些模块中的一些的设计通过将特定平台的 APIs 抽象为平台无关的 APIs 明显地鼓励及增强了 Python 程序的可移植性。 

### 内置函数
Python解释器内置了许多总是可用的函数和类型。在这里以字母顺序列出它们。

|          |            |Built-in Functions|          |          |
|----------|------------|------------------|----------|----------|
|all()     |            |                  |          |          |
|          |            |                  |object()  |          |
|          |enumerate() |                  |          |          |
|          |            |                  |open()    |          |
|          |            |issubclass()      |pow()     |super()   |
|          |            |                  |print()   |          |
|          |            |                  |range()   |          |
|          |getattr()   |                  |          |          |
|complex() |            |                  |          |          |

**all**(*iterable*)  
如果 *iterable* 的所有元素都为真则返回`True` (或者如果iterable为空)。相当于：

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

用法举例
```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = [1, 2, None]
>>> print(all(a))
True
>>> print(all(b))
True
>>> print(all(c))
False
```

*class* **complex([**_real_**[**, _imag_**]])**  
返回值为 *real* + _imag_\*1j 的复数，或将字符串或数字转换为复数。如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。如果省略了 *imag*，则默认值为零，构造函数会像 [int](https://docs.python.org/zh-cn/3/library/functions.html#int) 和 [float](https://docs.python.org/zh-cn/3/library/functions.html#float) 一样进行数值转换。如果两个实参都省略，则返回 `0j`。

对于一个普通 Python 对象 `x`，`complex(x)` 会委托给 `x.__complex__()`。 如果 `__complex__()` 未定义则将回退至 `__float__()`。 如果 `__float__()` 未定义则将回退至 [\_\_index\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

**注解:** 当从字符串转换时，字符串在 `+` 或 `-` 的周围必须不能有空格。例如 `complex('1+2j')` 是合法的，但 `complex('1 + 2j')` 会触发 [ValueError](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。

[数字类型 --- int, float, complex](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric) 描述了复数类型。

*在 3.6 版更改:* 您可以使用下划线将代码文字中的数字进行分组。

*在 3.8 版更改:* 如果 [\_\_complex\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__complex__) 和 [\_\_float\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__float__) 未定义则回退至 [\_\_index\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

**enumerate**(*iterable, start=0*)  
返回一个枚举对象。*iterable* 必须是一个序列，或 [迭代器](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)，或其他支持迭代的对象。 [enumerate()](https://docs.python.org/zh-cn/3/library/functions.html?highlight=enumerate#enumerate) 返回的迭代器的 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法返回一个元组，里面包含一个计数值（从 *start* 开始，默认为 0）和通过迭代 *iterable* 获得的值。

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
>>>
```

等价于：

```python
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

**getattr**(*object, name*__[__*, default*__]__)  
返回 *object* 的 *name* 属性的值。*name* 必须是一个字符串。如果这个字符串是这个对象的一个属性的名称，则结果为那个属性的值。例如，`getattr(x, 'foobar')` 等同于 `x.foobar`。如果名称属性不存在，则返回 *default* 如果有提供的话，否则抛出 [AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError)。

**issubclass**(*class, classinfo*)  
如果 *class* 是 *classinfo* 的子类（直接、间接或 [虚拟](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class) 的），则返回 true。*classinfo* 可以是类对象的元组，此时 *classinfo* 中的每个元素都会被检查。其他情况，会触发 [TypeError](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。

```python
>>> import io
>>> issubclass(io.FileIO, io.RawIOBase)
True
>>> 
```

*class* **object**  
返回一个没有特征的新对象。[object](https://docs.python.org/zh-cn/3/library/functions.html#object) 是所有类的基类。它具有所有 Python 类实例的通用方法。这个函数不接受任何实参。

**注解:** 由于 [object](https://docs.python.org/zh-cn/3/library/functions.html#object) 没有 [\_\_dict\_\_](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__)，因此无法将任意属性赋给 [object](https://docs.python.org/zh-cn/3/library/functions.html#object) 的实例。  
<br />  

**open**(*file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None*)  
打开 *file* 并返回一个对应的[文件对象](https://docs.python.org/3.6/glossary.html#term-file-object)。如果文件不能被打开，则抛出一个[OSError](https://docs.python.org/3.6/library/exceptions.html#OSError)异常。

*file* is a [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object) giving the pathname (绝对的或者相对于当前工作目录的) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless *closefd* is set to `False`.)

*mode* 是一个可选字符串，用于指定打开文件的模式。默认值为`'r'`，意味着在文本模式下以只读方式打开。其它常用值是`'w’`意味着写(如果文件已经存在则截断文件), `'x'`意味着专门创建（exclusive creation），而`'a'`意味着附加 (在一些Unix系统，意味着所有写操作被附加到文件末尾而不考虑当前搜索位置). 在文本模式下，如果 *encoding* 没有指定，使用的编码将依赖于平台：`locale.getpreferredencoding(False)` 将被调用以得到当前区域编码（locale encoding）。(读写裸字节 (raw bytes)使用binary模式且不要指定 *encoding*.) 可用的模式是：

|Character |Meaning                                        |
|----------|-----------------------------------------------|
|`'r'`     |只读模式打开（默认）                              |
|`'w'`     |open for writing, 首先截断文件                   |
|`'x'`     |open for exclusive creation, 如果文件已存在则失败 |
|`'a'`     |open for writing, 如果文件存在则附加到文件末尾     |
|`'b'`     |二进制模式                                      |
|`'t'`     |文本模式（默认）                                 |
|`'+'`     |open a disk file for updating (读和写)          |
|`'U'`     |[通用新行](https://docs.python.org/3.6/glossary.html#term-universal-newlines) 模式（已弃用）        |

默认模式是 `'r'` (打开只读文本, 同义词 `'rt'`). 对于二进制读写访问，模式 `'w+b'` 打开并将文件截断为0字节。`'r+b'` 打开文件时不截断。

就像在[概述](https://docs.python.org/3.6/library/io.html#io-overview)中提到的，Python区分二进制和文本I/O。以二进制模式（*mode*参数包含`'b'`）打开的文件返回内容作为[bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes)对象无需任何解码。在文本模式(默认, 或者当 *mode* 参数中包含 `'t'` ), 文件内容作为[str](https://docs.python.org/3.6/library/stdtypes.html#str)被返回，字节首先被一个平台相关的编码或者指定的*编码*（如果指定了*encoding*参数）解码。

**注意：** Python不依赖于底层操作系统的文本文件的概念；所有的处理都是由Python自己完成，因此是跨平台的。

*buffering*是一个可选整型数用于设置缓冲区策略。传递0关闭缓冲区(仅在二进制模式下允许), 1 选择行缓冲区 (仅在文本模式下可用), 
大于1的整型数表示一个固定大小的块缓冲区的大小，以字节为单位。当没有给出*buffering*参数时, 默认的缓冲区策略工作如下：  
* 二进制文件被缓冲在固定大小的块中；the size of the buffer is chosen using a heuristic trying to determine the underlying device's "block size" and falling back on [io.DEFAULT_BUFFER_SIZE](https://docs.python.org/3.6/library/io.html#io.DEFAULT_BUFFER_SIZE). 在许多系统中，缓冲区通常是4096或者8192字节长。  
* "Interactive" 文本文件([isatty()](https://docs.python.org/3.6/library/io.html#io.IOBase.isatty) 返回`True`的文件) 使用行缓冲区。其它文本文件使用上面描述的二进制文件的缓冲策略。

*encoding* 是用来解码或者编码文件的编码的名字。这个应该仅用于文本模式。默认编码依赖于平台(不管 [locale.getpreferredencoding()](https://docs.python.org/3.6/library/locale.html#locale.getpreferredencoding) 返回什么), 但任何Python支持的[文本编码](https://docs.python.org/3.6/glossary.html#term-text-encoding)都可以被使用。支持的编码列表请看[codecs](https://docs.python.org/3.6/library/codecs.html#module-codecs)模块。

*errors* 是一个可选字符串，用于指定如何处理编码及解码错误——这不能被用于二进制模式。许多标准错误处理程序是可用的 (listed under [Error Handlers](https://docs.python.org/3.6/library/codecs.html#error-handlers)), 但任何已经通过[codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error)注册的错误处理名字也是有效的。标准名字包括：  
* `'strict'` 如果有编码错误则抛出一个[ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)异常。默认值 `None` 有相同的效果。
* `'ignore'` 忽略错误。注意，忽略编码错误可能导致数据丢失。
* `'replace'` 导致一个替换标记(例如`'?'`)被插入到有畸形数据的地方。
* `'surrogateescape'` 将任何不正确的字节表示为Unicode私有使用区域范围（从 U+DC80 到 U+DCFF）内的代码点。当写数据且`surrogateescape`错误处理程序被使用时这些私有代码点将被转回为相同的字节。这在处理未知编码文件时很有用。
* `'xmlcharrefreplace'` 仅当向文件中写数据时支持。字符不被编码支持的时候被替换为适当的XML字符引用 `&#nnn;`.
* `'backslashreplace'` 通过Python的反斜杠转义序列替换畸形数据。
* `'namereplace'` (也是仅当写数据的时候支持) 用`\N{...}`转义序列替换不支持的字符。

*newline* 控制[通用新行](https://docs.python.org/3.6/glossary.html#term-universal-newlines)模式如何工作(它仅用于文本模式). 它可以是 `None`, `''`, `'\n'`, `'\r'`, 和 `'\r\n'`. 它的工作方式如下：  
* 当从流读取输入时，如果 *newline* 是 `None`，通用换行模式开启。输入中的行可以以 `'\n'`, `'\r'`, 或者 `'\r\n'` 结尾，且在返回给调用方以前这些被翻译成 `'\n'` 。如果 *newline* 是 `''`，通用换行模式开启，行尾结束符号返回给调用方的时候没有被翻译。如果 *newline* 是其它合法的值，输入行仅被给定的字符串终结，且返回给调用方的行尾结束符号没有被翻译。
* 当向流写入输出的时候，如果 *newline* 是 `None`，所有写入的 `'\n'` 字符都被翻译成系统默认的行分隔符，[os.linesep](#https://docs.python.org/3.6/library/os.html#os.linesep). 如果 *newline* 是 `''` 或者 `'\n'`, 则不翻译。如果 *newline* 是任何其它的合法值，所有写入的 `'\n'` 字符都被翻译为指定的字符串。

如果 *closefd* 是 `False` 且给定的是一个文件描述符而不是一个文件名，则当文件被关闭的时候底层的文件描述符将保持打开状态。如果给定的是一个文件名则 *closefd* 必须是 `True` (默认值) ，否则将抛出一个错误。

A custom opener can be used by passing a callable as *opener*. The underlying file descriptor for the file object is then obtained by calling *opener* with (*file, flags*). *opener* must return an open file descriptor (passing [os.open](https://docs.python.org/3.6/library/os.html#os.open) as *opener* results in functionality similar to passing `None`).

新创建的文件是[不可继承的](https://docs.python.org/3.6/library/os.html#fd-inheritance)。

下面的例子使用[os.open()](https://docs.python.org/3.6/library/os.html#os.open)函数的 [dir_fd](https://docs.python.org/3.6/library/os.html#dir-fd) 参数打开一个相对于给定目录的文件：

```python
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor
```

[open()](https://docs.python.org/3.6/library/functions.html#open)函数返回的[文件对象](https://docs.python.org/3.6/glossary.html#term-file-object)的类型依赖于模式。当[open()](https://docs.python.org/3.6/library/functions.html#open)以文本模式打开一个文件时(`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), 它返回一个 [io.TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase) 的子类(具体地是 [io.TextIOWrapper](https://docs.python.org/3.6/library/io.html#io.TextIOWrapper)). When used to open a file in a binary mode with buffering, 返回类是[io.BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase)的一个子类. The exact class varies: in read binary mode, 它返回一个[io.BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader)类; in write binary and append binary modes, 它返回一个[io.BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter)类, and in read/write mode, 它返回一个[io.BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom)类. 当buffering关闭时，the raw stream, 返回一个[io.RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase)的子类[io.FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO)。

### 文本模式
```python
>>> with open('test.txt', 'r') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'rt') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'wt') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'a') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'at') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'r+') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'r+t') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w+') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w+t') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> import io
>>> issubclass(io.TextIOWrapper, io.TextIOBase)
True
```

### 开启buffering的二进制模式
```python
>>> with open('test.txt', 'rb') as f:
...     print(type(f))
...
<class '_io.BufferedReader'>
>>> with open('test.txt', 'wb') as f:
...     print(type(f))
...
<class '_io.BufferedWriter'>
>>> with open('test.txt', 'ab') as f:
...     print(type(f))
...
<class '_io.BufferedWriter'>
>>> with open('test.txt', 'r+b') as f:
...     print(type(f))
...
<class '_io.BufferedRandom'>
>>> with open('test.txt', 'w+b') as f:
...     print(type(f))
...
<class '_io.BufferedRandom'>
>>> import io
>>> issubclass(io.BufferedReader, io.BufferedIOBase)
True
>>> issubclass(io.BufferedWriter, io.BufferedIOBase)
True
>>> issubclass(io.BufferedRandom, io.BufferedIOBase)
True
```

### 关闭buffering的二进制模式
```python
>>> with open('test.txt', 'rb', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'wb', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'ab', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'r+b', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'w+b', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> import io
>>> issubclass(io.FileIO, io.RawIOBase)
True
```

也看下文件处理模块，例如，[fileinput](https://docs.python.org/3.6/library/fileinput.html#module-fileinput), [io](https://docs.python.org/3.6/library/io.html#module-io) (where [open()](https://docs.python.org/3.6/library/functions.html#open) is declared), [os](https://docs.python.org/3.6/library/os.html#module-os), [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path), [tempfile](https://docs.python.org/3.6/library/tempfile.html#module-tempfile), and [shutil](https://docs.python.org/3.6/library/shutil.html#module-shutil).

*在版本3.3中发生变化：*  
* 增加了*opener*参量（parameter）.
* 增加了 `'x'` 模式。
* [IOError](https://docs.python.org/3.6/library/exceptions.html#IOError) used to be raised, it is now an alias of [OSError]().
* 如果以exclusive creation mode (`'x’`) 打开的文件已经存在，则抛出 [FileExistsError](https://docs.python.org/3.6/library/exceptions.html#FileExistsError).

*在版本3.4中发生变化：*  
* The file is now non-inheritable.

`'U'` 模式 *从版本3.4开始弃用，将在版本4.0中被移除*。

*在版本3.5中发生变化：*  
* 如果系统调用被终止且信号处理程序没有抛出异常，现在函数将重试系统调用而不是抛出一个[InterruptedError](https://docs.python.org/3.6/library/exceptions.html#InterruptedError)异常 (原理请看 [PEP 475](https://www.python.org/dev/peps/pep-0475)).
* 新增 `'namereplace'` 错误处理程序。

*在版本3.6中发生变化：*  
* 增加支持：接受实现了 [os.PathLike](https://docs.python.org/3.6/library/os.html#os.PathLike) 的对象。
* 在 Windows平台, opening a console buffer may return a subclass of [io.RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) other than [io.FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO).  
<br />  

**pow**(*x*, *y*[, *z*])  
返回 *x* 的 *y* 次方；如果 *z* 出现，则返回 *x* 的 *y* 次方再以 *z* 取模(比`pow(x, y) % z`的计算效率更高).两个参数的形式 `pow(x, y)` 等同于使用幂运算: `x**y`。

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. 对于 [整型数](https://docs.python.org/3.6/library/functions.html#int) 操作数，结果与操作数的类型相同 (强制之后) 除非第二个参数是负的；在那种情况下，所有参数被转换成浮点数并返回一个浮点数结果。例如，`10**2` 返回 `100`，但 `10**-2` 返回 `0.01`。如果第二个参数是负的，第三个参数必须被省略。如果 *z* 出现，*x* 和 *y* 必须是整数类型，且 *y* 必须是非负的。

**根据一段时间的收益，计算复合年化收益**  
计算8年翻5倍的复合年化收益，即5开8次方根，亦即5的1/8次幂

```python
>>> pow(5, 1/8) - 1
0.22284454499385187
>>>
```

**print**(_*objects, sep=' ', end='\n', file=sys.stdout, flush=False_)  
打印 *objects* 到文本流 *file*, separated by *sep* and followed by *end*. 如果出现*sep*, *end*, *file* 和 *flush*, 则必须被作为关键字参数给出。  

所有非关键字参数被转换成字符串就像 [str()](https://docs.python.org/3.6/library/stdtypes.html#str) 做的那样并写入到流，separated by *sep* and followed by *end*。*sep* 和 *end* 都必须是字符串；它们也可以是 `None`，意味着使用默认值（*sep* 的默认值为一个空格，*end* 的默认值为一个换行符）。如果没有给定 *objects*， [print()](https://docs.python.org/3.6/library/functions.html#print) 将仅写入 *end*。  

The *file* argument must be an object with a `write(string)` method; if it is not present or `None`, [sys.stdout](https://docs.python.org/3.6/library/sys.html#sys.stdout) will be used. Since printed arguments are converted to text strings, [print()](https://docs.python.org/3.6/library/functions.html#print) cannot be used with binary mode file objects. For these, use `file.write(...)` instead.

输出是否缓冲通常由 *file* 决定，但如果 *flush* 关键字参数是 true, 则流被强制 flushed.

_在版本3.3中发生变化：_ 增加了 *flush* 关键字参数。

将 print 函数的输出信息写入到 p.log 文件中：  

```python
>>> with open('p.log', 'a') as f:
...     print('a 代表附加模式', file=f)
...
>>>
```

**range**(*stop*)  
**range**(*start, stop*[*, step*])  
根据 [Ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) 和 [序列类型 — 列表, 元组, range](https://docs.python.org/3/library/stdtypes.html#typesseq) 中的文档，[range](https://docs.python.org/3/library/stdtypes.html#range) 实际上是一个不可变的序列类型，而不是一个函数。

```python
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> 
```

```python
>>> for i in range(5, 0, -1):
...     print(i)
... 
5
4
3
2
1
>>> 
```

**super**([*type*__[__*, object-or-type*__]]__)  
*super* 有两种典型的用法。在一个单继承的类层次结构中，*super* 可以被用来引用父类而无需明确地指出它们，从而使代码更易于维护。这种用法与其它程序设计语言中 *super* 的用法十分相似。

```python
>>> class A:
...     def __init__(self):
...         print("Dunder init func in class A.")
...
>>> class B(A):
...     def __init__(self):
...         print("Dunder init func in class B.")
...
>>> b = B()
Dunder init func in class B.
>>> class B(A):
...     def __init__(self):
...         super().__init__()
...         print("Dunder init func in class B.")
...
>>> b = B()
Dunder init func in class A.
Dunder init func in class B.
>>> 
```

## 内置类型
### 数值类型 — int, float, complex
存在三种不同的数字类型: *整数*, *浮点数* 和 *复数*。 此外，布尔值属于整数的子类型。 整数具有无限的精度。

所有数字类型（复数除外）都支持下列运算（有关运算优先级，请参阅：[运算符优先级](https://docs.python.org/zh-cn/3/reference/expressions.html#operator-summary)）:

运算        |结果            |注释  |完整文档  
------------|---------------|------|-------  
`pow(x, y)` |*x* 的 *y* 次幂 |(5)  |[pow()](https://docs.python.org/zh-cn/3/library/functions.html#pow)  
`x ** y`    |*x* 的 *y* 次幂 |(5)  |    

注释：

5. Python 将 `pow(0, 0)` 和 `0 ** 0` 定义为 `1`，这是编程语言的普遍做法。

##### 整型数类型的按位运算
这个表格列出的按位运算按优先级升序排列：

Operation  |Result          |Notes
-----------|----------------|-----
`x ^ y`    |x和y的按位异或   |(4)

```python
>>> 0 ^ 1
1
>>> 0 ^ 0
0
>>> 1 ^ 1
0
>>>
```

### 集合类型 --- set, frozenset
*set* 对象是由具有唯一性的 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) 对象所组成的无序多项集。 常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算，例如交集、并集、差集与对称差集等等。 （关于其他容器对象请参看 [dict](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#dict), [list](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#list) 与 [tuple](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#tuple) 等内置类，以及 [collections](https://docs.python.org/zh-cn/3/library/collections.html#module-collections) 模块。）

与其他多项集一样，集合也支持 `x in set`, `len(set)` 和 `for x in set`。 作为一种无序的多项集，集合并不记录元素位置或插入顺序。 相应地，集合不支持索引、切片或其他序列类的操作。

目前有两种内置集合类型，[set](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#set) 和 [frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#frozenset)。 [set](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#set) 类型是可变的 --- 其内容可以使用 add() 和 remove() 这样的方法来改变。 由于是可变类型，它没有哈希值，且不能被用作字典的键或其他集合的元素。 [frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#frozenset) 类型是不可变并且为 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) --- 其内容在被创建后不能再改变；因此它可以被用作字典的键或其他集合的元素。

除了可以使用 [set](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#set) 构造器，非空的 set (不是 frozenset) 还可以通过将以逗号分隔的元素列表包含于花括号之内来创建，例如: `{'jack', 'sjoerd'}`。

两个类的构造器具有相同的作用方式：

*class* **set**([*iterable*])  
*class* **frozenset**([*iterable*])  
返回一个新的 set 或 frozenset 对象，其元素来自于 *iterable*。 集合的元素必须为 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable)。 要表示由集合对象构成的集合，所有的内层集合必须为 [frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#frozenset) 对象。 如果未指定 *iterable*，则将返回一个新的空集合。

[set](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#set) 和 [frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=set#frozenset) 的实例提供以下操作：

**len(s)**  
返回集合 *s* 中的元素数量（即 *s* 的基数）。

**x in s**  
检测 *x* 是否为 *s* 中的成员。

**x not in s**  
检测 *x* 是否非 *s* 中的成员。

**union**(_\*others_)  
**set | other | ...**  
返回一个新集合，其中包含来自原集合以及 others 指定的所有集合中的元素。

**intersection**(_\*others_)  
**set & other & ...**  
返回一个新集合，其中包含原集合以及 others 指定的所有集合中共有的元素。

**difference**(_\*others_)  
**set - other - ...**  
返回一个新集合，其中包含原集合中在 others 指定的其他集合中不存在的元素。

```python
>>> s1 = {1, 2, 3, 4}
>>> s2 = {3, 4, 5, 6}
>>> s1 - s2
{1, 2}
>>>
```

**symmetric_difference**(_other_)  
**set ^ other**  
返回一个新集合，其中的元素或属于原集合或属于 *other* 指定的其他集合，但不能同时属于两者。

## 文本处理服务
这章描述的模块提供了广泛的字符串操作运算和其它的文本处理服务。

### string — 通用字符串操作
**源代码：** [Lib/string.py](https://github.com/python/cpython/tree/3.7/Lib/string.py)

**另请参阅：** [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#textseq)

[字符串方法](https://docs.python.org/3/library/stdtypes.html#string-methods)

#### 格式化字符串语法
[str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) 方法和 [Formatter](https://docs.python.org/3/library/string.html#string.Formatter) 类共享相同的格式化字符串语法 (尽管在 [Formatter](https://docs.python.org/3/library/string.html#string.Formatter) 的情况下，子类可以定义它们自己的格式化字符串语法)。The syntax is related to that of [formatted string literals](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings), 但有不同。

*在版本3.1中发生变化：* [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) 的位置参数说明符可以被省略，所以 `'{} {}'.format(a, b)` 相当于 `'{0} {1}'.format(a, b)`。

*在版本3.4中发送变化：* [Formatter](https://docs.python.org/3/library/string.html#string.Formatter) 位置参数说明符可以被省略。

一些简单的格式化字符串例子：

```python
"First, thou shalt count to {0}"  # 引用第一个位置参数
"Bring me a {}"                   # 含蓄地引用第一个位置参数
"From {} to {}"                   # 等同于 "From {0} to {1}"
```

### re — 正则表达式操作
**源代码：** [Lib/re.py](https://github.com/python/cpython/tree/3.8/Lib/re.py)

这个模块提供了与 Perl 语言类似的正则表达式匹配操作。

被搜索的模式和字符串可以都是 Unicode 字符串 ([str](https://docs.python.org/3/library/stdtypes.html#str)) 也可以都是 8-bit 字符串 ([bytes](https://docs.python.org/3/library/stdtypes.html#bytes))。然而，Unicode 字符串和 8-bit 字符串不能被混用：即，你不能用一个字节模式去匹配一个 Unicode 字符串或者反之亦然；类似地，当请求一个替换时，替换字符串必须和模式及搜索字符串是相同的类型。

正则表达式使用反斜杠字符 (`'\'`) 来表示特殊形式或是允许在使用特殊字符时不引发它们的特殊含义。 这会与 Python 的字符串字面值中对相同字符出于相同目的的用法产生冲突；例如，要匹配一个反斜杠字面值，用户可能必须写成 `'\\\\'` 来作为模式字符串，因为正则表达式必须为 `\\`，而每个反斜杠在普通 Python 字符串字面值中又必须表示为 `\\`。 而且还要注意，在 Python 的字符串字面值中使用的反斜杠如果有任何无效的转义序列，现在将会产生 [DeprecationWarning](https://docs.python.org/zh-cn/3/library/exceptions.html#DeprecationWarning) 并将在未来改为 [SyntaxError](https://docs.python.org/zh-cn/3/library/exceptions.html#SyntaxError)。 此行为即使对于正则表达式来说有效的转义字符同样会发生。

解决办法是对于正则表达式模式使用 Python 的原始字符串表示法；在带有 `'r'` 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 因此 `r"\n"` 表示包含 `'\'` 和 `'n'` 两个字符的字符串，而 `"\n"` 则表示只包含一个换行符的字符串。 模式在 Python 代码中通常都会使用这种原始字符串表示法来表示。

绝大部分正则表达式操作都提供为模块函数和方法，在 [编译正则表达式](https://docs.python.org/zh-cn/3/library/re.html#re-objects). 这些函数是一个捷径，不需要先编译一个正则对象，但是损失了一些优化参数。

**参见:** 第三方模块 [regex](https://pypi.org/project/regex/) , 提供了与标准库 [re](https://docs.python.org/zh-cn/3/library/re.html#module-re) 模块兼容的API接口, 同时还提供了额外的功能和更全面的Unicode支持。

#### 正则表达式语法
特殊字符是：

`.`  
(点.) 默认模式下，这匹配除了一个换行符以外的任何字符。如果指定了 [DOTALL](https://docs.python.org/3.6/library/re.html#re.DOTALL) 标志，这将匹配任何字符，包括一个换行符。

`+`  
对它前面的正则式匹配1到任意次重复。 `ab+` 会匹配 `'a'` 后面跟随1个以上到任意个 `'b'`，它不会匹配 `'a'`。

`?`  
Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. `ab?` 将匹配 `‘a’` 或者 `‘ab’`。

`*?`, `+?`, `??`  
限定符 `'*'`, `'+'`, 和 `'?'` 都是*贪婪的*；它们匹配尽可能多的文本。有时这种行为不是被期望的；如果正则表达式 `<.*>` 与 `'<a> b <c>'` 进行匹配，它将匹配整个字符串，而不仅仅是 `'<a>'`。在限定符的后面添加 `?` 使它执行非贪婪匹配或最小匹配的方式；匹配尽可能少的字符。使用正则表达式 `<.*?>` 将仅匹配 `'<a>'`。

```python
>>> import re
>>> re.findall(r'a(.*)a', 'abcbaabcaabca')
['bcbaabcaabc']
>>> re.findall(r'a(.*?)a', 'abcbaabcaabca')
['bcb', 'bc', 'bc']
>>>
```

`\`  
要么转义特殊字符 (允许你匹配字符像 `'*'`，`'?'`，等等)，要么表示一个特殊序列；特殊序列在下面讨论。

如果你没有使用原始字符串来表达模式，记住在字符串中Python也使用反斜杠作为一个转义序列；如果转义序列没有被Python解析器识别，则反斜杠和随后的字符将被包含在结果字符串中。然而，如果Python将识别结果序列，则反斜杠应该被重复两次。这是复杂且难懂的，所以强烈推荐你使用原始字符串，除了最简单的表达式。

`[]`  
用来表明一个字符集合。在集合中：

* 字符可以被单独列出，如 `[amk]` 将匹配 `'a'`, `'m'`, 或者 `'k'`。  
* 可以通过给定两个字符并用一个 `-` 分隔它们来表示字符范围，例如 `[a-z]` 将匹配任意的小写ASCII字母，`[0-5][0-9]` 将匹配从 `00` 到 `59` 的所有两位数，`[0-9A-Fa-f]` 将匹配任意十六进制数字。如果 `-` 被转义了(如 `[a\-z]`) 或者 如果它被放在第一个或最后一个字符(如 `[-a]` 或者 `[a-]`)，它将匹配一个文字 `'-'`。  
* 在集合中特殊字符将失去他们的特殊含义。如，`[(+*)]` 将匹配任意文字字符 `'('`, `'+'`, `'*'`, 或者 `')'`。  
* 在一个集合中字符类如 `\w` 或者 `\S` (在下面定义) 也被接受，虽然它们匹配的字符依赖于 [ASCII](https://docs.python.org/3/library/re.html#re.ASCII) 或者 [LOCALE](https://docs.python.org/3/library/re.html#re.LOCALE) 模式是否生效。  
* 不在一个范围内的字符可以通过补全集合来匹配。如果集合的第一个字符是 `'^'`，则所有不在集合中的字符将被匹配。例如，`[^5]` 将匹配除了 `5` 以外的任意字符，而 `[^^]` 将匹配除了 `^` 以外的所有字符。如果 `^` 不是集合中的第一个字符则它没有特殊含义。  
* 要在集合中匹配文字 `']'` ，可以在它前面放一个反斜杠，或者将它放在集合的开始位置。例如，`[()[\]{}]` 和 `[]()[{}]` 都将匹配一个括号。

* 像 [Unicode Technical Standard #18](https://unicode.org/reports/tr18/) 中对嵌套集合和集合操作的支持未来应该会被增加。这将改变语法，所以目前为了促进这个改变在两义情况（ambiguous cases）中将抛出一个 [FutureWarning](https://docs.python.org/3/library/exceptions.html#FutureWarning)。那包括以一个文字 `'['` 开头的集合或者包含文字字符序列 `'--'`, `'&&'`, `'~~'`, 和 `'||'` 的集合。为了避免警告请用一个反斜杠转义它们。

*在版本3.7中发送变化：* 如果一个字符集合包含在未来将会改变语义的结构成分则抛出 [FutureWarning](https://docs.python.org/3/library/exceptions.html#FutureWarning)。

`(...)`  
（组合），匹配括号内的任意正则表达式，并标识出组合的开始和结尾。匹配完成后，组合的内容可以被获取，并可以在之后用 `\number` 转义序列进行再次匹配，之后进行详细说明。要匹配字符 `'('` 或者 `')'`, 用 `\(` 或 `\)`, 或者把它们包含在字符集合里: `[(]`, `[)]`。

特殊序列由 `'\'` 和一个下面列出的字符构成。如果普通字符不是一个 ASCII 数字或一个 ASCII 字母，则结果是正则表达式将匹配第二个字符。例如，`\$` 匹配字符 `'$'`。

`\number`  
匹配相同数字的组的内容。组从 1 开始编号。例如，`(.+) \1` 匹配 `'the the'` 或 `'55 55'`，但是不匹配 `'thethe'` (注意组后面的空格)。这个特殊的序列只能用来匹配前 99 个组中的一个。如果 *number* 的第一个数字是 0，或者 `number` 是一个 3 位八进制数，它将不会被解释为一个组匹配，而是作为字符 `number` 的八进制值。在一个字符类 `'['` 和 `']'` 里面，所有数字被转义为字符。

```python
>>> import re
>>> strings = 'the the'
>>> result = re.search('(\w+) \1', strings)
>>> print(result)
None
>>> result = re.search(r'(\w+) \1', strings)
>>> print(result)
<re.Match object; span=(0, 7), match='the the'>
>>>
```

如果模式中包含 `\number` ，则模式必须使用 Python 原始字符串表示法，即在正则表达式模式前面加上 `r` 前缀。

`\s`  
For Unicode (str) patterns:  
匹配 Unicode 空白字符 (包括 `[ \t\n\r\f\v]`，及一些其它字符，例如在许多语言的排版规则中所要求的 non-breaking spaces)。如果 ASCII 标志被使用，则仅匹配 `[ \t\n\r\f\v]`。

For 8-bit (bytes) patterns:  
匹配 ASCII 字符集中被认为是空白的字符；这等同于 `[ \t\n\r\f\v]`。

`\w`  
For Unicode (str) patterns:  
匹配 Unicode 单词字符；这包括在任意语言中可以成为一个单词的一部分的大多数字符，也包括数字和下划线。如果 [ASCII](https://docs.python.org/3/library/re.html#re.ASCII) 标志被使用，则仅匹配 `[a-zA-Z0-9_]` (但标志影响整个正则表达式，所以在这种情况下使用一个明确的 `[a-zA-Z0-9_]` 可能是一个更好的选择)。

For 8-bit (bytes) patterns:  
匹配ASCII字符集中被认为是字母数字的字符；这相当于 `[a-zA-Z0-9_]`。如果 [LOCALE](https://docs.python.org/3/library/re.html#re.LOCALE) 标志被使用，则匹配当前区域设置中被认为是字母数字的字符及下划线。

`\W`  
匹配任意一个不是一个单词字符的字符。这是 `\w` 的反义词。如果 [ASCII](https://docs.python.org/3/library/re.html#re.ASCII) 标志被使用这将等同于 `[^a-zA-Z0-9_]`。如果 [LOCALE](https://docs.python.org/3/library/re.html#re.LOCALE) 标志被使用，则匹配当前区域中被认为是字母数字的字符及下划线。

#### 模块内容
这个模块定义了数个函数，常量和一个异常。一些函数是编译的正则表达式的全功能方法的简化版。大多数重大的应用总是使用编译后的形式。

*在版本3.6中发生变化：* 标志常量现在是 RegexFlag 的实例，RegexFlag 是 [enum.IntFlag](https://docs.python.org/3/library/enum.html#enum.IntFlag) 的一个子类。

re.**compile**(*pattern, flags=0*)  
将一个正则表达式模式编译进一个[正则表达式对象](https://docs.python.org/3/library/re.html#re-objects)，正则表达式对象可以使用它的 [match()](https://docs.python.org/3/library/re.html#re.Pattern.match)，[search()](https://docs.python.org/3/library/re.html#re.Pattern.search) 和其它方法来进行匹配，详情如下。

表达式的行为可以通过指定一个 *flags* 值来进行修改。标志值可以是下面任意一个变量，组合使用按位或(即 `|` 操作符)。

The sequence  

```python
prog = re.compile(pattern)
result = prog.match(string)
```

等同于

```python
result = re.match(pattern, string)
```

但当表达式在一个单一程序中将要被使用几次时，重复使用 [re.compile()](https://docs.python.org/3.6/library/re.html#re.compile) 及保存的结果正则表达式对象是更高效的。

**注意：** 传递给 [re.compile()](https://docs.python.org/3/library/re.html#re.compile) 及模块级别的匹配函数的最新的模式的编译版本被缓存了，所以每次仅使用几个（a few）正则表达式的程序不必担心编译正则表达式。

re.**I**  
re.**IGNORECASE**  
执行不区分大小写的匹配；表达式像 `[A-Z]` 将也匹配小写字母。Full Unicode matching (例如 `Ü` 匹配 `ü`) also works unless the [re.ASCII](https://docs.python.org/3/library/re.html#re.ASCII) flag is used to disable non-ASCII matches. 当前区域设置不会改变这个标志的效果除非 [re.LOCALE](https://docs.python.org/3/library/re.html#re.LOCALE) 标志也被使用。相当于行内标志 `(?i)`。

注意当 Unicode 模式 `[a-z]` 或者 `[A-Z]` 与 [IGNORECASE](https://docs.python.org/3/library/re.html#re.IGNORECASE) 标志组合使用时，它们将匹配52个 ASCII 字母及 4 个额外的非ASCII字母：`‘İ’` (U+0130, 大写拉丁字母I上面带一个点), `‘ı’` (U+0131, 小写拉丁字母i不带点), `‘ſ’` (U+017F, Latin small letter long s) 和 `‘K’` (U+212A, 开尔文符号)。如果 [ASCII](https://docs.python.org/3/library/re.html#re.ASCII) 标志被使用，则仅字母 `‘a’` 到 `‘z’` 和 `‘A’` 到 `‘Z’` 被匹配 (但标志影响整个正则表达式，所以在这种情况下使用一个明确的 `(?-i:[a-zA-Z])` 可能是一个更好的选择)。

re.**S**  
re.**DOTALL**  
让 `'.'` 特殊字符匹配任何字符，包括换行符；如果没有这个标记，`'.'` 就匹配 *除了* 换行符的其他任意字符。对应内联标记 `(?s)` 。

re.**search**(*pattern, string, flags=0*)  
扫描 *string* 查找第一个正则表达式 *pattern* 产生一个匹配的位置，并返回一个对应的[匹配对象](https://docs.python.org/3/library/re.html#match-objects)。如果字符串中没有位置匹配模式则返回 `None`；注意这不同于在字符串中的某点查找一个零长度的匹配。

re.**match**(*pattern, string, flags=0*)  
如果 *string* 的开始位置有0个或多个字符匹配正则表达式 *pattern*，则返回一个对应的[匹配对象](https://docs.python.org/3/library/re.html#match-objects)。如果字符串不匹配模式，则返回 `None`；注意，这不同于 zero-length match。

注意，即使在[多行](https://docs.python.org/3/library/re.html#re.MULTILINE)模式下，[re.match()](https://docs.python.org/3/library/re.html#re.match) 将仅匹配字符串的开始位置而不是每一行的开始位置。

如果你想在 *string* 的任意位置定位一个匹配，使用 [search()](https://docs.python.org/3/library/re.html#re.search) 替代 (另请参考 [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match))。

```python
>>> import re
>>> re.match('c', 'abcdef')   # No match
>>> re.search('c', 'abcdef')  # Match
<_sre.SRE_Match object; span=(2, 3), match='c'>
```

**匹配中文**    
[\u4e00-\u9fd5]虽然不是所有中文的Unicode代码点范围，但它几乎已经包含了所有常用的汉字的Unicode代码点。在Unicode标准版本10.0.0中包含汉字代码点的块共有9个，具体可以查询Unicode官网。Python 3.6.4支持的Unicode标准版本为9.0.0，[\u4e00-\u9fd5]是Unicode标准版本8.0的CJK Unified Ideographs块的代码点范围。

匹配一个或多个中文

```python
>>> import re
>>> s = 'Python is a programming language.'
>>> re.search(u'[\u4e00-\u9fd5]+', s)
>>> s = 'Python不是大蟒蛇。'
>>> re.search(u'[\u4e00-\u9fd5]+', s)
<_sre.SRE_Match object; span=(6, 11), match='不是大蟒蛇'>
```

re.**findall**(*pattern, string, flags=0*)  
返回 *string* 中所有非重叠的 *模式* 匹配，作为一个字符串列表。*string* 被从左到右搜索，匹配按被找到的顺序返回。If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. 空匹配被包含在结果中。

**注意：** 因为当前实现的限制一个空匹配后面的字符没有被包含在下一个匹配中，所以 `findall(r'^|\w+', 'two words')` 返回 `['', 'wo', 'words']` (注意丢失的 “t”)。这在Python 3.7中将发送变化。【Python 3.6】

*在版本 3.7 中发送变化：* 现在非空匹配可以从前一个空匹配后面开始。

Python 3.6

```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=8, releaselevel='final', serial=0)
>>> import re
>>> re.findall(r'^|\w+', 'two words')
['', 'wo', 'words']
>>> 
```

Python 3.7

```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)
>>> import re
>>> re.findall(r'^|\w+', 'two words')
['', 'two', 'words']
>>> 
```

匹配 sitemap 文件中的所有链接

```python
import re
import urllib.request


sitemap = urllib.request.urlopen('https://example.com/sitemap.xml').read()
links = re.findall('<loc>(.*?)</loc>', sitemap.decode())

```

re.**sub**(*pattern, repl, string, count=0, flags=0*)  
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in *string* by the replacement *repl*. 如果没有找到模式，返回未改变的 *string*。 *repl* 可以是一个字符串或者一个函数；如果它是一个字符串，它里面的任何反斜杠转义都将被处理。即， `\n` 被转换成一个单一的新行字符，`\r` 被转换成一个回车，等等。未知的 ASCII 字母转义被保留给将来使用并被当做错误来看。其它未知的转义例如 `\&` 被单独留下。反向引用，如 `\6`，被模式中的组 6 匹配的子串替换。例如：

```python
>>> import re
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'
>>> 
```

```python
>>> import re
>>> url = 'http://example.webscraping.com/places/default/view/Australia-1'
>>> re.sub('[^/0-9a-zA-Z\-. _]', '_', url)
'http_//example.webscraping.com/places/default/view/Australia-1'
>>>
```

模式可以是一个字符串或者一个[模式对象](https://docs.python.org/3/library/re.html#re-objects)。

可选参数 *count* 是发现的模式将被替换的最大数；*count* 必须是一个非负整数。如果忽略或者为 0 ，所有出现的模式都将被替换。 

re.**purge()**  
清除正则表达式缓存。

#### 正则表达式对象
编译的正则表达式对象支持下面的方法和属性：

Pattern.**search**__(__*string*__[__, *pos*__[__, *endpos*__]])__  
扫描 *string* 查找这个正则表达式产生一个匹配的第一个位置，并返回一个对应的[匹配对象](https://docs.python.org/3/library/re.html#match-objects)。如果字符串中没有位置匹配模式则返回 `None` ；注意这不同于在字符串中的某点查找一个零长匹配。

Pattern.**match**__(__*string*__[__, *pos*__[__, *endpos*__]])__  
如果 *string* 的*起始位置*（beginning）有零个或多个字符匹配这个正则表达式，则返回一个对应的[匹配对象](https://docs.python.org/3/library/re.html#match-objects)。如果字符串不匹配模式则返回 `None`；注意这不同于一个零长匹配。

```python
>>> import re
>>> pattern = re.compile("o")
>>> pattern.match("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
<re.Match object; span=(1, 2), match='o'>
>>>
```

#### 匹配对象
匹配对象总是有一个值为 `True` 的布尔值。因为当没有匹配时 [match()](https://docs.python.org/3/library/re.html#re.Pattern.match) 和 [search()](https://docs.python.org/3/library/re.html#re.Pattern.search) 返回 `None`，你可以用一个简单的 `if` 语句测试是否有一个匹配：

```python
match = re.search(pattern, string)
if match:
    process(match)
```

匹配对象支持下面的方法和属性：

Match.**group**(**[**_group1_, ...**]**)  
返回一个或多个匹配的子组。如果是一个单一的参数，则结果是一个单一的字符串；如果有多个参数，则结果是一个元组且每个元素对应一个参数。没有参数时，*group1* 默认为 0 (返回完整匹配)。如果某个 *groupN* 参数是 0，则对应的返回值是整个匹配的字符串；如果它是在范围 [1..99] 内，则它是对应的括号内的组匹配的字符串。如果一个组的数值是负数或者比模式中定义的组的数值大，则抛出一个 [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) 异常。如果一个包含于模式的一部分的组没有匹配，则对应的结果是 `None`。如果一个包含于模式的一部分的组匹配多次，则仅最后的匹配被返回。

```python
>>> import re
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')
>>>
```

如果正则表达式使用 `(?P<name>...)` 语法，*groupN* 参数也可以是通过组名标识组的字符串。如果一个字符串参数没有在模式中用作一个组名，则抛出一个 [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) 异常。

一个适当复杂的例子：

```python
>>> import re
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')
'Malcolm'
>>> m.group('last_name')
'Reynolds'
>>>
```

命名的组也可以通过它们的索引来引用：

```python
>>> m.group(1)
'Malcolm'
>>> m.group(2)
'Reynolds'
>>>
```

如果一个组匹配多次，仅最后一个匹配可以被访问：

```python
>>> m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
>>> m.group(0)
'a1b2c3'
>>> m.group(1)                        # Returns only the last match.
'c3'
>>>
```

Match.**\_\_getitem\_\_**__(__*g*__)__  
这与 `m.group(g)` 是相同的。这允许更容易地从一个匹配中访问一个单独的组：

```python
>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m[0]       # The entire match
'Isaac Newton'
>>> m[1]       # The first parenthesized subgroup.
'Isaac'
>>> m[2]       # The second parenthesized subgropu.
'Newton'
>>>
```

*版本 3.6 中新增。*

Match.**groups**(*default=None*)  
返回一个包含所有匹配的子组的元组，从 1 到模式中的所有组。*default* 参数用于不参与匹配的组；它默认为 `None`。

例如：

```python
>>> import re
>>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> m.groups()
('24', '1632')
>>>
```

如果我们使小数位及其后面的所有数成为可选，则不是所有组都可以参与匹配。这些组将默认为 `None` 除非指定 *default* 参数：

```python
>>> import re
>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')
>>> m.groups('1')   # Now, the second group defaults to '1'. 
('24', '1')
>>> m.groups('X')   # Now, the second group defaults to 'X'. 
('24', 'X')
>>>
```

Match.**start([**_group_**])**  
Match.**end([**_group_**])**  
返回 *group* 匹配的子串的起始索引和结束索引；*group* 默认为 0 (意为整个匹配的子串)。

注意如果 *group* 匹配一个空串，`m.start(group)` 将等于 `m.end(group)`。例如，在 `m = re.search('b(c?)', 'cba')` 之后，`m.start(0)` 是 1，`m.end(0)` 是 2，`m.start(1)` 和 `m.end(1)` 都是 2，而 `m.start(2)` 抛出一个 [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) 异常。

```python
>>> import re
>>> m = re.search('b(c?)', 'cba')
>>> m
<re.Match object; span=(1, 2), match='b'>
>>> m.start(0)
1
>>> m.end(0)
2
>>> m.group(1)  # Group 1 match a null string.
''
>>> m.start(1)
2
>>> m.end(1)
2
>>>
```

一个将从邮件地址中删除 *remove_this* 的例子：

```python
>>> import re
>>> email = "tony@tiremove_thisger.net"
>>> m = re.search("remove_this", email)
>>> m
<re.Match object; span=(7, 18), match='remove_this'>
>>> m.start()
7
>>> m.end()
18
>>> email[:m.start()] + email[m.end():]
'tony@tiger.net'
>>>
```

Match.**span([**_group_**])**  
对于一个匹配 *m* ， 返回一个二元组 `(m.start(group), m.end(group))` 。 注意如果 `group` 没有在这个匹配中，就返回 `(-1, -1)` 。*group* 默认为0，就是整个匹配。

#### 正则表达式例子
##### search() vs. match()
Python 提供了两种不同的基于正则表达式的简单操作： [re.match()](https://docs.python.org/3/library/re.html#re.match) 仅在字符串的起始位置检查一个匹配，而 [re.search()](https://docs.python.org/3/library/re.html#re.search) 在字符串的任何位置检查一个匹配 (这也是 Perl 的默认操作)。

但是要注意在 [MULTILINE](https://docs.python.org/3/library/re.html#re.MULTILINE) 模式下 [match()](https://docs.python.org/3/library/re.html#re.match) 仅匹配字符串的起始位置，然后使用 [search()](https://docs.python.org/3/library/re.html#re.search) 与一个以 `'^'` 开头的正则表达式将匹配每一行的起始位置。

```python
>>> re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
>>> re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
<re.Match object; span=(4, 5), match='X'>
>>>
```

##### 文本转换
[sub()](https://docs.python.org/3/library/re.html#re.sub) 用一个字符串或者一个函数的结果替换每一个出现的模式。这个例子演示使用 [sub()](https://docs.python.org/3/library/re.html#re.sub) 及一个函数转换（“munge”）文本，或者使一个序列的每一个单词里的所有字符的顺序随机化除了每个单词的第一个和最后一个字符：

```python
>>> import re
>>> import random
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
... 
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poesorfsr Albedolamk, paelse rropet your aencbses prtomply.'
>>> re.findall(r"(\w)(\w+)(\w)", text)
[('P', 'rofesso', 'r'), ('A', 'bdolmale', 'k'), ('p', 'leas', 'e'), ('r', 'epor', 't'), ('y', 'ou', 'r'), ('a', 'bsence', 's'), ('p', 'romptl', 'y')]
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pfrsseoor Amlalbeodk, pselae reorpt your asbneecs pltormpy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Persofosr Abeladomlk, plsaee roeprt yuor abenecss prpolmty.'
>>>
```

##### 查找所有副词
[findall()](https://docs.python.org/3/library/re.html#re.findall) 匹配*所有*出现的模式，而不仅仅是第一个就像 [search()](https://docs.python.org/3/library/re.html#re.search) 所做的那样。例如，如果一个作家想在一些文本中查找所有副词，他们可能以下面这种方式使用 [findall()](https://docs.python.org/3/library/re.html#re.findall) ：

```python
>>> text = "He was carefully disguised but captured quickly by police."
>>> re.findall(r"\w+ly", text)
['carefully', 'quickly']
>>>
```

##### 其它正则表达式例子
**非贪婪匹配**  
非贪婪匹配是在 *匹配* 的前提下，匹配尽量少的字符。

```python
>>> import re
>>> html = '''<li data-view="7">
... <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
... </li>'''
>>> results = re.findall('<li.*?(\w+)</a>', html, re.S)
>>> print(results)
['沧海一声笑']
>>> results = re.findall('<li(.*?)(\w+)</a>', html, re.S)
>>> print(results)
[(' data-view="7">\n<a href="/2.mp3" singer="任贤齐">', '沧海一声笑')]
>>> 
```

`\s*?` 可以匹配空值

```python
>>> import re
>>> html = '''</a></li>'''
>>> results = re.findall('</a>\s*?</li>', html, re.S)
>>> print(results)
['</a></li>']
>>> results = re.findall('</a>(\s*?)</li>', html, re.S)
>>> print(results)
['']
>>>
```

### 二进制数据服务
在这章中描述的模块提供一些用于处理二进制数据的基本服务操作。关于二进制数据的其他操作，特别是与文件格式和网络协议相关的，在相关章节中描述。

#### codecs — 编解码器注册和相关基类
**源代码：** [Lib/codecs.py](https://github.com/python/cpython/tree/3.7/Lib/codecs.py)

这个模块定义了标准 Python 编解码器（编码器和解码器）的基类，并提供接口用来访问内部的 Python 编解码器注册表，该注册表负责管理编解码器和错误处理的查找过程。 大多数标准编解码器都属于 [文本编码](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding)，它们可将文本编码为字节串，但也提供了一些编解码器可将文本编码为文本，以及字节串编码为字节串。 自定义编解码器可以在任意类型间进行编码和解码，但某些模块特性仅适用于 [文本编码](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding) 或将数据编码为 **字节串** 的编解码器。

该模块定义了以下用于使用任何编解码器进行编码和解码的函数：

codecs.**encode**(*obj, encoding='utf-8', errors='strict'*)  
使用为 *encoding* 注册的编解码器对 *obj* 进行编码。

可以给定 *Errors* 以设置所需要的错误处理方案。 默认的错误处理方案 `'strict'` 表示编码错误将引发 [ValueError](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) (或更特定编解码器相关的子类，例如 [UnicodeEncodeError](https://docs.python.org/zh-cn/3/library/exceptions.html#UnicodeEncodeError))。 请参阅 [编解码器基类](https://docs.python.org/zh-cn/3/library/codecs.html#codec-base-classes) 了解有关编解码器错误处理的更多信息。

codecs.**decode**(*obj, encoding='utf-8', errors='strict'*)  
使用为 *encoding* 注册的编解码器对 *obj* 进行解码。

可以给定 *Errors* 以设置所需要的错误处理方案。 默认的错误处理方案 `'strict'` 表示编码错误将引发 [ValueError](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) (或更特定编解码器相关的子类，例如 [UnicodeDecodeError](https://docs.python.org/zh-cn/3/library/exceptions.html#UnicodeDecodeError))。 请参阅 [编解码器基类](https://docs.python.org/zh-cn/3/library/codecs.html#codec-base-classes) 了解有关编解码器错误处理的更多信息。

##### 无状态的编码和解码
基本 Codec 类定义了这些方法，同时还定义了无状态编码器和解码器的函数接口：

Codec.**encode**(*input*__[__, *errors*__]__)  
编码 *input* 对象并返回一个元组 (输出对象, 消耗长度)。 例如，[文本编码](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding) 会使用特定的字符集编码格式 (例如 `cp1252` 或 `iso-8859-1`) 将字符串转换为字节串对象。

*errors* 参数定义了要应用的错误处理方案。 默认为 `'strict'` 处理方案。

此方法不一定会在 Codec 实例中保存状态。 可使用必须保存状态的 [StreamWriter](https://docs.python.org/zh-cn/3/library/codecs.html#codecs.StreamWriter) 作为编解码器以便高效地进行编码。

编码器必须能够处理零长度的输入并在此情况下返回输出对象类型的空对象。

Codec.**decode**(*input*__[__, *errors*__]__)  
解码 *input* 对象并返回一个元组 (输出对象, 消耗长度)。 例如，[文本编码](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding) 的解码操作会使用特定的字符集编码格式将字节串对象转换为字符串对象。

对于文本编码格式和字节到字节编解码器，*input* 必须为一个字节串对象或提供了只读缓冲区接口的对象 -- 例如，缓冲区对象和映射到内存的文件。

*errors* 参数定义了要应用的错误处理方案。 默认为 `'strict'` 处理方案。

此方法不一定会在 Codec 实例中保存状态。 可使用必须保存状态的 [StreamReader](https://docs.python.org/zh-cn/3/library/codecs.html#codecs.StreamReader) 作为编解码器以便高效地进行解码。

解码器必须能够处理零长度的输入并在此情况下返回输出对象类型的空对象。

##### 编码格式与 Unicode
字符串在系统内部存储为 `0x0`--`0x10FFFF` 范围内的码位序列。 （请参阅 [PEP 393](https://www.python.org/dev/peps/pep-0393) 了解有关实现的详情。） 一旦字符串对象要在 CPU 和内存以外使用，字节的大小端顺序和字节数组的存储方式就成为一个关键问题。 如同使用其他编解码器一样，将字符串序列化为字节序列被称为 *编码*，而从字节序列重建字符串被称为 *解码*。 存在许多不同的文本序列化编解码器，它们被统称为 [文本编码](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding)。

最简单的文本编码格式 (称为 `'latin-1'` 或 `'iso-8859-1'`) 将码位 0--255 映射为字节值 `0x0`--`0xff`，这意味着包含 `U+00FF` 以上码位的字符串对象无法使用此编解码器进行编码。 这样做将引发 [UnicodeEncodeError](https://docs.python.org/zh-cn/3/library/exceptions.html#UnicodeEncodeError)，其形式类似下面这样（不过详细的错误信息可能会有所不同）: `UnicodeEncodeError: 'latin-1' codec can't encode character '\u1234' in position 3: ordinal not in range(256)`。

还有另外一组编码格式（所谓的字符映射编码）会选择全部 Unicode 码位的不同子集并设定如何将这些码位映射为字节值 `0x0`--`0xff`。 要查看这是如何实现的，只需简单地打开相应源码例如 `encodings/cp1252.py` (这是一个主要在 Windows 上使用的编码格式)。 其中会有一个包含 256 个字符的字符串常量，指明每个字符所映射的字节值。

所有这些编码格式只能对 Unicode 所定义的 1114112 个码位中的 256 个进行编码。 一种能够存储每个 Unicode 码位的简单而直接的办法就是将每个码位存储为四个连续的字节。 存在两种不同的可能性：以大端序存储或以小端序存储。 这两种编码格式分别被称为 `UTF-32-BE` 和 `UTF-32-LE`。 它们的缺点可以举例说明：如果你在一台小端序的机器上使用 `UTF-32-BE` 则你将必须在编码和解码时翻转字节。 `UTF-32` 避免了这个问题：字节的排列将总是使用自然顺序。 当这些字节被具有不同字节顺序的 CPU 读取时，则必须进行字节翻转。 为了能够检测 `UTF-16` 或 `UTF-32` 字节序列的大小端序，可以使用所谓的 BOM ("字节顺序标记")。 这对应于 Unicode 字符 `U+FEFF`。 此字符可添加到每个 `UTF-16` 或 `UTF-32` 字节序列的开头。 此字符的字节翻转版本 (`0xFFFE`) 是一个不可出现于 Unicode 文本中的非法字符。 因此当发现一个 `UTF-16` 或 `UTF-32` 字节序列的首个字符是 `U+FFFE` 时，就必须在解码时进行字节翻转。 不幸的是字符 `U+FEFF` 还有第二个含义 `ZERO WIDTH NO-BREAK SPACE`: 即宽度为零并且不允许用来拆分单词的字符。 它可以被用来为语言分析算法提供提示。 在 Unicode 4.0 中用 `U+FEFF` 表示 `ZERO WIDTH NO-BREAK SPACE` 已被弃用（改用 `U+2060` (`WORD JOINER`) 负责此任务）。 然而 Unicode 软件仍然必须能够处理 `U+FEFF` 的两个含义：作为 BOM 它被用来确定已编码字节的存储布局，并在字节序列被解码为字符串后将其去除；作为 `ZERO WIDTH NO-BREAK SPACE` 它是一个普通字符，将像其他字符一样被解码。

还有另一种编码格式能够对所有的 Unicode 字符进行编码：UTF-8。 UTF-8 是一种 8 位编码，这意味着在 UTF-8 中没有字节顺序问题。 UTF-8 字节序列中的每个字节由两部分组成：标志位（最重要的位）和内容位。 标志位是由零至四个值为 `1` 的二进制位加一个值为 `0` 的二进制位构成的序列。 Unicode 字符会按以下形式进行编码（其中 x 为内容位，当拼接为一体时将给出对应的 Unicode 字符）：

范围                           |编码
-------------------------------|------
`U-00000000` ... `U-0000007F`  |0xxxxxxx
`U-00000080` ... `U-000007FF`  |110xxxxx 10xxxxxx
`U-00000800` ... `U-0000FFFF`  |1110xxxx 10xxxxxx 10xxxxxx
`U-00010000` ... `U-0010FFFF`  |11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Unicode 字符最不重要的一个位就是最右侧的二进制位 x。

由于 UTF-8 是一种 8 位编码格式，因此 BOM 是不必要的，并且已编码字符串中的任何 `U+FEFF` 字符（即使是作为第一个字符）都会被视为是 `ZERO WIDTH NO-BREAK SPACE`。

在没有外部信息的情况下，就不可能毫无疑义地确定一个字符串使用了何种编码格式。 每种字符映射编码格式都可以解码任意的随机字节序列。 然而对 UTF-8 来说这却是不可能的，因为 UTF-8 字节序列具有不允许任意字节序列的特别结构。 为了提升 UTF-8 编码检测的可靠性，Microsoft 发明了一种 UTF-8 变体形式 (Python 2.5 称之为 `"utf-8-sig"`) 专门用于其 Notepad 程序：在任何 Unicode 字符在被写入文件之前，会先写入一个 UTF-8 编码的 BOM (它看起来是这样一个字节序列: `0xef`, `0xbb`, `0xbf`)。 由于任何字符映射编码后的文件都不大可能以这些字节值开头（例如它们会映射为

LATIN SMALL LETTER I WITH DIAERESIS  
RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK  
INVERTED QUESTION MARK  

对于 iso-8859-1 编码格式来说），这提升了根据字节序列来正确猜测 `utf-8-sig` 编码格式的成功率。 所以在这里 BOM 的作用并不是帮助确定生成字节序列所使用的字节顺序，而是作为帮助猜测编码格式的记号。 在进行编码时 utf-8-sig 编解码器将把 `0xef`, `0xbb`, `0xbf` 作为头三个字节写入文件。 在进行解码时 `utf-8-sig` 将跳过这三个字节，如果它们作为文件的头三个字节出现的话。 在 UTF-8 中并不推荐使用 BOM，通常应当避免它们的出现。

##### 标准编码
Python 自带了许多内置的编解码器，它们的实现或者是通过 C 函数，或者是通过映射表。 以下表格是按名称排序的编解码器列表，并提供了一些常见别名以及编码格式通常针对的语言。 别名和语言列表都不是详尽无遗的。 请注意仅有大小写区别或使用连字符替代下划线的拼写形式也都是有效的别名；因此，'utf-8' 是 'utf_8' 编解码器的有效别名。

**CPython implementation detail:** 有些常见编码格式可以绕过编解码器查找机制来提升性能。 这些优化机会对于 CPython 来说仅能通过一组有限的别名（大小写不敏感）来识别：utf-8, utf8, latin-1, latin1, iso-8859-1, iso8859-1, mbcs (Windows 专属), ascii, us-ascii, utf-16, utf16, utf-32, utf32, 也包括使用下划线替代连字符的的形式。 使用这些编码格式的其他别名可能会导致更慢的执行速度。

*在 3.6 版更改:* 可识别针对 us-ascii 的优化机会。

许多字符集都支持相同的语言。 它们在个别字符（例如是否支持 EURO SIGN 等）以及给字符所分配的码位方面存在差异。 特别是对于欧洲语言来说，通常存在以下几种变体：

* 某个 ISO 8859 编码集
* 某个 Microsoft Windows 编码页，通常是派生自某个 8859 编码集，但会用附加的图形字符来替换控制字符。
* 某个 IBM EBCDIC 编码页
* 某个 IBM PC 编码页，通常会兼容 ASCII

编码  |别名         |语言
-----|-------------|-----
ascii|646, us-ascii|英语
cp1252 |windows-1252 |西欧
gb2312 |chinese, csiso58gb231280, euc-cn, euccn, eucgb2312-cn, gb2312-1980, gb2312-80, iso-ir-58 |简体中文
gbk    |936, cp936, ms936 |统一汉语
gb18030 |gb18030-2000 |统一汉语
hz     |hzgb, hz-gb, hz-gb-2312 |简体中文
latin_1 |iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1 |西欧
utf_8  |U8, UTF, utf8 |所有语言

##### Python 专属的编码格式
有一些预定义编解码器是 Python 专属的，因此它们在 Python 之外没有意义。 这些编解码器按其所预期的输入和输出类型在下表中列出（请注意虽然文本编码是编解码器最常见的使用场景，但下层的编解码器架构支持任意数据转换而不仅是文本编码）。 对于非对称编解码器，所列目的描述的是编码方向。

**文字编码**

以下编解码器提供了 [str](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 到 [bytes](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 的编码和 [bytes-like object](https://docs.python.org/zh-cn/3/glossary.html#term-bytes-like-object) 到 [str](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 的解码，类似于 Unicode 文本编码。

编码 |别名|目的
-----|---|--------
mbcs |ansi, dbcs |Windows 专属：根据 ANSI 代码页（CP_ACP）对操作数进行编码。
oem  |   |Windows 专属：根据 OEM 代码页（CP_OEMCP）对操作数进行编码。 *3.6 新版功能.*

**二进制转换**

以下编解码器提供了二进制转换: [bytes-like object](https://docs.python.org/zh-cn/3/glossary.html#term-bytes-like-object) 到 [bytes](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 的映射。 它们不被 [bytes.decode()](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes.decode) 所支持（该方法只生成 [str](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 类型的输出）。

编码       |别名     |目的      |编码器/解码器
-----------|--------|----------|-------------
hex_codec  |hex     |将操作数转换为十六进制表示，每个字节有两位数 |[binascii.b2a_hex()](https://docs.python.org/zh-cn/3/library/binascii.html#binascii.b2a_hex) / [binascii.a2b_hex()](https://docs.python.org/zh-cn/3/library/binascii.html#binascii.a2b_hex)

## 数据类型
### collections --- 容器数据类型
**源代码：** [Lib/collections/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.8/Lib/collections/__init__.py)

这个模块实现了特定目标的容器，以提供Python标准内建容器 [dict](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) , [list](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) , [set](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) , 和 [tuple](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 的替代选择。

|       |       |  
--------|--------  
[namedtuple()](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple)  |创建命名元组子类的工厂函数  
[deque](https://docs.python.org/zh-cn/3/library/collections.html#collections.deque)      |类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)  
[ChainMap](https://docs.python.org/zh-cn/3/library/collections.html#collections.ChainMap)  |类似字典(dict)的容器类，将多个映射集合到一个视图里面  
[Counter](https://docs.python.org/zh-cn/3/library/collections.html#collections.Counter)   |字典的子类，提供了可哈希对象的计数功能  
[OrderedDict](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict)  |字典的子类，保存了他们被添加的顺序  
[defaultdict](https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict)  |字典的子类，提供了一个工厂函数，为字典查询提供一个默认值  
[UserDict](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserDict)  |封装了字典对象，简化了字典子类化  
[UserList](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserList)  |封装了列表对象，简化了列表子类化  
[UserString](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserString)  |封装了列表对象，简化了字符串子类化  

*从版本 3.3 开始弃用，将在版本 3.9 中被移除：* 已将 [容器抽象基类](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections-abstract-base-classes) 移至 [collections.abc](https://docs.python.org/zh-cn/3/library/collections.abc.html#module-collections.abc) 模块。 为了保持向下兼容性，它们在 Python 3.8 版的这个模块中仍然存在。

### collections.abc --- 容器的抽象基类
*3.3 新版功能:* 该模块曾是 [collections](https://docs.python.org/zh-cn/3/library/collections.html#module-collections) 模块的组成部分。

**源代码：** [Lib/\_collections\_abc.py](https://github.com/python/cpython/tree/3.8/Lib/_collections_abc.py)

该模块定义了一些 [抽象基类](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class)，它们可用于判断一个具体类是否具有某一特定的接口；例如，这个类是否可哈希，或其是否为映射类。

#### 容器抽象基类

这个容器模块提供了以下 [ABCs](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class):

抽象基类  |继承自   |抽象方法   |Mixin 方法
---------|---------|----------|----------
[Container](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Container)  |  |`__contains__`  |  
[Hashable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Hashable)    |  |`__hash__`  |  
[Iterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable)    |  |`__iter__`  |  
[Iterator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterator)    |[Iterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable)  |`__next__`  |`__iter__`
[Reversible](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Reversible) |[Iterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable)  |`__reversed__`  |  
[Generator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Generator)  |[Iterator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterator)  |`send`, `throw`  |`close`, `__iter__`, `__next__`
[Sized](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sized)  |  |`__len__`  |  
[Callable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Callable)  |  |`__call__`  |  
[Collection](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Collection)  |[Sized](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sized), [Iterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable), [Container](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Container)  |`__contains__`, `__iter__`, `__len__`  |  
[Sequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence)  |[Reversible](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Reversible), [Collection](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Collection)  |`__getitem__`, `__len__`  |`__contains__`, `__iter__`, `__reversed__`, `index`, 和 `count`  
[MutableSequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableSequence)  |[Sequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence)  |`__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert`  |继承自 [Sequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence) 的方法，以及 `append`, `reverse`, `extend`, `pop`, `remove`，和 `__iadd__`  
[ByteString](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.ByteString)  |[Sequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence)  |`__getitem__`, `__len__`  |继承自 [Sequence](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence) 的方法  
[Set](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Set)  |[Collection](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Collection)  |`__contains__`, `__iter__`, `__len__`  |`__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__xor__`, 和 `isdisjoint`  
[MutableSet](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableSet)  |[Set](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Set)  |`__contains__`, `__iter__`, `__len__`, `add`, `discard`  |继承自 [Set](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Set) 的方法以及 `clear`, `pop`, `remove`, `__ior__`, `__iand__`, `__ixor__`，和 `__isub__`  
[Mapping](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Mapping)  |[Collection](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Collection)  |`__getitem__`, `__iter__`, `__len__`  |`__contains__`, `keys`, `items`, `values`, `get`, `__eq__`, 和 `__ne__`  
[MutableMapping](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableMapping)  |[Mapping](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Mapping)  |`__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__`  |继承自 [Mapping](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Mapping) 的方法以及 `pop`, `popitem`, `clear`, `update`，和 `setdefault`  
[MappingView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MappingView)  |[Sized](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sized)  |  |`__len__`  
[ItemsView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.ItemsView)  |[MappingView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MappingView), [Set](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Set)  |  |`__contains__`, `__iter__`  
[KeysView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.KeysView)  |[MappingView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MappingView), [Set](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Set)  |  |`__contains__`, `__iter__`  
[ValuesView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.ValuesView)  |[MappingView](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MappingView), [Collection](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Collection)  |  |`__contains__`, `__iter__`  
[Awaitable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Awaitable)  |  |`__await__`  |  
[Coroutine](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Coroutine)  |[Awaitable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Awaitable)  |`send`, `throw`  |`close`  
[AsyncIterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.AsyncIterable)  |  |`__aiter__`  |  
[AsyncIterator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.AsyncIterator)  |[AsyncIterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.AsyncIterable)  |`__anext__`  |`__aiter__`  
[AsyncGenerator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.AsyncGenerator)  |[AsyncIterator](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.AsyncIterator)  |`asend`, `athrow`  |`aclose`, `__aiter__`, `__anext__`  

*class* collections.abc.**Iterable**  
提供了 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法的抽象基类。

使用 `isinstance(obj, Iterable)` 可以检测一个类是否已经注册到了 [Iterable](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable) 或者实现了 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 函数，但是无法检测这个类是否能够使用 [\_\_getitem\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法进行迭代。检测一个对象是否是 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable) 的唯一可信赖的方法是调用 `iter(obj)`。  
</br>

*class* collections.abc.**Iterator**  
提供了 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__iter__) 和 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的抽象基类。参见 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator) 的定义。  
</br>

## 函数式编程模块
### itertools -- 为高效循环创建迭代器的函数

本模块实现一系列 [迭代器](https://docs.python.org/zh-cn/3/glossary.html#term-iterator) ，这些迭代器受到APL，Haskell和SML的启发。为了适用于Python，它们都被重写过。

#### Itertool函数
下列模块函数均创建并返回迭代器。有些迭代器不限制输出流长度，所以它们只应在能截断输出流的函数或循环中使用。

itertools.**count**(*start=0, step=1*)  
创建一个迭代器，它从 *start* 值开始，返回均匀间隔的值。经常用来作为 [map()](https://docs.python.org/3.6/library/functions.html#map) 的一个参数来生成连续的数据点。也和 [zip()](https://docs.python.org/3.6/library/functions.html#zip) 一起用来增加序列数。大致等同于：

```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
```

当计算浮点数时，有时更高的精准度可以通过代入乘法代码来实现，例如：`(start + step * i for i in count())`。

*在版本3.1中发生变化：* 增加 *step* 参数并允许非整型数参数。  
</br>

itertools.**groupby**(*iterable, key=None*)  
创建一个迭代器，返回 *iterable* 中连续的键和组。*key* 是一个为每个元素计算键值的函数。如果未指定或为 `None`，*key* 缺省为恒等函数（identity function），返回元素不变。一般来说，the iterable needs to already be sorted on the same key function.

groupby() 操作类似于Unix中的 `uniq`。每当 key 函数产生的键值改变时，迭代器会分组或生成一个新组（这就是为什么通常需要使用同一个键值函数先对数据进行排序）。That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.

返回的组本身也是一个迭代器，它与 [groupby()](https://docs.python.org/3/library/itertools.html#itertools.groupby) 共享底层的可迭代对象。因为源是共享的，when the [groupby()](https://docs.python.org/3/library/itertools.html#itertools.groupby) object is advanced, the previous group is no longer visible. 因此，如果稍后还需要返回结果，可保存为列表：

```python
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
```

[groupby()](https://docs.python.org/3/library/itertools.html#itertools.groupby) 大致等同于：

```python
class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        self.id = object()
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey, self.id))
    def _grouper(self, tgtkey, id):
        while self.id is id and self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)
```

```python
>>> from itertools import groupby
>>> [k for k, g in groupby('AAAABBBCCDAABBB')]
['A', 'B', 'C', 'D', 'A', 'B']
>>> [list(g) for k, g in groupby('AAAABBBCCD')]
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
>>> [len(list(g)) for k, g in groupby('AAAABBBCCD')]
[4, 3, 2, 1]
>>>
```

## 文件和目录访问
这章描述的模块处理磁盘文件和目录。例如，有读取文件内容的模块，有以便携的方式操作路径的模块，和创建临时文件的模块。这章中完整的模块列表是：

### os.path — 通用路径名操作
**Source code:** [Lib/posixpath.py](https://github.com/python/cpython/tree/3.6/Lib/posixpath.py) (for POSIX), [Lib/ntpath.py](https://github.com/python/cpython/tree/3.6/Lib/ntpath.py) (for Windows NT), and [Lib/macpath.py](https://github.com/python/cpython/tree/3.6/Lib/macpath.py) (for Macintosh)

这个模块实现了一些关于路径名的有用的函数。读或写文件请看 [open()](https://docs.python.org/3.6/library/functions.html#open)，访问文件系统请看 [os](https://docs.python.org/3.6/library/os.html#module-os) 模块。

os.path.**abspath**(*path*)  
返回路径名 *path* 的标准化绝对路径。在大多数平台，这等同于调用函数 [normpath()](https://docs.python.org/3/library/os.path.html#os.path.normpath) 如下： `normpath(join(os.getcwd(), path))`。

*在版本3.6中发生变化：* 接受一个 [path-like 对象](https://docs.python.org/3/glossary.html#term-path-like-object)。

```sh
# pwd
/root
# cat temp.py 
```

```python
import os


print(__file__)
print(os.path.abspath(__file__))
```

```sh
# python3.7 temp.py 
temp.py
/root/temp.py
```

os.path.**dirname**(*path*)  
返回路径名 *path* 的目录名。

*在版本3.6中发生变化：* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

```python
>>> import os.path
>>> os.path.dirname('/root/mystie/polls/urls.py')                                                         
'/root/mystie/polls'
>>> os.path.dirname(os.path.dirname('/root/mysite/polls/urls.py'))
'/root/mysite'
>>> os.path.dirname(os.path.dirname(os.path.dirname('/root/mysite/polls/urls.py')))
'/root'
>>> 

```

os.path.**exists**(*path*)  
如果 *path* 指向一个存在的路径或者一个打开的文件描述符则返回 `True`。如果指向损坏的符号链接，则返回 `False`。在一些平台，如果被请求的文件没有被授予执行 [os.stat()](https://docs.python.org/3.6/library/os.html#os.stat) 的权限，则这个函数可能返回 `False`，即使这个 *path* 物理存在。

*在版本3.3中发生变化：* *path* 现在可以是一个整型数：如果它是一个打开的文件描述符则返回 `True`，否则返回 `False`。

*在版本3.6中发生变化：* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。  
<br />

os.path.**getctime**(*path*)  
Return the system's ctime which, on some systems (like Unix) is the time of the last metadata change, and, 在另一些系统上 (像 Windows), 则是 *path* 的创建时间。 The return value is a number giving the number of seconds since the epoch (see the [time](https://docs.python.org/zh-cn/3/library/time.html#module-time) module). 如果文件不存在或者无法访问则抛出 [OSError](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError) 。

*在 3.6 版更改:* 接受一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。  
<br />

os.path.**join**(_path, *paths_)  
智能地连接一个或多个路径组件。返回值是 *path* 和所有 _*paths_ 成员的串联，且除了最后一个部分，每一个非空的部分后面都跟着一个正确的目录分隔符 (`os.sep`)，这意味着如果最后一个部分为空则结果将必定以一个分隔符结尾。如果一个组件是一个绝对路径，则所有前面的组件都被丢弃且连接从绝对路径组件继续。

在 Windows 平台，当遇到一个绝对路径组件 (如，`r'\foo'`) 时驱动器号不重置。如果一个组件包含一个驱动器号，则所有前面的组件被丢弃且驱动器号被重置。注意，因为每个驱动器都有一个当前目录，`os.path.join("c:", "foo")` represents a path relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`。

*在版本3.6中发生变化：* *path* 和 *paths* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

## 通用操作系统服务
这章描述的模块提供在（几乎）所有操作系统上都可用的操作系统特征接口，如文件和时钟。这些接口通常是根据 Unix 或 C 接口仿写的，但它们在大多数其它系统下也是可用的。这里是一个概述：

### os --- 各种各样的操作系统接口
**源代码：** [Lib/os.py](https://github.com/python/cpython/tree/3.8/Lib/os.py)

这个模块提供了一种便携的方式使用依赖于操作系统的功能。如果你仅仅只想读或写一个文件请看 [open()](https://docs.python.org/3/library/functions.html#open)，如果你想操作路径，请看 [os.path](https://docs.python.org/3/library/os.path.html#module-os.path) 模块，如果你想在命令行下读取所有文件中的所有行请看 [fileinput](https://docs.python.org/3/library/fileinput.html#module-fileinput) 模块。创建临时文件和目录请看 [tempfile](https://docs.python.org/3/library/tempfile.html#module-tempfile) 模块，高级文件和目录处理请看 [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) 模块。

#### 进程参数
这些函数和数据项提供了操作当前进程和用户的信息。

os.**getpid()**  
返回当前的进程id。

os.**getppid()**  
返回父进程的id。当父进程退出时，在 Unix 上返回的id是其中一个 init 进程 (1)，在 Windows 上它仍是同一个id，这个id有可能已经被另一个进程重用了。

**可用性：** Unix，Windows。

*在版本3.2中发生变化：* 增加对Windows的支持。

#### 文件和目录
在一些 Unix 平台，这些函数中的很多支持这些特性中的一个或多个：

* **指定一个文件描述符：** 对于一些函数，*path* 参数不仅可以是一个指定路径名的字符串，也可以是一个文件描述符。The function will then operate on the file referred to by the descriptor. (For POSIX systems, Python will call the `f...` version of the function.)

  你可以在你的平台上使用 [os.supports_fd](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.supports_fd) 来检查是否可以将 *path* 指定为一个文件描述符。如果它不可用，使用它将抛出一个 [NotImplementedError](https://docs.python.org/zh-cn/3/library/exceptions.html#NotImplementedError)。

  If the function also supports *dir_fd* or *follow_symlinks* arguments, it is an error to specify one of those when supplying *path* as a file descriptor.

* **paths relative to directory descriptors:** If *dir_fd* is not `None`, it should be a file descriptor referring to a directory, and the path to operate on should be relative; path will then be relative to that directory. 如果路径是绝对的，`dir_fd` 将被忽略。 (For POSIX systems, Python will call the `...at` or `f...at` version of the function.)

  你可以使用 [os.supports_dir_fd](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.supports_dir_fd) 检查你的平台是否支持 *dir_fd*。如果它是不可用的，使用它将抛出一个 [NotImplementedError](https://docs.python.org/zh-cn/3/library/exceptions.html#NotImplementedError)。

* **not following symlinks:** If *follow_symlinks* is `False`, and the last element of the path to operate on is a symbolic link, the function will operate on the symbolic link itself instead of the file the link points to. (For POSIX systems, Python will call the `l...` version of the function.)

  你可以使用 [os.supports_follow_symlinks](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.supports_follow_symlinks) 检查在你的平台上是否支持 *follow_symlinks*。如果它是不可用的，使用它将抛出一个 [NotImplementedError](https://docs.python.org/zh-cn/3/library/exceptions.html#NotImplementedError)。

os.**listdir**(*path='.'*)  
返回一个包含 *path* 指定的目录中的条目名称的列表。列表是任意顺序的，且不包括特殊条目 `'.'` 和 `'..'` 即使它们出现在目录中。

*path* 可以是一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。如果 *path* 是 *bytes* 类型 (直接或间接地通过 [PathLike](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.PathLike) 接口)，则返回的文件名也将是 *bytes* 类型；在所有其它情形下，它们将是 *str* 类型。

这个函数也支持指 [指定一个文件描述符](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#path-fd)；文件描述符必须指向一个目录。

**注解：** 要将 `str` 文件名编码为 `bytes`，使用 [fsencode()](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.fsencode)。

**参见：** The [scandir()](https://docs.python.org/zh-cn/3/library/os.html?highlight=listdir#os.scandir) function returns directory entries along with file attribute information, giving better performance for many common use cases.

*在 3.2 版更改:* *path* 参数变成了可选的。

*3.3 新版功能:* Added support for specifying an open file descriptor for *path*.

*在 3.6 版更改:* 接受一个 [类路径对象](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)。

os.**rename**(*src, dst, \*, src\_dir\_fd=None, dst\_dir\_fd=None*)  
将文件或目录 *src* 重命名为 *dst*。如果 *dst* 已存在，the operation will fail with an [OSError](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError) subclass in a number of cases:

在 Windows 平台，如果 *dst* 已存在则总是抛出一个 [FileExistsError](https://docs.python.org/zh-cn/3/library/exceptions.html#FileExistsError) 。

On Unix, if *src* is a file and *dst* is a directory or vice-versa, an [IsADirectoryError](https://docs.python.org/zh-cn/3/library/exceptions.html#IsADirectoryError) or a [NotADirectoryError](https://docs.python.org/zh-cn/3/library/exceptions.html#NotADirectoryError) will be raised respectively. 如果 *src* 和 *dst* 都是目录且 *dst* 是空的，则 *dst* 将被安静地替换。如果 *dst* 是一个非空的目录，则抛出一个 [OSError](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError) 。如果两者都是文件，*dst* 将会被安静地替换如果用户有权限的话。 The operation may fail on some Unix flavors if *src* and *dst* are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

This function can support specifying *src_dir_fd* and/or *dst_dir_fd* to supply [paths relative to directory descriptors](https://docs.python.org/zh-cn/3/library/os.html#dir-fd).

If you want cross-platform overwriting of the destination, use [replace()](https://docs.python.org/zh-cn/3/library/os.html#os.replace).

*3.3 新版功能:* *src_dir_fd* 和 *dst_dir_fd* 参数。

*在 3.6 版更改:* Accepts a [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object) for *src* and *dst*.

#### 进程管理
这些函数可能被用于创建和管理进程。

os.**system**(*command*)  
在一个子 Shell 中执行 *command* (一个字符串)。这是通过调用标准 C 函数 system() 实现的，并且有相同的限制。Changes to [sys.stdin](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdin), etc. are not reflected in the environment of the executed command. 如果 *command* 产生了任何输出，它将被发送到解释器的标准输出流。

在 Unix 平台，the return value is the exit status of the process encoded in the format specified for [wait()](https://docs.python.org/zh-cn/3/library/os.html#os.wait). 注意 POSIX 没有指定 C system() 函数的返回值的含义，所以 Python 函数的返回值依赖于系统。

```python
>>> import os
>>> os.system('hostname')
archlinux
0        # 除了 shell 命令的输出，还输出了 system() 函数的退出状态码
>>>
```

在 Windows 平台，the return value is that returned by the system shell after running *command*. shell 是由 Windows 环境变量 COMSPEC 指定的：它通常是 **cmd.exe**，which returns the exit status of the command run; on systems using a non-native shell, consult your shell documentation.

The [subprocess](https://docs.python.org/zh-cn/3/library/subprocess.html#module-subprocess) module provides more powerful facilities for spawning new processes and retrieving their results; 使用那个模块比使用这个函数更好。See the [Replacing Older Functions with the subprocess Module](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess-replacements) section in the [subprocess](https://docs.python.org/zh-cn/3/library/subprocess.html#module-subprocess) documentation for some helpful recipes.

Raises an [auditing event](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `os.system` with argument `command`.

可用性: Unix, Windows。

#### 各种各样的系统信息

下面的数据值被用于支持路径操作运算。这些是为所有平台定义。

高层次的路径名操作被定义在 [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path) 模块中。

os.**sep**  
操作系统用来分隔路径名组件的字符。POSIX 为 `'/'` 而 Windows 为 `'\\'`。Note that knowing this is not sufficient to be able to parse or concatenate pathnames — 使用 [os.path.split()](https://docs.python.org/3.6/library/os.path.html#os.path.split) 和 [os.path.join()](https://docs.python.org/3.6/library/os.path.html#os.path.join) — 但它偶尔是有用的。Also available via [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path)。

### time — 时间的访问和转化
这个模块提供了各种各样的时间相关的函数。相关的功能 (functionality)，请参见 [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) 和 [calendar](https://docs.python.org/3/library/calendar.html#module-calendar) 模块。

尽管此模块始终可用，但并非所有平台上都提供所有功能。 此模块中定义的大多数函数调用都具有相同名称的平台C库函数。 因为这些函数的语义因平台而异,所以使用时最好查阅平台相关文档。

按顺序解释一些术语和惯例。

* *epoch* 是时间的起始点，且取决于平台。对于 Unix, epoch 是 1970-1-1, 00:00:00 (UTC). 要找出指定平台的 epoch 是什么，请查看 `time.gmtime(0)`。

* 术语 *Unix 纪元秒数 (seconds since the epoch)* 是指自国际标准时间 1970 年 1 月 1 日零时以来经过的总秒数，通常不包括 [闰秒](https://en.wikipedia.org/wiki/Leap_second)。 在所有符合 POSIX 标准的平台上，闰秒都会从总秒数中被扣除。

* 此模块中的功能可能无法处理纪元之前或将来的远期日期和时间。未来的截止点由C库决定；对于32位系统，它通常在2038年。

* **2000年（Y2K）问题 ：**Python依赖于平台的C库，它通常没有2000年问题，因为所有日期和时间都在内部表示为自纪元以来的秒数。函数 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 在给出 `%y` 格式代码时可以解析2位数年份。当解析2位数年份时，它们将根据 POSIX 和 ISO C 标准进行转换：值 69--99 映射到 1969--1999，值 0--68 映射到2000--2068。

* UTC 是 Coordinated Universal Time (以前叫 Greenwich Mean Time, 或 GMT). 首字母缩略词 UTC 不是一个错误而是英语与法语间的一个折衷。

* DST是夏令时，在一年中的一部分时间（通常）调整时区一小时。 DST规则很神奇（由当地法律确定），并且每年都会发生变化。 C 库有一个包含本地规则的表（通常是从系统文件中读取以获得灵活性），并且在这方面是True Wisdom的唯一来源。

* 时间值由 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime)，[localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 和 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 返回，并被 [asctime()](https://docs.python.org/zh-cn/3/library/time.html#time.asctime)， [mktime()](https://docs.python.org/zh-cn/3/library/time.html#time.mktime) 和 [strftime()](https://docs.python.org/zh-cn/3/library/time.html#time.strftime) 接受，是一个 9 个整数的序列。 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime)， [localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 和 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 的返回值还提供各个字段的属性名称。

  请参阅 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 以获取这些对象的描述。

  *在 3.3 版更改:* 在平台支持相应的 `struct tm` 成员时，[struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 类型被扩展提供 tm_gmtoff 和 tm_zone 属性。

  *在 3.6 版更改:* [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 的属性 tm_gmtoff 和 tm_zone 现在可在所有平台上使用。

* 使用以下函数在时间表示之间进行转换：  
  
  从                 |到                   |使用
  -------------------|---------------------|----------------
  seconds since the epoch |UTC 的 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) |[gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime)
  seconds since the epoch |本地时间的 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) |[localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime)
  UTC 的 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) |seconds since the epoch |[calendar.timegm()](https://docs.python.org/zh-cn/3/library/calendar.html#calendar.timegm)
  本地时间的 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) |seconds since the epoch |[mktime()](https://docs.python.org/zh-cn/3/library/time.html#time.mktime)

#### 函数
time.**gmtime**(\[*secs*\])  
将一个以 epoch 为起始点以秒为单位的时间表达式转换成一个 UTC 格式的 [struct_time](https://docs.python.org/3/library/time.html#time.struct_time) 且 dst 标志总是为0。如果 *secs* 没有提供或者为 [None](https://docs.python.org/3/library/constants.html#None)，则使用 [time()](https://docs.python.org/3/library/time.html#time.time) 返回的当前时间。小数部分的秒被忽略。[struct_time](https://docs.python.org/3/library/time.html#time.struct_time) 对象的描述请看上面。这个函数的反转请看 [calendar.timegm()](https://docs.python.org/3/library/calendar.html#calendar.timegm)。

time.**localtime**(**[**_secs_**]**)  
与 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime) 相似但转换为当地时间。如果未提供 *secs* 或为 [None](https://docs.python.org/zh-cn/3/library/constants.html#None) ，则使用由 [time()](https://docs.python.org/zh-cn/3/library/time.html#time.time) 返回的当前时间。当 DST 适用于给定时间时，dst标志设置为 `1` 。

time.**sleep**(*secs*)  
将当前线程按指定的秒数推迟执行。参数可以是一个浮点数以指定一个更精确的睡眠时间。The actual suspension time may be less than that requested because any caught signal will terminate the [sleep()](https://docs.python.org/zh-cn/3/library/time.html#time.sleep) following execution of that signal’s catching routine. 此外，由于系统中其他活动的安排，暂停时间可能比请求的时间长任意量。

*在版本3.5中发生变化：* 即使睡眠被信号中断，该函数现在至少睡眠 *secs* ，除非信号处理程序引发异常 (原理请看 [PEP 475](https://www.python.org/dev/peps/pep-0475))。  
<br />

time.**strftime**(*format*__[__*, t*__]__)  
转换一个元组或 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 表示的由 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime) 或 [localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 返回的时间到由 *format* 参数指定的字符串。如果未提供 *t* ，则使用由 [localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 返回的当前时间。 *format* 必须是一个字符串。如果 *t* 中的任何字段超出允许范围，则引发 [ValueError](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 。

0是时间元组中任何位置的合法参数；如果它通常是非法的，则该值被强制改为正确的值。

以下指令可以嵌入 *format* 字符串中。它们显示时没有可选的字段宽度和精度规范，并被 [strftime()](https://docs.python.org/zh-cn/3/library/time.html#time.strftime) 结果中的指示字符替换：

指令 |意义                                         |注释
-----|---------------------------------------------|-----
`%a` |本地化的缩写星期中每日的名称。                  |
`%A` |本地化的星期中每日的完整名称。                  |
`%b` |本地化的月缩写名称。                           |
`%B` |本地化的月完整名称。                           |
`%c` |本地化的适当日期和时间表示。                    |
`%d` |十进制数 [01,31] 表示的月中日。                |
`%H` |十进制数 [00,23] 表示的小时（24小时制）。       |
`%I` |十进制数 [01,12] 表示的小时（12小时制）。       |
`%j` |十进制数 [001,366] 表示的年中日。               |
`%m` |十进制数 [01,12] 表示的月。                    |
`%M` |十进制数 [00,59] 表示的分钟。                  |
`%p` |本地化的 AM 或 PM 。                          |(1)
`%S` |十进制数 [00,61] 表示的秒。                    |(2)
`%U` |十进制数 [00,53] 表示的一年中的周数（星期日作为一周的第一天）作为。在第一个星期日之前的新年中的所有日子都被认为是在第0周。 |(3)
`%w` |十进制数 [0(星期日),6] 表示的周中日。           |
`%W` |十进制数 [00,53] 表示的一年中的周数（星期一作为一周的第一天）作为。在第一个星期一之前的新年中的所有日子被认为是在第0周。 |(3)
`%x` |本地化的适当日期表示。                          |
`%X` |本地化的适当时间表示。                          |
`%y` |十进制数 [00,99] 表示的没有世纪的年份。          |
`%Y` |十进制数表示的带世纪的年份。                     |
`%z` |时区偏移以格式 +HHMM 或 -HHMM 形式的 UTC/GMT 的正或负时差指示，其中H表示十进制小时数字，M表示小数分钟数字 [-23:59, +23:59] 。 |
`%Z` |时区名称（如果不存在时区，则不包含字符）。        |
`%%` |字面的 `'%'` 字符。                            |

**注释:**

(1). 当与 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 函数一起使用时，如果使用 `%I` 指令来解析小时， `%p` 指令只影响输出小时字段。

(2). 范围真的是 `0` 到 `61` ；值 `60` 在表示 [leap seconds](https://en.wikipedia.org/wiki/Leap_second) 的时间戳中有效，并且由于历史原因支持值 `61` 。

(3). 当与 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 函数一起使用时， `%U` 和 `%W` 仅用于指定星期几和年份的计算。

下面是一个示例，一个与 [RFC 2822](https://tools.ietf.org/html/rfc2822.html) Internet电子邮件标准以兼容的日期格式。

```python
>>> from time import gmtime, strftime
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Sat, 12 Oct 2019 06:33:53 +0000'
>>>
```

现在不推荐使用 `%Z` ，但是所有 ANSI C 库都不支持扩展为首选小时/分钟偏移量的```%z```转义符。 此外，严格的 1982 年原始 [RFC 822](https://tools.ietf.org/html/rfc822.html) 标准要求两位数的年份（%y而不是%Y），但是实际在2000年之前很久就转移到了4位数年。之后， [RFC 822](https://tools.ietf.org/html/rfc822.html) 已经废弃了，4位数的年份首先被推荐 [RFC 1123](https://tools.ietf.org/html/rfc1123.html) ，然后被 [RFC 2822](https://tools.ietf.org/html/rfc2822.html) 强制执行。

某些平台可能支持其他指令，但只有此处列出的指令具有 ANSI C 标准化的含义。要查看平台支持的完整格式代码集，请参阅 *strftime(3)* 文档。

在某些平台上，可选的字段宽度和精度规范可以按照以下顺序紧跟在指令的初始 `'%'` 之后；这也不可移植。字段宽度通常为2，除了 `%j` ，它是3。  
<br />

*class* time.**struct_time**  
返回的时间值序列的类型为 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime) 、 [localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 和 [strptime()](https://docs.python.org/zh-cn/3/library/time.html#time.strptime) 。它是一个带有 [named tuple](https://docs.python.org/zh-cn/3/glossary.html#term-named-tuple) 接口的对象：可以通过索引和属性名访问值。 存在以下值：

索引 |属性       |值
----|-----------|------------
0   |tm_year    |（例如，1993）
1   |tm_mon     |range [1, 12]
2   |tm_mday    |range [1, 31]
3   |tm_hour    |range [0, 23]
4   |tm_min     |range [0, 59]
5   |tm_sec     |range [0, 61]； 见 [strftime()](https://docs.python.org/zh-cn/3/library/time.html#time.strftime) 介绍中的 **(2)**
6   |tm_wday    |range [0, 6] ，周一为 0
7   |tm_yday    |range [1, 366]
8   |tm_isdst   |0, 1 或 -1；如下所示
N/A |tm_zone    |时区名称的缩写
N/A |tm_gmtoff  |以秒为单位的UTC以东偏离

请注意，与C结构不同，月份值是 [1,12] 的范围，而不是 [0,11] 。

在调用 [mktime()](https://docs.python.org/zh-cn/3/library/time.html#time.mktime) 时， tm_isdst 可以在夏令时生效时设置为1，而在夏令时不生效时设置为0。 值-1表示这是未知的，并且通常会导致填写正确的状态。

当一个长度不正确的元组被传递给期望 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 的函数，或者具有错误类型的元素时，会引发 [TypeError](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 。  
<br />

time.**time()** → float  
以 [epoch](https://docs.python.org/3/library/time.html#epoch) 为起始点以秒为单位返回当前时间作为一个浮点数。epoch 明确的日期及 [leap seconds](https://en.wikipedia.org/wiki/Leap_second) 的处理依赖于平台。在 Windows 和 大多数 Unix 系统中，epoch 是 1970-1-1, 00:00:00 (UTC) and leap seconds are not counted towards the time in seconds since the epoch. 这通常被称为 [Unix time](https://en.wikipedia.org/wiki/Unix_time). 要找出指定平台的 epoch 是什么，请查看 `time.gmtime(0)`。

请注意，即使时间总是作为浮点数返回，但并非所有系统都提供高于1秒的精度。虽然此函数通常返回非递减值，但如果在两次调用之间设置了系统时钟，则它可以返回比先前调用更低的值。

返回的数字 [time()](https://docs.python.org/zh-cn/3/library/time.html#time.time) 可以通过将其传递给 [gmtime()](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime) 函数或转换为UTC中更常见的时间格式（即年、月、日、小时等）或通过将它传递给 [localtime()](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 函数获得本地时间。在这两种情况下都返回一个 [struct_time](https://docs.python.org/zh-cn/3/library/time.html#time.struct_time) 对象，日历日期组件可以从中作为属性访问。

### platform --- 获取底层平台的标识数据
**源代码：** [Lib/platform.py](https://github.com/python/cpython/tree/3.8/Lib/platform.py)

**注解：** 具体的平台按字母顺序列出，其中 Linux 包含在 Unix 章节中。

#### 跨平台

platform.**architecture**(*executable=sys.executable, bits='', linkage=''*)  
Queries the given executable (defaults to the Python interpreter binary) for various architecture information.

Returns a tuple `(bits, linkage)` which contain information about the bit architecture and the linkage format used for the executable. 两个值都是作为字符串返回。

Values that cannot be determined are returned as given by the parameter presets. If bits is given as `''`, the `sizeof(pointer)` (or `sizeof(long)` on Python version < 1.5.2) is used as indicator for the supported pointer size.

The function relies on the system's `file` command to do the actual work. This is available on most if not all Unix platforms and some non-Unix platforms and then only if the executable points to the Python interpreter. 当上面的需求不满足时，将使用合理的默认值。

**注解：** On Mac OS X (and perhaps other platforms), executable files may be universal files containing multiple architectures.

To get at the "64-bitness" of the current interpreter, it is more reliable to query the [sys.maxsize](https://docs.python.org/zh-cn/3/library/sys.html#sys.maxsize) attribute:

```python
is_64bits = sys.maxsize > 2**32
```

```python
>>> import platform
>>> platform.architecture()
('64bit', 'ELF')
>>>
```

platform.**platform**(*aliased=0, terse=0*)  
Returns a single string identifying the underlying platform with as much useful information as possible.

The output is intended to be *human readable* rather than machine parseable. It may look different on different platforms and this is intended.

If *aliased* is true, the function will use aliases for various platforms that report system names which differ from their common names, for example SunOS will be reported as Solaris. The [system_alias()](https://docs.python.org/zh-cn/3/library/platform.html#platform.system_alias) function is used to implement this.

Setting *terse* to true causes the function to return only the absolute minimum information needed to identify the platform.

*在 3.8 版更改:* 在 macOS 中, the function now uses [mac_ver()](https://docs.python.org/zh-cn/3/library/platform.html#platform.mac_ver), if it returns a non-empty release string, to get the macOS version rather than the darwin version.

```python
>>> import platform
>>> platform.platform()
'Linux-5.1.15-arch1-1-ARCH-x86_64-with-arch-Arch-Linux'
>>>
```

platform.**python_compiler()**  
返回一个用于编译 Python 的编译器的标识字符串。

```python
>>> import platform
>>> platform.python_compiler()
'GCC 9.1.0'
>>>
```

platform.**python_implementation()**  
返回一个标识 Python 实现的字符串。可能的返回值是：`'CPython'`, `'IronPython'`, `'Jython'`, `'PyPy'`.

```python
>>> platform.python_implementation()
'CPython'
>>>
```

platform.**system()**  
返回系统/OS的名字，例如：`'Linux'`, `'Windows'`, 或者 `'Java'`。如果这个值不能被确定则会返回一个空字符串。

```python
>>> platform.system()
'Linux'
>>>
```

## 并发执行
### threading — 基于线程的并行
**源代码：** [Lib/threading.py](https://github.com/python/cpython/tree/3.7/Lib/threading.py)

这个模块在低级 [\_thread](https://docs.python.org/3/library/_thread.html#module-_thread) 模块之上构建了高级线程接口。另请参见 [queue](https://docs.python.org/3/library/queue.html#module-queue) 模块。

*在版本3.7中发生变化：* 这个模块过去是可选的，现在总是可用的。

**注意：** 虽然它们没有在下面被列出来，在Python 2.x 系列的这个模块中使用驼峰名的一些方法和函数仍被这个模块支持。

这个模块定义了下面的函数：

threading.**current_thread()**  
返回当前的 [Thread](https://docs.python.org/3/library/threading.html#threading.Thread) 对象，对应调用者的控制线程。如果调用者的控制线程不是通过 [threading](https://docs.python.org/3/library/threading.html#module-threading) 模块创建的，将返回一个虚拟的带有功能限制的线程对象。

##### 线程对象
[Thread](https://docs.python.org/3/library/threading.html#threading.Thread) 类表示一个在一个单独的控制线程中运行的活动。有两种方式指定活动：通过传递一个可调用对象给构造函数，或者通过在子类中重写 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法。子类中不应该重写其它方法（除了构造函数）。换句话说，仅重写这个类的 \_\_init\_\_() 和 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法。

一旦一个线程对象被创建，它的活动必须通过调用线程的 [start()](https://docs.python.org/3/library/threading.html#threading.Thread.start) 方法来启动。这将在一个单独的控制线程中调用 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法。

一旦线程的活动被启动，则线程被认为是 ‘活的’。当它的 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法终止时则该线程不再是活的 – 不管是正常终止，还是通过抛出一个未处理的异常。[is_alive()](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive) 方法测试线程是否是活的。

其它线程可以调用一个线程的 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 方法。这将阻塞调用线程直到 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 方法被调用的线程被终止。

每个线程都有一个名称。这个名字可以传递给构造函数，可以通过 [name](https://docs.python.org/3/library/threading.html#threading.Thread.name) 属性读取或更改这个名称。

一个线程可以被标记为一个 “守护线程”。这个标志的意义是当仅有守护线程留下时整个Python程序退出。初始值从创建线程继承。这个标志可以通过 [daemon](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) 属性或 *daemon* 构造函数参数设置。

**注意：** 在关机时守护线程会突然停止。它们的资源 (如打开的文件，数据库事务，等等。) 可能不会正确地释放。如果你希望你的线程平滑地停止，使它们成为非守护线程并使用一个合适的信号机制如一个 [事件](https://docs.python.org/3/library/threading.html#threading.Event)。

有一个 “主线程” 对象；这对应Python程序中的初始控制线程。它不是一个守护线程。

“虚拟线程对象” 被创建是有可能的。这些是对应 “异性线程” 的线程对象，即控制线程在 threading 模块之外启动的线程对象，如直接从 C 代码启动。虚拟线程对象有功能限制；它们总是被认为是活的和守护式的，且不能被 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join)ed。它们从来不会被删除，因为检测异性线程的终止是不可能的。

*class* threading.**Thread**(*group=None, target=None, name=None, args=(), kwargs={}, \*, daemon=None*)  
这个构造函数被调用时应该总是使用关键字参数。参数是：

*group* 应该为 `None`；保留给将来扩展当 ThreadGroup 类实现的时候。

*target* 是被 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法调用的可调用对象。默认为 `None`，意味着不调用任何东西。

*name* 是线程的名字。默认情况下，一个唯一的名字以 “Thread-N” 的形式被构建，其中 *N* 是一个较小的十进制数。

*args* 是用于目标调用的参数元组。默认为 `()`。

*kwargs* 是一个用于目标调用的关键字参数字典。默认为 `{}`。

如果不是 `None`，*daemon* 显示地设置线程是否是守护式的。如果为 `None` (默认值)，守护式属性从当前线程继承。

如果子类重写构造函数，它必须确保在对线程做任何别的事以前先调用基类构造函数 (`Thread.__init__()`)。

*在版本3.3中发生变化：* 增加了 *daemon* 参数。

**start()**  
启动线程的活动。

它必须被每个线程对象至多调用一次。它安排对象的 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法在一个单独的控制线程中被调用。

如果相同的线程对象调用该方法超过一次将抛出一个 [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)。

**run()**  
代表线程的活动的方法。

你可以在子类中重写这个方法。标准 [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) 方法调用传递给对象的构造函数作为 *target* 参数的可调用对象，如果有的话，并分别从 *args* 和 *kwargs* 参数中读取顺序参数和关键字参数。

**join**(*timeout=None*)  
等待直到线程终止。这将阻塞调用线程直到 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 方法被调用的线程终止 – 不论是正常终止还是通过一个未处理的异常 – 或者直到可选的 timeout 出现。

当 *timeout* 参数存在且不为 `None`时，它必须是一个为操作指定超时时间的浮点数 (或者 fractions thereof)，单位为秒。因为 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 总是返回 `None`，你必须在 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 之后调用 [is_alive()](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive) 以决定是否出现超时 – 如果线程仍是活的，[join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 调用超时。

当 *timeout* 参数不存在或者为 `None`时，操作将阻塞直到线程终止。

一个线程可以被 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join)ed 很多次。

如果试图加入当前线程 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 将抛出一个 [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)因为那将导致一个死锁。在线程启动以前试图 [join()](https://docs.python.org/3/library/threading.html#threading.Thread.join) 该线程将抛出相同的异常。

**name**  
一个仅用于标识目的的字符串。它没有语义。多个线程可以指定相同的名字。初始名称由构造函数设置。

**getName()**  
**setName()**  
[name](https://docs.python.org/3/library/threading.html#threading.Thread.name) 的旧的 getter/setter API；直接使用 [name](https://docs.python.org/3/library/threading.html#threading.Thread.name) 属性替代。

**ident**  
这个线程的 ‘线程标识符’ 或者 `None` 如果线程还没有启动的话。这是一个非零的整型数。参考 [get_ident()](https://docs.python.org/3/library/threading.html#threading.get_ident) 函数。线程标识符可以被回收当一个线程退出而另一个线程被创建时。即使在线程退出以后线程标识符仍是可用的。

**is_alive()**  
返回线程是否是活的。

This method returns `True` just before the [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) method starts until just after the [run()](https://docs.python.org/3/library/threading.html#threading.Thread.run) method terminates. 模块函数 [enumerate()](https://docs.python.org/3/library/threading.html#threading.enumerate) 返回一个所有激活的线程列表。

**daemon**  
一个布尔值表明这个线程是否是一个守护线程 (True) 或者不是 (False)。这个值必须在 [start()](https://docs.python.org/3/library/threading.html#threading.Thread.start) 被调用以前设置，否则抛出 [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)。它的初始值从创建线程继承 (creating thread)；主线程不是一个守护线程，因此所有在主线程中创建的线程的默认 [daemon](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) 都是 `False` ([daemon](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) = `False`)。

当没有激活的非守护线程留下时，整个Python程序退出。

**isDaemon()**  
**setDaemon()**  
用于 [daemon](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) 的旧的 getter/setter API；直接使用 [daemon](https://docs.python.org/3/library/threading.html#threading.Thread.daemon) 作为一个属性替代。

**CPython实现细节：** 在CPython中，因为[全局解释器锁](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)，每次仅有一个线程可以执行Python代码 (虽然某些面向性能的库可以克服这个限制)。如果你希望你的应用程序可以更好地利用多核机器的计算资源，建议你使用 [multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 或者 [concurrent.futures.ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)。然而，如果你想同时运行多个 I/O-bound 任务，threading 仍是一个合适的模型。

### multiprocessing — 基于进程的并行
**源代码：** [Lib/multiprocessing/](https://github.com/python/cpython/tree/3.7/Lib/multiprocessing/)

#### 介绍

[multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 是一个支持使用一个类似于 [threading](https://docs.python.org/3/library/threading.html#module-threading) 模块的API大量生成进程的包。[multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 包既提供本地并发又提供远程并发，通过使用子进程替代线程有效地回避了[全局解释器锁](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)。因为这，[multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 模块允许程序员彻底地利用指定机器上的多个处理器。它既可以在 Unix 上运行又可以在 Windows 上运行。

##### 进程类

在 [multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing)中，进程是通过创建一个[进程](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process)对象然后调用它的 [start()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start) 方法繁衍的。[Process](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process) 遵循 [threading.Thread](https://docs.python.org/3/library/threading.html#threading.Thread) 的API。一个很小的多进程程序的例子是

```python
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

显示单独的被调用的进程ID，这里是一个扩展的例子：

```python
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

对于为什么 `if __name__ == '__main__'` 部分是必要的一个解释，请看 [Programming guidelines](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming)。

##### 上下文和启动方法
取决于平台，[multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 支持三种方式启动一个进程。这些*启动方法*是

* *spawn*  
    父进程启动一个全新的python解释器进程。子进程将只继承那些运行进程对象的 [run()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run) 方法所必须的资源。特别地，不必要的文件描述符和句柄（handles）将不会从父进程继承。使用这种方法启动一个进程与使用 *fork* 或 *forkserver* 相比要慢很多。

在 Unix 和 Windows上可用。*spawn* 是 Windows 上的默认启动方法。

* *fork*  
父进程使用 [os.fork()](https://docs.python.org/3/library/os.html#os.fork) 来 fork Python 解释器。子进程，当它开始时，实际上与父进程完全相同。父进程的所有资源都被子进程继承。注意安全地 forking 一个多线程进程是有问题的。

仅在 Unix 上可用。*fork* 是 Unix 上的默认启动方式。

* *forkserver*  
当程序启动并选择 *forkserver* 启动方法时，一个服务器进程被启动。从那时起，每当需要一个新进程，父进程连接到服务器并请求它fork一个新进程。fork server 进程是一个单一的线程所以它使用 [os.fork()](https://docs.python.org/3/library/os.html#os.fork) 是安全的。没有不必要的资源被继承。

在支持通过 Unix 管道传递文件描述符的 Unix 平台上可用。

*在版本3.4中发生变化：* 在所有unix平台上增加了 *spawn*，在一些unix平台增加了 *forkserver*。在 Windows 上子进程不再继承所有父进程可继承的句柄。

#### 参考
[multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) 包大部分复制的 [threading](https://docs.python.org/3/library/threading.html#module-threading) 模块的API。

##### 进程和异常
*class* multiprocessing.**Process**(*group=None, target=None, name=None, args=(), kwargs={}, \*, daemon=None*)  
进程对象在一个单独的进程中运行表示活跃的。[Process](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process) 类有等同于 [threading.Thread](https://docs.python.org/3/library/threading.html#threading.Thread) 的所有方法。

构造函数应该总是通过关键字参数被调用。*group* 应该总是 `None`；它存在仅仅是为了与 [threading.Thread](https://docs.python.org/3/library/threading.html#threading.Thread) 兼容。*target* 是被 [run()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run) 方法调用的可调用对象。它默认为 `None`，意味着没有东西被调用。*name* 是进程名 (详细信息请看 [name](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.name))。*args* 是用于目标调用的参数元组。*kwargs* 是一个用于目标调用的关键字参数字典。如果提供，the keyword-only *daemon* argument sets the process [daemon](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.daemon) flag to `True` or `False`。如果为 `None` (默认值)，this flag will be inherited from the creating process。

默认情况下，没有参数传递给 *target*。

如果一个子类重写构造函数，它必须确保在对进程做任何别的事以前先调用基类构造函数 (Process.\_\_init\_\_())。

*在版本3.3中发生变化：* 增加了 *daemon* 参数。

**run()**  
代表进程的活动的方法。

你可以在子类中重写这个方法。标准 [run()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run) 方法调用传递给对象的构造函数作为目标参数的可调用对象，如果有的话，并分别从 *args* 和 *kwargs* 参数中读取顺序参数和关键字参数。

**start()**  
启动进程的活性。

它必须被每个进程对象至多调用一次。它安排对象的 [run()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run) 方法在一个单独的进程中被调用。

**join**([*timeout*])  
如果可选参数 *timeout* 为 `None` (默认值)，则该方法将阻塞直到进程的 [join()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join) 方法被调用终止。如果 *timeout* 是一个正数，它将最多阻塞 *timeout* 秒。注意如果它的进程终止或者如果这个方法超时则这个方法返回 `None`。检查进程的[退出代码](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.exitcode)以确定它是否被终止了。

一个进程可以被 joined 很多次。

一个进程不能 join 它自己因为这将导致一个死锁。在进程启动以前试图 join 一个进程是一个错误。

**name**  
进程的名称。名称是一个字符串仅用于标识目的。它没有语义。多个进程可能被指定相同的名称。

初始名称由构造函数设置。如果没有明确的名称提供给构造函数，一个名称的形式 ‘Process-N<sub>1</sub>:N<sub>2</sub>:…:N<sub>k</sub>’ 被构造，其中每个 N<sub>k</sub> 是父进程的 N-th 子进程。

**is_alive()**  
返回进程是否是活的。

大体上，从 [start()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start) 方法返回那一刻起直到子进程终止，进程对象是活跃的。

**daemon**  
进程的 *daemon* 标志，一个布尔值。这个标志必须在 [start()](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start) 被调用以前被设置。

初始值从创建进程（creating process）继承。

当一个进程退出时，它将试图终止它的所有 daemonic 子进程。

注意一个 daemonic 进程不允许创建子进程。Otherwise a daemonic process would leave its children orphaned if it gets terminated when its parent process exits. 另外，这些**不是** Unix 守护进程或服务，它们是普通进程，如果 non-daemonic 进程已经退出则它们将被终止 (且不被 joined)。

除了 [threading.Thread](https://docs.python.org/3/library/threading.html#threading.Thread) API，[进程](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process)对象也支持下面的属性和方法：

**pid**  
返回进程ID。在进程被繁衍以前，这个的返回值为 `None`。

**exitcode**  
子进程的退出代码。如果进程还没有被终止则返回 `None`。负值 *-N* 表明子进程被信号 *N* 终止。

##### 其它

multiprocessing.**cpu_count()**  
返回系统中CPU的个数。

这个数字不等同于当前进程可以使用的CPU个数。可用的CPU个数可以通过 `len(os.sched_getaffinity(0))` 获取。

可能抛出 [NotImplementedError](https://docs.python.org/3/library/exceptions.html#NotImplementedError)。

**另请参见：** [os.cpu_count()](https://docs.python.org/3/library/os.html#os.cpu_count)

### subprocess --- 子进程管理
**源代码:** [Lib/subprocess.py](https://github.com/python/cpython/tree/3.8/Lib/subprocess.py)

[subprocess](https://docs.python.org/zh-cn/3/library/subprocess.html#module-subprocess) 模块允许你生成新的进程，连接它们的输入、输出、错误管道，并且获取它们的返回码。此模块打算代替一些老旧的模块与功能：

```
os.system
os.spawn*
```

在下面的段落中，你可以找到关于 [subprocess](https://docs.python.org/zh-cn/3/library/subprocess.html#module-subprocess) 模块如何代替这些模块和功能的相关信息。

**参见:** [PEP 324](https://www.python.org/dev/peps/pep-0324) -- 提出 subprocess 模块的 PEP

#### 使用 subprocess 模块
推荐的调用子进程的方式是在任何它支持的用例中使用 [run()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.run) 函数。对于更进阶的用例，也可以使用底层的 [Popen](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen) 接口。

[run()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.run) 函数是在 Python 3.5 被添加的；如果你需要与旧版本保持兼容，查看 [Older high-level API](https://docs.python.org/zh-cn/3/library/subprocess.html#call-function-trio) 段落。

subprocess.**run**(*args, \*, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None*)  
运行被 *arg* 描述的指令。等待指令完成，然后返回一个 [CompletedProcess](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.CompletedProcess) 实例。

```python
>>> subprocess.run('hostname')
archlinux
CompletedProcess(args='hostname', returncode=0)
>>>
```

以上显示的参数仅仅是最常见的一些，[常用参数](https://docs.python.org/zh-cn/3/library/subprocess.html#frequently-used-arguments) 在下面描述（因此在缩写签名中仅使用关键字标示）。完整的函数签名基本和 [Popen](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen) 的构造函数一样，此函数接受的大多数参数都被传递给该接口。（*timeout*, *input*, *check* 和 *capture_output* 除外）。

如果 *capture_output* 设为 true，stdout 和 stderr 将会被捕获。在使用时，内置的 [Popen](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen) 对象将自动用 `stdout=PIPE` 和 `stderr=PIPE` 创建。*stdout* 和 *stderr* 参数不应当与 *capture_output* 同时提供。如果你希望捕获并将两个流合并在一起，使用 `stdout=PIPE` 和 `stderr=STDOUT` 来代替 *capture_output*。

*timeout* 参数将被传递给 [Popen.communicate()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen.communicate)。如果发生超时，子进程将被杀死并等待。 [TimeoutExpired](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.TimeoutExpired) 异常将在子进程中断后被抛出。

*input* 参数将被传递给 [Popen.communicate()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen.communicate) 以及子进程的标准输入. 如果使用此参数, 它必须是一个字节序列. 如果指定了 *encoding* 或 *errors* 或者将 *text* 设置为 `True`, 那么也可以是一个字符串. 当使用此参数时, 内部的 [Popen](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen) 对象将自动被创建, 伴随着设置 `stdin=PIPE`, 并且 *stdin* 可能不被使用.

如果 *check* 设为 True, 并且进程以非零状态码退出, 一个 [CalledProcessError](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.CalledProcessError) 异常将被抛出. 这个异常的属性将设置为参数, 退出码, 以及标准输出和标准错误, 如果被捕获到.

如果 *encoding* 或者 *error* 被指定, 或者 *text* 被设为 True, 标准输入, 标准输出和标准错误的文件对象将通过指定的 *encoding* 和 *errors* 以文本模式打开, 否则以默认的 [io.TextIOWrapper](https://docs.python.org/zh-cn/3/library/io.html#io.TextIOWrapper) 打开. *universal_newline* 参数等同于 *text* 并且提供了向后兼容性. 默认情况下, 文件对象是以二进制模式打开的.

如果 *env* 不是 `None`, 它必须是一个字典, 为新的进程设置环境变量; 它用于替换继承的当前进程的环境的默认行为. 它将直接被传递给 [Popen](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen).

例如:

```python
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')
```

*3.5 新版功能.*

*在 3.6 版更改:* 添加了 *encoding* 和 *errors* 形参.

*在 3.7 版更改:* 添加了 *text* 形参, 作为 *universal_newlines* 的一个更好理解的别名. 添加了 *capture_output* 形参.  
</br>

*class* subprocess.**CompletedProcess**  
[run()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.run) 的返回值, 代表一个进程已经结束.

**args**  
被用作启动进程的参数. 可能是一个列表或字符串.

**returncode**  
子进程的退出状态码. 通常来说, 一个为 0 的退出码表示进程运行正常.

一个负值 `-N` 表示子进程被信号 `N` 中断 (仅 POSIX).

**stdout**  
从子进程捕获到的标准输出. 一个字节序列, 或一个字符串, 如果 [run()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.run) 是设置了 *encoding*, *errors* 或者 `text=True` 来运行的. 如果未有捕获, 则为 `None`.

如果你通过 `stderr=subprocess.STDOUT` 运行, 标准输入和标准错误将被组合在一起, 并且 stderr 将为 `None`.

```python
>>> subprocess.run('hostname').stdout
archlinux
>>>
```

**stderr**  
捕获到的子进程的标准错误. 一个字节序列, 或者一个字符串, 如果 [run()](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.run) 是设置了参数 *encoding*, *errors* 或者 `text=True` 运行的. 如果未有捕获, 则为 `None`.

**check_returncode()**  
如果 [returncode](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.CompletedProcess.returncode) 非零, 抛出 [CalledProcessError](https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.CalledProcessError).

*3.5 新版功能.*

## 网络和进程间通信
### socket --- 底层网络接口
**源代码:** [Lib/socket.py](https://github.com/python/cpython/tree/3.8/Lib/socket.py)

这个模块提供了访问BSD *套接字* 的接口。在所有现代Unix系统、Windows、macOS和其他一些平台上可用。

**注解：** 一些行为可能因平台不同而异，因为调用的是操作系统的套接字API。

这个 Python 接口是用 Python 的面向对象风格对 Unix 系统调用和套接字库接口的直译：函数 [socket()](https://docs.python.org/3/library/socket.html#socket.socket) 返回一个 *套接字对象* ，其方法是对各种套接字系统调用的实现。形参类型一般与 C 接口相比更高级：例如在 Python 文件 `read()` 和 `write()` 操作中，接收操作的缓冲区分配是自动的，发送操作的缓冲区长度是隐式的。

**参见：**

**模块** [socketserver](https://docs.python.org/zh-cn/3/library/socketserver.html#module-socketserver)  
用于简化网络服务端编写的类。

**模块** [ssl](https://docs.python.org/zh-cn/3/library/ssl.html#module-ssl)  
套接字对象的TLS/SSL封装。

#### 套接字协议族
根据系统以及构建选项，此模块提供了各种套接字协议簇。

特定的套接字对象需要的地址格式将根据此套接字对象被创建时指定的地址族被自动选择。套接字地址表示如下：

* 一对 `(host, port)` 被用于 [AF_INET](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_INET) 地址族，*host* 是一个表示为互联网域名表示法之内的主机名或者一个 IPv4 地址的字符串，例如 `'daring.cwi.nl'` 或 `'100.50.200.5'`，*port* 是一个整数。

    * 对于 IPv4 地址，有两种可接受的特殊形式被用来代替一个主机地址： `''` 代表 INADDR_ANY，用来绑定到所有接口；字符串 `'<broadcast>'` 代表 INADDR_BROADCAST。此行为不兼容 IPv6，因此，如果你的 Python 程序打算支持 IPv6，则可能需要避开这些。

如果你在 IPv4/v6 套接字地址的 *host* 部分中使用了一个主机名，此程序可能会表现不确定行为，因为 Python 使用 DNS 解析返回的第一个地址。套接字地址将被解析为一个不同的 IPv4/v6 地址，依赖于 DNS 解析的结果和/或 host 配置。为了确定的行为，在 *host* 部分中使用一个数字的地址。

#### 模块内容
[socket](https://docs.python.org/zh-cn/3/library/socket.html#module-socket) 模块导出以下元素。

##### 常数
The AF_* and SOCK_* constants are now AddressFamily and SocketKind [IntEnum](https://docs.python.org/zh-cn/3/library/enum.html#enum.IntEnum) collections.

*3.4 新版功能.*

socket.**AF_UNIX**  
socket.**AF_INET**  
socket.**AF_INET6**  
这些常量代表地址 (和协议) 族，被用于 [socket()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket) 的第一个参数。如果 [AF_UNIX](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_UNIX) 常量没有被定义则这个协议是不被支持的。更多可能可用的常量依赖于系统。

socket.**SOCK_STREAM**  
socket.**SOCK_DGRAM**  
socket.**SOCK_RAW**  
socket.**SOCK_RDM**  
socket.**SOCK_SEQPACKET**  
这些常量代表套接字类型，被用于 [socket()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket) 的第二个参数。更多可能可用的常量依赖于系统。 (通常似乎只有 [SOCK_STREAM](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_STREAM) 和 [SOCK_DGRAM](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_DGRAM) 是有用的。)

##### 函数
**创建套接字**  
下面所有的函数都创建 [套接字对象](https://docs.python.org/zh-cn/3/library/socket.html#socket-objects)。

socket.**socket**(*family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None*)  
使用指定的地址族，套接字类型以及协议号创建一个新的套接字。地址族应为 [AF_INET](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_INET) (默认值)，[AF_INET6](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_UNIX)，[AF_UNIX](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_UNIX)，[AF_CAN](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_CAN)，[AF_PACKET](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_PACKET)，或者 [AF_RDS](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_RDS)。套接字类型应为 [SOCK_STREAM](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_STREAM) (默认值)，[SOCK_DGRAM](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_DGRAM)， [SOCK_RAW](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_RAW) 或者另一个可能的 `SOCK_` 常量。协议号通常为 0 并且可能被忽略，或者在地址族为 [AF_CAN](https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_CAN) 的情况下，协议必须为 CAN_RAW, [CAN_BCM](https://docs.python.org/zh-cn/3/library/socket.html#socket.CAN_BCM) 或 [CAN_ISOTP](https://docs.python.org/zh-cn/3/library/socket.html#socket.CAN_ISOTP) 中的一个。

如果 *fileno* 被指定了，*family*, *type*, 和 *proto* 的值将从指定的文件描述符中自动检测。 Auto-detection can be overruled by calling the function with explicit *family*, *type*, or *proto* arguments. 这只影响 Python 如何表示例如 [socket.getpeername()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.getpeername) 而不会影响实际的 OS 资源。不像 [socket.fromfd()](https://docs.python.org/zh-cn/3/library/socket.html#socket.fromfd)，*fileno* 将返回同一个套接字而不是一个副本。This may help close a detached socket using [socket.close()](https://docs.python.org/zh-cn/3/library/socket.html#socket.close)。

新创建的套接字是 [不可继承的](https://docs.python.org/zh-cn/3/library/os.html#fd-inheritance)。

`socket.__new__` 带有参数 `self`, `family`, `type`, `protocol` 将抛出一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing)。

*在 3.3 版更改:* 增加了 AF_CAN 和 AF_RDS 地址族。

*在 3.4 版更改:* 增加了 CAN_BCM 协议。

*在 3.4 版更改:* 返回的套接字现在是不可继承的。

*在 3.7 版更改:* 增加了 CAN_ISOTP 协议。

*在 3.7 版更改:* 当 [SOCK_NONBLOCK](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_NONBLOCK) 或 [SOCK_CLOEXEC](https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_CLOEXEC) 位标识被应用于 *type* 时，它们被清除了，并且 [socket.type](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.type) 将不会反映它们。它们仍然被传递给底层的系统 *socket()* 调用。因此::

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
```

将仍然在支持 `SOCK_NONBLOCK` 的操作系统上创建一个非阻塞的套接字，但 `sock.type` 将被设置为 `socket.SOCK_STREAM`。  
<br>

**其他功能**  

[socket](https://docs.python.org/zh-cn/3/library/socket.html#module-socket) 模块也提供各种网络相关的服务： 

socket.**close**(*fd*)  
关闭一个套接字文件描述符。这就像 [os.close()](https://docs.python.org/zh-cn/3/library/os.html#os.close)，但只用于套接字。在一些平台 (最值得注意的 Windows) [os.close()](https://docs.python.org/zh-cn/3/library/os.html#os.close) 对于套接字文件描述符无效。

*3.7 新版功能.*

socket.**gethostname()**  
返回一个包含当前正在执行的Python解释器所在的机器的主机名的字符串。

```python
>>> import socket
>>> socket.gethostname()
'archlinux'
```

#### 套接字对象
套接字对象拥有下面的方法。除了 [makefile()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.makefile)，这些方法对应于适用于套接字的 Unix 系统调用。

*在 3.2 版更改:* 增加了对[上下文管理器](https://docs.python.org/zh-cn/3/glossary.html#term-context-manager)协议的支持。退出上下文管理器等同于调用 [close()](https://docs.python.org/zh-cn/3/library/socket.html#socket.close)。

socket.**accept()**  
接受一个连接。套接字必须绑定到一个地址并监听连接。返回值是一对 `(conn, address)`，其中 *conn* 是一个 *新的* 套接字对象，用于在连接上发送和接收数据，而 *address* 是绑定到连接的另一端的套接字上的地址。

新创建的套接字是 [不可继承的](https://docs.python.org/zh-cn/3/library/os.html#fd-inheritance)。

*在 3.4 版更改:* 套接字现在是不可继承的。

*在 3.5 版更改:* 如果系统调用被中断且信号处理程序没有抛出一个异常，这个方法现在将重试系统调用而不是抛出一个 [InterruptedError](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常 (基本原理参见 [PEP 475](https://www.python.org/dev/peps/pep-0475)。

socket.**bind**(*address*)  
将套接字绑定到 *address*。套接字必须还没有被绑定。 (*address* 的格式依赖于地址簇 --- 参见上面。)

Raises an [auditing event](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `socket.bind` with arguments `self, address`.

socket.**close()**  
Mark the socket closed. The underlying system resource (例如：一个文件描述符) is also closed when all file objects from [makefile()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.makefile) are closed. 一旦发生这种情况，后面所有针对套接字对象的操作都将失败。远端将不会再收到数据 (当队列的数据被清除之后)。

Sockets are automatically closed when they are garbage-collected, 但是推荐明确地 [close()](https://docs.python.org/zh-cn/3/library/socket.html#socket.close) 它们，或者使用一个 [with](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 语句包围它们。

*在 3.6 版更改:* 现在，当调用底层的 close() 时，如果出现错误将抛出一个 [OSError](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError)。

**注解：** [close()](https://docs.python.org/zh-cn/3/library/socket.html#socket.close) 释放分配给一个连接的资源但不一定立即关闭这个连接。如果你想及时地关闭这个连接，在调用 [close()](https://docs.python.org/zh-cn/3/library/socket.html#socket.close) 前先调用 [shutdown()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.shutdown)。

socket.**connect**(*address*)  
按 *address* 连接到一个远程套接字。 (*address* 的格式依赖于地址族 --- 见上面。)

如果连接被一个信号中断，这个方法将等待直到连接完成，或者抛出一个超时的 [socket.timeout](https://docs.python.org/zh-cn/3/library/socket.html#socket.timeout)，如果信号处理程序没有抛出一个异常且套接字是阻塞的或者有一个超时。对于非阻塞的套接字，这个方法将抛出一个 [InterruptedError](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常如果连接被一个信号中断的话 (或者由信号处理程序抛出这个异常)。

Raises an [auditing event](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `socket.connect` with arguments `self`, `address`.

*在 3.5 版更改:* 这个方法现在将等待直到连接完成而不是抛出一个 [InterruptedError](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常如果连接被一个信号中断，信号处理程序没有抛出一个异常且套接字是阻塞的或者有一个超时 (原理请参见 [PEP 475](https://www.python.org/dev/peps/pep-0475)。

socket.**fileno()**  
返回套接字的文件描述符 (一个小的整型数)，或者 -1 如果失败的话。This is useful with [select.select()](https://docs.python.org/zh-cn/3/library/select.html#select.select).

在 Windows 下这个方法返回的小的整型数不能被用于一个文件描述符可以被使用的地方 (例如 [os.fdopen()](https://docs.python.org/zh-cn/3/library/os.html#os.fdopen))。Unix 没有这个限制。

socket.**getpeername()**  
返回套接字连接的远程地址。对于找出一个远程 IPv4/v6 套接字的端口号这是有用的，例如。 (返回的地址格式依赖于地址族 --- 见上面。) 在一些系统上这个函数是不支持的。

socket.**getsockname()**  
返回套接字自己的地址。这对于找出一个 IPv4/v6 套接字的端口号是有用的。 (返回地址的格式依赖于地址族 --- 见上面。)

socket.**getblocking()**  
如果套接字处于阻塞模式则返回 `True`，如果处于非阻塞模式则返回 `False`。

这等同于检查 `socket.gettimeout() == 0`。

*3.7 新版功能.*

socket.**listen**([*backlog*])  
启用一个服务器来接受连接。如果指定了 *backlog*，它必须至少为 0 (如果它小于 0，则它将被设置为 0)；它指定在系统拒绝新的连接以前将允许未接受的连接的个数。如果没有指定，将选择一个合理的默认值。

*在 3.5 版更改:* *backlog* 参数现在是可选的。

socket.**recv**(*bufsize*[, *flags*])  
从套接字接收数据。返回值是一个字节对象，代表收到的数据。一次接收的最大数据量由 *bufsize* 指定。可选参数 *flags* 的含义参考 Unix 手册页面 [*recv(2)*](https://manpages.debian.org/recv(2))；它默认为0。

**注解：** 为了最匹配硬件及网络现状，*bufsize* 的值应该是一个相对小的2的幂，例如，4096。

*在 3.5 版更改:* 如果系统调用被中断且信号处理程序没有抛出一个异常，这个方法现在将重试系统调用而不是抛出一个 [InterruptedError](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常 (原理参见 [PEP 475](https://www.python.org/dev/peps/pep-0475))。

socket.**send**(*bytes*[, *flags*])  
发送数据到套接字。套接字必须连接到一个远程套接字。可选参数 *flags* 的含义与上面的 [recv()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.recv) 中的含义相同。返回发送的字节数。应用程序负责检查所有数据是否已发送；如果只传输了一些数据，应用程序必须尝试递送剩余的数据。关于这个主题的详细信息，请查阅 [套接字编程指南](https://docs.python.org/zh-cn/3/howto/sockets.html#socket-howto)。

*在 3.5 版更改:* 如果系统调用被中断且信号处理程序没有抛出一个异常，这个方法现在将重试系统调用而不是抛出一个 [InterruptedError](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常 (原理参见 [PEP 475](https://www.python.org/dev/peps/pep-0475))。

socket.**shutdown**(*how*)  
Shut down one or both halves of the connection. 如果 *how* 是 SHUT_RD, 则不允许后面的接收。如果 *how* 是 SHUT_WR, 则不允许后面的发送。如果 *how* 是 SHUT_RDWR, 则后面的发送和接收都不被允许。  
<br>

注意套接字没有 read() 或者 write() 方法；使用不带 *flags* 参数的 [recv()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.recv) 和 [send()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.send) 替代。

套接字对象也有这些 (只读) 属性，它们对应于 [socket](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket) 构造函数中指定的值。

socket.**family**  
套接字族。

socket.**type**  
套接字类型。

socket.**proto**  
套接字协议。

#### 关于套接字超时的说明

一个套接字对象可以是下面三种模式中的一种：blocking，non-blocking，或者 timeout。默认情况下套接字总是按阻塞模式被创建，但这可以通过调用 [setdefaulttimeout()](https://docs.python.org/zh-cn/3/library/socket.html#socket.setdefaulttimeout) 来改变。

* 在 *阻塞模式* 下，operations block until complete or the system returns an error (例如连接超时)。

* 在 *非阻塞模式* 下，operations fail (with an error that is unfortunately system-dependent) if they cannot be completed immediately: functions from the [select](https://docs.python.org/zh-cn/3/library/select.html#module-select) can be used to know when and whether a socket is available for reading or writing.

* 在 *超时模式* 下， operations fail if they cannot be completed within the timeout specified for the socket (它们抛出一个 [超时](https://docs.python.org/zh-cn/3/library/socket.html#socket.timeout) 异常) or if the system returns an error.

**注解：** 在操作系统级别，sockets in *timeout mode* are internally set in non-blocking mode. Also, the blocking and timeout modes are shared between file descriptors and socket objects that refer to the same network endpoint. This implementation detail can have visible consequences if e.g. you decide to use the [fileno()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.fileno) of a socket.

#### 示例

注意一个服务器必须按顺序执行 [socket()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket)，[bind()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.bind)，[listen()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.listen)，[accept()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.accept) (可能需要重复 [accept()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.accept) 以服务多个客户端)，而一个客户端仅仅只需要按顺序执行 [socket()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket)，[connect()](https://docs.python.org/zh-cn/3/library/socket.html#socket.socket.connect)。 

## 互联网数据处理
### json --- JSON 编码和解码器
**源代码:** [Lib/json/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.8/Lib/json/__init__.py)

[JSON (JavaScript Object Notation)](http://json.org/)，由 [RFC 7159](https://tools.ietf.org/html/rfc7159.html) (淘汰 [RFC 4627](https://tools.ietf.org/html/rfc4627.html)) 和 [ECMA-404](http://www.ecma-international.org/publications/standards/Ecma-404.htm) 指定，是一个受 [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 对象字面量语法启发的轻量级数据交换格式（然而它不是一个严格意义上的 JavaScript 的字集 [1]）。

[1] 正如 [RFC 7159 的勘误表](https://www.rfc-editor.org/errata_search.php?rfc=7159) 中所提到的, JSON 允许文字 U+2028 (行分隔符) 和 U+2029 (段分隔符) 字符出现在字符串中，而 JavaScript (自 ECMAScript 版本 5.1 起) 不允许。

[json](https://docs.python.org/zh-cn/3.8/library/json.html#module-json) 提供了与标准库 [marshal](https://docs.python.org/zh-cn/3.8/library/marshal.html#module-marshal) 和 [pickle](https://docs.python.org/zh-cn/3.8/library/pickle.html#module-pickle) 相似的API接口。

对基本的 Python 对象层次结构进行编码：

```python
>>> import json
>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
>>> print(json.dumps("\"foo\bar"))
"\"foo\bar"
>>> print(json.dumps('\u1234'))
"\u1234"
>>> print(json.dumps('\\'))
"\\"
>>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
>>> from io import StringIO
>>> io = StringIO()
>>> json.dump(['streaming API'], io)
>>> io.getvalue()
'["streaming API"]'
```

紧凑编码：

```python
>>> import json
>>> json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'
```

美化输出：

```python
>>> import json
>>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
```

JSON解码:

```python
>>> import json
>>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
['foo', {'bar': ['baz', None, 1.0, 2]}]
>>> json.loads('"\\"foo\\bar"')
'"foo\x08ar'
>>> json.loads('"\\b"')
'\x08'
>>> from io import StringIO
>>> io = StringIO('["streaming API"]')
>>> json.load(io)
['streaming API']
```

特殊JSON对象解码:

```python
>>> import json
>>> def as_complex(dct):
...     if '__complex__' in dct:
...         return complex(dct['real'], dct['imag'])
...     return dct
...
>>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
...     object_hook=as_complex)
(1+2j)
>>> import decimal
>>> json.loads('1.1', parse_float=decimal.Decimal)
Decimal('1.1')
```

扩展 [JSONEncoder](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONEncoder):

```python
>>> import json
>>> class ComplexEncoder(json.JSONEncoder):
...     def default(self, obj):
...         if isinstance(obj, complex):
...             return [obj.real, obj.imag]
...         # Let the base class default method raise the TypeError
...         return json.JSONEncoder.default(self, obj)
...
>>> json.dumps(2 + 1j, cls=ComplexEncoder)
'[2.0, 1.0]'
>>> ComplexEncoder().encode(2 + 1j)
'[2.0, 1.0]'
>>> list(ComplexEncoder().iterencode(2 + 1j))
['[2.0', ', 1.0', ']']
```

从命令行使用 [json.tool](https://docs.python.org/zh-cn/3.8/library/json.html#module-json.tool) 来验证并美化输出：

```sh
➜  ~ echo '{"json":"obj"}' |python -m json.tool
{
    "json": "obj"
}
➜  ~ echo '{1.2:3.4}' |python -m json.tool
Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

详细文档请参见 [命令行接口](https://docs.python.org/zh-cn/3.8/library/json.html#json-commandline)。

**注解：** JSON 是 [YAML](http://yaml.org/) 1.2 的一个子集。由该模块的默认设置生成的 JSON （尤其是默认的 “分隔符” 设置值）也是 YAML 1.0 and 1.1 的一个子集。因此该模块也能够用于序列化为 YAML。

**注解：** 默认情况下这个模块的编码器和解码器保存输入和输出的顺序。仅当底层容器是无序的的时候，顺序才会丢失。

在 Python 3.7 以前， [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict) was not guaranteed to be ordered, so inputs and outputs were typically scrambled unless [collections.OrderedDict](https://docs.python.org/zh-cn/3.8/library/collections.html#collections.OrderedDict) was specifically requested. 从 Python 3.7 开始，普通的 [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict) 变成保存顺序的了，所以生成和分析 JSON 不必再指定 [collections.OrderedDict](https://docs.python.org/zh-cn/3.8/library/collections.html#collections.OrderedDict) 了。

#### 基本使用
json.**dump**(*obj, fp, \*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, \*\*kw*)  
使用这个 [转换表](https://docs.python.org/zh-cn/3.8/library/json.html#py-to-json-table) 来序列化 *obj* 为一个 JSON 格式的流并输出到 *fp* （一个支持 `.write()` 的 [类文件对象](https://docs.python.org/zh-cn/3.8/glossary.html#term-file-like-object)）。

如果 *skipkeys* 是 true （默认为 `False`），那么那些不是基本对象（包括 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str), [int](https://docs.python.org/zh-cn/3.8/library/functions.html#int)、[float](https://docs.python.org/zh-cn/3.8/library/functions.html#float)、[bool](https://docs.python.org/zh-cn/3.8/library/functions.html#bool)、`None`）的字典的键会被跳过；否则引发一个 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。

[json](https://docs.python.org/zh-cn/3.8/library/json.html#module-json) 模块始终产生 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str) 对象而非 [bytes](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#bytes) 对象。因此，`fp.write()` 必须支持 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str) 输入。

如果 *ensure_ascii* 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。如果 *ensure_ascii* 是 false，这些字符会原样输出。

如果 *check_circular* 是为假值 (默认为 `True`)，那么容器类型的循环引用检验会被跳过并且循环引用会引发一个 [OverflowError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#OverflowError) (或者更糟的情况)。

如果 *allow_nan* 是 false（默认为 `True`），那么在对严格 JSON 规格范围外的 [float](https://docs.python.org/zh-cn/3.8/library/functions.html#float) 类型值（`nan`、`inf` 和 `-inf`）进行序列化时会引发一个 [ValueError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#ValueError)。如果 *allow_nan* 是 true，则使用它们的 JavaScript 等价形式（`NaN`、`Infinity` 和 `-Infinity`）。

如果 *indent* 是一个非负整数或者字符串，那么 JSON 数组元素和对象成员会被美化输出为该值指定的缩进等级。如果缩进等级为零、负数或者 `""`，则只会添加换行符。`None`（默认值）选择最紧凑的表达。使用一个正整数会让每一层缩进同样数量的空格。如果 *indent* 是一个字符串（比如 `"\t"`），那个字符串会被用于缩进每一层。

*在 3.2 版更改:* 允许使用字符串作为 *indent* 而不再仅仅是整数。

当指定时，*separators* 应当是一个 `(item_separator, key_separator)` 元组。当 *indent* 为 `None` 时，默认值取 `(', ', ': ')`，否则取 `(',', ': ')`。为了得到最紧凑的 JSON 表达式，你应该指定其为 `(',', ':')` 以消除空白字符。

*在 3.4 版更改:* 现当 *indent* 不是 `None` 时，采用 `(',', ': ')` 作为默认值。

当 *default* 被指定时，其应该是一个函数，每当某个对象无法被序列化时它会被调用。它应该返回该对象的一个可以被 JSON 编码的版本或者引发一个 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。如果没有被指定，则会直接引发 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。

如果 *sort_keys* 是 true（默认为 `False`），那么字典的输出会以键的顺序排序。

为了使用一个自定义的 [JSONEncoder](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONEncoder) 子类（比如：覆盖了 default() 方法来序列化额外的类型）， 通过 *cls* 关键字参数来指定；否则将使用 [JSONEncoder](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONEncoder)。

*在 3.6 版更改:* 所有的可选参数现在是 [keyword-only](https://docs.python.org/zh-cn/3.8/glossary.html#keyword-only-parameter) 的了。

**注解：** 与 [pickle](https://docs.python.org/zh-cn/3.8/library/pickle.html#module-pickle) 和 [marshal](https://docs.python.org/zh-cn/3.8/library/marshal.html#module-marshal) 不同，JSON 不是一个具有框架的协议，所以尝试多次使用同一个 *fp* 调用 [dump()](https://docs.python.org/zh-cn/3.8/library/json.html#json.dump) 来序列化多个对象会产生一个不合规的 JSON 文件。

json.**dumps**(*obj, \*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, \*\*kw*)  
使用这个 [转换表](https://docs.python.org/zh-cn/3.8/library/json.html#py-to-json-table) 将 *obj* 序列化为 JSON 格式的 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str)。 其参数的含义与 [dump()](https://docs.python.org/zh-cn/3.8/library/json.html#json.dump) 中的相同。

**注解：** JSON 中的键-值对中的键永远是 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str) 类型的。当一个对象被转化为 JSON 时，字典中所有的键都会被强制转换为字符串。这所造成的结果是字典被转换为 JSON 然后转换回字典时可能和原来的不相等。换句话说，如果 x 具有非字符串的键，则有 `loads(dumps(x)) != x`。

```python
>>> x = {1: 'a', 2: 'b', 3: 'c'}
>>> json.dumps(x)
'{"1": "a", "2": "b", "3": "c"}'
>>> json.loads(json.dumps(x))
{'1': 'a', '2': 'b', '3': 'c'}
>>> json.loads(json.dumps(x)) != x
True
>>> 
```

json.**load**(*fp, \*, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \*\*kw*)  
使用这个 [转换表](https://docs.python.org/zh-cn/3.8/library/json.html#json-to-py-table) 将 *fp* (一个支持 `.read()` 并包含一个 JSON 文档的 [text file](https://docs.python.org/zh-cn/3.8/glossary.html#term-text-file) 或者 [binary file](https://docs.python.org/zh-cn/3.8/glossary.html#term-binary-file)) 反序列化为一个 Python 对象。

*object_hook* 是一个可选的函数，它会被调用于每一个解码出的对象字面量（即一个 [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict)）。*object_hook* 的返回值会取代原本的 [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict)。这一特性能够被用于实现自定义解码器（如 [JSON-RPC](http://www.jsonrpc.org/) 的类型提示)。

*object_pairs_hook* is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. *object_pairs_hook* 的返回值将被用来替换 [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict)。这一特性能够被用于实现自定义解码器。如果也定义了 *object_hook*，应优先考虑 *object_pairs_hook*。

*在 3.1 版更改:* 增加 *object_pairs_hook* 的支持。

*parse_float*, 如果指定了，will be called with the string of every JSON float to be decoded. 默认情况下，这等同于 `float(num_str)`。这可以被用于为 JSON 浮点数 (例如 [decimal.Decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html#decimal.Decimal)) 使用另一种数据类型或者解析器 。

*parse_int*, 如果指定了，will be called with the string of every JSON int to be decoded. 默认情况下，这等同于 `int(num_str)`。这可以被用于为 JSON 整型数（例如 [float](https://docs.python.org/zh-cn/3.8/library/functions.html#float)）使用另一种数据类型或者解析器。

*parse_constant*, 如果指定了，will be called with one of the following strings: `'-Infinity'`, `'Infinity'`, `'NaN'`. 如果遇到了无效的 JSON 数字，这可以被用来抛出一个异常。

*在 3.1 版更改:* *parse_constant* doesn't get called on 'null', 'true', 'false' anymore.

若要使用一个自定义的 [JSONDecoder](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecoder) 子类，请指定 `cls` 关键字参数；否则将使用 [JSONDecoder](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecoder)。额外的关键字参数将被传递给类的构造函数。

如果正在反序列化的数据不是一个有效的 JSON 文档，将抛出一个 [JSONDecodeError](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecodeError)。

*在 3.6 版更改:* 所有的可选参数现在是 [keyword-only](https://docs.python.org/zh-cn/3.8/glossary.html#keyword-only-parameter) 的了。

*在 3.6 版更改:* *fp* 现在可以是一个 [二进制文件](https://docs.python.org/zh-cn/3.8/glossary.html#term-binary-file)。输入编码必须是 UTF-8, UTF-16 或者 UTF-32.

json.**loads**(*s, \*, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \*\*kw*)  
使用这个 [转换表](https://docs.python.org/zh-cn/3.8/library/json.html#json-to-py-table) 将 *s* (一个包含一个 JSON 文档的 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str), [bytes](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#bytes) 或 [bytearray](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#bytearray) 实例) 反序列化为一个 Python 对象。

其它参数与 [load()](https://docs.python.org/zh-cn/3.8/library/json.html#json.load) 中的含义相同, 除了从 Python 3.1 起被忽略和弃用的 *encoding*。

如果正在被反序列化的数据不是一个有效的 JSON 文档，将抛出一个 [JSONDecodeError](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecodeError)。

*从版本 3.1 开始被弃用，将在版本 3.9 中被移除：* *encoding* 关键字参数。

*在 3.6 版更改:* *s* 现在可以为 [bytes](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#bytes) 或 [bytearray](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#bytearray) 类型。 输入编码应为 UTF-8, UTF-16 或 UTF-32。

#### 编码器和解码器
*class* json.**JSONDecoder**(*\*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None*)  
简单的JSON解码器。

默认情况下，解码执行以下翻译:

JSON          |Python
--------------|-------
object        |dict
array         |list
string        |str
number (int)  |int
number (real) |float
true          |True
false         |False
null          |None

它还将“NaN”、“Infinity”和“-Infinity”理解为它们对应的“float”值，这超出了JSON规范。

*object_hook*, 如果指定了，will be called with the result of every JSON object decoded and its return value will be used in place of the given [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict). 这可以被用来提供自定义反序列化 (例如：支持 JSON-RPC 类提示)。

*object_pairs_hook*, if specified will be called with the result of every JSON object decoded with an ordered list of pairs. *object_pairs_hook* 的返回值将被用来替换 [dict](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#dict). 这个特性可以被用来实现自定义解码器。如果 *object_hook* 也定义了，则优先执行 *object_pairs_hook* 。

*在 3.1 版更改:* 增加了 *object_pairs_hook* 的支持。

*parse_float*, 如果指定了，will be called with the string of every JSON float to be decoded.默认情况下，这等同于 `float(num_str)`。对于 JSON 浮点数 (例如 [decimal.Decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html#decimal.Decimal)) 来说，这可以被用于使用另一种数据类型或者解析器。

*parse_int*, 如果指定了，will be called with the string of every JSON int to be decoded. 默认情况下，这等同于 `int(num_str)`。这可以被用于为 JSON 整型数使用另一种数据类型(例如 [float](https://docs.python.org/zh-cn/3.8/library/functions.html#float))或者解析器。

*parse_constant*, 如果指定了，will be called with one of the following strings: `'-Infinity'`, `'Infinity'`, `'NaN'`. 如果遇到了无效的 JSON 数字这可以被用来抛出一个异常。

如果 *strict* 是 false (默认为 `True`), 则字符串中将允许包含控制字符。在这个上下文中控制字符是那些字符编码在 0--31 范围内的字符，包括 `'\t'` (tab), `'\n'`, `'\r'` 和 `'\0'`。

如果正在被反序列化的数据不是一个有效的 JSON 文档，将抛出一个 [JSONDecodeError](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecodeError)。

*在 3.6 版更改:* 现在所有参赛都是 [keyword-only](https://docs.python.org/zh-cn/3.8/glossary.html#keyword-only-parameter) 的了。

**decode**(*s*)  
返回 *s* 的 Python 表示形式（包含一个 JSON 文档的 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str) 实例）。

如果给定的 JSON 文档无效则将引发 [JSONDecodeError](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONDecodeError)。

**raw_decode**(*s*)  
从 *s* 中解码出 JSON 文档（以 JSON 文档开头的一个 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str) 对象）并返回一个 Python 表示形式为 2 元组以及指明该文档在 *s* 中结束位置的序号。

这可以用于从一个字符串解码JSON文档，该字符串的末尾可能有无关的数据。

*class* json.**JSONEncoder**(*\*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None*)  
用于Python数据结构的可扩展JSON编码器。

默认情况下支持下面的对象和类型：

Python                                  |JSON
----------------------------------------|--------
dict                                    |object
list, tuple                             |array
str                                     |string
int, float, int- & float-derived Enums  |number
True                                    |true
False                                   |false
None                                    |null

*在 3.4 版更改:* 增加了 int- 和 float-derived Enum 类型的支持。

To extend this to recognize other objects, subclass and implement a [default()](https://docs.python.org/zh-cn/3.8/library/json.html#json.JSONEncoder.default) method with another method that returns a serializable object for `o` if possible, otherwise it should call the superclass implementation (to raise [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)).

如果 *skipkeys* 是 false (默认值), 当试图编码的键不是 [str](https://docs.python.org/zh-cn/3.8/library/stdtypes.html#str), [int](https://docs.python.org/zh-cn/3.8/library/functions.html#int), [float](https://docs.python.org/zh-cn/3.8/library/functions.html#float) 或者 `None` 时则抛出一个 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。如果 *skipkeys* 是 true，则那些键将被简单地跳过。

如果 *ensure_ascii* 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。如果 *ensure_ascii* 是 false，这些字符会原样输出。

如果 *check_circular* 是 true (默认值), then lists, dicts, and custom encoded objects will be checked for circular references during encoding to prevent an infinite recursion (which would cause an [OverflowError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#OverflowError)). 否则，不进行这样的检查。

如果 *allow_nan* 是 true (默认值), 则 `NaN`, `Infinity`, 和 `-Infinity` will be encoded as such. This behavior is not JSON specification compliant, but is consistent with most JavaScript based encoders and decoders. 否则，编码这样的浮点数将抛出一个 [ValueError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#ValueError)。

如果 *sort_keys* 是 true (默认值: `False`), 则字典的输出将按键排序；this is useful for regression tests to ensure that JSON serializations can be compared on a day-to-day basis.

如果 *indent* 是一个非负整数或者字符串，那么 JSON 数组元素和对象成员会被美化输出为该值指定的缩进等级。如果缩进等级为零、负数或者 `""`，则只会添加换行符。`None` （默认值）选择最紧凑的表达。使用一个正整数会让每一层缩进同样数量的空格。如果 *indent* 是一个字符串（比如 `"\t"`），那个字符串会被用于缩进每一层。

*在 3.2 版更改:* 允许使用字符串作为 *indent* 而不再仅仅是整数。

当指定时，*separators* 应当是一个 `(item_separator, key_separator)` 元组。当 *indent* 为 `None` 时，默认值取 `(', ', ': ')`，否则取 `(',', ': ')`。为了得到最紧凑的 JSON 表达式，你应该指定其为 `(',', ':')` 以消除空白字符。

*在 3.4 版更改:* 现当 *indent* 不是 `None` 时，采用 `(',', ': ')` 作为默认值。

当 *default* 被指定时，其应该是一个函数，每当某个对象无法被序列化时它会被调用。它应该返回该对象的一个可以被 JSON 编码的版本或者引发一个 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。如果没有被指定，则会直接引发 [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)。

*在 3.6 版更改:* 现在所有参赛都是 [keyword-only](https://docs.python.org/zh-cn/3.8/glossary.html#keyword-only-parameter) 的了。

**default**(*o*)  
Implement this method in a subclass such that it returns a serializable object for *o*, or calls the base implementation (to raise a [TypeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html#TypeError)).

例如，为了支持任意的迭代器，你应该像这样实现 default :

```python
def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, o)
```

**encode**(*o*)  
返回一个代表一个 Python 数据结构的 JSON 字符串，*o*。例如：

```python
>>> json.JSONEncoder().encode({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'
>>>
```

**iterencode**(*o*)  
编码指定的对象，*o*, and yield each string representation as available. 例如：

```python
for chunk in json.JSONEncoder().iterencode(bigobject):
    mysocket.write(chunk)
```

## 互联网协议与支持
#### urllib.request — 打开URLs的可扩展库
**源代码：** [Lib/urllib/request.py](https://github.com/python/cpython/tree/3.7/Lib/urllib/request.py)

The [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — 基本的和摘要认证，重定向，cookies等等。

__另请参阅：__ 更高层次的HTTP客户端接口推荐 [Requests package](http://docs.python-requests.org/)。

**[urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) 模块定义了下面的函数：**

urllib.request.**urlopen**(_url, data=None,_ **[**_timeout,_ __]__\*, _cafile=None, capath=None, cadefault=False, context=None_)  
打开URL _url_，_url_ 可以是一个字符串或者一个 [Request](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) 对象。

*data* must be an object specifying additional data to be sent to the server, or `None` if no such data is needed. 详见 [Request](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) 。

This function always returns an object which can work as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) and has methods such as

* geturl() — return the URL of the resource retrieved, commonly used to determine if a redirect was followed  
* info() — 返回页面的元信息，例如头信息， in the form of an [email.message_from_string()](https://docs.python.org/3/library/email.parser.html#email.message_from_string) instance (see [Quick Reference to HTTP Headers](http://jkorpela.fi/http.html))  
* getcode() – 返回响应的HTTP状态代码。

urllib.request.**build_opener**(\[*handler, ...*\])  
返回一个 [OpenerDirector](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector) 实例，which chains the handlers in the order given. *handlers* 可以是 [BaseHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler) 的实例，或者 [BaseHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler) 的子类 (在这种情况下它必须能够不带任何参数调用构造函数)。下面这些类的实例将出现在 *handlers* 的前面，除非 *handlers* 包含它们，它们的实例或者它们的子类：[ProxyHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler) (如果检测到了代理设置), [UnknownHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.UnknownHandler), [HTTPHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPHandler), [HTTPDefaultErrorHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPDefaultErrorHandler), [HTTPRedirectHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler), [FTPHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.FTPHandler), [FileHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.FileHandler), [HTTPErrorProcessor](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor).

如果安装的Python支持SSL (例如，如果 [ssl](https://docs.python.org/3/library/ssl.html#module-ssl) 模块可以被导入), [HTTPSHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPSHandler) 也将被加入。

一个 [BaseHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler) 子类也可能改变它的 `handler_order` 属性以修改它在处理程序列表中的位置。  
<br />  

**提供下面的类：**

class urllib.request.**Request**(*url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None*)  
This class is an abstraction of a URL request.

*url* 应该是一个包含一个有效的URL的字符串。

*data* 必须是一个指定额外的数据发送给服务器的对象，或者 `None` 如果不需要这样的数据。当前只有 HTTP 请求使用 *data*。支持的对象类型包括字节，file-like 对象，以及可迭代对象。如果没有提供 `Content-Length` 或 `Transfer-Encoding` 信息头字段，[HTTPHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPHandler) 将根据 *data* 的类型设置这些信息头。发送字节对象将使用 `Content-Length`，发送文件及其它可迭代对象将使用 [RFC 7230](https://tools.ietf.org/html/rfc7230.html) 3.3.1节中定义的 `Transfer-Encoding: chunked`。

对于一个 HTTP POST 请求方法，*data* 应该是一个标准的 *application/x-www-form-urlencoded* 格式缓冲区。[urllib.parse.urlencode()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) 函数接受一个映射或2-元组序列然后返回一个这种格式的 ASCII 字符串。在作为 *data* 参数使用以前它必须被编码为字节。

*headers* 应该是一个字典， and will be treated as if [add_header()](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header) was called with each key and value as arguments. This is often used to “spoof” the `User-Agent` header value, which is used by a browser to identify itself – 一些HTTP服务器仅允许来自普通浏览器的请求而阻止来自脚本的请求。例如，Mozilla Firefox 可能标识自己为 `"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0"`, 而 [urllib](https://docs.python.org/3/library/urllib.html#module-urllib) 的默认用户代理字符串是 `"Python-urllib/3.7"` (on Python 3.6)。

如果 *data* 参数出现，一个适当的 `Content-Type` 信息头应该被包含。如果这个信息头没有提供且 *data* 不是 `None`，则 `Content-Type: application/x-www-form-urlencoded` 将作为一个默认值被添加。

最简单的Python下载代码

```python
>>> from urllib.request import urlopen
>>> print(urlopen('https://www.jianshu.com/robots.txt'))
```

`www.jianshu.com` 默认不允许Python爬虫爬取，需设置User-Agent。

**支持自定义User-Agent的Python下载代码**  
使用urllib.request模块时，最好是指定User-Agent，因为默认的User-Agent（"Python-urllib/3.7"）限制太多。

```python
>>> from urllib.request import urlopen, Request                                                                                                                                          [0/377]
>>> headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.158 Safari/537.36 Viv/2.5.1525.43'}
>>> req = Request('https://www.jianshu.com/robots.txt', headers=headers)                    
>>> print(urlopen(req).read().decode('utf-8'))
```

*class* urllib.request.**OpenerDirector**  
[OpenerDirector](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector) 类通过链接起来的 [BaseHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler)s 打开URLs。它管理处理程序链以及从错误中恢复。

*class* urllib.request.**BaseHandler**  
这是所有注册处理程序的基类——且仅处理简单的注册机制。

*class* urllib.request.**ProxyHandler**(*proxies=None*)  
使请求通过一个代理。如果给定 *proxies*，它必须是一个映射协议名称到代理URLs的字典。默认是从环境变量 `<protocol>_proxy` 中读取代理列表。如果没有设置代理环境变量，则在 Windows 环境下代理设置从注册表的Internet设置部分获取，而在 macOS 环境下代理信息从macOS系统配置框架中获取。

禁用自动检测代理可以通过传递一个空字典实现。

`no_proxy` 环境变量可以用于指定不应通过代理到达的主机；如果设置，它应该是一个逗号分隔的主机名后缀列表，可以选择附加 `:port`，例如 `cern.ch,ncsa.uiuc.edu,some.host:8080`。

**注意：** 如果设置了 `REQUEST_METHOD` 变量 `HTTP_PROXY` 将被忽略；请看关于 [getproxies()](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies) 的文档。

#### OpenerDirector对象
[OpenerDirector](https://docs.python.org/3.6/library/urllib.request.html#urllib.request.OpenerDirector) 实例拥有以下方法：

OpenerDirector.**add_handler**(*handler*)  
*handler* 必须是 [BaseHandler](https://docs.python.org/3.6/library/urllib.request.html#urllib.request.BaseHandler) 的一个实例。搜索下面的方法，并将其添加到可能的链中 (注意 HTTP errors 是一个特例)。

* protocol_open() — signal that the handler knows how to open *protocol* URLs.
* http_error_type() — signal that the handler knows how to handle HTTP errors with HTTP error code *type*.
* protocol_error() — signal that the handler knows how to handle errors from (non-`http`) protocol.
* protocol_request() — signal that the handler knows how to pre-process *protocol* requests.
* protocol_response() — signal that the handler knows how to post-process *protocol* responses.

OpenerDirector.**open**(*url, data=None*\[*, timeout*\])  
打开指定 *url* (可以是一个请求对象或者一个字符串), 可选择传递指定 *data*。Arguments, return values and exceptions raised are the same as those of [urlopen()](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) (which simply calls the [open()](https://docs.python.org/3/library/functions.html#open) method on the currently installed global [OpenerDirector](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector)). 可选参数 *timeout* 以秒为单位指定了一个超时时间用于阻断操作，如连接尝试 (如果没有指定，将使用全局的默认超时设置)。实际上超时特性只能用于 HTTP, HTTPS 和 FTP 连接)。

#### urllib.parse — 将URLs解析为组件
**源代码:** [Lib/urllib/parse.py](https://github.com/python/cpython/tree/3.7/Lib/urllib/parse.py)

这个模块定义了一个标准接口将统一资源定位符 (URL) 字符串分解为多个组件 (寻址方案，网络定位，路径等。)，将多个组件合并还原成一个 URL 字符串，以及根据一个给定的“基类URL”将一个“相对URL”转换成一个绝对URL。

##### URL解析
URL解析函数聚焦于将一个URL字符串分成多个组件，或组合URL组件为一个URL字符串。

urllib.parse.**urlparse**(*urlstring, scheme='', allow_fragments=True*)  
将一个URL解析为六个组件，返回一个6元组。这对应一个URL的常规结构：`scheme://netloc/path;parameters?query#fragment`。每一个元组元素都是一个字符串，也有可能是空的。The components are not broken up in smaller parts (例如，网络位置是一个单字符串), and % escapes are not expanded. 上面显示的分隔符不是结果的一部分，除了*路径*组件中的首部斜线，如果出现则保留。例如：

```python
>>> from urllib.parse import urlparse
>>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
>>> o
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
>>> o.scheme
'http'
>>> o.port
80
>>> o.geturl()
'http://www.cwi.nl:80/%7Eguido/Python.html'
>>>
```

根据 [RFC 1808](https://tools.ietf.org/html/rfc1808.html) 中的语法规范，只有当netloc由 '//' 正确引出时，urlparse 才能识别一个netloc。否则输入被假定是一个相对链接从而导致以一个路径组件开始。

```python
>>> from urllib.parse import urlparse
>>> urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
>>> urlparse('www.cwi.nl/%7Eguido/Python.html')
ParseResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html', params='', query='', fragment='')
>>> urlparse('help/Python.html')
ParseResult(scheme='', netloc='', path='help/Python.html', params='', query='', fragment='')
>>>
```

*scheme* 参数给定默认的寻址方案，仅用于当URL没有指定寻址方案时。它应该与 *urlstring* 是同种类型 (文本或字节), except that the default value `''` is always allowed, and is automatically converted to `b''` if appropriate.

如果 *allow_fragments* 参数是 false, 则分片标识符不被识别。相反，它们将被解析为 path, parameters 或 query 组件的一部分, 且在返回值中 `fragment` 被设置为空串。

返回值实际上是 [tuple](https://docs.python.org/3.6/library/stdtypes.html#tuple) 的一个子类的一个实例。This class has the following additional read-only convenience attributes:

Attribute   |Index  |Value                  |Value if not present
------------|-------|-----------------------|--------------------
scheme      |0      |URL scheme specifier   |*scheme* parameter
netloc      |1      |网络定位部分             |空串
path        |2      |Hierarchical path      |空串
params      |3      |最后一个路径元素的参数    |空串
query       |4      |Query 组件              |空串
fragment    |5      |分片标识符               |空串
username    |       |用户名                  |[None](https://docs.python.org/3.6/library/constants.html#None)
password    |       |密码                    |[None](https://docs.python.org/3.6/library/constants.html#None)
hostname    |       |主机名（小写字母）        |[None](https://docs.python.org/3.6/library/constants.html#None)
port        |       |数字端口号，如果存在      |[None](https://docs.python.org/3.6/library/constants.html#None)

如果在URL中指定了一个无效的端口，则读取端口属性时将抛出一个 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。关于结果对象的详细信息请看 [Structured Parse Results](https://docs.python.org/3.6/library/urllib.parse.html#urlparse-result-object) 章节。

`netloc` 属性中不匹配的方括号将抛出一个 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。

*在版本3.2中发生变化：* 增加解析IPv6 URL的功能。

*在版本3.3中发生变化：* The fragment is now parsed for all URL schemes (除非 *allow_fragment* 是 false), in accordance with [RFC 3986](https://tools.ietf.org/html/rfc3986.html). 之前，存在一个支持分片的方案的白名单。

*在版本3.6中发生变化：* 现在，超出范围的端口号抛出 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)，而不是返回 [None](https://docs.python.org/3.6/library/constants.html#None)。

urllib.parse.**urljoin**(*base, url, allow_fragments=True*)  
通过组合一个 "base URL" (*base*) 和另一个 URL (*url*) 来构造一个完整的 ("绝对的") URL。Informally, this uses components of the base URL, in particular the addressing scheme, the network location and (part of) the path, to provide missing components in the relative URL. 例如：

```python
>>> from urllib.parse import urljoin
>>> urljoin('https://docs.python.org/3.6/library/urllib.parse.html', 'urllib.error.html')
'https://docs.python.org/3.6/library/urllib.error.html'
>>>
```

The *allow_fragments* argument has the same meaning and default as for [urlparse()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlparse).

**注意：** 如果 *url* 是一个绝对 URL (即，以 `//` 或 `scheme://` 开头), 则 *url*’s 主机名和/或方案将出现在结果中。例如：

```python
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', '//www.python.org/%7Eguido')
'http://www.python.org/%7Eguido'
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'https://www.python.org/%7Eguido')
'https://www.python.org/%7Eguido'
>>>
```

If you do not want that behavior, preprocess the *url* with [urlsplit()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlsplit) and [urlunsplit()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlunsplit), removing possible *scheme* and *netloc* parts.

*在版本3.5中发生变化：* Behaviour updated to match the semantics defined in [RFC 3986](https://tools.ietf.org/html/rfc3986.html).

urllib.parse.**urldefrag**(*url*)  
如果 *url* 包含一个分片标识符，则返回一个不带分片标识符的修改后的 *url* 版本，及分片标识符作为一个单独的字符串。如果 *url* 中没有分片标识符，则返回原 *url* 及一个空串。

返回值实际上是 [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) 的一个子类的一个实例。这个类还有下面额外的方便的只读属性：

Attribute  |Index  |Value            |Value if not present
-----------|-------|-----------------|--------------------
url        | 0     |不带分片的 URL    |空串
fragment   | 1     |分片标识符        |空串

关于结果对象的详细信息请看[结构化的解析结果](https://docs.python.org/3/library/urllib.parse.html#urlparse-result-object)小节。

*在版本3.2中发生变化：* 结果是一个结构化的对象而不是一个简单的2-元组。

### urllib.error — urllib.request抛出的异常类
**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/error.py)

[urllib.error](https://docs.python.org/3.6/library/urllib.error.html#module-urllib.error) 模块为[urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request) 抛出的异常定义了异常类。异常基类是 [URLError](https://docs.python.org/3.6/library/urllib.error.html#urllib.error.URLError).

下列异常通过 [urllib.error](https://docs.python.org/3.6/library/urllib.error.html#module-urllib.error) 适当地抛出：

*exception* urllib.error.**URLError**  
当处理程序遇到一个问题时，抛出这个异常 (或者衍生的异常)。它是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的一个子类。

**reason**  
这个错误的原因。它可以是一个消息字符串或者另一个异常实例。

*在版本3.3中发生变化：* [URLError](https://docs.python.org/3.6/library/urllib.error.html#urllib.error.URLError) has been made a subclass of [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) instead of [IOError](https://docs.python.org/3.6/library/exceptions.html#IOError).

```python
>>> import urllib.error
>>> issubclass(urllib.error.ContentTooShortError, urllib.error.URLError)
True
>>> issubclass(urllib.error.HTTPError, urllib.error.URLError)
True
>>> issubclass(urllib.error.URLError, OSError)
True
```

从Python 3.3开始，[IOError](https://docs.python.org/3.6/library/exceptions.html#IOError) 是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的别名。

### urllib.robotparser — 解析robots.txt
**源代码：** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/robotparser.py)

这个模块提供一个单一的类，[RobotFileParser](https://docs.python.org/3.6/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser), 这个类回答关于一个具体的用户代理是否能在一个发布了 `robots.txt` 的网站上提取一个URL的问题。关于 `robots.txt` 文件结构的详细信息，请参考 [http://www.robotstxt.org/orig.html](http://www.robotstxt.org/orig.html).

*class* urllib.robotparser.**RobotFileParser**(*url=''*)  
This class provides methods to read, parse and answer questions about the `robots.txt` file at *url*.

**set_url**(*url*)  
设置 `robots.txt` 文件的URL

**read()**  
读取 `robots.txt` URL 并将其提供给解析器。

**can_fetch**(*useragent, url*)  
根据解析的 `robots.txt` 文件中的规则，如果 *useragent* 允许获取 *url* ，则返回 `True`，否则返回 `False`。

## Python运行时服务
### \_\_main\_\_ --- 顶层脚本环境
`'__main__'` 是顶层代码执行的作用域的名称。模块的 \_\_name\_\_ 在通过标准输入、脚本文件或是交互式命令读入的时候会等于 `'__main__'`。

模块可以通过检查自己的 \_\_name\_\_ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 `python -m` 运行时条件性地执行一些代码，而在被 import 时不会执行。

```python
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

对软件包来说，通过加入 `__main__.py` 模块可以达到同样的效果，当使用 `-m` 运行模块时，其中的代码会被执行。

当没有添加 `if __name__ == "__main__":` 代码块时：

```python
➜  test$ cat a.py
def func():
    print('This message is from function func() in a.py')


func()

➜  test$ cat b.py
import a

➜  test$ python b.py
This message is from function func() in a.py
➜  test$ 
```

当添加 `if __name__ == "__main__":` 代码块后：

```python
➜  test$ cat a.py
def func():
    print('This message is from function func() in a.py')


if __name__ == "__main__":
    func()

➜  test$ cat b.py
import a

➜  test$ python b.py
➜  test$ 
```

通过上面的例子可以看出，在 `a.py` 模块中添加 `if __name__ == "__main__":` 代码块后，在其它模块中导入 `a.py` 模块时，`if __name__ == "__main__":` 代码块内的代码不会被执行。

## Python语言参考
### 3. 数据模型
#### 3.3. 特殊方法名
##### 3.3.1. 基本自定义
object.**\_\_init\_\_**(*self*__[__, ...__]__)  
当实例被创建（通过 [\_\_new\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__new__)）之后调用，但在实例返回调用者之前。参数是传递给类构造函数表达式的那些。如果基类有一个 [\_\_init\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__init__) 方法，衍生类的 [\_\_init\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__init__) 方法，如果有的话，必须明确地调用它以确保正确地初始化实例的基类部分；例如： `super().__init__([args...])`。

因为在构造对象时 [\_\_new\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__new__) 和 [\_\_init\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__init__) 一起工作 ([\_\_new\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__new__) 创建它，[\_\_init\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__init__) 定制它)，不能通过 [\_\_init\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__init__) 返回非`None`值；这样做会导致在运行时抛出一个 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)。

```python
>>> class TestInt:
...     def __init__(self):
...         return 0
...
>>> ti = TestInt()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() should return None, not 'int'
>>> class TestString:
...     def __init__(self):
...         return "string"
...
>>> ts = TestString()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() should return None, not 'str'
>>> class Test:
...     def __init__(self):
...         return None
...
>>> t = Test()
>>> class Test:
...     def __init__(self):
...         pass
...
>>> t = Test()
>>>
```

object.**\_\_str\_\_**(*self*)  
由 [str(object)](https://docs.python.org/3/library/stdtypes.html#str) 调用，然后内置函数 [format()](https://docs.python.org/3/library/functions.html#format) 及 [print()](https://docs.python.org/3/library/functions.html#print) 计算 “通俗的” 或令人满意地可打印的代表一个对象的字符串。返回值必须是一个[字符串](https://docs.python.org/3/library/stdtypes.html#textseq)对象。

这个方法不同于 [object.\_\_repr\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__repr__)，它不期待 [\_\_str\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__str__) 返回一个有效的 Python 表达式：一个更方便或更简明的表示法可以被使用。

默认实现由内置 [object](https://docs.python.org/3/library/functions.html#object) 调用 [object.\_\_repr\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__repr__) 定义。

object.**\_\_bool\_\_**(*self*)  
调用以实现真值测试及内置操作 `bool()`；应该返回 `False` 或 `True`。当这个方法没有被定义时，[\_\_len\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__len__) 被调用，如果它被定义了，且如果它的结果是非零的，则该对象被认为是真的。如果一个类既没有定义 [\_\_len\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__len__) 也没有定义 [\_\_bool\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__bool__)，则它所有的实例都被认为是真的。

##### 3.3.7. 仿真容器类型
可以定义下面的方法用来实现容器对象。容器通常是序列 (例如列表或元组) 或映射 (像字典)，但也可以表示其它容器。第一组方法通常用于要么仿真一个序列要么仿真一个映射；不同之处在于，对一个序列而言，允许的键应该是整型数 *k* 且 `0 <= k < N` ，其中 *N* 是序列的长度，或者定义了一个元素范围的分片对象。也建议映射提供行为类似于 Python 标准字典对象的方法 keys(), values(), items(), get(), clear(), setdefault(), pop(), popitem(), copy(), 和 update()。[collections.abc](https://docs.python.org/3/library/collections.abc.html#module-collections.abc) 模块提供了一个 [MutableMapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping) 抽象基类以帮助从一个基本集合 [\_\_getitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__getitem__), [\_\_setitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__setitem__), [\_\_delitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__delitem__), 和 keys() 中创建那些方法。可变序列应该提供方法 append(), count(), index(), extend(), insert(), pop(), remove(), reverse() 和 sort(), 就像 Python 标准列表对象。最后，序列类型应该通过定义下面描述的方法 [\_\_add\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__add__), [\_\_radd\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__radd__), [\_\_iadd\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__iadd__), [\_\_mul\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__mul__), [\_\_rmul\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__rmul__) 和 [\_\_imul\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__imul__) 来实现加法 (意味着连结) 和乘法 (意味着重复)；它们不应该定义其它数字运算符。建议映射和序列都实现 [\_\_contains\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__contains__) 方法以允许有效地使用 `in` 运算符；对于映射，`in` 应该搜索映射的键；对于序列，它应该搜寻值。进一步建议映射和序列都实现 [\_\_iter\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__iter__) 方法以允许有效地迭代容器；对于映射，[\_\_iter\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__iter__) 应该和 keys() 一样；对于序列，它应该迭代值。

object.**\_\_len\_\_**(*self*)  
调用以实现内置函数 [len()](https://docs.python.org/3/library/functions.html#len)。应该返回对象的长度，一个 `>=` 0 的整型数。同样，一个没有定义 [\_\_bool\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__bool__) 方法且其 [\_\_len\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__len__) 方法返回 `0` 的对象在一个布尔上下文中被认为是假的。

**CPython实现细节：** 在CPython中，对象的长度要求至多为 [sys.maxsize](https://docs.python.org/3/library/sys.html#sys.maxsize)。如果对象的长度大于 [sys.maxsize](https://docs.python.org/3/library/sys.html#sys.maxsize) 一些特性 (如 [len()](https://docs.python.org/3/library/functions.html#len)) 可能抛出 [OverflowError](https://docs.python.org/3/library/exceptions.html#OverflowError)。为避免真值测试中抛出 [OverflowError](https://docs.python.org/3/library/exceptions.html#OverflowError)，一个对象必须定义一个 [\_\_bool\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__bool__) 方法。

object.**\_\_getitem\_\_**(*self, key*)  
调用以实现 `self[key]` 的计算。对于序列类型，可接受的键应该是整型数和分片对象。注意负索引的特殊解释 (如果类希望仿真一种序列类型) 取决于 [\_\_getitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) 方法。如果 *key* 是一种不适当的类型，可能抛出 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)；如果一个值在序列索引的集合之外 (在任何负值的特殊解释之后)，应该抛出 [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)。对于映射类型，如果 *key* 缺失 (不在容器中)，应该抛出 [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)。

**注意：** 对于非法索引，[for](https://docs.python.org/3/reference/compound_stmts.html#for) 循环期待抛出一个 [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) 以允许正确地检测序列的末尾。

object.**\_\_setitem\_\_**(*self, key, value*)  
调用以实现赋值给 `self[key]`。注意事项同 [\_\_getitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)。这应该仅为映射实现如果对象支持改变键的值，或者如果可以增加新键，或者对于序列如果元素可以被替换。对于不正确的 *key* 值应该抛出和 [\_\_getitem\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) 方法相同的异常。

## 5. 导入系统
一个 [module](https://docs.python.org/zh-cn/3/glossary.html#term-module) 内的 Python 代码通过 [importing](https://docs.python.org/zh-cn/3/glossary.html#term-importing) 操作就能够访问另一个模块内的代码。 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句是发起调用导入机制的最常用方式，但不是唯一的方式。 [importlib.import_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module) 以及内置的 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 等函数也可以被用来发起调用导入机制。

[import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句结合了两个操作；它先搜索指定名称的模块，然后将搜索结果绑定到当前作用域中的名称。 import 语句的搜索操作定义为对 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 函数的调用并带有适当的参数。 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 的返回值会被用于执行 import 语句的名称绑定操作。 请参阅 import 语句了解名称绑定操作的更多细节。

对 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 的直接调用将仅执行模块搜索以及在找到时的模块创建操作。 不过也可能产生某些副作用，例如导入父包和更新各种缓存 (包括 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules))，只有 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句会执行名称绑定操作。

当 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句被执行时，标准的内置 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 函数会被调用。 其他发起调用导入系统的机制 (例如 [importlib.import_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module)) 可能会选择绕过 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 并使用它们自己的解决方案来实现导入机制。

当一个模块首次被导入时，Python 会搜索该模块，如果找到就创建一个 module 对象 (参见 [types.ModuleType](https://docs.python.org/zh-cn/3/library/types.html#types.ModuleType)) 并初始化它。 如果指定名称的模块未找到，则会引发 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError)。 当发起调用导入机制时，Python 会实现多种策略来搜索指定名称的模块。 这些策略可以通过使用使用下文所描述的多种钩子来加以修改和扩展。

*在 3.3 版更改:* 导入系统已被更新以完全实现 [PEP 302](https://www.python.org/dev/peps/pep-0302) 中的第二阶段要求。 不会再有任何隐式的导入机制 —— 整个导入系统都通过 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 暴露出来。 此外，对原生命名空间包的支持也已被实现 (参见 [PEP 420](https://www.python.org/dev/peps/pep-0420))。

### 5.1. importlib
[importlib](https://docs.python.org/zh-cn/3/library/importlib.html#module-importlib) 模块提供了一个丰富的 API 用来与导入系统进行交互。 例如 [importlib.import_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module) 提供了相比内置的 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 更推荐、更简单的 API 用来发起调用导入机制。 更多细节请参看 [importlib](https://docs.python.org/zh-cn/3/library/importlib.html#module-importlib) 库文档。

### 5.2. 包
Python 只有一种模块对象类型，所有模块都属于该类型，无论模块是用 Python、C 还是别的语言实现。 为了帮助组织模块并提供名称层次结构，Python 还引入了 [包](https://docs.python.org/zh-cn/3/glossary.html#term-package) 的概念。

你可以把包看成是文件系统中的目录，并把模块看成是目录中的文件，但请不要对这个类似做过于字面的理解，因为包和模块不是必须来自于文件系统。 为了方便理解本文档，我们将继续使用这种目录和文件的类比。 与文件系统一样，包通过层次结构进行组织，在包之内除了一般的模块，还可以有子包。

要注意的一个重点概念是所有包都是模块，但并非所有模块都是包。 或者换句话说，包只是一种特殊的模块。 特别地，任何具有 `__path__` 属性的模块都会被当作是包。

所有模块都有自己的名字。 子包名与其父包名以点号分隔，与 Python 的标准属性访问语法一致。 例如你可能看到一个名为 [sys](https://docs.python.org/zh-cn/3/library/sys.html#module-sys) 的模块，以及一个名为 [email](https://docs.python.org/zh-cn/3/library/email.html#module-email) 的包，这个包又有一个名为 [email.mime](https://docs.python.org/zh-cn/3/library/email.mime.html#module-email.mime) 的子包和该子包中的名为 email.mime.text 的子包。

#### 5.2.1. 常规包
Python 定义了两种类型的包，[常规包](https://docs.python.org/zh-cn/3/glossary.html#term-regular-package) 和 [命名空间包](https://docs.python.org/zh-cn/3/glossary.html#term-namespace-package)。 常规包是传统的包类型，它们在 Python 3.2 及之前就已存在。 常规包通常以一个包含 `__init__.py` 文件的目录形式实现。 当一个常规包被导入时，这个 `__init__.py` 文件会隐式地被执行，它所定义的对象会被绑定到该包命名空间中的名称。`__init__.py` 文件可以包含与任何其他模块中所包含的 Python 代码相似的代码，Python 将在模块被导入时为其添加额外的属性。

例如，以下文件系统布局定义了一个最高层级的 `parent` 包和三个子包:

```
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```

导入 `parent.one` 将隐式地执行 `parent/__init__.py` 和 `parent/one/__init__.py`。 后续导入 `parent.two` 或 `parent.three` 则将分别执行 `parent/two/__init__.py` 和 `parent/three/__init__.py`。

#### 5.2.2. 命名空间包
命名空间包是由多个 [部分](https://docs.python.org/zh-cn/3/glossary.html#term-portion) 构成的，每个部分为父包增加一个子包。 各个部分可能处于文件系统的不同位置。 部分也可能处于 zip 文件中、网络上，或者 Python 在导入期间可以搜索的其他地方。 命名空间包并不一定会直接对应到文件系统中的对象；它们有可能是无实体表示的虚拟模块。

命名空间包的 `__path__` 属性不使用普通的列表。 而是使用定制的可迭代类型，如果其父包的路径 (或者最高层级包的 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)) 发生改变，这种对象会在该包内的下一次导入尝试时自动执行新的对包部分的搜索。

命名空间包没有 `parent/__init__.py` 文件。 实际上，在导入搜索期间可能找到多个 `parent` 目录，每个都由不同的部分所提供。 因此 `parent/one` 的物理位置不一定与 `parent/two` 相邻。 在这种情况下，Python 将为顶级的 `parent` 包创建一个命名空间包，无论是它本身还是它的某个子包被导入。

另请参阅 [PEP 420](https://www.python.org/dev/peps/pep-0420) 了解对命名空间包的规格描述。

### 5.3. 搜索
为了开始搜索，Python 需要被导入模块（或者包，对于当前讨论来说两者没有差别）的完整 [限定名称](https://docs.python.org/zh-cn/3/glossary.html#term-qualified-name)。 此名称可以来自 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句所带的各种参数，或者来自传给 [importlib.import_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module) 或 [\_\_import\_\_()](https://docs.python.org/zh-cn/3/library/functions.html#__import__) 函数的形参。

此名称会在导入搜索的各个阶段被使用，它也可以是指向一个子模块的带点号路径，例如 `foo.bar.baz`。 在这种情况下，Python 会先尝试导入 `foo`，然后是 `foo.bar`，最后是 `foo.bar.baz`。 如果这些导入中的任何一个失败，都会引发 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError)。

#### 5.3.1. 模块缓存
在导入搜索期间首先会被检查的地方是 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules)。 这个映射起到缓存之前导入的所有模块的作用（包括其中间路径）。 因此如果之前导入过 `foo.bar.baz`，则 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 将包含 `foo`, `foo.bar` 和 `foo.bar.baz` 条目。 每个键的值就是相应的模块对象。

在导入期间，会在 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 查找模块名称，如存在则其关联的值就是需要导入的模块，导入过程完成。 然而，如果值为 `None`，则会引发 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError)。 如果找不到指定模块名称，Python 将继续搜索该模块。

[sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 是可写的。删除键可能不会破坏关联的模块（因为其他模块可能会保留对它的引用），但它会使命名模块的缓存条目无效，导致 Python 在下次导入时重新搜索命名模块。键也可以赋值为 `None` ，强制下一次导入模块导致 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError) 。

但是要小心，因为如果你还保有对某个模块对象的引用，同时停用其在 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 中的缓存条目，然后又再次导入该名称的模块，则前后两个模块对象将 *不是* 同一个。 相反地，[importlib.reload()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.reload) 将重用 *同一个* 模块对象，并简单地通过重新运行模块的代码来重新初始化模块内容。

#### 5.3.2. 查找器和加载器
如果指定名称的模块在 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 找不到，则将发起调用 Python 的导入协议以查找和加载该模块。 此协议由两个概念性模块构成，即 [查找器](https://docs.python.org/zh-cn/3/glossary.html#term-finder) 和 [加载器](https://docs.python.org/zh-cn/3/glossary.html#term-loader)。 查找器的任务是确定是否能使用其所知的策略找到该名称的模块。 同时实现这两种接口的对象称为 [导入器](https://docs.python.org/zh-cn/3/glossary.html#term-importer) —— 它们在确定能加载所需的模块时会返回其自身。

Python 包含了多个默认查找器和导入器。 第一个知道如何定位内置模块，第二个知道如何定位冻结模块。 第三个默认查找器会在 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 中搜索模块。 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 是一个由文件系统路径或 zip 文件组成的位置列表。 它还可以扩展为搜索任意可定位资源，例如由 URL 指定的资源。

导入机制是可扩展的，因此可以加入新的查找器以扩展模块搜索的范围和作用域。

查找器并不真正加载模块。 如果它们能找到指定名称的模块，会返回一个 *模块规格说明*，这是对模块导入相关信息的封装，供后续导入机制用于在加载模块时使用。

以下各节描述了有关查找器和加载器协议的更多细节，包括你应该如何创建并注册新的此类对象来扩展导入机制。

*在 3.4 版更改:* 在之前的 Python 版本中，查找器会直接返回 [加载器](https://docs.python.org/zh-cn/3/glossary.html#term-loader)，现在它们则返回模块规格说明，其中 *包含* 加载器。 加载器仍然在导入期间被使用，但负担的任务有所减少。

#### 5.3.3. 导入钩子
导入机制被设计为可扩展；其中的基本机制是 *导入钩子*。 导入钩子有两种类型: *元钩子* 和 *导入路径钩子*。

元钩子在导入过程开始时被调用，此时任何其他导入过程尚未发生，但 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 缓存查找除外。 这允许元钩子重载 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 过程、冻结模块甚至内置模块。 元钩子的注册是通过向 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 添加新的查找器对象，具体如下所述。

导入路径钩子是作为 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) (或 `package.__path__`) 过程的一部分，在遇到它们所关联的路径项的时候被调用。 导入路径钩子的注册是通过向 [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 添加新的可调用对象，具体如下所述。

#### 5.3.4. 元路径
当指定名称的模块在 [sys.modules](https://docs.python.org/zh-cn/3/library/sys.html#sys.modules) 中找不到时，Python 会接着搜索 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path)，其中包含元路径查找器对象列表。 这些查找器按顺序被查询以确定它们是否知道如何处理该名称的模块。 元路径查找器必须实现名为 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) 的方法，该方法接受三个参数：名称、导入路径和目标模块（可选）。 元路径查找器可使用任何策略来确定它是否能处理指定名称的模块。

如果元路径查找器知道如何处理指定名称的模块，它将返回一个说明对象。 如果它不能处理该名称的模块，则会返回 `None`。 如果 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 处理过程到达列表末尾仍未返回说明对象，则将引发 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError)。 任何其他被引发异常将直接向上传播，并放弃导入过程。

元路径查找器的 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) 方法调用带有两到三个参数。 第一个是被导入模块的完整限定名称，例如 `foo.bar.baz`。 第二个参数是供模块搜索使用的路径条目。 对于最高层级模块，第二个参数为 None，但对于子模块或子包，第二个参数为父包 `__path__` 属性的值。 如果相应的 `__path__` 属性无法访问，将引发 [ModuleNotFoundError](https://docs.python.org/zh-cn/3/library/exceptions.html#ModuleNotFoundError)。 第三个参数是一个将被作为稍后加载目标的现有模块对象。 导入系统仅会在重加载期间传入一个目标模块。

对于单个导入请求可以多次遍历元路径。 例如，假设所涉及的模块都尚未被缓存，则导入 `foo.bar.baz` 将首先执行顶级的导入，在每个元路径查找器 (`mpf`) 上调用 `mpf.find_spec("foo", None, None)`。 在导入 `foo` 之后，`foo.bar` 将通过第二次遍历元路径来导入，调用 `mpf.find_spec("foo.bar", foo.__path__, None)`。 一旦 `foo.bar` 完成导入，最后一次遍历将调用 `mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)`。

有些元路径查找器只支持顶级导入。 当把 `None` 以外的对象作为第三个参数传入时，这些导入器将总是返回 `None`。

Python 的默认 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 具有三种元路径查找器，一种知道如何导入内置模块，一种知道如何导入冻结模块，还有一种知道如何导入来自 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 的模块 (即 [path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder))。

*在 3.4 版更改:* 元路径查找器的 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) 方法替代了 [find_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder.find_module)，后者现已弃用，它将继续可用但不会再做改变，导入机制仅会在查找器未实现 `find_spec()` 时尝试使用它。

#### 5.4.2. 子模块
当使用任意机制 (例如 `importlib` API, `import` 及 `import-from` 语句或者内置的 `__import__()`) 加载一个子模块时，父模块的命名空间中会添加一个对子模块对象的绑定。 例如，如果包 `spam` 有一个子模块 `foo`，则在导入 `spam.foo` 之后，`spam` 将具有一个 绑定到相应子模块的 `foo` 属性。 假如现在有如下的目录结构:

```
spam/
    __init__.py
    foo.py
    bar.py
```

并且 `spam/__init__.py` 中有如下几行内容:

```python
from .foo import Foo
from .bar import Bar
```

`foo.py` 文件中有如下内容：

```python
def Foo():
    pass
```

`bar.py` 文件中有如下内容：

```python
def Bar():
    pass
```

则执行如下代码将在 `spam` 模块中添加对 `foo` 和 `bar` 的名称绑定:

```python
>>> import spam
>>> spam.foo
<module 'spam.foo' from '/home/ywh/tmp/spam/foo.py'>
>>> spam.bar
<module 'spam.bar' from '/home/ywh/tmp/spam/bar.py'>
```

按照通常的 Python 名称绑定规则，这看起来可能会令人惊讶，但它实际上是导入系统的一个基本特性。 保持不变的一点是如果你有 `sys.modules['spam']` 和 `sys.modules['spam.foo']` (例如在上述导入之后就是如此)，则后者必须显示为前者的 `foo` 属性。

```python
>>> import sys
>>> sys.modules['spam']
<module 'spam' from '/home/ywh/tmp/spam/__init__.py'>
>>> sys.modules['spam'].foo
<module 'spam.foo' from '/home/ywh/tmp/spam/foo.py'>
>>> sys.modules['spam.foo']
<module 'spam.foo' from '/home/ywh/tmp/spam/foo.py'>
>>>
```

#### 5.4.3. 模块规格说明
导入机制在导入期间会使用有关每个模块的多种信息，特别是加载之前。 大多数信息都是所有模块通用的。 模块规格说明的目的是基于每个模块来封装这些导入相关信息。

在导入期间使用规格说明可允许状态在导入系统各组件之间传递，例如在创建模块规格说明的查找器和执行模块的加载器之间。 最重要的一点是，它允许导入机制执行加载的样板操作，在没有模块规格说明的情况下这是加载器的责任。

模块的规格说明会作为模块对象的 `__spec__` 属性对外公开。 有关模块规格的详细内容请参阅 [ModuleSpec](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.ModuleSpec)。

*3.4 新版功能.*

#### 5.4.4. 导入相关的模块属性
导入机制会在加载期间会根据模块的规格说明填充每个模块对象的这些属性，并在加载器执行模块之前完成。

**\_\_name\_\_**  
`__name__` 属性必须被设为模块的完整限定名称。 此名称被用来在导入系统中唯一地标识模块。

**\_\_package\_\_**  
模块的 `__package__` 属性必须设定。 其取值必须为一个字符串，但可以与 `__name__` 取相同的值。 当模块是包时，其 `__package__` 值应该设为其 `__name__` 值。 当模块不是包时，对于最高层级模块 `__package__` 应该设为空字符串，对于子模块则应该设为其父包名。 更多详情可参阅 [PEP 366](https://www.python.org/dev/peps/pep-0366)。

该属性取代 `__name__` 被用来为主模块计算显式相对导入，相关定义见 [PEP 366](https://www.python.org/dev/peps/pep-0366)。 预期它与 `__spec__.parent` 具有相同的值。

*在 3.6 版更改:* `__package__` 预期与 `__spec__.parent` 具有相同的值。

**\_\_spec\_\_**  
`__spec__` 属性必须设为在导入模块时要使用的模块规格说明。 对 `__spec__` 的正确设定将同时作用于 [解释器启动期间初始化的模块](https://docs.python.org/zh-cn/3/reference/toplevel_components.html#programs)。 唯一的例外是 `__main__`，其中的 `__spec__` 会 [在某些情况下设为 None](https://docs.python.org/zh-cn/3/reference/import.html#main-spec).

当 `__package__` 未定义时， `__spec__.parent` 会被用作回退项。

*3.4 新版功能.*

*在 3.6 版更改:* 当 `__package__` 未定义时，`__spec__.parent` 会被用作回退项。

**\_\_path\_\_**  
如果模块为包（不论是正规包还是命名空间包），则必须设置模块对象的 `__path__` 属性。 属性值必须为可迭代对象，但如果 `__path__` 没有进一步的用处则可以为空。 如果 `__path__` 不为空，则在迭代时它应该产生字符串。 有关 `__path__` 语义的更多细节将在 [下文](https://docs.python.org/zh-cn/3/reference/import.html#package-path-rules) 中给出。

不是包的模块不应该具有 `__path__` 属性。

查询Django包的安装路径

```python
>>> import django
>>> django.__path__
['/usr/local/lib/python3.6/dist-packages/django']
>>> 
```

**\_\_file\_\_**  
**\_\_cached\_\_**  
`__file__` 是可选项。 如果设置，此属性的值必须为字符串。 导入系统可以选择在其没有语法意义时不设置 `__file__` (例如从数据库加载的模块)。

如果设置了 `__file__`，则也可以再设置 `__cached__` 属性，后者取值为编译版本代码（例如字节码文件）所在的路径。 设置此属性不要求文件已存在；该路径可以简单地指向应该存放编译文件的位置 (参见 [PEP 3147](https://www.python.org/dev/peps/pep-3147))。

当未设置 `__file__` 时也可以设置 `__cached__`。 但是，那样的场景很不典型。 最终，加载器会使用 `__file__` 和/或 `__cached__`。 因此如果一个加载器可以从缓存加载模块但是不能从文件加载，那种非典型场景就是适当的。

#### 5.4.5. module.__path__
根据定义，如果一个模块具有 `__path__` 属性，它就是包。

包的 `__path__` 属性会在导入其子包期间被使用。 在导入机制内部，它的功能与 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 基本相同，即在导入期间提供一个模块搜索位置列表。 但是，`__path__` 通常会比 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 受到更多限制。

`__path__` 必须是由字符串组成的可迭代对象，但它也可以为空。 作用于 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 的规则同样适用于包的 `__path__`，并且 [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) (见下文) 会在遍历包的 `__path__` 时被查询。

包的 `__init__.py` 文件可以设置或更改包的 `__path__` 属性，而且这是在 [PEP 420](https://www.python.org/dev/peps/pep-0420) 之前实现命名空间包的典型方式。 随着 [PEP 420](https://www.python.org/dev/peps/pep-0420) 的引入，命名空间包不再需要提供仅包含 `__path__` 操控代码的 `__init__.py` 文件；导入机制会自动为命名空间包正确地设置 `__path__`。

#### 5.4.7. 已缓存字节码的失效
在 Python 从 `.pyc` 文件加载已缓存字节码之前，它会检查缓存是否由最新的 `.py` 源文件生成。 默认情况下，Python 通过在所写入缓存文件中保存源文件的最近修改时间戳和大小来实现这一点。 在运行时，导入系统会通过比对缓存文件中保存的元数据和源文件的元数据确定该缓存的有效性。

Python 也支持“基于哈希的”缓存文件，即保存源文件内容的哈希值而不是其元数据。 存在两种基于哈希的 `.pyc` 文件：检查型和非检查型。 对于检查型基于哈希的 `.pyc` 文件，Python 会通过求哈希源文件并将结果哈希值与缓存文件中的哈希值比对来确定缓存有效性。 如果检查型基于哈希的缓存文件被确定为失效，Python 会重新生成并写入一个新的检查型基于哈希的缓存文件。 对于非检查型 `.pyc` 文件，只要其存在 Python 就会直接认定缓存文件有效。 确定基于哈希的 `.pyc` 文件有效性的行为可通过 [--check-hash-based-pycs](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-check-hash-based-pycs) 旗标来重载。

*在 3.7 版更改:* 增加了基于哈希的 `.pyc` 文件。在此之前，Python 只支持基于时间戳来确定字节码缓存的有效性。

### 5.5. 基于路径的查找器
在之前已经提及，Python 带有几种默认的元路径查找器。 其中之一是 [path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) ([PathFinder](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.PathFinder))，它会搜索包含一个 [路径条目](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 列表的 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path)。 每个路径条目指定一个用于搜索模块的位置。

基于路径的查找器自身并不知道如何进行导入。 它只是遍历单独的路径条目，将它们各自关联到某个知道如何处理特定类型路径的路径条目查找器。

默认的路径条目查找器集合实现了在文件系统中查找模块的所有语义，可处理多种特殊文件类型例如 Python 源码 (`.py` 文件)，Python 字节码 (`.pyc` 文件) 以及共享库 (例如 `.so` 文件)。 在标准库中 [zipimport](https://docs.python.org/zh-cn/3/library/zipimport.html#module-zipimport) 模块的支持下，默认路径条目查找器还能处理所有来自 zip 文件的上述文件类型。

路径条目不必仅限于文件系统位置。 它们可以指向 URL、数据库查询或可以用字符串指定的任何其他位置。

基于路径的查找器还提供了额外的钩子和协议以便能扩展和定制可搜索路径条目的类型。 例如，如果你想要支持网络 URL 形式的路径条目，你可以编写一个实现 HTTP 语义在网络上查找模块的钩子。 这个钩子（可调用对象）应当返回一个支持下述协议的 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)，以被用来获取一个专门针对来自网络的模块的加载器。

预先的警告：本节和上节都使用了 *查找器* 这一术语，并通过 [meta path finder](https://docs.python.org/zh-cn/3/glossary.html#term-meta-path-finder) 和 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) 两个术语来明确区分它们。 这两种类型的查找器非常相似，支持相似的协议，且在导入过程中以相似的方式运作，但关键的一点是要记住它们是有微妙差异的。 特别地，元路径查找器作用于导入过程的开始，主要是启动 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 遍历。

相比之下，路径条目查找器在某种意义上说是基于路径的查找器的实现细节，实际上，如果需要从 [sys.meta_path](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 移除基于路径的查找器，并不会有任何路径条目查找器被发起调用。

#### 5.5.1. 路径条目查找器
[path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) 会负责查找和加载通过 [path entry](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 字符串来指定位置的 Python 模块和包。 多数路径条目所指定的是文件系统中的位置，但它们并不必受限于此。

作为一种元路径查找器，[path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) 实现了上文描述的 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) 协议，但是它还对外公开了一些附加钩子，可被用来定制模块如何从 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 查找和加载。

有三个变量由 [path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder), [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path), [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 和 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 所使用。 包对象的 `__path__` 属性也会被使用。 它们提供了可用于定制导入机制的额外方式。

[sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 包含一个提供模块和包搜索位置的字符串列表。 它初始化自 PYTHONPATH 环境变量以及多种其他特定安装和实现的默认设置。 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 条目可指定的名称有文件系统中的目录、zip 文件和其他可用于搜索模块的潜在“位置”（参见 [site](https://docs.python.org/zh-cn/3/library/site.html#module-site) 模块），例如 URL 或数据库查询等。 在 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 中只能出现字符串和字节串；所有其他数据类型都会被忽略。 字节串条目使用的编码由单独的 [路径条目查找器](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) 来确定。

[path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) 是一种 [meta path finder](https://docs.python.org/zh-cn/3/glossary.html#term-meta-path-finder)，因此导入机制会通过调用上文描述的基于路径的查找器的 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.PathFinder.find_spec) 方法来启动 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 搜索。 当要向 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.PathFinder.find_spec) 传入 `path` 参数时，它将是一个可遍历的字符串列表 —— 通常为用来在其内部进行导入的包的 `__path__` 属性。 如果 `path` 参数为 `None`，这表示最高层级的导入，将会使用 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)。

基于路径的查找器会迭代搜索路径中的每个条目，并且每次都查找与路径条目对应的 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) ([PathEntryFinder](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder))。 因为这种操作可能很耗费资源（例如搜索会有 *stat()* 调用的开销），基于路径的查找器会维持一个缓存来将路径条目映射到路径条目查找器。 这个缓存放于 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) (尽管如此命名，但这个缓存实际存放的是查找器对象而非仅限于 [importer](https://docs.python.org/zh-cn/3/glossary.html#term-importer) 对象)。 通过这种方式，对特定 [path entry](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 位置的 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) 的高耗费搜索只需进行一次。 用户代码可以自由地从 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 移除缓存条目，以强制基于路径的查找器再次执行路径条目搜索[3]。

[3] 在遗留代码中，有可能在 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 中找到 [imp.NullImporter](https://docs.python.org/zh-cn/3/library/imp.html#imp.NullImporter) 的实例。 建议将这些代码修改为使用 `None` 代替。 详情参见 [Porting Python code](https://docs.python.org/zh-cn/3/whatsnew/3.3.html#portingpythoncode)。

如果路径条目不存在于缓存中，基于路径的查找器会迭代 [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 中的每个可调用对象。 对此列表中的每个 [路径条目钩子](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-hook) 的调用会带有一个参数，即要搜索的路径条目。 每个可调用对象或是返回可处理路径条目的 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)，或是引发 [ImportError](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError)。 基于路径的查找器使用 [ImportError](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 来表示钩子无法找到与 [path entry](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 相对应的 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)。 该异常会被忽略并继续进行 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 的迭代。 每个钩子应该期待接收一个字符串或字节串对象；字节串对象的编码由钩子决定（例如可以是文件系统使用的编码 UTF-8 或其它编码），如果钩子无法解码参数，它应该引发 [ImportError](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError)。

如果 [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 迭代结束时没有返回 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)，则基于路径的查找器 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.PathFinder.find_spec) 方法将在 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 中存入 `None` (表示此路径条目没有对应的查找器) 并返回 `None`，表示此 [meta path finder](https://docs.python.org/zh-cn/3/glossary.html#term-meta-path-finder) 无法找到该模块。

如果 [sys.path_hooks](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 中的某个 [path entry hook](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-hook) 可调用对象的返回值 *是* 一个 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)，则以下协议会被用来向查找器请求一个模块的规格说明，并在加载该模块时被使用。

当前工作目录 -- 由一个空字符串表示 -- 的处理方式与 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 中的其他条目略有不同。 首先，如果发现当前工作目录不存在，则 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 中不会存放任何值。 其次，每个模块查找会对当前工作目录的值进行全新查找。 第三，由 [sys.path_importer_cache](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_importer_cache) 所使用并由 [importlib.machinery.PathFinder.find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.PathFinder.find_spec) 所返回的路径将是实际的当前工作目录而非空字符串。

#### 5.5.2. 路径条目查找器协议
为了支持模块和已初始化包的导入，也为了给命名空间包提供组成部分，路径条目查找器必须实现 [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) 方法。

[find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) 接受两个参数，即要导入模块的完整限定名称，以及（可选的）目标模块。 `find_spec()` 返回模块的完全填充好的规格说明。 这个规格说明总是包含“加载器”集合（但有一个例外）。

为了向导入机制提示该规格说明代表一个命名空间的 [portion](https://docs.python.org/zh-cn/3/glossary.html#term-portion)。 路径条目查找器会将规格说明中的 "loader" 设为 `None` 并将 "submodule_search_locations" 设为一个包含该部分的列表。

*在 3.4 版更改:* [find_spec()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) 替代了 [find_loader()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_loader) 和 [find_module()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_module)，后两者现在都已弃用，但会在 `find_spec()` 未定义时被使用。

较旧的路径条目查找器可能会实现这两个已弃用的方法中的一个而没有实现 `find_spec()`。 为保持向后兼容，这两个方法仍会被接受。 但是，如果在路径条目查找器上实现了 `find_spec()`，这两个遗留方法就会被忽略。

[find_loader()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder.find_loader) 接受一个参数，即被导入模块的完整限定名称。 `find_loader()` 会返回一个二元组，其中第一项为加载器，第二项为一个命名空间 [portion](https://docs.python.org/zh-cn/3/glossary.html#term-portion)。 当第一项（即加载器）为 `None` 时，这意味着路径条目查找器虽然没有指定名称模块的加载器，但它知道该路径条目为指定名称模块提供了一个命名空间部分。 这几乎总是表明一种情况，即 Python 被要求导入一个并不以文件系统中的实体形式存在的命名空间包。 当一个路径条目查找器返回的加载器为 `None` 时，该二元组返回值的第二项必须为一个序列，不过它也可以为空。

如果 `find_loader()` 所返回加载器的值不为 `None`，则该部分会被忽略，而该加载器会自基于路径的查找器返回，终止对路径条目的搜索。

为了向后兼容其他导入协议的实现，许多路径条目查找器也同样支持元路径查找器所支持的传统 `find_module()` 方法。 但是路径条目查找器 `find_module()` 方法的调用绝不会带有 `path` 参数（它们被期望记录来自对路径钩子初始调用的恰当路径信息）。

路径条目查找器的 `find_module()` 方法已弃用，因为它不允许路径条目查找器为命名空间包提供部分。 如果 `find_loader()` 和 `find_module()` 同时存在于一个路径条目查找器中，导入系统将总是调用 `find_loader()` 而不选择 `find_module()`。

### 5.7. 包相对导入
相对导入使用前缀点号。 一个前缀点号表示相对导入从当前包开始。 两个或更多前缀点号表示对当前包的上级包的相对导入，第一个点号之后的每个点号代表一级。 例如，给定以下的包布局结构:

```
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

不论是在 `subpackage1/moduleX.py` 还是 `subpackage1/__init__.py` 中，以下导入都是有效的:

```python
from .moduleY import spam
from .moduleY import spam as ham 
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo 
```

绝对导入可以使用 `import <>` 或 `from <> import <>` 语法，但相对导入只能使用第二种形式；其中的原因在于:

```python
import XXX.YYY.ZZZ
```

应当提供 `XXX.YYY.ZZZ` 作为可用表达式，但 `.moduleY` 不是一个有效的表达式。

### 5.8. 有关 \_\_main\_\_ 的特殊事项
对于 Python 的导入系统来说 [\_\_main\_\_](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 模块是一个特殊情况。 正如在 [另一节](https://docs.python.org/zh-cn/3/reference/toplevel_components.html#programs) 中所述，`__main__` 模块是在解释器启动时直接初始化的，与 [sys](https://docs.python.org/zh-cn/3/library/sys.html#module-sys) 和 [builtins](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 很类似。 但是，与那两者不同，它并不被严格归类为内置模块。 这是因为 `__main__` 被初始化的方式依赖于发起调用解释器所附带的旗标和其他选项。

#### 5.8.1. \_\_main\_\_.\_\_spec\_\_
根据 [\_\_main\_\_](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 被初始化的方式，`__main__.__spec__` 会被设置相应值或是 `None`。

当 Python 附加 [-m](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-m) 选项启动时，`__spec__` 会被设为相应模块或包的模块规格说明。 `__spec__` 也会在 `__main__` 模块作为执行某个目录，zip 文件或其它 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 条目的一部分加载时被填充。

在 [其余的情况](https://docs.python.org/zh-cn/3/using/cmdline.html#using-on-interface-options) 下 `__main__.__spec__` 会被设为 `None`，因为用于填充 [\_\_main\_\_](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 的代码不直接与可导入的模块相对应:

* 交互型提示
* [-c](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-c) 选项
* 从 stdin 运行
* 直接从源码或字节码文件运行

请注意在最后一种情况中 `__main__.__spec__` 总是为 `None`，*即使* 文件从技术上说可以作为一个模块被导入。 如果想要让 [\_\_main\_\_](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 中的元数据生效，请使用 [-m](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-m) 开关。

还要注意即使是在 `__main__` 对应于一个可导入模块且 `__main__.__spec__` 被相应地设定时，它们仍会被视为 *不同的* 模块。 这是由于以下事实：使用 `if __name__ == "__main__":` 检测来保护的代码块仅会在模块被用来填充 `__main__` 命名空间时而非普通的导入时被执行。

# Python 教程
## 5. 数据结构
### 5.1. 列表的更多特性
列表数据类型还有很多的方法。这里是列表对象方法的清单：

list.**reverse()**  
就地反转列表中的元素（原列表中元素的顺序被永久性的改变）。

```python
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L.reverse()
>>> L
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
```

## 6. 模块
如果你从Python解释器退出并再次进入，之前的定义（函数和变量）都会丢失。因此，如果你想编写一个稍长些的程序，最好使用文本编辑器为解释器准备输入并将该文件作为输入运行。这被称作编写 *脚本* 。随着程序变得越来越长，你或许会想把它拆分成几个文件，以方便维护。你亦或想在不同的程序中使用一个便捷的函数， 而不必把这个函数复制到每一个程序中去。

为支持这些，Python有一种方法可以把定义放在一个文件里，并在脚本或解释器的交互式实例中使用它们。这样的文件被称作 *模块* ；模块中的定义可以 *导入* 到其它模块或者 *主* 模块（你在顶级和计算器模式下执行的脚本中可以访问的变量集合）。

模块是一个包含Python定义和语句的文件。文件名就是模块名后跟文件后缀 `.py` 。在一个模块内部，模块名（作为一个字符串）可以通过全局变量 `__name__` 的值获得。例如，使用你最喜爱的文本编辑器在当前目录下创建一个名为 `fibo.py` 的文件， 文件中含有以下内容:

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):    # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

现在进入Python解释器，并用以下命令导入该模块:

```python
>>> import fibo
```

在当前的符号表中，这并不会直接进入到定义在 `fibo` 函数内的名称；它只是进入到模块名 `fibo` 中。你可以用模块名访问这些函数:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

如果你想经常使用某个函数，你可以把它赋值给一个局部变量:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1. 有关模块的更多信息
模块可以包含可执行的语句以及函数定义。这些语句用于初始化模块。它们仅在模块 *第一次* 在 import 语句中被导入时才执行。 【1】 (当文件被当作脚本运行时，它们也会执行。)

【1】 实际上，函数定义也是“被执行”的“语句”；模块级函数定义的执行在模块的全局符号表中输入该函数名。

每个模块都有它自己的私有符号表，该表用作模块中定义的所有函数的全局符号表。因此，模块的作者可以在模块内使用全局变量，而不必担心与用户的全局变量发生意外冲突。另一方面，如果你知道自己在做什么，则可以用跟访问模块内的函数的同样标记方法，去访问一个模块的全局变量，`modname.itemname`。

模块可以导入其它模块。习惯上但不要求把所有 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句放在模块（或脚本）的开头。被导入的模块名存放在调入模块的全局符号表中。

[import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句有一个变体，它可以把名字从一个被调模块内直接导入到现模块的符号表里。例如:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

这并不会把被调模块名引入到局部变量表里（因此在这个例子里，`fibo` 是未被定义的）。

还有一个变体甚至可以导入模块内定义的所有名称:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

这会调入所有非以下划线（`_`）开头的名称。 在多数情况下，Python程序员都不会使用这个功能，因为它在解释器中引入了一组未知的名称，而它们很可能会覆盖一些你已经定义过的东西。

注意通常情况下从一个模块或者包内调入 `*` 的做法是不太被接受的， 因为这通常会导致代码的可读性很差。不过，在交互式编译器中为了节省打字可以这么用。

如果模块名称之后带有 as，则跟在 as 之后的名称将直接绑定到所导入的模块。

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

这会和 `import fibo` 方式一样有效地调入模块， 唯一的区别是它以 `fib` 的名称存在的。

当和 [from](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#from) 一起使用时，它也可以起到类似的效果：

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

**注解：** 出于效率的考虑，每个模块在每个解释器会话中只被导入一次。因此，如果你更改了你的模块，则必须重新启动解释器， 或者，如果它只是一个要交互式地测试的模块，请使用 [importlib.reload()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.reload)，例如 `import importlib; importlib.reload(modulename)`。

#### 6.1.1. 以脚本的方式执行模块
当你用下面方式运行一个Python模块:

```sh
python fibo.py <arguments>
```

模块里的代码会被执行，就好像你导入了模块一样，但是 `__name__` 被赋值为 `"__main__"`。 这意味着通过在你的模块末尾添加这些代码:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

你既可以把这个文件当作脚本又可当作一个可调入的模块来使用， 因为那段解析命令行的代码只有在当模块是以“main”文件的方式执行的时候才会运行:

```sh
$ python fibo.py 50 
0 1 1 2 3 5 8 13 21 34
```

如果模块是被导入的，那些代码是不运行的:

```python
>>> import fibo
>>> 
```

这经常用于为模块提供一个方便的用户接口，或用于测试（以脚本的方式运行模块从而执行一些测试套件）。

#### 6.1.2. 模块搜索路径
当一个名为 spam 的模块被导入的时候，解释器首先寻找具有该名称的内置模块。如果没有找到，然后解释器从 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 变量给出的目录列表里寻找名为 `spam.py` 的文件。[sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path) 初始有这些目录地址:

* 包含输入脚本的目录（或者未指定文件时的当前目录）。
* [PYTHONPATH](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) （一个包含目录名称的列表，它和shell变量 PATH 有一样的语法）。
* 取决于安装的默认设置

**注解：** 在支持符号链接的文件系统上，包含输入脚本的目录是在追加符号链接后才计算出来的。换句话说，包含符号链接的目录并 **没有** 被添加到模块的搜索路径上。

在初始化后，Python程序可以更改 [sys.path](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)。包含正在运行脚本的文件目录被放在搜索路径的开头处， 在标准库路径之前。这意味着将加载此目录里的脚本，而不是标准库中的同名模块。 除非有意更换，否则这是错误。更多信息请参阅 [标准模块](https://docs.python.org/zh-cn/3/tutorial/modules.html#tut-standardmodules)。

#### 6.1.3. “编译过的”Python文件
为了加速模块载入，Python在 `__pycache__` 目录里缓存了每个模块的编译后版本，名称为 `module.version.pyc` ，其中名称中的版本字段对编译文件的格式进行编码； 它一般使用Python版本号。例如，在CPython版本3.3中，spam.py的编译版本将被缓存为 `__pycache__/spam.cpython-33.pyc`。此命名约定允许来自不同发行版和不同版本的Python的已编译模块共存。

Python根据编译版本检查源的修改日期，以查看它是否已过期并需要重新编译。这是一个完全自动化的过程。此外，编译的模块与平台无关，因此可以在具有不同体系结构的系统之间共享相同的库。

Python在两种情况下不会检查缓存。首先，对于从命令行直接载入的模块，它从来都是重新编译并且不存储编译结果；其次，如果没有源模块，它不会检查缓存。为了支持无源文件（仅编译）发行版本， 编译模块必须是在源目录下，并且绝对不能有源模块。

给专业人士的一些小建议:

* 你可以在Python命令中使用 [-O](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-o) 或者 [-OO](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-oo) 开关， 以减小编译后模块的大小。 `-O` 开关去除断言语句，`-OO` 开关同时去除断言语句和 \_\_doc\_\_ 字符串。由于有些程序可能依赖于这些，你应当只在清楚自己在做什么时才使用这个选项。“优化过的”模块有一个 `opt-` 标签并且通常小些。将来的发行版本或许会更改优化的效果。
* 一个从 `.pyc` 文件读出的程序并不会比它从 `.py` 读出时运行的更快，`.pyc` 文件唯一快的地方在于载入速度。
* [compileall](https://docs.python.org/zh-cn/3/library/compileall.html#module-compileall) 模块可以为一个目录下的所有模块创建.pyc文件。
* 关于这个过程，[PEP 3147](https://www.python.org/dev/peps/pep-3147) 中有更多细节，包括一个决策流程图。

### 6.2. 标准模块
Python附带了一个标准模块库，在单独的文档Python库参考（以下称为“库参考”）中进行了描述。一些模块内置于解释器中；它们提供对不属于语言核心但仍然内置的操作的访问，以提高效率或提供对系统调用等操作系统基元（primitives）的访问。这些模块的集合是一个配置选项，它也取决于底层平台。例如，[winreg](https://docs.python.org/zh-cn/3/library/winreg.html#module-winreg) 模块只在Windows操作系统上提供。一个特别值得注意的模块 [sys](https://docs.python.org/zh-cn/3/library/sys.html#module-sys)，它被内嵌到每一个Python解释器中。变量 `sys.ps1` 和 `sys.ps2` 定义用作主要和辅助提示的字符串:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C> 
```

这两个变量只有在编译器是交互模式下才被定义。

`sys.path` 变量是一个字符串列表，用于确定解释器的模块搜索路径。该变量被初始化为从环境变量 [PYTHONPATH](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) 获取的默认路径，或者如果 [PYTHONPATH](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH) 未设置，则从内置默认路径初始化。你可以使用标准列表操作对其进行修改:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

### 6.3. dir() 函数
内置函数 [dir()](https://docs.python.org/zh-cn/3/library/functions.html#dir) 用于查找模块定义的名称。 它返回一个排序过的字符串列表:

```python
>>> import fibo, sys
>>> dir(fibo)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
>>> dir(sys)
```

如果没有参数，[dir()](https://docs.python.org/zh-cn/3/library/functions.html#dir) 会列出你当前定义的名称:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo', 'sys']
```

注意：它列出所有类型的名称：变量，模块，函数，等等。

[dir()](https://docs.python.org/zh-cn/3/library/functions.html#dir) 不会列出内置函数和变量的名称。如果你想要这些，它们的定义是在标准模块 [builtins](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 中:

```python
>>> import builtins
>>> dir(builtins)
```

### 6.4. 包
包是一种通过用“带点号的模块名”来构造 Python 模块命名空间的方法。 例如，模块名 A.B 表示 `A` 包中名为 `B` 的子模块。正如模块的使用使得不同模块的作者不必担心彼此的全局变量名称一样，使用加点的模块名可以使得 NumPy 或 Pillow 等多模块软件包的作者不必担心彼此的模块名称一样。

假设你想为声音文件和声音数据的统一处理，设计一个模块集合（一个“包”）。由于存在很多不同的声音文件格式（通常由它们的扩展名来识别，例如：`.wav`， `.aiff`， `.au`），因此为了不同文件格式间的转换，你可能需要创建和维护一个不断增长的模块集合。 你可能还想对声音数据还做很多不同的处理（例如，混声，添加回声，使用均衡器功能，创造人工立体声效果）， 因此为了实现这些处理，你将另外写一个无穷尽的模块流。这是你的包的可能结构（以分层文件系统的形式表示）：

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

当导入这个包时，Python搜索 `sys.path` 里的目录，查找包的子目录。

必须要有 `__init__.py` 文件才能让 Python 将包含该文件的目录当作包。 这样可以防止具有通常名称例如 `string` 的目录在无意中隐藏稍后在模块搜索路径上出现的有效模块。 在最简单的情况下，`__init__.py` 可以只是一个空文件，但它也可以执行包的初始化代码或设置 `__all__` 变量，具体将在后文介绍。

包的用户可以从包中导入单个模块，例如:

```python
import sound.effects.echo
```

这会加载子模块 sound.effects.echo 。但引用它时必须使用它的全名。

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

导入子模块的另一种方法是

```python
from sound.effects import echo
```

这也会加载子模块 echo ，并使其在没有包前缀的情况下可用，因此可以按如下方式使用:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

另一种形式是直接导入所需的函数或变量:

```python
from sound.effects.echo import echofilter
```

同样，这也会加载子模块 echo，但这会使其函数 echofilter() 直接可用:

```python
echofilter(input, output, delay=0.7, atten=4)
```

请注意，当使用 `from package import item` 时，item可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数，类或变量。 `import` 语句首先测试是否在包中定义了item；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，则引发 [ImportError](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 异常。

相反，当使用 `import item.subitem.subsubitem` 这样的语法时，除了最后一项之外的每一项都必须是一个包；最后一项可以是模块或包，但不能是前一项中定义的类或函数或变量。

#### 6.4.1. 从包中导入 *
当用户写 `from sound.effects import *` 会发生什么？理想情况下，人们希望这会以某种方式传递给文件系统，找到包中存在哪些子模块，并将它们全部导入。这可能需要很长时间，导入子模块可能会产生不必要的副作用，这种副作用只有在显式导入子模块时才会发生。

唯一的解决方案是让包作者提供一个包的显式索引。[import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句使用下面的规范：如果一个包的 `__init__.py` 代码定义了一个名为 `__all__` 的列表，它会被视为在遇到 `from package import *` 时应该导入的模块名列表。在发布该包的新版本时，包作者可以决定是否让此列表保持更新。包作者如果认为从他们的包中导入 * 的操作没有必要被使用，也可以决定不支持此列表。例如，文件 `sound/effects/__init__.py` 可以包含以下代码:

```python
__all__ = ["echo", "surround", "reverse"]
```

这意味着 `from sound.effects import *` 将导入 sound 包的三个命名子模块。

如果没有定义 `__all__`，`from sound.effects import *` 语句 *不* 会从包 sound.effects 中导入所有子模块到当前命名空间；它只确保导入了包 sound.effects （可能运行任何在 `__init__.py` 中的初始化代码），然后导入包中定义的任何名称。这包括 `__init__.py` 定义的任何名称（以及显式加载的子模块）。它还包括由之前的 [import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句显式加载的包的任何子模块。思考下面的代码:

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

在这个例子中， echo 和 surround 模块是在执行 `from...import` 语句时导入到当前命名空间中的，因为它们定义在 sound.effects 包中。（这在定义了 `__all__` 时也有效。）

```python
>>> import sound.effects.echo
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sound']
>>> import sound.effects.surround
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sound']
>>> from sound.effects import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'echo', 'sound', 'surround']
>>> 
```

虽然某些模块被设计为在使用 `import *` 时只导出遵循某些模式的名称，但在生产代码中它仍然被认为是不好的做法。

请记住，使用 `from package import specific_submodule` 没有任何问题！ 实际上，除非导入的模块需要使用来自不同包的同名子模块，否则这是推荐的表示法。

#### 6.4.2. 子包参考
当包被构造成子包时（与示例中的 sound 包一样），你可以使用绝对导入来引用兄弟包的子模块。例如，如果模块 sound.filters.vocoder 需要在 sound.effects 包中使用 echo 模块，它可以使用 `from sound.effects import echo` 。

你还可以使用import语句的 `from module import name` 形式编写相对导入。这些导入使用前导点来指示相对导入中涉及的当前包和父包。例如，从 surround 模块，你可以使用:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

请注意，相对导入是基于当前模块的名称进行导入的。由于主模块的名称总是 `"__main__"` ，因此用作Python应用程序主模块的模块必须始终使用绝对导入。

#### 6.4.3. 多个目录中的包
包支持另一个特殊属性， [\_\_path\_\_](https://docs.python.org/zh-cn/3/reference/import.html#__path__) 。它被初始化为一个列表，其中包含在执行该文件中的代码之前保存包的文件 `__init__.py` 的目录的名称。这个变量可以修改；这样做会影响将来对包中包含的模块和子包的搜索。

虽然通常不需要此功能，但它可用于扩展程序包中的模块集。

## 9. 类
类提供了一种组合数据和功能的方法。创建一个新类意味着创建一个新 *类型* 的对象，从而允许创建一个该类型的新 *实例* 。每个类的实例可以拥有保存自己状态的属性。一个类的实例也可以有改变自己状态的（定义在类中的）方法。

和其他编程语言相比，Python 用非常少的新语法和语义将类加入到语言中。它是 C++ 和 Modula-3 中类机制的结合。Python 的类提供了面向对象编程的所有标准特性：类继承机制允许多个基类，派生类可以覆盖它基类的任何方法，一个方法可以调用基类中相同名称的的方法。对象可以包含任意数量和类型的数据。和模块一样，类也拥有 Python 天然的动态特性：它们在运行时创建，可以在创建后修改。

```sh
➜  tmp cat class.py 
class DynamicClass():
    def __init__(self):
        print("dunder init method.")

➜  tmp python class.py 
➜  tmp 
```

```sh
➜  tmp cat class.py   
class DynamicClass():
    def __init__(self):
        print("dunder init method.")


dc = DynamicClass()

➜  tmp python class.py
dunder init method.
➜  tmp 
```

在C++术语中，通常类成员（包括数据成员）是 *public* （除了见下文 [私有变量](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-private) ），所有成员函数都是 *virtual* 。与在Modula-3中一样，没有用于从其方法引用对象成员的简写：方法函数使用表示对象的显式第一个参数声明，该参数由调用隐式提供。与Smalltalk一样，类本身也是对象。这为导入和重命名提供了语义。与C++和Modula-3不同，内置类型可以用作用户扩展的基类。此外，与C++一样，大多数具有特殊语法（算术运算符，下标等）的内置运算符都可以重新定义为类实例。

(Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms. 我将使用 Modula-3 的术语，因为它的面向对象的语义比 C++ 更接近 Python，但是我认为只有很少的读者听说过它。)

### 9.1. 名称和对象
对象具有个性，多个名称（在多个作用域内）可以绑定到同一个对象。这在其他语言中称为别名。乍一看Python时通常不会理解这一点，在处理不可变的基本类型（数字，字符串，元组）时可以安全地忽略它。但是，别名对涉及可变对象，如列表，字典和大多数其他类型，的Python代码的语义可能会产生惊人的影响。这通常用于程序的好处，因为别名在某些方面表现得像指针。例如，传递一个对象很便宜，因为实现只传递一个指针；如果函数修改了作为参数传递的对象，调用者将看到更改 --- 这就不需要像 Pascal 中那样使用两个不同的参数传递机制。

### 9.2. Python 作用域和命名空间
在介绍类之前，我首先要告诉你一些Python的作用域规则。类定义对命名空间有一些巧妙的技巧，你需要知道作用域和命名空间如何工作才能完全理解正在发生的事情。顺便说一下，关于这个主题的知识对任何高级Python程序员都很有用。

让我们从一些定义开始。

*namespace* （命名空间）是一个从名字到对象的映射。 大部分命名空间当前都由 Python 字典实现，但一般情况下基本不会去关注它们（除了要面对性能问题时），而且也有可能在将来更改。 下面是几个命名空间的例子：存放内置函数的集合（包含 [abs()](https://docs.python.org/zh-cn/3/library/functions.html#abs) 这样的函数，和内建的异常等）；模块中的全局名称；函数调用中的局部名称。 从某种意义上说，对象的属性集合也是一种命名空间的形式。 关于命名空间的重要一点是，不同命名空间中的名称之间绝对没有关系；例如，两个不同的模块都可以定义一个 `maximize` 函数而不会产生混淆 --- 模块的用户必须在其前面加上模块名称。

顺便说明一下，我把任何跟在一个点号之后的名称都称为 *属性* --- 例如，在表达式 `z.real` 中，`real` 是对象 `z` 的一个属性。按严格的说法，对模块中名称的引用属于属性引用：在表达式 `modname.funcname` 中，`modname` 是一个模块对象而 `funcname` 是它的一个属性。在此情况下在模块的属性和模块中定义的全局名称之间正好存在一个直观的映射：它们共享相同的命名空间！ [1]

[1] 存在一个例外。 模块对象有一个秘密的只读属性 [\_\_dict\_\_](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__)，它返回用于实现模块命名空间的字典；[\_\_dict\_\_](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 是属性但不是全局名称。 显然，使用这个将违反命名空间实现的抽象，应当仅被用于事后调试器之类的场合。

属性可以是只读或者可写的。如果为后者，那么对属性的赋值是可行的。模块属性是可以写，你可以写出 `modname.the_answer = 42` 。可写的属性同样可以用 [del](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#del) 语句删除。例如， `del modname.the_answer` 将会从名为 `modname` 的对象中移除 the_answer 属性。

在不同时刻创建的命名空间拥有不同的生存期。包含内置名称的命名空间是在 Python 解释器启动时创建的，永远不会被删除。模块的全局命名空间在模块定义被读入时创建；通常，模块命名空间也会持续到解释器退出。被解释器的顶层调用执行的语句，从一个脚本文件读取或交互式地读取，被认为是 [\_\_main\_\_](https://docs.python.org/zh-cn/3/library/__main__.html#module-__main__) 模块调用的一部分，因此它们拥有自己的全局命名空间。（内置名称实际上也存在于一个模块中；这个模块称作 [builtins](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 。）

一个函数的本地命名空间在这个函数被调用时创建，并在函数返回或抛出一个不在函数内部处理的错误时被删除。（事实上，比起描述到底发生了什么，忘掉它更好。）当然，每次递归调用都会有它自己的本地命名空间。

一个 *作用域* 是一个命名空间可直接访问的 Python 程序的文本区域。 这里的 “可直接访问” 意味着对名称的非限定引用会尝试在命名空间中查找名称。

Although scopes are determined statically, they are used dynamically. 在执行期间的任意时刻，至少有 3 个嵌套的范围的命名空间可以被直接访问：

* 最先搜索的最内部作用域包含局部名称
* 从最近的封闭作用域开始搜索的任何封闭函数的范围包含非局部名称，也包括非全局名称
* 倒数第二个作用域包含当前模块的全局名称
* 最外面的范围（最后搜索）是包含内置名称的命名空间

如果一个名称被声明为全局变量，则所有引用和赋值将直接指向包含该模块的全局名称的中间作用域。 要重新绑定在最内层作用域以外找到的变量，可以使用 [nonlocal](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句声明为非本地变量。 如果没有被声明为非本地变量，这些变量将是只读的（尝试写入这样的变量只会在最内层作用域中创建一个 *新的* 局部变量，而同名的外部变量保持不变）。

通常，当前局部作用域将（按字面文本）引用当前函数的局部名称。 在函数以外，局部作用域将引用与全局作用域相一致的命名空间：模块的命名空间。 类定义将在局部命名空间内再放置另一个命名空间。

重要的是应该意识到作用域是按字面文本来确定的：在一个模块内定义的函数的全局作用域就是该模块的命名空间，无论该函数从什么地方或以什么别名被调用。 另一方面，实际的名称搜索是在运行时动态完成的 --- 但是，语言定义在 *编译时* 是朝着静态名称解析的方向演化的，因此不要过于依赖动态名称解析！ （事实上，局部变量已经是被静态确定了。）

Python 的一个特殊之处在于 -- 如果不存在生效的 [global](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句 -- 对名称的赋值总是进入最内层作用域。 赋值不会复制数据 --- 它们只是将名称绑定到对象。 删除也是如此：语句 `del x` 会从局部命名空间的引用中移除对 x 的绑定。 事实上，所有引入新名称的操作都使用局部作用域：特别地，[import](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句和函数定义会在局部作用域中绑定模块或函数名称。

[global](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；[nonlocal](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。

#### 9.2.1. 作用域和命名空间示例
这是一个演示如何引用不同的作用域和命名空间，以及 [global](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 和 [nonlocal](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 如何影响变量的绑定的例子：

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
```

示例代码的输出是：

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

请注意 *局部* 赋值（这是默认状态）不会改变 *scope_test* 对 *spam* 的绑定。 [nonlocal](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 赋值会改变 *scope_test* 对 *spam* 的绑定，而 [global](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 赋值会改变模块层级的绑定。

您还可以在 [global](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 赋值之前看到之前没有 *spam* 的绑定。

scope.py

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
```

运行结果：

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
Traceback (most recent call last):
  File "scopes.py", line 23, in <module>
    print("In global scope:", spam)
NameError: name 'spam' is not defined
```

### 9.3. 初探类
类引入了一些新语法，三种新对象类型和一些新语义。

#### 9.3.1. 类定义语法
最简单的类定义看起来像这样:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

类定义与函数定义 ([def](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 语句) 一样必须被执行才会起作用。 （你可以尝试将类定义放在 [if](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 语句的一个分支或是函数的内部。）

在实践中，类定义内的语句通常都是函数定义，但也允许有其他语句，有时还很有用 --- 我们会稍后再回来说明这个问题。 在类内部的函数定义通常具有一种特别形式的参数列表，这是方法调用的约定规范所指明的 --- 这个问题也将在稍后再说明。

当进入类定义时，将创建一个新的命名空间，并将其用作局部作用域 --- 因此，所有对局部变量的赋值都是在这个新命名空间之内。 特别的，函数定义会绑定到这里的新函数名称。

当（从结尾处）正常离开类定义时，将创建一个 *类对象*。 这基本上是一个包围在类定义所创建命名空间内容周围的包装器；我们将在下一节了解有关类对象的更多信息。 原始的（在进入类定义之前起作用的）局部作用域将重新生效，类对象将在这里被绑定到类定义头所给出的类名称 (在这个示例中为 ClassName)。

#### 9.3.2. 类对象
类对象支持两种操作：属性引用和实例化。

*属性引用* 使用 Python 中所有属性引用所使用的标准语法: `obj.name`。 有效的属性名称是类对象被创建时存在于类命名空间中的所有名称。 因此，如果类定义是这样的:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

那么 `MyClass.i` 和 `MyClass.f` 就是有效的属性引用，将分别返回一个整数和一个函数对象。 类属性也可以被赋值，因此可以通过赋值来更改 `MyClass.i` 的值。 \_\_doc\_\_ 也是一个有效的属性，将返回所属类的文档字符串: `"A simple example class"`。

类的 *实例化* 使用函数表示法。 可以把类对象视为是返回该类的一个新实例的不带参数的函数。 举例来说（假设使用上述的类）:

```python
x = MyClass()
```

创建类的新 *实例* 并将此对象分配给局部变量 `x`。

实例化操作（“调用”类对象）会创建一个空对象。 许多类喜欢创建带有特定初始状态的自定义实例。 为此类定义可能包含一个名为 [\_\_init\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 的特殊方法，就像这样:

```python
def __init__(self):
    self.data = []
```

当一个类定义了 [\_\_init\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 方法时，类的实例化操作会自动为新创建的类实例发起调用 [\_\_init\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__)。 因此在这个示例中，可以通过以下语句获得一个经初始化的新实例:

```python
x = MyClass()
```

当然，[\_\_init\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 方法还可以有额外参数以实现更高灵活性。 在这种情况下，提供给类实例化运算符的参数将被传递给 [\_\_init\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__)。 例如，:

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
... 
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
>>>
```

#### 9.3.3. 实例对象
现在我们可以用实例对象做什么？实例对象理解的唯一操作是属性引用。有两种有效的属性名称，数据属性和方法。

*数据属性* 对应于 Smalltalk 中的“实例变量”，以及 C++ 中的“数据成员”。 数据属性不需要声明；像局部变量一样，它们将在第一次被赋值时产生。 例如，如果 `x` 是上面创建的 MyClass 的实例，则以下代码段将打印数值 `16`，且不保留任何追踪信息:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

另一类实例属性引用称为 *方法*。 方法是“从属于”对象的函数。 （在 Python 中，方法这个术语并不是类实例所特有的：其他对象也可以有方法。 例如，列表对象具有 append, insert, remove, sort 等方法。 然而，在以下讨论中，我们使用方法一词将专指类实例对象的方法，除非另外显式地说明。）

实例对象的有效方法名称依赖于其所属的类。 根据定义，一个类中所有是函数对象的属性都是定义了其实例的相应方法。 因此在我们的示例中，`x.f` 是有效的方法引用，因为 `MyClass.f` 是一个函数，而 `x.i` 不是方法，因为 `MyClass.i` 不是一个函数。 但是 `x.f` 与 `MyClass.f` 并不是一回事 --- 它是一个 *方法对象*，不是函数对象。

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
    
x = MyClass()
print(type(MyClass.f))
print(type(x.f))
```

以上代码的输出为：

```
<class 'function'>
<class 'method'>
```

#### 9.3.4. 方法对象
通常，方法在绑定后立即被调用:

```python
x.f()
```

在 MyClass 示例中，这将返回字符串 `'hello world'`。 但是，立即调用一个方法并不是必须的: `x.f` 是一个方法对象，它可以被保存起来以后再调用。 例如:

```python
xf = x.f
while True:
    print(xf())
```

将继续打印 `hello world`，直到结束。

当一个方法被调用时到底发生了什么？ 你可能已经注意到上面调用 `x.f()` 时并没有带参数，虽然 f() 的函数定义指定了一个参数。 这个参数发生了什么事？ 当不带参数地调用一个需要参数的函数时 Python 肯定会引发异常 --- 即使参数实际未被使用...

实际上，你可能已经猜到了答案：方法的特殊之处就在于实例对象会作为函数的第一个参数被传入。 在我们的示例中，调用 `x.f()` 其实就相当于 `MyClass.f(x)`。 总之，调用一个具有 *n* 个参数的方法就相当于调用再多一个参数的对应函数，这个参数值为方法所属实例对象，位置在其他参数之前。

如果你仍然无法理解方法的运作原理，那么查看实现细节可能会澄清问题。 当一个实例的非数据属性被引用时，将搜索实例所属的类。 如果被引用的属性名称表示一个有效的类属性中的函数对象，会通过打包（指向）查找到的实例对象和函数对象到一个抽象对象的方式来创建方法对象：这个抽象对象就是方法对象。 当附带参数列表调用方法对象时，将基于实例对象和参数列表构建一个新的参数列表，并使用这个新参数列表调用相应的函数对象。

```python
>>> x.f()
'hello world'
>>> MyClass.f(x)
'hello world'
>>>
```

#### 9.3.5. 类和实例变量
一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

正如 [名称和对象](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-object) 中已讨论过的，共享数据可能在涉及 [mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable) 对象例如列表和字典的时候导致令人惊讶的结果。 例如以下代码中的 *tricks* 列表不应该被用作类变量，因为所有的 *Dog* 实例将只共享一个单独的列表:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

正确的类设计应该使用实例变量:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

### 9.4. 补充说明
如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:

```python
>>> class Warehouse:
...     purpose = 'storage'
...     region = 'west'
... 
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
>>>
```

数据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。 换句话说，类不能用于实现纯抽象数据类型。 实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。 （而在另一方面，用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；此特性可以通过用 C 编写 Python 扩展来使用。）

客户端应当谨慎地使用数据属性 --- 客户端可能通过直接操作数据属性的方式破坏由方法所维护的固定变量。 请注意客户端可以向一个实例对象添加他们自己的数据属性而不会影响方法的可用性，只要保证避免名称冲突 --- 再次提醒，在此使用命名约定可以省去许多令人头痛的麻烦。

在方法内部引用数据属性（或其他方法！）并没有简便方式。 我发现这实际上提升了方法的可读性：当浏览一个方法代码时，不会存在混淆局部变量和实例变量的机会。

方法的第一个参数常常被命名为 `self`。 这也不过就是一个约定: `self` 这一名称在 Python 中绝对没有特殊含义。 但是要注意，不遵循此约定会使得你的代码对其他 Python 程序员来说缺乏可读性，而且也可以想像一个 *类浏览器* 程序的编写可能会依赖于这样的约定。

任何一个作为类属性的函数都为该类的实例定义了一个相应方法。 函数定义的文本并非必须包含于类定义之内：将一个函数对象赋值给一个局部变量也是可以的。 例如:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

现在 `f`, `g` 和 `h` 都是 C 类的引用函数对象的属性，因而它们就都是 C 的实例的方法 --- 其中 `h` 完全等同于 `g`。 但请注意，本示例的做法通常只会令程序的阅读者感到迷惑。

```python
>>> c1 = C()
>>> c1.f(1, 3)
1
>>> c1.f(1, -3)
-2
>>> dir(C)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'f', 'g', 'h']
>>> hasattr(C, 'f')
True
>>> hasattr(C, 'f1')
False
>>>
```

方法可以通过使用 `self` 参数的方法属性调用其他方法:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

方法可以通过与普通函数相同的方式引用全局名称。 与方法相关联的全局作用域就是包含其定义的模块。 （类永远不会被作为全局作用域。） 虽然我们很少会有充分的理由在方法中使用全局作用域，但全局作用域存在许多合法的使用场景：举个例子，导入到全局作用域的函数和模块可以被方法所使用，在其中定义的函数和类也一样。 通常，包含该方法的类本身是在全局作用域中定义的，而在下一节中我们将会发现为何方法需要引用其所属类的很好的理由。

每个值都是一个对象，因此具有 *类* （也称为 *类型*），并存储为 `object.__class__` 。

### 9.5. 继承
当然，如果不支持继承，语言特性就不值得称为“类”。派生类定义的语法如下所示:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

名称 BaseClassName 必须定义于包含派生类定义的作用域中。 也允许用其他任意表达式代替基类名称所在的位置。 这有时也可能会用得上，例如，当基类定义在另一个模块中的时候:

```python
class DerivedClassName(modname.BaseClassName):
```

派生类定义的执行过程与基类相同。 当构造类对象时，基类会被记住。 此信息将被用来解析属性引用：如果请求的属性在类中找不到，搜索将转往基类中进行查找。 如果基类本身也派生自其他某个类，则此规则将被递归地应用。

派生类的实例化没有任何特殊之处: `DerivedClassName()` 会创建该类的一个新实例。 方法引用将按以下方式解析：搜索相应的类属性，如有必要将按基类继承链逐步向下查找，如果产生了一个函数对象则方法引用就生效。

派生类可能会重载其基类的方法。 因为方法在调用同一对象的其他方法时没有特殊权限，调用同一基类中定义的另一方法的基类方法最终可能会调用覆盖它的派生类的方法。 （对 C++ 程序员的提示：Python 中所有的方法实际上都是 `virtual` 方法。）

在派生类中的重载方法实际上可能想要扩展而非简单地替换同名的基类方法。 有一种方式可以简单地直接调用基类方法：即调用 `BaseClassName.methodname(self, arguments)`。 有时这对客户端来说也是有用的。 （请注意仅当此基类可在全局作用域中以 `BaseClassName` 的名称被访问时方可使用此方式。）

Python有两个内置函数可被用于继承机制：

* 使用 [isinstance()](https://docs.python.org/zh-cn/3/library/functions.html#isinstance) 来检查一个实例的类型: `isinstance(obj, int)` 仅会在 `obj.__class__` 为 [int](https://docs.python.org/zh-cn/3/library/functions.html#int) 或某个派生自 [int](https://docs.python.org/zh-cn/3/library/functions.html#int) 的类时为 `True`。

* 使用 [issubclass()](https://docs.python.org/zh-cn/3/library/functions.html#issubclass) 来检查类的继承关系: `issubclass(bool, int)` 为 `True`，因为 [bool](https://docs.python.org/zh-cn/3/library/functions.html#bool) 是 [int](https://docs.python.org/zh-cn/3/library/functions.html#int) 的子类。 但是，`issubclass(float, int)` 为 `False`，因为 [float](https://docs.python.org/zh-cn/3/library/functions.html#float) 不是 [int](https://docs.python.org/zh-cn/3/library/functions.html#int) 的子类。

#### 9.5.1. 多重继承
Python 也支持一种多重继承的形式。一个有多个基类的类定义看起来像这样：

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 因此，如果某一属性在 DerivedClassName 中未找到，则会到 Base1 中搜索它，然后（递归地）到 Base1 的基类中搜索，如果在那里未找到，再到 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 [super()](https://docs.python.org/zh-cn/3/library/functions.html#super) 的协同调用。 这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

动态改变顺序是有必要的，因为所有多重继承的情况都会显示出一个或更多的菱形关联（即至少有一个父类可通过多条路径被最底层类所访问）。 例如，所有类都是继承自 [object](https://docs.python.org/zh-cn/3/library/functions.html#object)，因此任何多重继承的情况都提供了一条以上的路径可以通向 [object](https://docs.python.org/zh-cn/3/library/functions.html#object)。 为了确保基类不会被访问一次以上，动态算法会用一种特殊方式将搜索顺序线性化， 保留每个类所指定的从左至右的顺序，只调用每个父类一次，并且保持单调（即一个类可以被子类化而不影响其父类的优先顺序）。 总而言之，这些特性使得设计具有多重继承的可靠且可扩展的类成为可能。 要了解更多细节，请参阅 [https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/)。

### 9.6. 私有变量
那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 `_spam`) 应该被当作是 API 的非公开部分 (无论它是函数、方法或是数据成员)。 这应当被视为一个实现细节，可能不经通知即加以改变。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 *名称改写*。 任何形式为 `__spam` 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 `_classname__spam`，其中 `classname` 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用。例如:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

```python
>>> a = [1, 2, 3]
>>> dir(Mapping)
['_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '
__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'update']
>>> dir(MappingSubclass)
['_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '
__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'update']
>>> ms = MappingSubclass(a)
>>> dir(ms)
['_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '
__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'items_list', 'update
']
>>> ms.items_list
[1, 2, 3]
>>> b = [4, 5, 6]
>>> ms._Mapping__update(b)
>>> ms.items_list
[1, 2, 3, 4, 5, 6]
>>>
```

上面的示例即使在 `MappingSubclass` 引入了一个 `__update` 标识符的情况下也不会出错，因为它会在 `Mapping` 类中被替换为 `_Mapping__update` 而在 `MappingSubclass` 类中被替换为 `_MappingSubclass__update`。

请注意，改写规则的设计主要是为了避免意外冲突；访问或修改被视为私有的变量仍然是可能的。这在特殊情况下甚至会很有用，例如在调试器中。

请注意传递给 `exec()` 或 `eval()` 的代码不会将发起调用类的类名视作当前类；这类似于 `global` 语句的效果，因此这种效果仅限于同时经过字节码编译的代码。 同样的限制也适用于 `getattr()`, `setattr()` 和 `delattr()`，以及对于 `__dict__` 的直接引用。

### 9.7. 杂项说明
有时会需要使用类似于 Pascal 的“record”或 C 的“struct”这样的数据类型，将一些命名数据项捆绑在一起。 这种情况适合定义一个空类:

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

一段需要特定抽象数据类型的 Python 代码往往可以被传入一个模拟了该数据类型的方法的类作为替代。 例如，如果你有一个基于文件对象来格式化某些数据的函数，你可以定义一个带有 read() 和 readline() 方法从字符串缓存获取数据的类，并将其作为参数传入。

实例方法对象也具有属性: `m.__self__` 就是带有 m() 方法的实例对象，而 `m.__func__` 则是该方法所对应的函数对象。

### 9.8. 迭代器
到目前为止，您可能已经注意到大多数容器对象都可以使用 [for](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种访问风格清晰、简洁又方便。 迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 在幕后，[for](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句会调用容器对象中的 [iter()](https://docs.python.org/zh-cn/3/library/functions.html#iter)。 该函数返回一个定义了 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的迭代器对象，该方法将逐一访问容器中的元素。 当元素用尽时，[\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 将引发 [StopIteration](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常来通知终止 for 循环。 你可以使用 [next()](https://docs.python.org/zh-cn/3/library/functions.html#next) 内置函数来调用 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法；这个例子显示了它的运作方式:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x7f9aa02d5150>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

看过迭代器协议的幕后机制，给你的类添加迭代器行为就很容易了。 定义一个 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法来返回一个带有 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的对象。 如果类已定义了 \_\_next\_\_()，则 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 可以简单地返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

### 9.9. 生成器
[Generator](https://docs.python.org/zh-cn/3/glossary.html#term-generator) 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似标准的函数，但当它们要返回数据时会使用 [yield](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 语句。 每次对生成器调用 [next()](https://docs.python.org/zh-cn/3/library/functions.html#next) 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）。 显示如何非常容易地创建生成器的示例如下:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

可以用生成器来完成的操作同样可以用前一节所描述的基于类的迭代器来完成。 但生成器的写法更为紧凑，因为它会自动创建 [\_\_iter\_\_()](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 和 [\_\_next\_\_()](https://docs.python.org/zh-cn/3/reference/expressions.html#generator.__next__) 方法。

另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数相比使用 `self.index` 和 `self.data` 这种实例变量的方式更易编写且更为清晰。

除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 [StopIteration](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration)。 这些特性结合在一起，使得创建迭代器能与编写常规函数一样容易。

### 9.10. 生成器表达式
某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。 这种表达式被设计用于生成器将立即被外层函数所使用的情况。 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存。

例如:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

# Python安装和使用
## 1. 命令行与环境
CPython 解析器会扫描命令行与环境用于获取各种设置信息。

**CPython implementation detail:** 其他实现的命令行方案可能有所不同。 更多相关资源请参阅 [其他实现](https://docs.python.org/zh-cn/3.7/reference/introduction.html#implementations)。

### 1.1. 命令行
对 Python 发起调用时，你可以指定以下的任意选项:

`
python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
`

当然最常见的用例就是简单地启动执行一个脚本:

`
python myscript.py
`

#### 1.1.1. 接口选项
解释器接口类似于 UNIX shell，但提供了一些额外的发起调用方法:

* 当调用时附带连接到某个 tty 设备的标准输入时，它会提示输入命令并执行它们，直到读入一个 EOF（文件结束字符，其产生方式是在 UNIX 中按 Ctrl-D 或在 Windows 中按 Ctrl-Z, Enter。）
* 当调用时附带一个文件名参数或以一个文件作为标准输入时，它会从该文件读取并执行脚本程序。
* 当调用时附带一个目录名参数时，它会从该目录读取并执行具有适当名称的脚本程序。
* 当调用时附带 `-c command` 时，它会执行 *command* 所给出的 Python 语句。 在这里 *command* 可以包含以换行符分隔的多条语句。 请注意前导空格在 Python 语句中是有重要作用的！
* 当调用时附带 `-m module-name` 时，会在 Python 模块路径中查找指定的模块，并将其作为脚本程序执行。

在非交互模式下，会对全部输入先解析再执行。

一个接口选项会终结解释器所读入的选项列表，后续的所有参数将被放入 [sys.argv](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.argv) -- 请注意其中首个元素即第零项 (`sys.argv[0]`) 会是一个表示程序源的字符串。

**-m** <module-name>  
在 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 中搜索指定名称的模块并将其内容作为 [\_\_main\_\_](https://docs.python.org/zh-cn/3.7/library/__main__.html#module-__main__) 模块来执行。

由于该参数为 *module* 名称，你不应给出文件扩展名 (`.py`)。 模块名称应为绝对有效的 Python 模块名称，但具体实现可能并不总是强制要求这一点（例如它可能允许你使用包含连字符的名称）。

包名称（包括命名空间包）也允许使用。 当所提供的是包名称而非普通模块名称时，解释器将把 `<pkg>.__main__` 作为主模块来执行。 此行为特意被设计为与作为脚本参数传递给解释器的目录和 zip 文件的处理方式类似。

**注解：** 此选项不适用于内置模块和以 C 编写的扩展模块，因为它们并没有对应的 Python 模块文件。 但是它仍然适用于预编译的模块，即使没有可用的初始源文件。

如果给出此选项，[sys.argv](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.argv) 的首个元素将为模块文件的完整路径 (在定位模块文件期间，首个元素将设为 `"-m"`)。 与 [-c](https://docs.python.org/zh-cn/3.7/using/cmdline.html#cmdoption-c) 选项一样，当前目录将被加入 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 的开头。

[-I](https://docs.python.org/zh-cn/3.7/using/cmdline.html#id2) 选项可用来在隔离模式下运行脚本，此模式中 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 既不包含当前目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。

**参见：**  
[PEP 338](https://www.python.org/dev/peps/pep-0338) -- 将模块作为脚本执行

*在 3.1 版更改:* 提供包名称来运行 `__main__` 子模块。

*在 3.4 版更改:* 同样支持命名空间包  
<br />

**-**  
从标准输入 ([sys.stdin](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.stdin)) 读取命令。 如果标准输入为一个终端，则使用 [-i](https://docs.python.org/zh-cn/3.7/using/cmdline.html#cmdoption-i)。

如果给出此选项，[sys.argv](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.argv) 的首个元素将为 `"-"` 并且当前目录将被加入 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 的开头。  
<br />

<**script**>  
执行 *script* 中的 Python 代码，该参数应为一个（绝对或相对）文件系统路径，指向某个 Python 文件、包含 `__main__.py` 文件的目录，或包含 `__main__.py` 文件的 zip 文件。

如果给出此选项，[sys.argv](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.argv) 的首个元素将为在命令行中指定的脚本名称。

如果脚本名称直接指向一个 Python 文件，则包含该文件的目录将被加入 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 的开头，并且该文件会被作为 [\_\_main\_\_](https://docs.python.org/zh-cn/3.7/library/__main__.html#module-__main__) 模块来执行。

如果脚本名称指向一个目录或 zip 文件，则脚本名称将被加入 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 的开头，并且该位置中的 `__main__.py` 文件会被作为 [\_\_main\_\_](https://docs.python.org/zh-cn/3.7/library/__main__.html#module-__main__) 模块来执行。

[-I](https://docs.python.org/zh-cn/3.7/using/cmdline.html#id2) 选项可用来在隔离模式下运行脚本，此模式中 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 既不包含脚本所在目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。  
<br />

如果没有给出接口选项，则使用 [-i](https://docs.python.org/zh-cn/3.7/using/cmdline.html#cmdoption-i)，`sys.argv[0]` 将为空字符串 (`""`)，并且当前目录会被加入 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 的开头。 此外，tab 补全和历史编辑会自动启用，如果你的系统平台支持此功能的话 (参见 [Readline configuration](https://docs.python.org/zh-cn/3.7/library/site.html#rlcompleter-config))。

**参见：** [调用解释器](https://docs.python.org/zh-cn/3.7/tutorial/interpreter.html#tut-invoking)

*在 3.4 版更改:* 自动启用 tab 补全和历史编辑。

#### 1.1.2. 通用选项
**-?**  
**-h**  
**--help**  
打印全部命令行选项的简短描述。

-V
--version
打印 Python 版本号并退出。 

如果重复给出，则打印有关构建的更多信息，例如:

```sh
$ python -VV
Python 3.7.4 (default, Jul 16 2019, 07:12:58) 
[GCC 9.1.0]
$ 
```

*3.6 新版功能:* `-VV` 选项。

#### 1.1.3. 其他选项

**-E**  
忽略所有 PYTHON* 环境变量，例如可能已设置的 [PYTHONPATH](https://docs.python.org/zh-cn/3.7/using/cmdline.html#envvar-PYTHONPATH) 和 [PYTHONHOME](https://docs.python.org/zh-cn/3.7/using/cmdline.html#envvar-PYTHONHOME)。

**-i**  
当有脚本被作为首个参数传入或使用了 [-c](https://docs.python.org/zh-cn/3.7/using/cmdline.html#cmdoption-c) 选项时，在执行脚本或命令之后进入交互模式，即使是在 [sys.stdin](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.stdin) 并不是一个终端的时候。 [PYTHONSTARTUP](https://docs.python.org/zh-cn/3.7/using/cmdline.html#envvar-PYTHONSTARTUP) 文件不会被读取。

这一选项的用处是在脚本引发异常时检查全局变量或者栈跟踪。 另请参阅 [PYTHONINSPECT](https://docs.python.org/zh-cn/3.7/using/cmdline.html#envvar-PYTHONINSPECT)。

**-I**  
在隔离模式下运行 Python。 这将同时应用 -E 和 -s。 在隔离模式下 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path) 既不包含脚本所在目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。 还可以施加更进一步的限制以防止用户注入恶意代码。

*3.4 新版功能.*

**-s**  
不要将 [用户 site-packages 目录](https://docs.python.org/zh-cn/3.7/library/site.html#site.USER_SITE) 添加到 [sys.path](https://docs.python.org/zh-cn/3.7/library/sys.html#sys.path)。

**参见：** [PEP 370](https://www.python.org/dev/peps/pep-0370) -- 分用户的 site-packages 目录

### 1.2. 环境变量
这些环境变量会影响 Python 的行为，它们是在命令行开关之前被处理的，但 -E 或 -I 除外。 根据约定，当存在冲突时命令行开关会覆盖环境变量的设置。

## Python Wiki
### WindowsCompilers
[Windows编译器](https://wiki.python.org/moin/WindowsCompilers)

虽然 Python 是一种解释型语言，在一些情况下你可能需要安装 Windows C++ 编译器。不像 Linux，Windows 编译器默认没有被包含在OS中。

例如，你将需要使用它们如果你想：

* 通过 Pip 从源代码安装一个非纯 Python 包 (如果没有提供 Wheel 包)。
* 编译一个 Cython 或 Pyrex 文件。

微软提供的官方 C++ 编译器叫作 *Visual C++*，你可以发现它们与 *Visual Studio* 捆绑在一起或者，对于一些版本，单独发行。存在一些可替代的编译器如 [MinGW](http://mingw.org/)，但是可能会与官方通过 Microsoft Visual C++ 编译发行的 CPython出现不兼容。

编译器的架构必须与Python的相同 (例如：如果你使用64位的 Python，你必须使用一个 x64 编译器)。

**一个特定的Python版本应该使用哪一个 Microsoft Visual C++ 编译器呢？**

每一个 Python 版本都使用一个特定的编译器版本 (例如：*CPython 2.7* 使用 *Visual C++ 9.0*，*CPython 3.3* 使用 *Visual C++ 10.0*，等等)。所以，你必须安装与你的Python版本对应的编译器版本：

Visual C++  |CPython
------------|-----------------------
14.0        |3.5, 3.6
10.0        |3.3, 3.4
9.0         |2.6, 2.7, 3.0, 3.1, 3.2

**Distutils笔记**  
如果要安装的包的 *setup.py* (仍然) 使用 *distutils* 而不是推荐的 *setuptools*，你可能需要额外的设置：

* *distutils* 仅支持非常少的编译器设置。这份指南中对应它们的章节明确地提及了 *distutils*。
* 对于其它设置，你需要从对应的工具链的 "SDK 提示符" 运行编译并设置 *DISTUTILS_USE_SDK* 环境变量为一个非空值。

**编译器安装和配置**

每一个编译器兼容的架构在括号中指出了。

在做任何事以前，安装或更新 *Setuptools* Python 包。它包含了增强的兼容性及增加了自动使用的编译器：

```sh
pip install --upgrade setuptools
```

Microsoft Visual C++ 14.0 standalone: Build Tools for Visual Studio 2017 (x86, x64, ARM, ARM64)  
这是一个独立的 Visual C++ 14.0 编译器版本，你不需要安装 *Visual Studio 2017*。

* 安装 [*Microsoft Build Tools for Visual Studio 2017*](https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017)。  
* *setuptools* Python 包的版本必须至少为 34.4.0。

Microsoft Visual C++ 14.0 with Visual Studio 2017 (x86, x64, ARM, ARM64)  
*Visual Studio 2017* 包含 *Visual C++ 14.0* 编译器。*setuptools* Python 包的版本必须至少为 34.4.0。

Microsoft Visual C++ 14.0 standalone: Visual C++ Build Tools 2015 (x86, x64, ARM)  
这是一个独立的 Visual C++ 14.0 编译器版本，你不必安装 *Visual Studio 2015*。

* 安装 *Microsoft Visual C++ Build Tools 2015*。检查 *Windows 8.1 SDK* 及 *Windows 10 SDK* 选项。  
* *setuptools* Python 包的版本必须至少为 24.0。

Visual C++ Build Tools 2015 已经被微软升级为 Build Tools for Visual Studio 2017 了。安装它请看前一段。

Microsoft Visual C++ 14.0 with Visual Studio 2015 (x86, x64, ARM)  
*Visual Studio 2015* 包含 *Visual C++ 14.0* 编译器。*Distutils* 将自动检测编译器并使用它。

# Python HOWTOs
## 套接字编程指南
**作者：** Gordon McMillan

### 套接字
我将只讨论关于 INET（比如：IPv4 地址族）的套接字，但是它将覆盖几乎 99% 的套接字使用场景。并且我将仅讨论 STREAM（比如：TCP）类型的套接字 - 除非你真的知道你在做什么（否则这篇 HOWTO 可能并不适合你），使用 STREAM 类型的套接字将会得到比其它类型更好的表现与性能。我将尝试揭开套接字的神秘面纱，也会讲到一些阻塞与非阻塞套接字的使用。但是我将以阻塞套接字为起点开始讨论。只有你了解它是如何工作的以后才能处理非阻塞套接字。

理解这些东西的难点之一在于「套接字」可以表示很多微妙差异的东西，这取决于上下文。所以首先，让我们先分清楚「客户端」套接字和「服务端」套接字之间的不同，客户端套接字表示对话的一端，服务端套接字更像是总机接线员。客户端程序只能（比如：你的浏览器）使用「客户端」套接字；网页服务器则可以使用「服务端」套接字和「客户端」套接字来会话。

#### 历史
目前为止，在各种形式的 IPC（进程间通信）中，套接字是最流行的。在任何指定的平台上，可能会有其它更快的 IPC 形式，但是就跨平台通信来说，套接字大概是唯一的玩法。

套接字做为 BSD Unix 操作系统的一部分在伯克利诞生，像野火一样在因特网传播。有一个很好的原因 —— 套接字与 INET 的结合使得与世界各地的任意机器间通信变得令人难以置信的简单（至少与其他方案对比来说）。

### 创建套接字
简略地说，当你点击带你来到这个页面的链接时，你的浏览器就已经做了下面这几件事情:

```python
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
```

当连接完成，套接字可以用来发送请求来接收页面上显示的文字。同样是这个套接字也会用来读取响应，最后再被销毁。是的，被销毁了。客户端套接字通常用来做一次交换（或者说一小组序列的交换）。

网络服务器发生了什么这个问题就有点复杂了。首页，服务器创建一个「服务端套接字」:

```python
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)
```

**注意：**  
* 低端口号通常被一些「常用的」服务（HTTP, SNMP 等）所保留。如果你想把程序跑起来，最好使用一个高位端口号（通常是4位的数字）。

* 最后，`listen` 方法的参数会告诉套接字库，我们希望在队列中累积多达 5 个（通常的最大值）连接请求后再拒绝外部连接。 如果所有其他代码都准确无误，这个队列长度应该是足够的。

现在我们已经有一个「服务端」套接字，监听了 80 端口，我们可以进入网络服务器的主循环了:

```python
while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()
```

事际上，通常有 3 种方法可以让这个循环工作起来 - 调度一个线程来处理 `clientsocket`，创建一个新的进程处理 `clientsocket`，或者把这个应用改成使用非阻塞套接字，亦或是使用 `select` 库来实现 "server" 套接字与任意活动 `clientsocket`s 之间的多路复用。稍后会详细介绍。现在最重要的是理解：这就是一个 "服务端"" 套接字做的 *所有* 事情。它并没有发送任何数据。也没有接收任何数据。它只创建 "客户端" 套接字。每个 `clientsocket` 都是为了响应某些*其它*"客户端"套接字 `connect()` 到我们绑定的主机和端口。一旦完成创建 `clientsocket`，我们就会返回并监听更多的连接请求。这两个"客户端"可以随意通信 - 它们使用了一些动态分配的端口，会话结束时端口会被回收。

### 使用一个套接字
当 `recv` 方法返回 0 字节时，就表示另一端已经关闭（或者它所在的进程关闭）了连接。你再也不能从这个连接上获取到任何数据了。你可以成功的发送数据；我将在后面讨论这一点。

像 HTTP 这样的协议只使用一个套接字进行一次传输。客户端发送一个请求，然后读取响应。就这么简单。套接字会被销毁。 这意味着客户端可以通过接收 0 字节来检测到响应的结束。

## 如何使用urllib包获取互联网资源
### 头信息
我们将在这讨论一个具体的HTTP头信息，详细解释如何为你的HTTP请求增加头信息。

一些网站不喜欢被程序浏览，或者给不同的浏览器发送不同的版本。默认情况下urllib以Python-urllib/x.y (x和y分别为Python发行版的主版本号和次版本号，如 Python-urllib/3.6)标识自己，这可能使网站迷惑，或者无法正常工作。一个浏览器标识自己的方式是通过User-Agent(用户代理)头信息。当你创建一个Request对象时，你可以传递一个头信息字典进去。

```python
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.whatismybrowser.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) \
Gecko/20100101 Firefox/58.0'
}

req = Request(url, headers=headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
myuseragent = soup.find_all('div', class_="user-agent")[0].a.get_text()
print(myuseragent)
```

上面代码的执行结果是：  
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0

当Request对象没有传递headers参数时，执行结果是：  
Python-urllib/3.6

# Python 打包用户指南 
## 教程
### 安装包
#### Source Distributions vs Wheels
[pip](https://packaging.python.org/key_projects/#pip) 可以从 [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist) 或者 [Wheels](https://packaging.python.org/glossary/#term-wheel) 安装，但如果两者都存在于 PyPI，则pip将优先安装一个兼容的 [wheel](https://packaging.python.org/glossary/#term-wheel)。

[Wheels](https://packaging.python.org/glossary/#term-wheel) are a pre-built [distribution](https://packaging.python.org/glossary/#term-distribution-package) format that provides faster installation compared to [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist), 特别是当一个项目包含编译的扩展时。

If [pip](https://packaging.python.org/key_projects/#pip) does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

#### Requirements files
Install a list of requirements specified in a [Requirements File](https://pip.pypa.io/en/latest/user_guide/#requirements-files).

`pip install -r requirements.txt`

## 指南
### 打包二进制扩展
#### 构建二进制扩展
##### Windows 平台的二进制扩展
在有可能编译一个二进制扩展之前，确认你有一个适当的编译器可用是有必要的。在 Windows 平台上，Visual C 通常用于构建官方的 CPython 解释器，也应该被用来构建兼容的二进制扩展。

Python 2.7 使用 Visual Studio 2008，Python 3.3 和 3.4 使用 Visual Studio 2010，而 Python 3.5+ 使用 Visual Studio 2015 或者更新版本。不幸的是，旧版的 Visual Studio 不再容易通过 Microsoft 获得，所以对于 Python 3.5 以前的版本，必须获取不同的编译器如果你还没有一个相关的版本。

为二进制扩展设置一个构建环境，步骤如下：

**For Python 2.7**

* 安装 “Visual C++ Compiler Package for Python 2.7”, 可以从微软官网 [下载](https://www.microsoft.com/en-gb/download/details.aspx?id=44266)。
* 在你的 setup.py 中使用 (一个最新版本的) setuptools (任何情况下，pip 都将为你做这个)。
* 完成。

**For Python 3.5**

* 安装 [Visual Studio 2015 Community Edition](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) (或者任意的更新版本)。
* 完成。

注意从 Python 3.5 起，Visual Studio 以一种向后兼容的方式工作，这意味着任何未来的 Visual Studio 版本都将有能力为所有 Python 3.5 以后的版本构建 Python 扩展。

在 Windows 平台上用推荐的编译器构建确保了一个兼容的 C 库至始至终都可以被 Python 进程使用。

# Python 有什么新变化？
“What’s New in Python” 系列短文将带你了解Python主版本间最重要的变化。当发布一个新版本后对任何想保持更新的人来说它们是 “必读” 的。

## What's New in Python 2.3
### 15 Extended Slices
从 Python 1.4 开始，切片语法已经支持一个可选的第三个参数 `step` 或 `stride` 。例如，这些都是合法的 Python 语法： L[1:10:2], L[:-1:1], L[::-1]。

负值也能正常工作，它生成一个反转顺序的列表副本（不影响原列中元素的顺序）：

```python
>>> L = range(10)
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

## What's New In Python 3.0
**作者：** Guido van Rossum

这篇文章解释了Python 3.0中的新特性，与2.6比较。Python 3.0，也被称为 “Python 3000” 或 “Py3K”，它是第一个有意向后不兼容的Python发行版。

一如既往，对于一个新版本，源发行版中的 `Misc/NEWS` 文件包含很多关于每一个发生变化的小事的详细信息。

### 常见绊脚石
这节列出了那些最可能使你犯错误的一些变化，如果你正在使用Python 2.5的话。

#### 文本 Vs. 数据代替 Unicode Vs. 8-bit
你认为你知道的关于二进制数据和 Unicode 的所有事情都已经改变了。

* Python 3.0 使用 *文本* 和 (二进制) *数据* 的概念代替 Unicode 字符串和 8-bit 字符串。所有文本都是 Unicode；然而 *编码的* Unicode 被表示为二进制数据。用于控制文本的类型是 [str](https://docs.python.org/3/library/stdtypes.html#str)，用于控制数据的类型是 [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)。与 2.x 情境最大的不同是在Python 3.0中任何试图混合文本和数据的操作都将抛出 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)，然而如果你在Python 2.x 中混合 Unicode 和 8-bit 字符串，它将工作如果 8-bit 字符串仅包含 7-bit (ASCII) 字节，但是如果它包含非ASCII值你将得到 [UnicodeDecodeError](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError)。这种因值而异的行为这些年来已经导致了许多愁容。  
* 对于 Unicode 文本你可以不再使用 `u"..."` 字母。然而，对于二进制数据你必须使用 `b"..."` 字母。  
* `StringIO` 和 `cStringIO` 模块已经消失了。改为，导入 [io](https://docs.python.org/3/library/io.html#module-io) 模块及为文本和数据分别使用 [io.StringIO](https://docs.python.org/3/library/io.html#io.StringIO) 或 [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)。

### 库变化
因为时间的限制，这个文档没有详尽地介绍标准库中非常广泛的变化。[PEP 3108](https://www.python.org/dev/peps/pep-3108) 是库的主要变化的参考文献。这是一个简述的回顾：

* Python 2.x 中一个常见的模式是有一个用纯Python实现的模块版本，与一个可选的实现为一个C扩展的加速版本；例如，[pickle](https://docs.python.org/3/library/pickle.html#module-pickle) 和 `cPickle`。这承担每次使用这些模块时导入加速版本及退回到纯Python版本的责任。在 Python 3.0中，加速版本被认为实现了纯Python的细节。用户应该总是导入标准版本，试图导入加速版本会退回到纯Python版本。[pickle](https://docs.python.org/3/library/pickle.html#module-pickle) / `cPickle` 对受到这种待遇。[profile](https://docs.python.org/3/library/profile.html#module-profile) 模块在3.1的清单上。`StringIO` 模块已经变成了 [io](https://docs.python.org/3/library/io.html#module-io) 模块的一个类。

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

## numpy
习惯上，我们按以下方式导入numpy：

```python
import numpy as np
```

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

### 输入/输出
#### pandas.read_excel
pandas.**read_excel**(\*args, \*\*kwargs)  
将一个 Excel 文件读取到一个 pandas DataFrame 中。  

**参数：**  
**io：** *__str, bytes, ExcelFile, xlrd.Book, path object, or file-like object__*  
任何有效的字符串路径都是可接受的。  

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

### 通用函数
pandas.concat  
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

### pandas.DataFrame.all
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

### pandas.DataFrame.index
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

### pandas.DataFrame.sort_values
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

### pandas.Series.isin
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

# Python Snippets
## proxy.py
Python HTTPS 代理代码

```python
import urllib.request


proxy_handler = urllib.request.ProxyHandler(proxies={'https': 'https://127.0.0.1:11824'})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('https://www.google.com')
print(response.read())
```

# Python2
## Python 2 语言参考
### 3. 数据模型
#### 3.4. 特殊方法名
##### 3.4.1. 基本自定义
object.**\_\_nonzero\_\_**(*self*)  
调用以实现真值测试及内置操作 `bool()`；应该返回 `False` 或者 `True`，或者它们的等值整型数 `0` 或 `1`。当这个方法没有被定义时，[\_\_len\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__len__) 被调用，如果它被定义了，且如果它的结果是非零的则对象被认为是真。如果一个类既没有定义 [\_\_len\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__len__) 也没有定义 [\_\_nonzero\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__nonzero__)，则它所有的实例都被认为是真。

##### 3.4.6. 仿真容器类型
object.**\_\_len\_\_**(*self*)  
调用以实现内置函数 [len()](https://docs.python.org/2/library/functions.html#len)。应该返回对象的长度，一个 `>=` 0 的整型数。同样，一个没有定义 [\_\_nonzero\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__nonzero__) 方法且其 [\_\_len\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__len__) 方法返回 `0` 的对象在一个布尔上下文中被认为是假的。

**CPython实现细节：** 在CPython中，对象的长度被要求至多为 [sys.maxsize](https://docs.python.org/2/library/sys.html#sys.maxsize)。如果对象的长度比 [sys.maxsize](https://docs.python.org/2/library/sys.html#sys.maxsize) 大，一些特性 (如 [len()](https://docs.python.org/2/library/functions.html#len)) 可能抛出 [OverflowError](https://docs.python.org/2/library/exceptions.html#exceptions.OverflowError)。为避免真值测试中抛出 [OverflowError](https://docs.python.org/2/library/exceptions.html#exceptions.OverflowError)，一个对象必须定义一个 [\_\_nonzero\_\_()](https://docs.python.org/2/reference/datamodel.html#object.__nonzero__) 方法。

# 数据库
**PRIMARY KEY**  
PRIMARY KEY 约束  
PRIMARY KEY 约束唯一标识数据库表中的每条记录。  
主键必须包含唯一的值。  
主键列不能包含 NULL 值。  
每个表都应该有一个主键，并且每个表只能有一个主键。  

## MongoDB
### 文档  
MongoDB将数据记录存储为BSON文档。BSON是 [JSON](https://docs.mongodb.com/manual/reference/glossary/#term-json) 文档的二进制形式，然而它比JSON包含更多的数据类型。对于BSON的说明，请看 [bsonspec.org](http://bsonspec.org/)。另请参见 [BSON 类型](https://docs.mongodb.com/manual/reference/bson-types/)。

#### 文档结构
MongoDB documents are composed of field-and-value pairs and have the following structure:

```sql
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

字段的值可以是任意的BSON [数据类型](https://docs.mongodb.com/manual/reference/bson-types/)，包括其它文档，数组，和文档数组。例如，下面的文档包含各种类型的值：

```sql
var mydoc = {
               _id: ObjectId("5099803df3f4948bd2f98391"),
               name: { first: "Alan", last: "Turing" },
               birth: new Date('Jun 23, 1912'),
               death: new Date('Jun 07, 1954'),
               contribs: [ "Turing machine", "Turing test", "Turingery" ],
               views : NumberLong(1250000)
            }
```

上面的字段拥有下面的数据类型：

* **_id** 保存一个 [ObjectId](https://docs.mongodb.com/manual/reference/bson-types/#objectid)。  
* **name** 保存一个嵌入式的包含 **first** 和 **last** 字段的文档。  
* **birth** 和 **death** 保存 *Date* 类型的值。  
* **contribs** 保存一个字符串数组。  
* **views** 保存一个 *NumberLong* 类型的值。


**字段名**  
字段名都是字符串。

[文档](https://docs.mongodb.com/manual/core/document/#) 的字段名有下列限制：

* 字段名 **\_id** 是保留字，用作一个主键；它的值在 collection 中必须是唯一的，不变的，可以是除了数组以外的任意类型。  
* 字段名不能包含 **null** 字符。  
* 顶层字段名不能以美元符号 ($) 开头。  
另外，从 MongoDB 3.6开始，服务器允许储存包含点(.)和美元符号($)的字段名。

#### 文档限制
文档拥有下面的属性：

**文档大小限制**  
BSON文档的最大值为16MB。

**文档字段顺序**  
MongoDB根据写操作来保存文档字段的顺序，除了下面的情况：

* **\_id** 字段总是文档的第一个字段。  
* 包含[重命名](https://docs.mongodb.com/manual/reference/operator/update/rename/#up._S_rename)字段名的更新可能导致文档中的字段重新排序。

*在版本2.6中发生变化：* 从版本2.6开始，MongoDB主动地尝试保持文档中字段的顺序。在版本2.6以前，MongoDB不主动地保持文档中字段的顺序。

**\_id 字段**  
在MongoDB中，每一个储存在collection中的文档都要求一个唯一的 [\_id](https://docs.mongodb.com/manual/reference/glossary/#term-id) 字段来作为一个[主键](https://docs.mongodb.com/manual/reference/glossary/#term-primary-key)。如果一个插入的文档省略了 **\_id** 字段，则MongoDB 驱动程序自动为 **\_id** 字段生成一个 [ObjectId](https://docs.mongodb.com/manual/reference/bson-types/#objectid)。

这也适用于通过带 [upsert: true](https://docs.mongodb.com/manual/reference/method/db.collection.update/#upsert-parameter) 的 update 操作插入的文档。

**\_id** 字段有下面的行为及约束：

* 默认情况下，MongoDB creates a unique index on the **\_id** field during the creation of a collection.  
* **\_id** 字段总是文档中的第一个字段。如果服务器收到的文档的 **\_id** 字段不在第一个字段，则服务器会将 **\_id** 字段移动到第一个字段。  
* **\_id** 字段的值可以是任意的 [BSON 数据类型](https://docs.mongodb.com/manual/reference/bson-types/)，除了数组。

### mongo Shell
查询collection中的所有记录

```sql
> db.collection.find()
```

查询collection中的指定列_id和timestamp

```sql
> db.collection.find({}, {_id: true, timestamp: true})
```

或

```sql
> db.collection.find({}, {_id: 1, timestamp: 1})
```

查询collection中的所有列，除了result列

```sql
> db.collection.find({}, {result: false})
```

或

```sql
> db.collection.find({}, {result: 0})
```

查询_id为`http://google.com`的记录

```sql
> db.collection.find({_id: 'http://google.com'})
```

查询前2条记录

```sql
> db.collection.find().limit(2)
```

**排序**  
将db.collection.find()查询的结果按timestamp的值升序排列

```sql
> db.collection.find({}, {_id: true, timestamp: true}).sort({timestamp: 1})
```

将db.collection.find()查询的结果按timestamp的值降序排列

```sql
> db.collection.find({}, {_id: true, timestamp: true}).sort({timestamp: -1})
```

重命名collection

```sql
> db.collection.renameCollection('newName')
```

#### 配置mongo Shell
**改变 mongo Shell Batch Size**  
[db.collection.find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find) 方法是一个从 [collection](https://docs.mongodb.com/manual/reference/glossary/#term-collection) 中检索文档的 JavaScript 方法。[db.collection.find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find) 方法返回一个游标给结果；然而，在 [mongo](https://docs.mongodb.com/manual/reference/program/mongo/#bin.mongo) shell 中，如果返回的游标没有赋值给一个通过 **var** 关键字定义的变量，则游标自动迭代20次，以打印匹配查询的前20个文档。[mongo](https://docs.mongodb.com/manual/reference/program/mongo/#bin.mongo) shell 将提示 **Type it** 以迭代另外20次。

你可以设置 **DBQuery.shellBatchSize** 属性以改变文档的数量（默认值为20），如下面的例子将它设置为10：

```sql
DBQuery.shellBatchSize = 10;
```

### mongo Shell方法
#### 集合方法
db.collection.findAndModify(**document**)

修改并返回一个单一的文档。默认情况下，返回的文档不包含 update 的修改。要返回带 update 的修改的文档，使用 **new** 选项。The [findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) method is a shell helper around the [findAndModify](https://docs.mongodb.com/manual/reference/command/findAndModify/#dbcmd.findAndModify) command.

[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 方法拥有下面的形式：

*在版本3.6中发生变化。*

```sql
db.collection.findAndModify({
    query: <document>,
    sort: <document>,
    remove: <boolean>,
    update: <document>,
    new: <boolean>,
    fields: <document>,
    upsert: <boolean>,
    bypassDocumentValidation: <boolean>,
    writeConcern: <document>,
    collation: <document>,
    arrayFilters: [ <filterdocument1>, ... ]
});
```

[db.collection.findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 方法接收一个带有下面的嵌套文档字段的文档参数：

Parameter  |Type  |Description
-----------|------|-----------
query      |文档  |可选的。用于修改的选择条件。**query** 字段使用的[查询选择器](https://docs.mongodb.com/manual/reference/operator/query/#query-selectors)与 [db.collection.find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find) 方法中所使用的[查询选择器](https://docs.mongodb.com/manual/reference/operator/query/#query-selectors)一致。虽然查询可能匹配多个文档，[db.collection.findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) **将仅选择一个文档进行修改**。
update     |文档  |必须指定 **remove** 或 **update** 字段。对选择的文档进行更新。**update** 字段使用与 [update operators](https://docs.mongodb.com/manual/reference/operator/update/#id1) 或 **field: value** 相同的规范来修改选择的文档。
new        |布尔  |可选的。当为 **真** 时，返回修改后的文档而不是原始文档。[db.collection.findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 方法的 **remove** 操作忽略 **new** 选项。默认值为 **false**。
upsert     |布尔  |可选的。与 **update** 字段一起使用。<br><br>当为 **真** 时，[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 执行两者中的一个：<br><br><ul><li>如果没有文档匹配**查询**则创建一个新的文档。详细信息请看 [upsert behavior](https://docs.mongodb.com/manual/reference/method/db.collection.update/#upsert-behavior)。</li><li>更新一个匹配**查询**的单一的文档。</li></ul>为避免多次 upserts，请确保**查询**字段是[唯一索引的](https://docs.mongodb.com/manual/core/index-unique/#index-type-unique)。<br><br>默认值为 **false**。

**返回数据**

对于删除操作，如果查询匹配一个文档，[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 返回删除的文档。如果没有匹配查询的文档，[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 返回 **null**。

对于更新操作，[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 返回下面的其中一个：

* 如果 **new** 参数没有设置或者为 **false**：
    * 如果查询匹配一个文档则返回修改前的文档；
    * 否则，**null**。
* 如果 **new** 为 **true**：
    * 如果查询返回一个匹配则返回修改后的文档；
    * 如果 **upsert: true** 且没有文档匹配查询，则返回插入的文档；
    * 否则，**null**。

*在版本3.0中发生变化：* 在之前的版本中，对于 update，如果 **sort** 指定了，且 **upsert: true**，**new** 选项没有设置或者为 **false**，则 [db.collection.findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 将返回一个空的文档 {} 而不是 **null**。
<br><br>

db.collection.findOne(**query, projection**)  

返回集合或[视图](https://docs.mongodb.com/manual/core/views/)中满足特定查询条件的一个文档。如果有多个文档满足查询条件，这个方法根据映射到磁盘上的文档的[自然顺序](https://docs.mongodb.com/manual/reference/glossary/#term-natural-order)返回第一个文档。在[限制集合](https://docs.mongodb.com/manual/reference/glossary/#term-capped-collection)中，自然顺序等同于插入顺序。如果没有文档满足查询条件，这个方法返回 null。

Parameter  |Type  |Description
-----------|------|-----------
query      |文档  |可选的。指定查询选择条件使用 [query operators](https://docs.mongodb.com/manual/reference/operator/)。
projection |文档  |可选的。指定返回的字段使用 [projection operators](https://docs.mongodb.com/manual/reference/operator/projection/)。省略这个参数将返回匹配文档的所有字段。

db.collection.insert()  

插入一个文档或多个文档到一个集合中。

[insert()](https://docs.mongodb.com/manual/reference/method/db.collection.insert/index.html#db.collection.insert) 方法拥有下面的语法：

*在版本2.6中发生变化。*

```sql
db.collection.insert(
   <document or array of documents>,
   {
     writeConcern: <document>,
     ordered: <boolean>
   }
)
```

Parameter    |Type      |Description
-------------|----------|-----------
document     |文档或数组 |要插入到集合中的一个文档或文档数组。
writeConcern |文档      |可选的。
ordered      |布尔      |可选的。

**举例**

```sql
db.products.insert( { item: "card", qty: 15 } )
```

插入多个文档

```sql
db.products.insert(
   [
     { _id: 11, item: "pencil", qty: 50, type: "no.2" },
     { item: "pen", qty: 20 },
     { item: "eraser", qty: 25 }
   ]
)
```

上面的操作插入了下面3个文档：

```sql
> db.products.find()
{ "_id" : 11, "item" : "pencil", "qty" : 50, "type" : "no.2" }
{ "_id" : ObjectId("5bc44295d1d2620f7c85bd05"), "item" : "pen", "qty" : 20 }
{ "_id" : ObjectId("5bc44295d1d2620f7c85bd06"), "item" : "eraser", "qty" : 25 }
> 
```

### mongoexport
**选项**  
--db &lt;database&gt;, -d &lt;database&gt;  
  指定数据库的名字

--collection &lt;collection&gt;, -c &lt;collection&gt;  
  指定要导出的collection

--fields &lt;field1[,field2]&gt;, -f &lt;field1[,field2]&gt;  
指定要导出的字段，如果有多个字段，使用逗号分隔

--type &lt;string&gt;  
  *默认值：* json  
  *在版本3.0中新增*  
  指定要导出的格式。为[CSV](https://docs.mongodb.com/manual/reference/glossary/#term-csv)格式指定csv，为[JSON](https://docs.mongodb.com/manual/reference/glossary/#term-json)格式指定json。  
  如果指定csv，则你必须使用[--fields](https://docs.mongodb.com/manual/reference/program/mongoexport/#cmdoption-mongoexport-fields)或[--fieldFile](https://docs.mongodb.com/manual/reference/program/mongoexport/#cmdoption-mongoexport-fieldfile)选项来声明要从collection中导出的字段。

--out &lt;file&gt;, -o &lt;file&gt;  
  指定一个文件以写入导出的数据。如果没有指定文件名，[mongoexport](https://docs.mongodb.com/manual/reference/program/mongoexport/#bin.mongoexport)会将数据写到标准输出。

**用法**  
*在版本3.0中发生变化：* [mongoexport](https://docs.mongodb.com/manual/reference/program/mongoexport/#bin.mongoexport)删除了--csv选项。使用[--type=csv](https://docs.mongodb.com/manual/reference/program/mongoexport/#cmdoption-mongoexport-type)选项来为输出指定CSV格式。

以csv格式导出cache数据库的twentythreads collection的_id字段

```sh
mongoexport --db cache --collection twentythreads --type=csv --fields _id --out url.csv
```

### Operators
#### Query and Projection Operators
**查询选择器**  
**比较**  

比较不同的BSON类型值，参考 [特定的BSON比较顺序](https://docs.mongodb.com/manual/reference/bson-type-comparison-order/#bson-types-comparison-order)。

Name  |Description
------|-----------------------
[$lt](https://docs.mongodb.com/manual/reference/operator/query/lt/#op._S_lt)   |匹配小于一个指定值的所有值。
[$ne](https://docs.mongodb.com/manual/reference/operator/query/ne/#op._S_ne)   |匹配所有不等于指定值的值。

#### Update Operators

下面的修改器在更新操作中是可用的；例如，在 [db.collection.update()](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update) 和 [db.collection.findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) 中。

在一个文档中指定运算表达式的形式：

```sql
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}
```

**注意：**  
指定运算符的详细信息，包括语法和例子，点击指定运算符跳转到它的参考页面。

**更新运算符**

**字段**  

Name    |Description
--------|------------
[$set](https://docs.mongodb.com/manual/reference/operator/update/set/#up._S_set)  |在一个文档中设置字段的值。

##### 字段更新运算符
**$set**

**定义**

[$set](https://docs.mongodb.com/manual/reference/operator/update/set/#up._S_set) 运算符用指定的值替换字段的值。

[$set](https://docs.mongodb.com/manual/reference/operator/update/set/#up._S_set) 运算符表达式拥有下面的形式：

```sql
{ $set: { <field1>: <value1>, ... } }
```

指定一个嵌套文档或一个数组中的一个<**字段**>，使用 [dot notation](https://docs.mongodb.com/manual/core/document/#document-dot-notation)。

## MySQL
将ID表的MARKET字段的长度改为10

```sql
mysql> alter table ID modify column MARKET varchar(10);
```

查询数据库 'ISCHOOLYARD' 下的所有表及相应的表注释

```sql
mysql> use information_schema;
mysql> select TABLE_NAME, TABLE_COMMENT from TABLES where TABLE_SCHEMA='ISCHOOLYARD';
```

### MySQL Workbench
在整个数据库中搜索指定字符串：  

1. 左侧导航窗口选中要搜索的数据库；  
2. 右键选择“Search Table Data...”；  
3. 在弹出的窗口中输入指定字符串。

### LOAD DATA INFILE语法

```sql
LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
    [IGNORE number {LINES | ROWS}]
    [(col_name_or_user_var
        [, col_name_or_user_var] ...)]
    [SET col_name={expr | DEFAULT},
        [, col_name={expr | DEFAULT}] ...]
```

```sh
mysql -h 192.168.2.4 -u user -p
Enter password:
```

```sql
mysql> use ocean;
mysql> load data local infile "/home/paxy/cardid.csv" into table ID fields terminated by ',';
```

将客户端上的cardid.csv文件以逗号（','）为字段分隔符导入到192.168.2.4上的MySQL数据库模式ocean的ID表中，该命令的导入几乎是瞬时的，比MySQL Workbench的Table Data Import快无数倍。

### UPDATE语法
UPDATE是一个数据操纵语言语句，用于修改表格中的行。

单表语法：

```sql
UPDATE [LOW_PRIORITY] [IGNORE] table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]

value:
    {expr | DEFAULT}

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```

将IDCARD表中id为2912157145的行的id修改为2113075673

```sql
update IDCARD set id='2113075673' where id='2912157145'
```

### 比较函数与运算符
**比较运算符**

Name  |Description
------|---------------------------
[IN()](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#function_in)  |检查一个值是否在一个值的集合中

* *expr* IN (*value,...*)

你永远都不应该在一个 IN 列表中混用引用的和非引用的值，因为引用值 (如字符串) 和非引用值 (如数字) 的比较规则不同。混用类型可能因此导致前后矛盾的结果。例如，不要像这样写一个 IN 表达式：

```sql
SELECT val1 FROM tbl1 WHERE val1 IN (1,2,'a');
```

用这种写法替代：

```sql
SELECT val1 FROM tbl1 WHERE val1 IN ('1','2','a');
```

```sql
select * from ID where CARDID in (1766800630,2841917174,0154495212);
```

等同于

```sql
select * from ID where CARDID=1766800630 or CARDID=2841917174 or CARDID=0154495212;
```

IN 查询相当于多个 OR 条件的叠加。

### 4.2.5 在命令行中使用选项
当命令行中指定的选项值包含空格时必须用引号括起来。例如，[--execute](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute) (或 -e) 选项可以和 [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 一起使用以将 SQL 语句传递给服务器。当这个选项被使用时，[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 用这个选项值执行这些语句然后退出。这些语句必须被引号括起来。例如，你可以用下面的命令获取一份用户账户列表：

```sh
shell> mysql -u root -p --execute="SELECT User, Host FROM mysql.user"
Enter password: ******
+------+-----------+
| User | Host      |
+------+-----------+
|      | gigan     |
| root | gigan     |
|      | localhost |
| jon  | localhost |
| root | localhost |
+------+-----------+
shell>
```

**注意**

长形式 ([--execute](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute)) 后跟一个等号 (=)。

### 4.5.1.1 mysql 客户端选项
[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 支持下面的选项，下面的选项可以在命令行中或一个选项文件的 [mysql] 和 [client] 组中指定。关于 MySQL 程序使用的选项文件的信息，请看章节 [4.2.2.2, “Using Option Files”](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)。

**mysql 客户端选项**

Option Name     |Description         |Introduced    |Deprecated   |Removed
----------------|--------------------|--------------|-------------|-------
[--execute](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute)  |执行指定语句然后退出  |             |            |     
[--named-commands](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_named-commands)  |启用命名的 mysql 命令  |     |     |          

* [--execute=*statement*](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute), -e *statement*

  执行指定语句然后退出。默认输出格式与使用 [--batch](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_batch) 选项的输出相似。对于一些例子，请看章节 [4.2.5, “Using Options on the Command Line”](https://dev.mysql.com/doc/refman/8.0/en/command-line-options.html)。和这个选项一起使用时，[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 不使用历史文件。

* [--named-commands](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_named-commands), -G  
  
  启用命名的 [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 命令。允许长格式的命令，而不只是短格式的命令。例如，`quit` 和 `\q` 都能被识别。禁用命名的命令请使用 [--skip-named-commands](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_named-commands)。另请参见 [章节 4.5.1.2, “mysql Client Commands”](https://dev.mysql.com/doc/refman/8.0/en/mysql-commands.html)。

#### 4.5.1.2 mysql 客户端命令
[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 将你发出的每一个 SQL 语句发送到服务器去执行。也有一个 [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 自己解释的命令集合。为得到这些命令的清单，请在 `mysql>` 提示符后键入 `help` 或者 `\h`：

```sql
mysql> help

List of all MySQL commands:
Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with $EDITOR.
ego       (\G) Send command to mysql server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to mysql server.
help      (\h) Display this help.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given
               outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing
               binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.

For server side help, type 'help contents'
```

* ego, \G

  将当前的语句发送到服务器去执行并使用垂直的格式显示结果。

```sql
mysql> select now() \G
*************************** 1. row ***************************
now(): 2019-12-19 16:08:50
1 row in set (0.00 sec)

mysql> select now()
    -> ego
*************************** 1. row ***************************
now(): 2019-12-19 16:08:55
1 row in set (0.00 sec)
```

* nopager, \n

  禁用输出分页。请看 `pager` 的描述。

  `nopager` 命令仅在 Unix 平台有效。

* pager [**command**], \P [**command**]

  启用输出分页。  
<br>  

这里有一些关于 `pager` 命令的小技巧：

* `-F` 和 `-X` 选项有可能和 **less** 一起使用以使 less 退出，如果输出适合在一个屏幕上显示的话，当不需要滚动时这很方便：

```sql
mysql> pager less -F -X
```

### 4.5.4 mysqldump — 一个数据库备份程序
[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 客户端工具执行 [逻辑备份](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_logical_backup)，生产一个可以被执行以重新生成原始数据库对象定义和表数据的 SQL 语句集合。 它转储一个或多个 MySQL 数据库，用于备份或传输给另一个 SQL 服务器。[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 命令也可以生成 CSV，其它分隔文本，或 XML 格式的输出。

* [性能和可扩展性考虑](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-performance)

* [调用语法](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-syntax)

* [选项语法 - 按字母顺序汇总](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-option-summary)

* [连接选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-connection-options)

* [选项文件选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-option-file-options)

* [DDL 选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-ddl-options)

* [调试选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-debug-options)

* [帮助选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-help-options)

* [国际化选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-i18n-options)

* [复制选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-replication-options)

* [格式化选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-format-options)

* [过滤选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-filter-options)

* [性能选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-performance-options)

* [事务性的选项](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-transaction-options)

* [选项组](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-option-groups)

* [例子](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-option-examples)

* [限制](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#mysqldump-restrictions)

**性能和可扩展性考虑**

**mysqldump** 的优势包括在恢复以前可以方便且灵活地查看甚至编辑输出。你可以克隆数据库用于开发和 DBA 的工作，或者产生一个已存在的数据库的轻微变化用于测试。它没有打算作为一个快速或可扩展的备份大量数据的解决方案。对于大数据量，即使备份步骤花费一个合理的时间，恢复数据也可能非常慢因为重放 SQL 语句会调用磁盘 I/O 用于插入，创建索引，等等。

对于大型的备份和恢复，[物理](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_physical) 备份更合适，以它们的原始格式拷贝数据文件可以更快地被恢复：

[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 可以一行行地检索和转储表的内容，或者它可以从一个表检索全部的内容并在转储它以前将其缓存到内存中。如果你正在转储大表将其缓存到内存中可能会是一个问题。一行行地转储表，使用 [--quick](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_quick) 选项（或者 [--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt)，该选项默认启用 [--quick](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_quick)）。[--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt) 选项（因此 [--quick](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_quick)）默认是启用的，所以要启用内存缓存，使用 [--skip-quick](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_quick)。

**调用语法**

通常有三种方式使用 [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)—为了转储一个或多个表的集合，一个或多个完整的数据库的集合，或者整个 MySQL 服务器—如下所示：

```sh
shell> mysqldump [options] db_name [tbl_name ...]
shell> mysqldump [options] --databases db_name ...
shell> mysqldump [options] --all-databases
```

转储整个数据库，不要在 *db_name* 后面指定任何表，或者使用 [--databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_databases) 或 [--all-databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_all-databases) 选项。

看你的 [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 版本支持的选项列表，使用命令 [mysqldump --help](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)。

**选项语法 - 按字母顺序总结**

[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 支持下面的选项，这些选项可以在命令行或一个选项文件的 [**mysqldump**] 和 [**client**] 组中指定。关于 MySQL 程序使用的选项文件的信息，参见章节 [4.2.7, “Using Option Files”](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)。

**mysqldump 选项**

**格式**         |**描述**        |**引入**       |**删除**
-----------------|---------------|---------------|---------
[--all-databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_all-databases)  |转储所有数据库中的所有表|        |
[--databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_databases)      |将所有名称参数解释为数据库名称   |        |
[--help](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_help)           |显示帮助信息然后退出  |        |
[--host](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_host)           |要连接的主机（IP地址或主机名）  |     |
[--opt](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_opt)           |代表 --add-drop-table --add-locks --create-options --disable-keys --extended-insert --lock-tables --quick --set-charset 的缩写 |       |
[--password](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_password)      |连接服务器时所使用的密码    |       |
[--port](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_port)         |用于连接的 TCP/IP 端口号  |        |
[--user](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_user)         |连接到服务器时所使用的 MySQL 用户名   |    |
[--verbose](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_verbose)      |详细模式             |     |
[--version](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_version)         |显示版本信息然后退出    |      |

**连接选项**

[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 命令登录进入一个 MySQL 服务器以提取信息。下面的选项指定了如何连接到 MySQL 服务器，要么在相同的机器上要么在一个远程系统上。

* --host=*host_name*, -h *host_name*

  从 MySQL 服务器转储数据到指定的主机上。默认主机是 localhost。

* --password[=*password*], -p[*password*]

  连接到服务器时使用的密码。如果你使用短选项形式（-p），选项和密码之间不能有空格。如果你在命令行的 --password 或 -p 选项后面省略了 *password* 值，[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 会提示你输入一个。

  在命令行中指定一个密码应该被认为是不安全的。见章节 [6.1.2.1, “End-User Guidelines for Password Security”](https://dev.mysql.com/doc/refman/8.0/en/password-security-user.html)。你可以使用一个选项文件以避免在命令行中指定密码。

* --port=*port_num*, -P *port_num*

  用于连接的 TCP/IP 端口号。

* --user=*user_name*, -u *user_name*

  连接到服务器时使用的 MySQL 用户名。

**筛选选项**

下面的选项控制哪些类型的模式对象将被写入到转储文件：按分类，如触发器或事件；按名字，例如，选择转储哪些数据库及表；或甚至使用一个 WHERE 子句从表数据中筛选行。

* --all-databases, -A

  转储所有数据库中的所有表。这等同于使用 [--databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_databases) 选项及在命令行中列出所有数据库的名称。

* --databases, -B

  转储几个数据库。通常地，[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 将命令行中的第一个名称参数作为一个数据库名而将其后的名称作为表名。使用这个选项，它将所有名称参数都作为数据库名。

  这个选项可以被用来转储 `performance_schema` 数据库，这个数据库通常不会被转储即使使用 [--all-databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_all-databases) 选项。

* --tables

  覆盖 [--databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_databases) 或 -B 选项。[mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) 将这个选项后面的所有名称参数都当作表名。

**例子**  
备份一个完整的数据库：

```sh
shell> mysqldump db_name > backup-file.sql
```

还原转储的文件到服务器中：

```sh
shell> mysql db_name < backup-file.sql
```

你可以用一个命令转储几个数据库：

```sh
shell> mysqldump --databases db_name1 [db_name2 ...] > my_databases.sql
```

转储所有数据库，使用 [--all-databases](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_all-databases) 选项：

```sh
shell> mysqldump --all-databases > all_databases.sql
```

### 11.1.2 日期和时间类型概述
MySQL 允许 [TIME](https://dev.mysql.com/doc/refman/8.0/en/time.html)，[DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 和 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 值含有小数部分的秒，最高精确到微秒（6位）。定义一个包含一个小数秒部分的列，使用语法 *type_name*(*fsp*)，其中 *type_name* 是 [TIME](https://dev.mysql.com/doc/refman/8.0/en/time.html), [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html), 或 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html), *fsp* 是小数秒精确度。例如：

```sql
CREATE TABLE t1 (t TIME(3), dt DATETIME(6));
```

*fsp* 值，如果指定，必须在0到6的范围之内。值为0表示没有小数部分。如果忽略，则默认精度为0。(This differs from the standard SQL default of 6, for compatibility with previous MySQL versions.)

一个表中的任意 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 或 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列都可以自动的初始化和更新内容。

### 11.3.2 CHAR 和 VARCHAR 类型
`CHAR` 和 `VARCHAR` 类型是相似的，但在存储及检索的方式上又是不同的。它们在最大长度及是否保留结尾的空格方面也是不同的。

当你创建表时，一个 `CHAR` 列的长度是你申明的固定的的长度。允许的长度是 0 到 255 之间的任意值。

`VARCHAR` 列中的值是变长字符串。可以被指定的长度值是 0 到 65,535。一个 `VARCHAR` 最大的有效长度受制于最大的行大小 (65,535 字节，由所有列共享) 以及所使用的字符集。请参见 [章节 8.4.7, “Limits on Table Column Count and Row Size”](https://dev.mysql.com/doc/refman/8.0/en/column-count-limit.html)。

### 11.3.5 为TIMESTAMP和DATETIME自动初始化和更新
[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 和 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列可以自动初始化及更新为当前的日期和时间 (即，当前的时间戳)。

对于一个表中的任意 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 或 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列，你可以指定当前时间戳作为默认值，自动更新值，或者两者：

* 对于插入的行，如果没有为自动初始化的列指定值，则该列的值被设置为当前时间戳。

* 一个自动更新的列会自动地更新为当前时间戳当行中的任意其它列的值从它的当前值发生变化时。一个自动更新的列会保持不变如果所有的其它列都被设置为他们的当前值。当其它列变化时，要阻止一个自动更新列更新，需显示地将它设置为它的当前值。更新一个自动更新列即使当其它列没有变化时，需显示地设置它为它应有的值（例如，设置为 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp)）。

另外，如果 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 系统变量被禁用，你可以通过指派一个 NULL 值来初始化或更新任何 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) (but not DATETIME) 列到当前的日期和时间，除了它已经用 NULL 属性定义以允许 NULL 值外。

指定自动化的内容，在列的定义中使用 **DEFAULT CURRENT_TIMESTAMP** 和 **ON UPDATE CURRENT_TIMESTAMP** 从句。从句的顺序没有关系。如果两个都出现在一个列的定义中，任何一个都可以先出现。任何 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 的同义词都和 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 拥有相同的含义。这些同义词是 [CURRENT_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp)，[NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)，[LOCALTIME](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtime)，[LOCALTIME()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtime)，[LOCALTIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtimestamp) 和 [LOCALTIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_localtimestamp)。

**DEFAULT CURRENT_TIMESTAMP** 和 **ON UPDATE CURRENT_TIMESTAMP** 的使用仅限于 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 和 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)。**DEFAULT** 从句也可以被用来指定一个常量 (非自动化的) 默认值；例如，**DEFAULT 0** 或 **DEFAULT '2000-01-01 00:00:00'**。

**注意**

下面使用 **DEFAULT 0** 的例子，可能会产生警告或错误，这依赖于严格 SQL 模式或 [NO_ZERO_DATE](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sqlmode_no_zero_date) SQL 模式是否启用。注意 [传统的](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sqlmode_traditional) SQL 模式包括严格模式和 [NO_ZERO_DATE](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sqlmode_no_zero_date)。见章节 [5.1.11, “服务器 SQL 模式”](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html)。

[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 或 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列定义可以指定当前时间戳为默认和自动更新值，其中一个，或者两个都不指定。不同的列可以有不同的自动化内容组合。下面的规则描述这些可能性：

* 同时具有 **DEFAULT CURRENT_TIMESTAMP** 和 **ON UPDATE CURRENT_TIMESTAMP**时，列用当前时间戳作为它的默认值并能够自动更新到当前时间戳。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -> dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-25 14:05:13 |
+---------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('GOD');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+------+---------------------+---------------------+
| name | ts                  | dt                  |
+------+---------------------+---------------------+
| GOD  | 2018-12-25 14:06:10 | 2018-12-25 14:06:10 |
+------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='God' where name='GOD';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+------+---------------------+---------------------+
| name | ts                  | dt                  |
+------+---------------------+---------------------+
| God  | 2018-12-25 14:07:07 | 2018-12-25 14:07:07 |
+------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-25 14:07:35 |
+---------------------+
1 row in set (0.00 sec)

mysql> 
```

* 带一个 **DEFAULT** 从句但不带 **ON UPDATE CURRENT_TIMESTAMP** 从句时，列接受指定的默认值且不会自动更新为当前时间戳。

  默认值取决于 **DEFAULT** 从句是否指定 **CURRENT_TIMESTAMP** 或者一个常量值。后跟 **CURRENT_TIMESTAMP**时，默认值是当前时间戳。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -> dt DATETIME DEFAULT CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('YWH');
Query OK, 1 row affected (0.01 sec)

mysql> select * from t1;
+------+---------------------+---------------------+
| name | ts                  | dt                  |
+------+---------------------+---------------------+
| YWH  | 2018-12-25 14:30:01 | 2018-12-25 14:30:01 |
+------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-25 14:30:20 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='ywh' where name='YWH';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+------+---------------------+---------------------+
| name | ts                  | dt                  |
+------+---------------------+---------------------+
| ywh  | 2018-12-25 14:30:01 | 2018-12-25 14:30:01 |
+------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

  后跟一个常量时，默认值是指定的值。在这种情况下，列没有任何自动化的内容。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP DEFAULT 0,
    -> dt DATETIME DEFAULT 0
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('XSHELL');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+--------+---------------------+---------------------+
| name   | ts                  | dt                  |
+--------+---------------------+---------------------+
| XSHELL | 0000-00-00 00:00:00 | 0000-00-00 00:00:00 |
+--------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-25 14:54:26 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='Xshell' where name='XSHELL';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+--------+---------------------+---------------------+
| name   | ts                  | dt                  |
+--------+---------------------+---------------------+
| Xshell | 0000-00-00 00:00:00 | 0000-00-00 00:00:00 |
+--------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

* 有一个 **ON UPDATE CURRENT_TIMESTAMP** 从句和一个常量 **DEFAULT** 从句时，列自动更新到当前时间戳并具有指定的常量默认值。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP,
    -> dt DATETIME DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('BLEECH');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+--------+---------------------+---------------------+
| name   | ts                  | dt                  |
+--------+---------------------+---------------------+
| BLEECH | 0000-00-00 00:00:00 | 0000-00-00 00:00:00 |
+--------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-26 09:32:08 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='Bleech' where name='BLEECH';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+--------+---------------------+---------------------+
| name   | ts                  | dt                  |
+--------+---------------------+---------------------+
| Bleech | 2018-12-26 09:32:39 | 2018-12-26 09:32:39 |
+--------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

* 当带有一个 **ON UPDATE CURRENT_TIMESTAMP** 从句而没有 **DEFAULT** 从句时，列自动更新到当前时间戳但是没有让当前时间戳作为它的默认值。

  这种情况下默认值与类型有关。[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 有一个默认值0除了定义了 **NULL** 属性外，在这种情况下默认值是 **NULL**。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts1 TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,     -- default 0
    -> ts2 TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP -- default NULL
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('SEIYA');
Query OK, 1 row affected (0.01 sec)

mysql> select * from t1;
+-------+---------------------+------+
| name  | ts1                 | ts2  |
+-------+---------------------+------+
| SEIYA | 0000-00-00 00:00:00 | NULL |
+-------+---------------------+------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-26 09:48:19 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='Seiya' where name='SEIYA';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+-------+---------------------+---------------------+
| name  | ts1                 | ts2                 |
+-------+---------------------+---------------------+
| Seiya | 2018-12-26 09:48:51 | 2018-12-26 09:48:51 |
+-------+---------------------+---------------------+
1 row in set (0.01 sec)

mysql> 
```

  [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 有一个默认值 **NULL** 除了定义了 **NOT NULL** 属性之外，在这种情况下默认值是0。

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> dt1 DATETIME ON UPDATE CURRENT_TIMESTAMP,         -- default NULL
    -> dt2 DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP -- default 0
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t1 (name, dt2)
    -> VALUES ('JAVA', 0);
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO t1 (name, dt2)
    -> VALUES ('PYTHON', '2012-12-12 00:00:00');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+--------+------+---------------------+
| name   | dt1  | dt2                 |
+--------+------+---------------------+
| JAVA   | NULL | 0000-00-00 00:00:00 |
| PYTHON | NULL | 2012-12-12 00:00:00 |
+--------+------+---------------------+
2 rows in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-26 10:47:59 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='Java' where name='JAVA';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE t1 SET name='Python' where name='PYTHON';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+--------+---------------------+---------------------+
| name   | dt1                 | dt2                 |
+--------+---------------------+---------------------+
| Java   | 2018-12-26 10:49:41 | 2018-12-26 10:49:41 |
| Python | 2018-12-26 10:50:06 | 2018-12-26 10:50:06 |
+--------+---------------------+---------------------+
2 rows in set (0.00 sec)

mysql> 
```

[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 和 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列没有自动化的属性除非他们被显示地指定，除了这种情况：如果 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 系统变量被禁用，则 *第一个* [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列同时拥有 **DEFAULT CURRENT_TIMESTAMP** 和 **ON UPDATE CURRENT_TIMESTAMP** 如果这两者都没有被显示地指定的话。要抑制第一个 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列的自动化属性，使用这些策略中的一个：

* 启用 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 系统变量。在这种情况下，指定自动初始化和更新的 **DEFAULT CURRENT_TIMESTAMP** 和 **ON UPDATE CURRENT_TIMESTAMP** 从句是可用的，但是不会被指派给任何 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列除非显示地包含在列的定义中。

* 另一种选择，如果 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 被禁用，做下面的其中一个操作：

    * 用一个 **DEFAULT** 从句为列定义一个常量默认值。

    * 指定 **NULL** 属性。这也导致列允许 **NULL** 值，意味着你不能通过为列设置 **NULL** 来指定当前时间戳。设定 **NULL** 会设置列为 **NULL**，而不是当前时间戳。指派当前时间戳，设置列为 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 或者一个同义词如 [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)。

细想这些表的定义：

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts1 TIMESTAMP DEFAULT 0,
    -> ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.17 sec)

mysql> CREATE TABLE t2 (
    -> name VARCHAR(20) NOT NULL,
    -> ts1 TIMESTAMP NULL,
    -> ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE t3 (
    -> name VARCHAR(20) NOT NULL,
    -> ts1 TIMESTAMP NULL DEFAULT 0,
    -> ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.01 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-27 10:38:30 |
+---------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO t1 (name)
    -> VALUES ('NOTEBOOK');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO t2 (name)
    -> VALUES ('COMPUTER');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO t3 (name)
    -> VALUES ('MOUSE');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+----------+---------------------+---------------------+
| name     | ts1                 | ts2                 |
+----------+---------------------+---------------------+
| NOTEBOOK | 0000-00-00 00:00:00 | 2018-12-27 10:39:38 |
+----------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select * from t2;
+----------+------+---------------------+
| name     | ts1  | ts2                 |
+----------+------+---------------------+
| COMPUTER | NULL | 2018-12-27 10:40:15 |
+----------+------+---------------------+
1 row in set (0.01 sec)

mysql> select * from t3;
+-------+---------------------+---------------------+
| name  | ts1                 | ts2                 |
+-------+---------------------+---------------------+
| MOUSE | 0000-00-00 00:00:00 | 2018-12-27 10:40:53 |
+-------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET name='Notebook' where name='NOTEBOOK';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE t2 SET name='Computer' where name='COMPUTER';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE t3 SET name='Mouse' where name='MOUSE';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+----------+---------------------+---------------------+
| name     | ts1                 | ts2                 |
+----------+---------------------+---------------------+
| Notebook | 0000-00-00 00:00:00 | 2018-12-27 10:42:11 |
+----------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select * from t2;
+----------+------+---------------------+
| name     | ts1  | ts2                 |
+----------+------+---------------------+
| Computer | NULL | 2018-12-27 10:42:40 |
+----------+------+---------------------+
1 row in set (0.00 sec)

mysql> select * from t3;
+-------+---------------------+---------------------+
| name  | ts1                 | ts2                 |
+-------+---------------------+---------------------+
| Mouse | 0000-00-00 00:00:00 | 2018-12-27 10:43:12 |
+-------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-27 10:43:55 |
+---------------------+
1 row in set (0.00 sec)

mysql> UPDATE t1 SET ts1=NULL where name='Notebook';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+----------+---------------------+---------------------+
| name     | ts1                 | ts2                 |
+----------+---------------------+---------------------+
| Notebook | 2018-12-27 11:02:01 | 2018-12-27 11:02:01 |
+----------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-12-27 11:02:47 |
+---------------------+
1 row in set (0.00 sec)

mysql> 
```

这些表有这些属性：

* 在每一个表的定义中，第一个 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列没有自动初始化或更新。

* 这些表的不同在于 **ts1** 列如何处理 **NULL** 值。对于表 t1，**ts1** 是 NOT NULL 且给它指派一个 **NULL** 值会将它设置为当前时间戳。对于表 t2 和 t3，**ts1** 允许 **NULL** 且给它指派一个 **NULL** 值会将它设置为 **NULL**。

* t2 和 t3 的不同在于 **ts1** 的默认值。对于表 t2，**ts1** 被定义为允许 **NULL**，所以在缺乏一个明确的 **DEFAULT** 从句时它的默认值也是 **NULL**。对于表 t3，**ts1** 允许 **NULL** 但是它有一个明确的默认值0。

**注意：** MySQL 5.5及以下版本仅支持为TIMESTAMP自动初始化和更新。

不管在哪里如果 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 或 [DATETIME](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列的定义中包含了一个明确的小数秒精度值，则在整个列的定义中必须使用相同的精度值。这是允许的：

```sql
CREATE TABLE t1 (
  ts TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
);
```

这是不允许的：

```sql
CREATE TABLE t1 (
  ts TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(3)
);
```

**TIMESTAMP 初始化及 NULL 属性**

如果 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 系统变量被禁用，[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列默认情况下是 **NOT NULL**，不能包含 **NULL** 值，且设定 **NULL** 会赋值为当前时间戳。要允许 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列包含 **NULL**，用 **NULL** 属性明确地声明它。在这种情况下，默认值也变成 **NULL** 除非用一个 **DEFAULT** 从句指定一个不同的默认值来覆盖它。**DEFAULT NULL** 可以被用来明确地指定 **NULL** 作为默认值。（对于一个没有声明 **NULL** 属性的 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列，**DEFAULT NULL** 是无效的。）如果 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列允许 **NULL** 值，指派 **NULL** 会将其设置为 **NULL**，而不是当前时间戳。

下边包含了几种允许 **NULL** 值的 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列：

```sql
mysql> CREATE TABLE t (
    -> name VARCHAR(20) NOT NULL,
    -> ts1 TIMESTAMP NULL DEFAULT NULL,
    -> ts2 TIMESTAMP NULL DEFAULT 0,
    -> ts3 TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t (name)
    -> VALUES ('BEE');
Query OK, 1 row affected (0.01 sec)

mysql> select * from t;
+------+------+---------------------+---------------------+
| name | ts1  | ts2                 | ts3                 |
+------+------+---------------------+---------------------+
| BEE  | NULL | 0000-00-00 00:00:00 | 2018-12-28 19:37:42 |
+------+------+---------------------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

一个允许 **NULL** 值的 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列在插入时间上不会取当前时间戳除非有下列情形之一：

* 它的默认值被定义为 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 且没有为列指定值

* [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 或任何它的同义词如 [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now) 被明确地插入到列中

换句话说，一个定义为允许 **NULL** 值的 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列仅当它的定义包含 **DEFAULT CURRENT_TIMESTAMP** 时才能自动初始化：

```sql
mysql> CREATE TABLE t (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO t (name)
    -> VALUES ('TEA');
Query OK, 1 row affected (0.00 sec)

mysql> select * from t;
+------+---------------------+
| name | ts                  |
+------+---------------------+
| TEA  | 2018-12-28 19:54:04 |
+------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

如果 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列允许 **NULL** 值但是它的定义不包含 **DEFAULT CURRENT_TIMESTAMP**，你必须明确地插入一个对应当前日期和时间的值。假设表 t1 和 t2 有这些定义：

```sql
CREATE TABLE t1 (ts TIMESTAMP NULL DEFAULT '0000-00-00 00:00:00');
CREATE TABLE t2 (ts TIMESTAMP NULL DEFAULT NULL);
```

设置两个表的 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列为插入时的当前时间戳，明确地给它赋那个值。例如：

```sql
INSERT INTO t2 VALUES (CURRENT_TIMESTAMP);
INSERT INTO t1 VALUES (NOW());
```

```sql
mysql> CREATE TABLE t1 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP NULL DEFAULT 0
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> CREATE TABLE t2 (
    -> name VARCHAR(20) NOT NULL,
    -> ts TIMESTAMP NULL DEFAULT NULL
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql> INSERT INTO t1 (name, ts)
    -> VALUES ('MySQL', NOW());
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO t2 (name, ts)
    -> VALUES ('Python', CURRENT_TIMESTAMP);
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+-------+---------------------+
| name  | ts                  |
+-------+---------------------+
| MySQL | 2018-12-29 16:28:54 |
+-------+---------------------+
1 row in set (0.00 sec)

mysql> select * from t2;
+--------+---------------------+
| name   | ts                  |
+--------+---------------------+
| Python | 2018-12-29 16:30:42 |
+--------+---------------------+
1 row in set (0.00 sec)

mysql> 
```

如果 [explicit_defaults_for_timestamp](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) 系统变量被启用，仅当声明了 **NULL** 属性 [TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列才允许 **NULL** 值。同样，[TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/datetime.html) 列不允许指派 **NULL** 以赋值为当前时间戳，不管是声明 **NULL** 还是 **NOT NULL** 属性。要赋值当前时间戳，将列设置为 [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 或者一个同义词如 [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)。

### 12.5 字符串函数
**字符串操作符**

**Name**           |**Description**
-------------------|---------------
[CHAR_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length)      |返回参数中字符的个数
[CHARACTER_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_character-length) |CHAR_LENGTH() 的同义词

* [CHAR_LENGTH(str)](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length)

  返回字符串 *str* 的长度，以字符度量。一个多字节字符视为一个单一的字符。这意味对于一个包含5个双字节字符的字符串，[LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_length) 返回10，然而 [CHAR_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length) 返回5。

* [CHARACTER_LENGTH(str)](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_character-length)

  [CHARACTER_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_character-length) 是 [CHAR_LENGTH()](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char-length) 的一个同义词。

```sql
SELECT count(*) FROM SMS_MESSAGE_TASK_HISTORY m,EDU_SCHOOL s where m.SCHOOL_ID=s.SCHOOL_ID and
date_format(SEND_TIME, '%Y-%m')='2018-10' and char_length(m.content)>280 and char_length(m.content)<=350;
```

查询2018年10月份SMS_MESSAGE_TASK_HISTORY表中content字段的字符数大于280且小于等于350的记录数。

### 12.7 日期和时间函数
**日期和时间函数**

Name                                    |Description
----------------------------------------|------------
[CURRENT_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp), [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp)  |NOW() 的同义词
[DATE_FORMAT()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format)  |将date格式化为指定的形式
[NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)  |返回当前的日期和时间

每个查询中每个返回当前日期和时间的函数仅在查询开始执行时计算一次。这意味着在一个单一查询中多次引用一个函数如 [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now) 总是产生相同的结果。

* [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp), [CURRENT_TIMESTAMP([fsp])](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp)

  [CURRENT_TIMESTAMP](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 和 [CURRENT_TIMESTAMP()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_current-timestamp) 是 [NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now) 的同义词。

* [NOW([fsp])](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)

  以 'YYYY-MM-DD HH:MM:SS' 或 YYYYMMDDHHMMSS 格式返回当前的日期和时间作为一个值，取决于这个函数是用于一个字符串还是数字环境。这个值用当前时区来展示。

  如果 *fsp* 参数给出并从0到6指定了一个小数秒精度，则返回值包含一个指定位数的小数秒部分。

MySQL 5.5.37，默认小数秒精度为6。

```sql
mysql> select NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2018-12-05 19:55:04 |
+---------------------+
1 row in set (0.00 sec)

mysql> select NOW() + 0;
+-----------------------+
| NOW() + 0             |
+-----------------------+
| 20181205195511.000000 |
+-----------------------+
1 row in set (0.00 sec)

mysql> select NOW(2);
+---------------------+
| NOW(2)              |
+---------------------+
| 2018-12-06 10:32:02 |
+---------------------+
1 row in set (0.00 sec)

mysql> select NOW(2) + 0;
+-----------------------+
| NOW(2) + 0            |
+-----------------------+
| 20181206103215.000000 |
+-----------------------+
1 row in set (0.00 sec)

mysql> select version();
+------------+
| version()  |
+------------+
| 5.5.37-log |
+------------+
1 row in set (0.00 sec)

```

MariaDB 5.5.60，默认小数秒精度为0。

```sql
MariaDB [mysql]> select NOW();                                                                       
+---------------------+
| NOW()               |
+---------------------+
| 2018-12-05 20:04:58 |
+---------------------+
1 row in set (0.01 sec)

MariaDB [mysql]> select NOW() + 0;
+----------------+
| NOW() + 0      |
+----------------+
| 20181205200512 |
+----------------+
1 row in set (0.00 sec)

MariaDB [mysql]> select NOW(2);
+------------------------+
| NOW(2)                 |
+------------------------+
| 2018-12-05 20:07:31.38 |
+------------------------+
1 row in set (0.01 sec)

MariaDB [mysql]> select NOW(2) + 0;
+-------------------+
| NOW(2) + 0        |
+-------------------+
| 20181205200737.46 |
+-------------------+
1 row in set (0.01 sec)

MariaDB [mysql]> select version();
+----------------+
| version()      |
+----------------+
| 5.5.60-MariaDB |
+----------------+
1 row in set (0.00 sec)

```

[NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now) 返回一个常量时间指明语句开始执行的时间。（在一个存储函数或触发器中，[NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now) 返回函数或触发语句开始执行的时间。）这与 [SYSDATE()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_sysdate) 返回它执行时的准确时间的行为不同。

```sql
mysql> SELECT NOW(), SLEEP(2), NOW();
+---------------------+----------+---------------------+
| NOW()               | SLEEP(2) | NOW()               |
+---------------------+----------+---------------------+
| 2018-12-06 11:02:13 |        0 | 2018-12-06 11:02:13 |
+---------------------+----------+---------------------+
1 row in set (2.00 sec)

mysql> SELECT SYSDATE(), SLEEP(2), SYSDATE();
+---------------------+----------+---------------------+
| SYSDATE()           | SLEEP(2) | SYSDATE()           |
+---------------------+----------+---------------------+
| 2018-12-06 11:03:09 |        0 | 2018-12-06 11:03:11 |
+---------------------+----------+---------------------+
1 row in set (2.00 sec)

```

### 13.1.9 ALTER TABLE语法

```sql
ALTER TABLE tbl_name
    [alter_specification [, alter_specification] ...]
    [partition_options]

alter_specification:
    table_options
  | ADD [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ADD [COLUMN] (col_name column_definition,...)
  | ADD {INDEX|KEY} [index_name]
        [index_type] (key_part,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]] PRIMARY KEY
        [index_type] (key_part,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]]
        UNIQUE [INDEX|KEY] [index_name]
        [index_type] (key_part,...) [index_option] ...
  | ADD FULLTEXT [INDEX|KEY] [index_name]
        (key_part,...) [index_option] ...
  | ADD SPATIAL [INDEX|KEY] [index_name]
        (key_part,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]]
        FOREIGN KEY [index_name] (col_name,...)
        reference_definition
  | ALGORITHM [=] {DEFAULT|INSTANT|INPLACE|COPY}
  | ALTER [COLUMN] col_name {SET DEFAULT literal | DROP DEFAULT}
  | ALTER INDEX index_name {VISIBLE | INVISIBLE}
  | CHANGE [COLUMN] old_col_name new_col_name column_definition
        [FIRST|AFTER col_name]
  | [DEFAULT] CHARACTER SET [=] charset_name [COLLATE [=] collation_name]
  | CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
  | {DISABLE|ENABLE} KEYS
  | {DISCARD|IMPORT} TABLESPACE
  | DROP [COLUMN] col_name
  | DROP {INDEX|KEY} index_name
  | DROP PRIMARY KEY
  | DROP FOREIGN KEY fk_symbol
  | FORCE
  | LOCK [=] {DEFAULT|NONE|SHARED|EXCLUSIVE}
  | MODIFY [COLUMN] col_name column_definition
        [FIRST | AFTER col_name]
  | ORDER BY col_name [, col_name] ...
  | RENAME COLUMN old_col_name TO new_col_name
  | RENAME {INDEX|KEY} old_index_name TO new_index_name
  | RENAME [TO|AS] new_tbl_name
  | {WITHOUT|WITH} VALIDATION
  | ADD PARTITION (partition_definition)
  | DROP PARTITION partition_names
  | DISCARD PARTITION {partition_names | ALL} TABLESPACE
  | IMPORT PARTITION {partition_names | ALL} TABLESPACE
  | TRUNCATE PARTITION {partition_names | ALL}
  | COALESCE PARTITION number
  | REORGANIZE PARTITION partition_names INTO (partition_definitions)
  | EXCHANGE PARTITION partition_name WITH TABLE tbl_name [{WITH|WITHOUT} VALIDATION]
  | ANALYZE PARTITION {partition_names | ALL}
  | CHECK PARTITION {partition_names | ALL}
  | OPTIMIZE PARTITION {partition_names | ALL}
  | REBUILD PARTITION {partition_names | ALL}
  | REPAIR PARTITION {partition_names | ALL}
  | REMOVE PARTITIONING
  | UPGRADE PARTITIONING

key_part: {col_name [(length)] | (expr)} [ASC | DESC]

index_type:
    USING {BTREE | HASH}

index_option:
    KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
  | {VISIBLE | INVISIBLE}

table_options:
    table_option [[,] table_option] ...

table_option:
    AUTO_INCREMENT [=] value
  | AVG_ROW_LENGTH [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB'|'LZ4'|'NONE'}
  | CONNECTION [=] 'connect_string'
  | {DATA|INDEX} DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTION [=] {'Y' | 'N'}
  | ENGINE [=] engine_name
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] value
  | MAX_ROWS [=] value
  | MIN_ROWS [=] value
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT|DYNAMIC|FIXED|COMPRESSED|REDUNDANT|COMPACT}
  | STATS_AUTO_RECALC [=] {DEFAULT|0|1}
  | STATS_PERSISTENT [=] {DEFAULT|0|1}
  | STATS_SAMPLE_PAGES [=] value
  | TABLESPACE tablespace_name [STORAGE {DISK|MEMORY|DEFAULT}]
  | UNION [=] (tbl_name[,tbl_name]...)

partition_options:
    (see CREATE TABLE options)
```

[ALTER TABLE](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html) 改变一个表的结构。例如，你可以增加或删除列，创建或销毁索引，改变已存在的列的类型，或者重命名列或表本身。你也可以改变特性如用于表或表注释的存储引擎。

**ALTER TABLE** 语句有几个额外的方面，在这节中按下面的主题描述：

* [表选项](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-options)

* [Performance and Space Requirements](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-performance)

* [Concurrency Control](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-concurrency)

* [Adding and Dropping Columns](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-add-drop-column)

* [重命名，重定义，及重新排序列](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-redefine-column)

* [Primary Keys and Indexes](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-index)

* [Foreign Keys](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-foreign-key)

* [Changing the Character Set](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-character-set)

* [Discarding and Importing InnoDB Tablespaces](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-discard-import)

* [Row Order for MyISAM Tables](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-row-order)

* [Partitioning Options](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-partition-options)
<br><br>

**表选项**

*table_options* 表示可以被用在 [CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html) 语句中的表选项，例如 **ENGINE**，**AUTO_INCREMENT**，**AVG_ROW_LENGTH**，**MAX_ROWS**，**ROW_FORMAT**，或 **TABLESPACE**。

* 改变表的默认字符集：

```sql
ALTER TABLE t1 CHARACTER SET = utf8;
```

另请参见 [改变字符集](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-character-set)。

* 增加（或改变）一个表的注释：

```sql
ALTER TABLE t1 COMMENT = 'New table comment';
```

**重命名，重定义，及重新排序列**

**CHANGE**，**MODIFY**，**RENAME COLUMN**，和 **ALTER** 从句使已存在的列的名字和定义能够被修改。它们有这些比较而言的特性：

* CHANGE:

    * 可以重命名一个列和修改它的定义，或者两者。

    * 它比 **MODIFY** 或 **RENAME COLUMN** 有更好的兼容性，但对于一些操作有便利性的代价。**CHANGE** 要求命名列两次如果不重命名它，及要求重新指定列的定义如果仅重命名它。

    * 与 **FIRST** 或 **AFTER** 一起使用时，可以重新排序列。

* MODIFY:

    * 可以改变一个列的定义但不能改变它的名字。

    * 改变一个列的定义不需要重命名它，比 **CHANGE** 更方便。

    * 和 **FIRST** 或 **AFTER** 一起使用时，可以重新排序列。

* RENAME COLUMN:

    * 可以改变一个列的名字，但不能改变它的定义。

    * 重命名一个列不需要改变它的定义，比 **CHANGE** 更方便。

* ALTER: 仅用于改变一个列的默认值。

**CHANGE** 是 MySQL 对标准 SQL 的一个扩展。**MODIFY** 和 **RENAME COLUMN** 是 MySQL 用于兼容 Oracle 的扩展。

修改列的定义使用 **CHANGE** 或 **MODIFY**，定义必须包含数据类型和所有应该应用到新列的属性，除了索引属性如 **PRIMARY KEY** 或 **UNIQUE**。出现在原始定义中但没有在新列中指定的属性不会转入。假设一个列 **col1** 被定义为 **INT UNSIGNED DEFAULT 1 COMMENT 'my column'** 然后你按下面的语句修改列，未来改变的仅有 **INT** 到 **BIGINT**：

```sql
ALTER TABLE t1 MODIFY col1 BIGINT;
```

上面的语句将数据类型从 **INT** 改为 **BIGINIT**，但它也丢弃了 **UNSIGNED**，**DEFAULT**，和 **COMMENT** 属性。要保留它们，语句必须明确地包含它们：

```sql
ALTER TABLE t1 MODIFY col1 BIGINT UNSIGNED DEFAULT 1 COMMENT 'my column';
```

### 13.2.6 INSERT语法

```sql
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {VALUES | VALUE} (value_list) [, (value_list)] ...
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    SELECT ...
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```

**INSERT INTO语法**  

用两种方式写 INSERT INTO 语句是可能的。

第一种方式指定列名和要被插入的值：

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

如果你为表格的所有列增加值，你不必在 SQL 查询中指定列名。然而，请确保值的顺序与表格中的列的顺序相同。INSERT INTO 语法将会如下：

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

### 13.2.10 SELECT语法

```sql
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
      [HIGH_PRIORITY]
      [STRAIGHT_JOIN]
      [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
      SQL_NO_CACHE [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [FROM table_references
      [PARTITION partition_list]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]
    [WINDOW window_name AS (window_spec)
        [, window_name AS (window_spec)] ...]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        export_options
      | INTO DUMPFILE 'file_name'
      | INTO var_name [, var_name]]
    [FOR {UPDATE | SHARE} [OF tbl_name [, tbl_name] ...] [NOWAIT | SKIP LOCKED] 
      | LOCK IN SHARE MODE]]
```

* LIMIT 子句可以用来约束 [SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html) 语句返回的行数。LIMIT 带一个或两个数字参数，且数字参数都必须是非负的整型数常量，有这些例外：

    * Within prepared statements, LIMIT 参数可以用占位符标记 ? 来指定。

    * Within stored programs, LIMIT 参数可以用整型数值的程序参数或本地变量来指定。

带一个参数时，这个值指定从结果集的开头返回的行数：

```sql
SELECT * FROM tbl LIMIT 5;     # 检索最前面的5行
```

#### 13.2.10.1 SELECT ... INTO语法
[SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html) 的 [SELECT ... INTO](https://dev.mysql.com/doc/refman/8.0/en/select-into.html) 形式可以将一个查询结果存储到变量中或者将其写入到一个文件中：

* SELECT ... INTO *var_list* 选择列值并将它们存储到变量中。

* SELECT ... INTO OUTFILE 将选择的行写入到一个文件中。列分隔符和行分隔符可以被指定以生成一个特定的输出格式。

* SELECT ... INTO DUMPFILE 将一个单一的行写入到一个文件，不带任何格式。

[SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html) 语法描述 (参见章节 [13.2.10, “SELECT Syntax”](https://dev.mysql.com/doc/refman/8.0/en/select.html)) 在靠近语句的末尾处展示 INTO 从句。在 *select_expr* 列表后面紧跟 INTO 从句也是可以的。

[SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html) 的 [SELECT ... INTO OUTFILE '*file_name*'](https://dev.mysql.com/doc/refman/8.0/en/select-into.html) 形式将选择的行写入到一个文件中。这个文件在服务器主机上被创建，所以为了使用这个语法你必须拥有 [FILE](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_file) 权限。*file_name* 不能是一个已存在的文件，which among other things prevents files such as /etc/passwd and database tables from being destroyed. 系统变量 [character_set_filesystem](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_character_set_filesystem) 控制这个文件名的解释。

[SELECT ... INTO OUTFILE](https://dev.mysql.com/doc/refman/8.0/en/select-into.html) 语句的主要目的是让你非常快地将一个表转储到服务器上的一个文本文件中。如果你想在其他主机而不是服务器主机上创建一个结果文件，你通常不能使用 [SELECT ... INTO OUTFILE](https://dev.mysql.com/doc/refman/8.0/en/select-into.html) 因为还没有办法写一个相对于服务器主机的文件系统的文件路径。

然而，如果在远程主机上安装了 MySQL 客户端软件，你可以使用一个客户端命令如 mysql -e "SELECT ..." > *file_name* 在客户端主机上生成这个文件替代。

在一个除了服务器主机的不同主机上创建结果文件也是可能的，如果远程主机上的文件的位置可以在服务器的文件系统上通过一个网络映射的路径访问的话。在这种情况下，不要求目标机器上存在 [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) (或其他 MySQL 客户端程序)。

[SELECT ... INTO OUTFILE](https://dev.mysql.com/doc/refman/8.0/en/select-into.html) 是 [LOAD DATA INFILE](https://dev.mysql.com/doc/refman/8.0/en/load-data.html) 的补充。列值转换成 CHARACTER SET 从句中指定的字符集后被写入。如果不存在这样的从句，值将被使用二进制字符集转储。实际上，没有字符集转换。如果一个结果集包含的列有各自的字符集，则输出数据文件将同样如此，然后你可能不能正确地加载这个文件。

这个语句的 *export_options* 部分包含的 FIELDS 和 LINES 从句的语法与 [LOAD DATA INFILE](https://dev.mysql.com/doc/refman/8.0/en/load-data.html) 语句所使用的语法是相同的。关于 FIELDS 和 LINES 从句的信息，包括它们的默认值和允许的值，参见 [Section 13.2.7, “LOAD DATA INFILE Syntax”](https://dev.mysql.com/doc/refman/8.0/en/load-data.html)。

FIELDS ESCAPED BY 控制如何写特殊字符。如果 FIELDS ESCAPED BY character 是非空的，it is used when necessary to avoid ambiguity as a prefix that precedes following characters on output:

* The FIELDS ESCAPED BY character

* The FIELDS [OPTIONALLY] ENCLOSED BY character

* The first character of the FIELDS TERMINATED BY and LINES TERMINATED BY values

* ASCII NUL (the zero-valued byte; what is actually written following the escape character is ASCII 0, not a zero-valued byte)

FIELDS TERMINATED BY, ENCLOSED BY, ESCAPED BY, 或 LINES TERMINATED BY 字符 *必须* 必须被转义以便你能可靠地读回这个文件。ASCII NUL is escaped to make it easier to view with some pagers.

结果文件不必遵照SQL语法，所以没有别的东西需要被转义。

如果 FIELDS ESCAPED BY 字符为空，没有字符被转义且 NULL 输出为 NULL，而不是 \N。指定一个空转义字符很可能不是一个好主意，particularly if field values in your data contain any of the characters in the list just given.

这是一个生成一个被很多程序使用的逗号分隔值（CSV）格式的文件的例子：

```sql
SELECT a,b,a+b INTO OUTFILE '/tmp/result.txt'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM test_table;
```

如果你使用 INTO DUMPFILE 代替 INTO OUTFILE，MySQL 将仅写一行到文件中，不带任何列或行终止符以及不执行任何转义处理。如果你想在一个文件中存储一个 [BLOB](https://dev.mysql.com/doc/refman/8.0/en/blob.html) 值，这是有用的。

**注意**

由 INTO OUTFILE 或 INTO DUMPFILE 创建的任何文件对于服务器主机上的所有用户都是可写的。这个原因是 MySQL server 不能创建一个属于除了运行 MySQL server的用户以外的任何用户的文件。 (你应该永远不要使用 root 用户运行 [mysqld](https://dev.mysql.com/doc/refman/8.0/en/mysqld.html) 也是因为这个和其它原因。) 这个文件因此必须是全局可写的以便你可以操作它的内容。

如果系统变量 [secure_file_priv](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_secure_file_priv) 被设置为一个非空目录名，被写入的文件必须放在那个目录。

```sql
mysql> SELECT m.RECEIVE_NUM,m.SEND_TIME,m.CONTENT,s.SCHOOL_NAME 
FROM ISCHOOLYARD.SMS_MESSAGE_TASK_HISTORY m, ISCHOOLYARD.EDU_SCHOOL s 
where m.SCHOOL_ID=s.SCHOOL_ID and date_format(SEND_TIME, '%Y-%m')='2018-10' 
INTO OUTFILE '/tmp/201810.csv' 
FIELDS TERMINATED BY ',' ENCLOSED BY '"';
```

将2018年10月份的短信记录导出到服务器上的/tmp目录下，文件名为201810.csv。

# Anaconda
**Windows平台**  
使用conda命令时，建议通过下面的方式打开终端：  
Anaconda Navigator——Environments——base (root)——Open Terminal

# Android Studio
下载地址：[https://developer.android.com/studio](https://developer.android.com/studio)  

Linux平台安装Android Studio  
1. 直接将 android-studio-ide-182.5314842-linux.zip 解压到要安装的目录下，推荐解压到 /opt 目录；  
2. 进入 /opt/android-studio/bin 目录，执行 `./studio.sh` 命令；
3. 安装好后，以后直接 `./stuido.sh` 命令即可启动 Android Studio。

# Appium
GitHub：[https://github.com/appium/appium](https://github.com/appium/appium)  
官方网站：[http://appium.io](http://appium.io)  
官方文档：[http://appium.io/docs/cn/about-appium/intro/](http://appium.io/docs/cn/about-appium/intro/)  
下载链接：[https://github.com/appium/appium-desktop/releases](https://github.com/appium/appium-desktop/releases)  
Python Client：[https://github.com/appium/python-client](https://github.com/appium/python-client)  

## 安装Appium
安装Appium有两种方式，一种是直接下载安装包 Appium Desktop 来安装，另一种是通过 Node.js 的包管理器npm来安装。

### Appium Desktop
Windows和macOS平台推荐直接到 [https://github.com/appium/appium-desktop/releases](https://github.com/appium/appium-desktop/releases) 页面下载对应的安装包（分别是 appium-desktop-setup-1.11.0.exe
 和 Appium-1.11.0.dmg
）来安装。  

Linux平台推荐通过 npm 来进行安装。  
Ubuntu 18.04.2 LTS

```sh
# apt-get update
# apt-get install npm
# npm install -g appium
# appium
[Appium] Welcome to Appium v1.12.0
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

通过系统源中的npm命令（由npm包提供）安装appium时（`npm install -g appium`），会提示：

```
WARN engine appium@1.12.0: wanted: {"node":">=8","npm":">=6"} (current: {"node":"8.10.0","npm":"3.5.2"})
```

所以在下面的CentOS 7.6中我们通过nvm来安装新版本的Node.js，以提供appium期望的node版本和npm版本（EPEL源中的nodejs 6.16.0和npm 3.10.10的版本较旧）。

CentOS 7.6  
安装appium的过程中需要用到jar命令，所以需要事先安装相应的依赖包：

```sh
# yum install java-1.8.0-openjdk-devel
```

```sh
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
$ command -v nvm
nvm
```sh

如果没有输出nvm，执行下面的命令：

```sh
$ source ~/.bashrc
```

如果当前用户使用的Shell是zsh，则将下面的内容添加到 `~/.zshrc` 文件中：

```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

之后再执行 `source ~/.zshrc` 命令。

```sh
$ nvm install v10.15.3
$ npm install -g appium
```

对于root用户，通过npm安装appium时，必须加上 `--unsafe-perm` 参数：

```sh
# npm install -g appium --unsafe-perm
```

如果没有加上 `--unsafe-perm` 参数，会出现类似下面的错误提示：

```
Error: EACCES: permission denied, mkdir '/usr/local/node10/lib/node_modules/appium/node_modules/appium-c
hromedriver/2019220-30468-q3igt0.f1o6'
```

因为安装appium时，会到 [https://chromedriver.storage.googleapis.com](https://chromedriver.storage.googleapis.com) 站点下载 `chromedri
ver_linux64.zip`，所以如果因网络问题而无法安装的话，需要为npm设置代理

```
[14:37:01] [Chromedriver Install] Downloading https://chromedriver.storage.googleapis.com/2.46/chromedri
ver_linux64.zip...
```

```sh
$ npm config set proxy http://192.168.2.10:8118
$ npm config set https-proxy http://192.168.2.10:8118
```

删除代理设置：

```sh
$ npm config delete proxy
$ npm config delete https-proxy
```

# Charles
官方网站：[https://www.charlesproxy.com](https://www.charlesproxy.com)  
下载链接：[https://www.charlesproxy.com/download](https://www.charlesproxy.com/download)  

安装Charles根证书  
Windows平台  

1. Help——SSL Proxying——Install Charles Root Certificate；
2. 安装证书——本地计算机(L)——将所有的证书都放入下列存储(P)——受信任的根证书颁发机构。

macOS平台  

1. Help——SSL Proxying——Install Charles Root Certificate；
2. 在弹出的对话框中选择“添加”；
3. 在“钥匙串访问”窗口中，找到“Charles Proxy CA”，之后双击；
4. 在弹出的对话框中展开“信任”，在“使用此证书时”右边的下拉列表框中选择“始终信任”。

# ChromeDriver
官方网站：[http://chromedriver.chromium.org](http://chromedriver.chromium.org)  
下载地址：[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)  

下载ChromeDriver时需要注意ChromeDriver版本和Chrome版本的对应关系。

在Windows平台下，chromedriver.exe 文件建议复制到Python Scripts目录（即Python安装目录下的Scripts目录）。

在macOS及Linux平台下，chromedriver文件建议复制到/usr/local/bin目录。

**注意用户的一致性：**  
在Linux平台下，若登录图形界面的用户为A，如果在终端中运行的程序最终会调用图形界面程序，应使用A用户运行该程序，切不可用root用户或是其他用户来运行该程序，否则会出现一些异常。

# GeckoDriver
GitHub：[https://github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver)  
下载地址：[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)  

在Windows平台下，建议将geckodriver.exe文件放到Python Scripts目录下。

在Linux和macOS平台下，建议将geckodriver文件复制到/usr/local/bin目录下。

## PhantomJS
官方网站：[http://phantomjs.org](http://phantomjs.org)  
官方文档：[http://phantomjs.org/quick-start.html](http://phantomjs.org/quick-start.html)  
下载地址：[http://phantomjs.org/download.html](http://phantomjs.org/download.html)  
API接口说明：[http://phantomjs.org/api/command-line.html](http://phantomjs.org/api/command-line.html)  

**重要：** PhantomJS 的开发工作目前已暂停。

PhantomJS 是一个无界面的、可以用 JavaScript 进行脚本编程的 web 浏览器。它可以运行在 Windows, macOS, Linux, 和 FreeBSD 上。

**Windows平台**  
将phantomjs-2.1.1-windows.zip解压后，建议直接将bin目录中的phantomjs.exe文件复制到Python Scripts目录。

**Linux平台**  
将phantomjs-2.1.1-linux-x86_64.tar.bz2解压后，建议直接将bin目录下的phantomjs文件复制到/usr/local/bin目录下。

**macOS平台**  
将phantomjs-2.1.1-macosx.zip解压后，建议直接将bin目录下的phantomjs文件复制到/usr/local/bin目录下。

# vim
在vim中输入下面的指令，看vim是否支持python或python3，返回1则表示支持

```vim
:echo has('python') || has('python3')
```

显示当前文件的文件类型

```vim
:set ft?
```

查看你的 `completeopt` 的设置状态

```vim
:set completeopt?
```

**查找**  
在Normal模式下按下`/`，然后输入要查找的字符并按下回车键，vim便会跳转到第一个匹配位置，按`n`查找下一个，按`N`查找上一个。

## vim插件
### YouCompleteMe
#### 命令
**`:YcmDebugInfo`**  
可以查看用于当前文件的编译命令