* [导航](#导航)
* [Markdown](#markdown)
* [Python](#python)
    * [Python标准库](#python标准库)
        * [内置函数](#内置函数)
        * [内置类型](#内置类型)
            * [数值类型 — int, float, complex](#数值类型--int-float-complex)
                * [整型数类型的按位运算](#整型数类型的按位运算)
        * [文件和目录访问](#文件和目录访问)
            * [os.path — 通用路径名操作](#ospath--通用路径名操作)
        * [通用操作系统服务](#通用操作系统服务)
            * [os — 各种各样的操作系统接口](#os--各种各样的操作系统接口)
                * [进程参数](#进程参数)
                * [各种各样的系统信息](#各种各样的系统信息)
        * [并行执行](#并行执行)
            * [threading — 基于线程的并行](#threading--基于线程的并行)
                * [线程对象](#线程对象)
            * [multiprocessing — 基于进程的并行](#multiprocessing--基于进程的并行)
                * [介绍](#介绍)
                    * [进程类](#进程类)
                    * [上下文和启动方法](#上下文和启动方法)
                * [参考](#参考)
                    * [进程和异常](#进程和异常)
                    * [其它](#其它)
        * [互联网协议与支持](#互联网协议与支持)
            * [urllib.parse — 将URLs解析为组件](#urllibparse--将urls解析为组件)
                * [URL解析](#url解析)
    * [Python语言参考](#python语言参考)
        * [3. 数据模型](#3-数据模型)
            * [3.3. 特殊方法名](#33-特殊方法名)
                * [3.3.1. 基本自定义](#331-基本自定义)
                * [3.3.7. 仿真容器类型](#337-仿真容器类型)
    * [PyPI](#pypi)
        * [aiohttp](#aiohttp)
        * [Beautiful Soup](#beautiful-soup)
        * [Django](#django)
            * [settings.py](#settingspy)
        * [Flask](#flask)
        * [lxml](#lxml)
        * [mitmproxy](#mitmproxy)
        * [pip](#pip)
        * [PyMongo](#pymongo)
        * [PyMySQL](#pymysql)
        * [pyquery](#pyquery)
        * [pyspider](#pyspider)
        * [redis-py](#redis-py)
        * [Requests](#requests)
        * [tesserocr](#tesserocr)
        * [Tornado](#tornado)
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
            * [4.5.1.1 mysql选项](#4511-mysql选项)
        * [4.5.4 mysqldump — 一个数据库备份程序](#454-mysqldump--一个数据库备份程序)
        * [11.1.2 日期和时间类型概述](#1112-日期和时间类型概述)
        * [11.3.5 为TIMESTAMP和DATETIME自动初始化和更新](#1135-为timestamp和datetime自动初始化和更新)
        * [12.5 字符串函数](#125-字符串函数)
        * [12.7 日期和时间函数](#127-日期和时间函数)
        * [13.1.9 ALTER TABLE语法](#1319-alter-table语法)
        * [13.2.6 INSERT语法](#1326-insert语法)
        * [13.2.10 SELECT语法](#13210-select语法)
            * [13.2.10.1 SELECT ... INTO语法](#132101-select--into语法)
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

Markdown中的多个空行会被当做一个空行来处理。

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

# Python
## Python标准库
### 内置函数
Python解释器内置了许多总是可用的函数和类型。在这里以字母顺序列出它们。

|          |          |Built-in Functions|          |          |
|----------|----------|------------------|----------|----------|
|          |          |                  |          |super()   |
|          |          |                  |range()   |          |

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

### 内置类型
#### 数值类型 — int, float, complex
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

os.path.**join**(_path, *paths_)  
智能地连接一个或多个路径组件。返回值是 *path* 和所有 _*paths_ 成员的串联，且除了最后一个部分，每一个非空的部分后面都跟着一个正确的目录分隔符 (`os.sep`)，这意味着如果最后一个部分为空则结果将必定以一个分隔符结尾。如果一个组件是一个绝对路径，则所有前面的组件都被丢弃且连接从绝对路径组件继续。

在 Windows 平台，当遇到一个绝对路径组件 (如，`r'\foo'`) 时驱动器号不重置。如果一个组件包含一个驱动器号，则所有前面的组件被丢弃且驱动器号被重置。注意，因为每个驱动器都有一个当前目录，`os.path.join("c:", "foo")` represents a path relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`。

*在版本3.6中发生变化：* *path* 和 *paths* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

## 通用操作系统服务
这章描述的模块提供在（几乎）所有操作系统上都可用的操作系统特征接口，如文件和时钟。这些接口通常是根据 Unix 或 C 接口仿写的，但它们在大多数其它系统下也是可用的。这里是一个概述：

### os — 各种各样的操作系统接口
**源代码：** [Lib/os.py](https://github.com/python/cpython/tree/3.7/Lib/os.py)

这个模块提供了一种便携的方式使用依赖于操作系统的功能。如果你仅仅只想读或写一个文件请看 [open()](https://docs.python.org/3/library/functions.html#open)，如果你想操作路径，请看 [os.path](https://docs.python.org/3/library/os.path.html#module-os.path) 模块，如果你想在命令行下读取所有文件中的所有行请看 [fileinput](https://docs.python.org/3/library/fileinput.html#module-fileinput) 模块。创建临时文件和目录请看 [tempfile](https://docs.python.org/3/library/tempfile.html#module-tempfile) 模块，高级文件和目录处理请看 [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) 模块。

#### 进程参数
这些函数和数据条目提供当前进程和用户的信息及操作。

os.**getpid()**  
返回当前的进程id。

os.**getppid()**  
返回父进程的id。当父进程退出时，在 Unix 上返回的id是其中一个 init 进程 (1)，在 Windows 上它仍是同一个id，这个id有可能已经被另一个进程重用了。

**可用性：** Unix，Windows。

*在版本3.2中发生变化：* 增加对Windows的支持。

#### 各种各样的系统信息

下面的数据值被用于支持路径操作运算。这些是为所有平台定义。

高层次的路径名操作被定义在 [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path) 模块中。

os.**sep**  
操作系统用来分隔路径名组件的字符。POSIX 为 `'/'` 而 Windows 为 `'\\'`。Note that knowing this is not sufficient to be able to parse or concatenate pathnames — 使用 [os.path.split()](https://docs.python.org/3.6/library/os.path.html#os.path.split) 和 [os.path.join()](https://docs.python.org/3.6/library/os.path.html#os.path.join) — 但它偶尔是有用的。Also available via [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path)。

## 并行执行
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

### 互联网协议与支持
#### urllib.parse — 将URLs解析为组件
##### URL解析
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

### Django
Django官网  
[https://www.djangoproject.com](https://www.djangoproject.com)

安装Django  
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

### Flask
GitHub：[https://github.com/pallets/flask](https://github.com/pallets/flask)  
官方文档：[http://flask.pocoo.org](http://flask.pocoo.org)  
中文文档：[http://docs.jinkan.org/docs/flask](http://docs.jinkan.org/docs/flask/)  

安装Flash

```sh
$ pip3 install flask
```

### lxml
官方网站：[https://lxml.de](https://lxml.de)  
GitHub：[https://github.com/lxml/lxml](https://github.com/lxml/lxml)  

安装lxml

```sh
$ pip3 install lxml
```

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

### pip
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
#### 选项
-U, --upgrade  
升级所有指定的包到最新的可用版本。依赖的处理依赖于使用的 upgrade-strategy。

--user  
Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%Python on Windows. (See the Python documentation for site.USER_BASE for full details.)

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
官方文档：[http://www.python-requests.org/en/master/](http://www.python-requests.org/en/master/)  
中文文档：[http://docs.python-requests.org/zh_CN/latest/](http://docs.python-requests.org/zh_CN/latest/)  

**安装requests**  

```sh
$ pip3 install requests
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

### 4.5.1.1 mysql选项
[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 支持下面的选项，下面的选项可以在命令行中或一个选项文件的 [mysql] 和 [client] 组中指定。关于 MySQL 程序使用的选项文件的信息，请看章节 [4.2.7, “Using Option Files”](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)。

**mysql选项**

Format     |Description         |Introduced   |Removed
-----------|--------------------|-------------|-------
[--execute](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute)  |执行指定语句然后退出  |             |      

* [--execute=*statement*](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_execute), -e *statement*

  执行指定语句然后退出。默认输出格式与使用 [--batch](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_batch) 选项的输出相似。对于一些例子，请看章节 [4.2.5, “Using Options on the Command Line”](https://dev.mysql.com/doc/refman/8.0/en/command-line-options.html)。和这个选项一起使用时，[mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) 不使用历史文件。

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
[NOW()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_now)  |返回当前的日期和时间

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