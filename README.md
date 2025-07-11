# Python 文档
主要是我平时使用 Python 时遇到问题后查阅官方文档，之后翻译相应的部分，有些会补充相应的代码。翻译的文档主要来源于 Python 标准库、Python 语言参考、Python 教程及 Pandas 等 Python 第三方库的官方文档。  

[pypi.md](https://github.com/godontop/pydocs/blob/master/pypi.md)  
通过 pip 安装的 Python 包的相关文档及代码。  
<br>  

* [Python 3 标准库](#python-3-标准库)
    * [内置函数](#内置函数)
    * [内置常量](#内置常量)
    * [内置类型](#内置类型)
        * [布尔运算 — and, or, not](#布尔运算--and-or-not)
        * [数值类型 — int, float, complex](#数值类型--int-float-complex)
            * [整型数类型的按位运算](#整型数类型的按位运算)
        * [序列类型 — 列表, 元组, range](#序列类型--列表-元组-range)
            * [通用序列操作](#通用序列操作)
            * [可变序列类型](#可变序列类型)
            * [列表](#列表)
            * [元组](#元组)
            * [Ranges](#ranges)
        * [文本序列类型 — str](#文本序列类型--str)
            * [字符串方法](#字符串方法)
            * [格式化字符串字面值（f-字符串）](#格式化字符串字面值f-字符串)
            * [printf-style 字符串格式化](#printf-style-字符串格式化)
        * [二进制序列类型 — 字节、字节数组、内存视图](#二进制序列类型--字节字节数组内存视图)
            * [字节和字节数组操作](#字节和字节数组操作)
        * [集合类型 --- set, frozenset](#集合类型-----set-frozenset)
        * [映射类型 — 字典](#映射类型--字典)
            * [字典视图对象](#字典视图对象)
        * [上下文管理器类型](#上下文管理器类型)
        * [特殊属性](#特殊属性)
    * [内置异常](#内置异常)
        * [基类](#基类)
        * [具体异常](#具体异常)
            * [OS异常](#os异常)
        * [异常层次结构](#异常层次结构)
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
        * [glob --- Unix 风格的路径名模式扩展](#glob-----unix-风格的路径名模式扩展)
    * [文件格式](#文件格式)
        * [csv — CSV文件读写](#csv--csv文件读写)
            * [模块内容](#模块内容-1)
            * [Writer对象](#writer对象)
    * [通用操作系统服务](#通用操作系统服务)
        * [os --- 各种各样的操作系统接口](#os-----各种各样的操作系统接口)
            * [进程参数](#进程参数)
            * [文件和目录](#文件和目录)
            * [进程管理](#进程管理)
            * [调度程序接口](#调度程序接口)
            * [各种各样的系统信息](#各种各样的系统信息)
        * [io --- 处理流的核心工具](#io-----处理流的核心工具)
            * [高阶模块接口](#高阶模块接口)
            * [类层次结构](#类层次结构)
                * [I/O 基类](#io-基类)
                * [原始文件 I/O](#原始文件-io)
                * [缓冲流](#缓冲流)
                * [文本 I/O](#文本-io)
        * [time — 时间的访问和转化](#time--时间的访问和转化)
            * [函数](#函数)
        * [getopt — C-风格的命令行选项解析器](#getopt--c-风格的命令行选项解析器)
        * [logging --- Python 的日志记录工具](#logging-----python-的日志记录工具)
            * [日志级别](#日志级别)
            * [LogRecord属性](#logrecord属性)
            * [模块级别的函数](#模块级别的函数)
        * [platform --- 获取底层平台的标识数据](#platform-----获取底层平台的标识数据)
        * [ctypes --- Python 的外部函数库](#ctypes-----python-的外部函数库)
            * [ctypes reference](#ctypes-reference)
                * [查找共享库](#查找共享库)
                * [实用函数](#实用函数)
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
            * [使用 subprocess 模块](#使用-subprocess-模块)
                * [常用参数](#常用参数)
            * [较旧的高阶 API](#较旧的高阶-api)
    * [网络和进程间通信](#网络和进程间通信)
        * [socket --- 底层网络接口](#socket-----底层网络接口)
    * [互联网数据处理](#互联网数据处理)
        * [json --- JSON 编码和解码器](#json-----json-编码和解码器)
    * [互联网协议与支持](#互联网协议与支持)
        * [urllib.request — 打开URLs的可扩展库](#urllibrequest--打开urls的可扩展库)
            * [OpenerDirector对象](#openerdirector对象)
        * [urllib.parse — 将URLs解析为组件](#urllibparse--将urls解析为组件)
            * [URL解析](#url解析)
            * [URL 转码](#url-转码)
        * [urllib.error — urllib.request抛出的异常类](#urlliberror--urllibrequest抛出的异常类)
        * [urllib.robotparser — 解析robots.txt](#urllibrobotparser--解析robotstxt)
        * [http.client — HTTP协议客户端](#httpclient--http协议客户端)
            * [HTTPConnection 对象](#httpconnection-对象)
            * [HTTPResponse对象](#httpresponse对象)
        * [socketserver — 一个网络服务器框架](#socketserver--一个网络服务器框架)
            * [服务器对象](#服务器对象)
        * [http.server — HTTP 服务器](#httpserver--http-服务器)
    * [Python运行时服务](#python运行时服务)
        * [sys — 系统专用参量和函数](#sys--系统专用参量和函数)
        * [\_\_main\_\_ --- 顶层代码环境](#__main__-----顶层代码环境)
        * [traceback — 打印或检索堆栈回溯](#traceback--打印或检索堆栈回溯)
            * [TracebackException 对象](#tracebackException-对象)
* [Python语言参考](#python语言参考)
    * [3. 数据模型](#3-数据模型)
        * [3.2. 标准类型层次结构](#32-标准类型层次结构)
        * [3.3. 特殊方法名](#33-特殊方法名)
            * [3.3.1. 基本自定义](#331-基本自定义)
            * [3.3.6. 仿真可调用对象](#336-仿真可调用对象)
            * [3.3.7. 仿真容器类型](#337-仿真容器类型)
    * [4. 执行模型](#4-执行模型)
        * [4.1. 程序的结构](#41-程序的结构)
        * [4.3. 异常](#43-异常)
    * [5. 导入系统](#5-导入系统)
        * [5.1. importlib](#51-importlib)
        * [5.2. 包](#52-包)
        * [5.3. 搜索](#53-搜索)
        * [5.5. 基于路径的查找器](#55-基于路径的查找器)
        * [5.7. 包相对导入](#57-包相对导入)
        * [5.8. 有关 \_\_main\_\_ 的特殊事项](#58-有关-__main__-的特殊事项)
    * [6. 表达式](#6-表达式)
        * [6.14. lambda 表达式](#614-lambda-表达式)
    * [7. 简单语句](#7-简单语句)
        * [7.3. assert语句](#73-assert语句)
        * [7.12. global语句](#712-global语句)
    * [8. 复合语句](#8-复合语句)
        * [8.4. try 语句](#84-try-语句)
        * [8.5. with 语句](#85-with-语句)
* [Python 教程](#python-教程)
    * [2. 使用Python解释器](#2-使用python解释器)
        * [2.1. 调用解释器](#21-调用解释器)
    * [4. 更多控制流工具](#4-更多控制流工具)
        * [4.3. range() 函数](#43-range-函数)
        * [4.4. break 和 continue 语句, 和循环中的 else 子句](#44-break-和-continue-语句-和循环中的-else-子句)
        * [4.9 函数定义详解](#49-函数定义详解)
            * [4.9.6. Lambda 表达式](#496-lambda-表达式)
    * [5. 数据结构](#5-数据结构)
        * [5.1. 列表的更多特性](#51-列表的更多特性)
    * [6. 模块](#6-模块)
        * [6.1. 有关模块的更多信息](#61-有关模块的更多信息)
        * [6.2. 标准模块](#62-标准模块)
        * [6.3. dir() 函数](#63-dir-函数)
        * [6.4. 包](#64-包)
    * [7. 输入和输出](#7-输入和输出)
        * [7.2. 读和写文件](#72-读和写文件)
            * [7.2.1. 文件对象的方法](#721-文件对象的方法)
    * [8. 错误和异常](#8-错误和异常)
        * [8.1. 语法错误](#81-语法错误)
        * [8.2. 异常](#82-异常)
        * [8.3. 处理异常](#83-处理异常)
        * [8.4. 触发异常](#84-触发异常)
        * [8.5. 异常链](#85-异常链)
        * [8.6. 用户自定义异常](#86-用户自定义异常)
        * [8.7. 定义清理操作](#87-定义清理操作)
        * [8.8. 预定义的清理操作](#88-预定义的清理操作)
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
* [Python Snippets](#python-snippets)
    * [proxy.py](#proxypy)
* [Anaconda](#anaconda)
* [Android Studio](#android-studio)
* [Appium](#appium)
* [Charles](#charles)
* [ChromeDriver](#chromedriver)
* [GeckoDriver](#geckodriver)
* [PhantomJS](#phantomjs)


# Python 3 标准库
Python 3 版本：3.6.4——3.8

[Python 语言参考](https://docs.python.org/3/reference/index.html#reference-index)描述的是 Python 语言精确的语法及语义，这个库参考手册描述的是和 Python 一起发布的标准库。它也描述一些通常包含在 Python 发行版中的可选组件。

Python 标准库包含提供访问系统功能如文件 I/O 的内置模块（C 语言所写），这些功能是 Python 程序员原本无法访问的，也包含用 Python 写的为日常编程中出现的许多问题提供标准解决方案的模块。这些模块中的一些的设计通过将特定平台的 APIs 抽象为平台无关的 APIs 明显地鼓励及增强了 Python 程序的可移植性。 

### 内置函数
Python解释器内置了许多总是可用的函数和类型。在这里以字母顺序列出它们。

|          |            |Built-in Functions|          |          |
|----------|------------|------------------|----------|----------|
|abs()     |            |                  |          |          |
|all()     |            |                  |          |          |
|          |            |hex()             |          |          |
|          |            |id()              |object()  |sorted()  |
|          |enumerate() |input()           |          |          |
|          |eval()      |int()             |open()    |          |
|          |            |isinstance()      |ord()     |          |
|          |            |issubclass()      |pow()     |super()   |
|          |            |                  |print()   |          |
|          |            |                  |          |type()    |
|          |            |                  |range()   |          |
|          |getattr()   |                  |repr()    |          |
|          |globals()   |                  |          |          |
|complex() |hasattr()   |                  |          |          |

**abs**(*x*)  
返回一个数的绝对值。参数可以是一个整型数或者一个浮点数。如果参数是一个复数，its magnitude is returned.  

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

**eval(**_expression_**[**, _globals_**[**, _locals_**]]**)  
实参是一个字符串，以及可选的 globals 和 locals。如果提供，*globals* 必须是一个字典。如果提供，*locals* 可以是任何映射对象。  

*expression* 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，使用 *globals* 和 *locals* 字典作为全局和局部命名空间。 如果 *globals* 字典存在且不包含键 `__builtins__` 的值，则会在解析 *expression* 之前在该键下插入对内置模块 [builtins](https://docs.python.org/3.9/library/builtins.html#module-builtins) 字典的引用。 这意味着 *expression* 通常具有对标准 [builtins](https://docs.python.org/3.9/library/builtins.html#module-builtins) 模块的完全访问权限且受限的环境会被传播。 如果省略 *locals* 字典则其默认值为 *globals* 字典。 如果两个字典同时省略，则表达式执行时会使用 [eval()](https://docs.python.org/3.9/library/functions.html#eval) 被调用的环境中的 *globals* 和 *locals*。 请注意，*eval()* 无法访问封闭环境中的[嵌套范围](https://docs.python.org/3.9/glossary.html#term-nested-scope)（非局部）。  

返回值就是表达式的求值结果。 语法错误将作为异常被报告。 例如：  

```python
>>> x = 1
>>> eval('x + 1')
2
>>>
```

这个函数也可以用来执行任何代码对象（如 [compile()](https://docs.python.org/3.9/library/functions.html#compile) 创建的那些）。这种情况下，参数是代码对象，而不是字符串。如果编译该对象时的 *mode* 参数是 `'exec'`，那么 [eval()](https://docs.python.org/3.9/library/functions.html#eval) 的返回值为 `None` 。  

**提示：** [exec()](https://docs.python.org/3.9/library/functions.html#exec) 函数支持动态执行语句。 [globals()](https://docs.python.org/3.9/library/functions.html#globals) 和 [locals()](https://docs.python.org/3.9/library/functions.html#locals) 函数各自返回当前的全局和本地字典，这对于传递给 [eval()](https://docs.python.org/3.9/library/functions.html#eval) 或 [exec()](https://docs.python.org/3.9/library/functions.html#exec) 使用可能很有用。  

另外可以参阅 [ast.literal_eval()](https://docs.python.org/3.9/library/ast.html#ast.literal_eval)，该函数可以安全执行仅包含文字的表达式字符串。  

以代码对象作为参数引发[审计事件](https://docs.python.org/3.9/library/sys.html#auditing) `exec`。 也可能引发代码编译事件。    

**getattr**(*object, name*__[__*, default*__]__)  
返回 *object* 的 *name* 属性的值。*name* 必须是一个字符串。如果这个字符串是这个对象的一个属性的名称，则结果为那个属性的值。例如，`getattr(x, 'foobar')` 等同于 `x.foobar`。如果名称属性不存在，则返回 *default* 如果有提供的话，否则抛出 [AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError)。

```python
>>> class Obj():
...     pass
... 
>>> obj = Obj()
>>> obj.aurows = 7
>>> getattr(obj, 'aurows')
7
>>>
```

**globals()**  
返回实现当前模块命名空间的字典。 对于函数内的代码，这是在定义函数时设置的，并且无论在哪里调用函数都保持不变。  

```python
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> aurows = 7
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'aurows': 7}
>>> globals()['aurows']
7
>>>
```  

**hasattr**(*object, name*)  
参数是一个对象和一个字符串。如果字符串是对象的某个属性的名称则结果为 `True` ，否则返回 `False` 。(这是通过调用 `getattr(object, name)` 并看它是否抛出一个 [AttributeError](https://docs.python.org/3.6/library/exceptions.html#AttributeError) 来实现的。  

**hex**(*x*)  
将一个整型数转换成一个以 "0x" 为前缀的小写字母十六进制字符串。

```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```  

**id**(*object*)  
返回一个对象的 “身份”。在这个对象的生命周期内这是一个保证唯一和不变的整型数。两个生命周期不重叠的对象可能有相同的 [id()](https://docs.python.org/3/library/functions.html#id) 值。

**CPython 实现细节：** 这是对象在内存中的地址。  

```python
>>> class A:
...     def __init__(self):
...         pass
...
>>> a = A()
>>> print(a)
<__main__.A object at 0x000001E4E5391518>
>>> id(a)
2082609894680
>>> hex(id(a))
'0x1e4e5391518'
>>> hex(id(a)).upper()
'0X1E4E5391518'
>>> hex(id(a))[0:2] + hex(id(a))[2:].upper()
'0x1E4E5391518'
>>>
```  

**input([_prompt_])**  
如果存在 *prompt* 实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除去末尾的换行符）并返回。当读取到 EOF 时，则触发 [EOFError](https://docs.python.org/3.7/library/exceptions.html#EOFError)。例如:  

```python
>>> s = input('--> ')
--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"
>>>
```

如果加载了 [readline](https://docs.python.org/3.10/library/readline.html#module-readline) 模块，[input()](https://docs.python.org/3.10/library/functions.html#input) 将使用它来提供复杂的行编辑和历史记录功能。  

在读取输入之前，引发一个 [审计事件](https://docs.python.org/3.10/library/sys.html#auditing) `builtins.input` 附带参数 `prompt`。  

在成功读取输入之后，引发一个 [审计事件](https://docs.python.org/3.10/library/sys.html#auditing) `builtins.input/result` 附带结果。  

*class* **int**(*x=0*)  
*class* **int**(*x, base=10*)  
返回一个从数字或者字符串 *x* 构建的整数对象，如果没有给定参数则返回0。

如果 *x* 不是一个数字或者指定了 *base*，则 *x* 必须是一个表示一个以 *base* 为基数的[整型文字](https://docs.python.org/3.6/reference/lexical_analysis.html#integers)的字符串，[字节](https://docs.python.org/3.6/library/stdtypes.html#bytes)或[字节数组](https://docs.python.org/3.6/library/stdtypes.html#bytearray)实例。*base* 的默认值是10。允许的值是 0 和 2-36. 

将十六进制转换为十进制：

```python
>>> int('0xff', 16)
255
>>> int('0xFF', 16)
255
>>> int('0x9FFF', 16)
40959
```  

**isinstance**(*object, classinfo*)  
Return true if the *object* argument is an instance of the *classinfo* argument, or of a (direct, indirect or [virtual](https://docs.python.org/3.6/glossary.html#term-abstract-base-class)) subclass thereof. 如果 *object* 不是一个指定类型的对象，则函数总是返回 false. If *classinfo* is a tuple of type objects (or recursively, other such tuples), return true if *object* is an instance of any of the types. If *classinfo* is not a type or tuple of types and such tuples, a [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError) exception is raised.
<br />  

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

**ord**(*c*)  
给定一个表示一个Unicode字符的字符串，返回一个代表该字符的Unicode代码点的整型数。例如， `ord('a')` 返回整型数 `97`，`ord('€')` (欧元符号) 返回 `8364`。这是 [chr()](https://docs.python.org/3.6/library/functions.html#chr) 的逆向操作。

函数 ord(c) 返回的是一个十进制整型数。

```python
>>> ord('a')
97
>>> ord('€')
8364
>>> ord('中')
20013
>>> hex(20013)
'0x4e2d'
>>> u'\u4e2d'
'中'
```  

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

**repr(**_object_**)**  
返回一个包含一个对象的可打印表示形式的字符串。 对于许多类型来说，该函数会尝试返回一个字符串，该字符串在被传递给 [eval()](https://docs.python.org/3.9/library/functions.html#eval) 时会产生具有相同值的对象，在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称和通常包括对象名称和地址的附加信息。 类可以通过定义 [\_\_repr\_\_()](https://docs.python.org/3.9/reference/datamodel.html#object.__repr__) 方法来控制此函数为它的实例所返回的内容。  

```python
>>> a = 'string' 
>>> repr(a) 
"'string'"
>>> eval(repr(a)) 
'string'
>>> eval(repr(a)) == a
True
>>> lis = [1, 2, 3]   
>>> repr(lis) 
'[1, 2, 3]'
>>> eval(repr(lis)) == lis
True
>>>
```

**sorted(**_iterable, /, *, key=None, reverse=False_**)** 
根据 iterable 中的项返回一个新的已排序列表。

具有两个可选参数，它们都必须指定为关键字参数。

*key* 指定带有单个参数的函数，用于从 *iterable* 的每个元素中提取用于比较的键 (例如 `key=str.lower`)。 默认值为 `None` (直接比较元素)。

*reverse* 为一个布尔值。 如果设为 `True`，则每个列表元素将按反向顺序比较进行排序。

使用 [functools.cmp_to_key()](https://docs.python.org/zh-cn/3.13/library/functools.html#functools.cmp_to_key) 可将老式的 *cmp* 函数转换为 *key* 函数。

内置的 [sorted()](https://docs.python.org/zh-cn/3.13/library/functions.html#sorted) 确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。

排序算法只使用 `<` 在项目之间比较。 虽然定义一个 [__lt__()](https://docs.python.org/zh-cn/3.13/reference/datamodel.html#object.__lt__) 方法就足以进行排序，但 [PEP 8](https://peps.python.org/pep-0008/) 建议实现所有六个 [富比较](https://docs.python.org/zh-cn/3.13/reference/expressions.html#comparisons) 。 这将有助于避免在与其他排序工具（如 [max()](https://docs.python.org/zh-cn/3.13/library/functions.html#max) ）使用相同的数据时出现错误，这些工具依赖于不同的底层方法。实现所有六个比较也有助于避免混合类型比较的混乱，因为混合类型比较可以调用反射到 [__gt__()](https://docs.python.org/3.13/reference/datamodel.html#object.__gt__) 的方法。

有关排序示例和简要排序教程，请参阅 [排序的技术](https://docs.python.org/3.13/howto/sorting.html#sortinghowto) 。 

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

*class* **type**(*object*)  
*class* **type**(*name, bases, dict*)  
带一个参数时，返回 *object* 的类型。返回值是一种类型对象并且通常和 [object.\_\_class\_\_](https://docs.python.org/3.6/library/stdtypes.html#instance.__class__) 返回相同的对象。

推荐使用内置函数 [isinstance()](https://docs.python.org/3.6/library/functions.html#isinstance) 测试一个对象的类型, because it takes subclasses into account.

```python
>>> obj = "It's a string."
>>> type(obj)
<class 'str'>
>>> obj.__class__
<class 'str'>
>>> isinstance(obj, str)
True
```  

## 内置常量
有一小部分常量在命名空间中。它们是：

**False**  
[bool](https://docs.python.org/3/library/functions.html#bool) 类型的false值。给 `False` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**True**  
[bool](https://docs.python.org/3/library/functions.html#bool) 类型的true值。给 `True` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**None**  
`NoneType` 类型唯一的值。`None` 经常用于表示一个不存在的值，如当默认参数没有传递给函数时。给 `None` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**\_\_debug\_\_**  
如果Python启动时没带 [-O](https://docs.python.org/3/using/cmdline.html#cmdoption-o) 选项则这个常量为真。另请参见 [assert](https://docs.python.org/3/reference/simple_stmts.html#assert) 语句。

**注意：** 名称 [None](https://docs.python.org/3/library/constants.html#None), [False](https://docs.python.org/3/library/constants.html#False), [True](https://docs.python.org/3/library/constants.html#True) 和 [__debug__](https://docs.python.org/3/library/constants.html#__debug__) 不能被再分配 (给它们赋值，哪怕是一个属性名称，也会抛出 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)), 所以它们可以被认为是 “true” 常量。  

## 内置类型
### 布尔运算 — and, or, not
这些是布尔运算，按优先级升序排列：

|Operation   |Result                            |Notes |
|------------|----------------------------------|------|
|`x or y`    |如果x是false，则y，否则x            |(1)   |
|`x and y`   |如果x是false，则x，否则y            |(2)   |
|`not x`     |如果x是false，则`True`，否则`False` |(3)   |

备注：  
1. 这是一个缩短操作，因此仅当第一个参数为false时，它才会计算第二个参数。
2. 这是一个缩短操作，因此仅当第一个参数为true时，它才会计算第二个参数。
3. `not` 的优先级低于非布尔运算，因此 `not a == b` 被解释为 `not (a == b)`, 而 `a == not b` 是一个语法错误。  

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

### 序列类型 — 列表, 元组, range
有三种基本的序列类型：列表，元组, 和 range 对象。专门处理[二进制数据](https://docs.python.org/3/library/stdtypes.html#binaryseq)和[文本字符串](https://docs.python.org/3/library/stdtypes.html#textseq)的额外的序列类型在专门的章节中描述。

#### 通用序列操作
大多数序列类型（不可变的和可变的）都支持下表中的操作。Python 提供的抽象基类 [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence) 使自定义序列类型正确地实现这些操作变得容易。

下表列出的序列操作按优先级升序排列。下表中，*s* 和 *t* 是相同类型的序列，*n*, *i*, *j* 和 *k* 是整型数，*x* 是符合由 *s* 所限制的类型及值的一个任意对象。

Operation   |Result                      |Notes
------------|----------------------------|------
`s[i:j]`    |从 *i* 到 *j* 的 *s* 的分片  |(3)(4)  
`s[i:j:k]`  |*s* 从 *i* 到 *j* 且步长为 *k* 的切片  |(3)(5)  

**注意：**

1. 

2. 

3. 如果 *i* 或 *j* 为负值，则索引是相对于序列 *s* 的末端: 索引号会被替换为 `len(s) + i` 或 `len(s) + j`。 但要注意 `-0` 仍然为 `0`。

```python
>>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[2:-2] 
['c', 'd', 'e']
>>> s[2:len(s) + (-2)]
['c', 'd', 'e']
```

4. 从 *i* 到 *j* 的 *s* 的分片的定义就像序列的元素的索引为 *k* 且 `i <= k < j`。如果 *i* 或 *j* 大于 `len(s)`，使用 `len(s)`。如果 *i* 被忽略或者为 `None`，则使用 `0`。如果 *j* 被忽略或者为 `None`，使用 `len(s)`。如果 `i` 大于或等于 `j`，则分片为空。

```python
>>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> len(s)
7
>>> s[8:16]
[]
>>> s[len(s):len(s)]
[]
>>> s[3:16]
['d', 'e', 'f', 'g']
>>> s[3:len(s)]
['d', 'e', 'f', 'g']
>>>
```

5. *s* 从 *i* 到 *j* 步长为 *k* 的切片被定义为索引为 `x = i + n*k` 的项组成的序列，其中 `0 <= n < (j-i)/k` 的。 换句话说，索引号为 `i`, `i+k`, `i+2*k`, `i+3*k`，以此类推，当达到 *j* 时停止 (但永远不包括 *j*)。 当 *k* 为正值时，*i* 和 *j* 会被减至 `len(s)` 如果它们比 `len(s)` 大的话。 当 *k* 为负值时，*i* 和 *j* 会被减至 `len(s) - 1` 如果它们比 `len(s)` 更大的话。 如果 *i* 或 *j* 被省略或为 `None`，它们会成为“终止”值 (是哪一端的终止值则取决于 *k* 的符号)。 请注意，*k* 不可为零。 如果 *k* 为 `None`，则当作 `1` 处理。

```python
>>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[4:9:1]
['e', 'f', 'g']
>>> s[4:len(s):1] 
['e', 'f', 'g']
>>> s[10:4:-1]
['g', 'f']
>>> s[len(s) - 1:4:-1]
['g', 'f']
>>>
```

如果 *k* 为正，则 *i* 必须小于 *j* ，否则切片为空。  
如果 *k* 为负，则 *i* 必须大于 *j* ，否则切片为空。  

#### 可变序列类型
可变序列定义了下表中的操作。Python 提供的抽象基类 [collections.abc.MutableSequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence) 使自定义序列类型正确地实现这些操作变得更容易。

表中的 *s* 表示可变序列类型的一个实例，*t* 是任何可迭代对象，*x* 是符合由 *s* 所限制的类型及值的一个任意对象 (例如，[bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray) 仅接受符合 `0 <= x <= 255` 值限制的整型数)。

Operation                  |Result                |Notes
---------------------------|----------------------|-----
`s.extend(t)` 或 `s += t`  |用 `t` 的内容扩展 `s`  |  
`s.remove(x)`              |从 *s* 中删除第一个 x，其中 `s[i]` 等于 x  |(3)  

**注意：**  

3. 当在 *s* 中找不到 *x* 时，`remove()` 会引发 [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)。  

```python
>>> s = [1, 2]
>>> t = ('a', 'b')
>>> s.extend(t)
>>> print(s)
[1, 2, 'a', 'b']
>>>
```

#### 列表
列表是可变序列，通常用于存储同类元素的集合(元素精确的相似度因应用程序而变化).

class **list**([*iterable*])

列表实现了所有的通用序列操作和可变序列操作。列表还提供如下额外的方法：  
**sort**(_*, key=None, reverse=False_)  
这个方法就地对列表进行排序，仅使用 `<` 比较元素。异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败（而列表可能会处于被部分修改的状态）。

[sort()](https://docs.python.org/3.6/library/stdtypes.html#list.sort) 仅接受传递两个关键字参数([仅关键字参数](https://docs.python.org/3.6/glossary.html#keyword-only-parameter)):

*key* 指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 `key=str.lower`)。 对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。 默认值 `None` 表示直接对列表项排序而不计算一个单独的键值。

可以使用 [functools.cmp_to_key()](https://docs.python.org/zh-cn/3.13/library/functools.html#functools.cmp_to_key) 将 2.x 风格的 *cmp* 函数转换为 *key* 函数。 

*reverse* 是一个布尔值。如果设置为 True，则列表元素将按逆序排列（即从大到小）。

To remind users that it operates by side effect, 它不返回排序后的序列(使用 sorted() 明确地请求一个新的排序后的列表实例).  

```python
letters = ['d', 'a', 'e', 'c', 'b']
print(letters.sort())
```

**Result:**  
None

list.sort()方法的返回值是None，要打印排序后的列表，应使用下面的代码：

```python
letters = ['d', 'a', 'e', 'c', 'b']
letters.sort()
print(letters)
```

**Result:**  
['a', 'b', 'c', 'd', 'e']

#### 元组
元组是不可变序列，通常用于储存异构数据的多项集（例如由 [enumerate()](https://docs.python.org/zh-cn/3.13/library/functions.html#enumerate) 内置函数所产生的二元组）。 元组也被用于需要同构数据的不可变序列的情况（例如允许存储到 [set](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#set) 或 [dict](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#dict) 的实例）。

_class_ **tuple([**_iterable_**])** 
可以用多种方式构建元组：

* 使用一对圆括号来表示空元组: `()` 
* 使用一个后缀的逗号来表示单元组: `a,` 或 `(a,)` 
* 使用以逗号分隔的多个项: `a, b, c` 或 `(a, b, c)` 
* 使用内置的 [tuple()](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#tuple): `tuple()` 或 `tuple(iterable)` 

由第二和第三种构建元组的方式可知，构建非空元组的关键在于逗号，而非圆括号。 

```python
>>> a = ([])
>>> b = (1)
>>> c = ([],)
>>> d = (1,)
>>> type(a)
<class 'list'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'tuple'>
>>> type(d)
<class 'tuple'>
>>> print(a, b, c, d, sep='\n')
[]
1
([],)
(1,)
>>> 
```

构造器将构造一个元组，其中的项与 _iterable_ 中的项具有相同的值与顺序。 _iterable_ 可以是序列、支持迭代的容器或其他可迭代对象。 如果 _iterable_ 已经是一个元组，会不加改变地将其返回。 例如，`tuple('abc')` 返回 `('a', 'b', 'c')` 而 `tuple( [1, 2, 3] )` 返回 `(1, 2, 3)`。 如果没有给出参数，构造器将创建一个空元组 `()`。

```python
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> 
```

请注意决定生成元组的其实是逗号而不是圆括号。 圆括号只是可选的，生成空元组或需要避免语法歧义的情况除外。 例如，`f(a, b, c)` 是在调用函数时附带三个参数，而 `f((a, b, c))` 则是在调用函数时附带一个三元组。

元组实现了所有 [一般](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#typesseq-common) 序列的操作。

对于通过名称访问相比通过索引访问更清晰的异构数据多项集，[collections.namedtuple()](https://docs.python.org/zh-cn/3.13/library/collections.html#collections.namedtuple) 可能是比简单元组对象更为合适的选择。  
 

#### Ranges
[range](https://docs.python.org/3/library/stdtypes.html#range) 类型代表一种不可变的数字序列且通常用于在 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 循环中循环一个特定的次数。

*class* **range**(*stop*)  
*class* **range**(*start, stop*[*, step*])  
range 构造函数的参数必须是整型数(要么是内置 [int](https://docs.python.org/3/library/functions.html#int) 要么是任何实现了 `__index__` 特殊方法的对象)。如果省略了 *step* 参数，则它默认为 `1`。如果省略了 *start* 参数，则它默认为 `0`。如果 *step* 是 zero, 则抛出 [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)。

对于正数 *step*, 一个 range `r` 的内容由公式 `r[i] = start + step*i` 决定，其中 `i >= 0` 且 `r[i] < stop`。

对于负数 *step*, range的内容仍然由公式 `r[i] = start + step*i` 决定，但约束条件是 `i >= 0` 和 `r[i] > stop`。

如果 `r[0]` 不满足值的约束条件则range对象将为空。Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.  

Range 示例：  

```python
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
>>>
```

**start**  
*start* 参数的值 (或者 `0` 如果该参数未提供的话)

**stop**  
*stop* 参数的值

**step**  
*step* 参数的值 (或者 `1` 如果该参数未提供的话)

```python
>>> r = range(3, 3)
>>> len(r)
0
>>> r = range(3, -1)
>>> len(r)
0
>>> 
```

如果 *step* 参数的值为正或者省略，则 *start* 的值应小于 *stop* 的值，否则 range 对象为空。  

### 文本序列类型 — str
在Python中，文本数据是通过 [str](https://docs.python.org/3.6/library/stdtypes.html#str) 对象或 *strings* 来处理的。字符串是不可变的Unicode代码点[序列](https://docs.python.org/3.6/library/stdtypes.html#typesseq)。字符串的写法有多种方式：

* 单引号: `'allows embedded "double" quotes'`
* 双引号: `"allows embedded 'single' quotes"`.
* 三引号: `'''Three single quotes'''`, `"""Three double quotes"""`

三引号字符串可能跨越多行 - 所有关联的空白都将被包含在字符串中。

如果一个单一表达式的各个字符串之间仅有空格，那么它们将被含蓄地转换成一个单字符串。即，`("spam " "eggs") == "spam eggs"`。单一字符串等于单一表达式中各个字符串拼接的结果。

```python
>>> ("spam" "eggs") == "spameggs"
True
>>> ("spam " "eggs") == "spam eggs"
True
>>> ("spam "  "eggs") == "spam eggs"
True
```

#### 字符串方法
字符串实现了所有[常见的](https://docs.python.org/3.6/library/stdtypes.html#typesseq-common)序列操作，连同下面描述的额外的方法。

str.**encode**(*encoding="utf-8", errors="strict"*)  
返回一个编码的字符串版本作为一个字节对象。默认编码是 `'utf-8'`。*errors* 可以设置为一个不同的错误处理方案。*errors* 的默认值是 `'strict'`，意为编码错误将抛出一个 [UnicodeError](https://docs.python.org/3.6/library/exceptions.html#UnicodeError)。其它可能的值是 `'ignore'`, `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` 和任何其它通过 [codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error) 注册的名字，参考 [Error Handlers](https://docs.python.org/3.6/library/codecs.html#error-handlers) 章节。可能的编码列表，请参考 [Standard Encodings](https://docs.python.org/3.6/library/codecs.html#standard-encodings) 章节。

*在版本3.1中发生变化：* 增加了对关键字参数的支持。

str.**endswith**(*suffix*[, *start*[, *end*]])  
如果字符串以指定的 *suffix* 结尾返回 `True`，否则返回 `False`。*suffix* can also be a tuple of suffixes to look for. With optional *start*, test beginning at that position. With optional *end*, stop comparing at that position.

str.**format(**_\*args, \*\*kwargs_**)**  
执行字符串格式化操作。 调用此方法的字符串可以包含文字文本或由大括号 `{}` 界定的替换字段。每个替换字段包含一个位置参数的数字索引，或者一个关键字参数的名称。返回的字符串副本中每个替换字段都会被替换为对应参数的字符串值。

```python
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
```

```python
>>> 'translate {table} {keys} {values}'.format(table='biao', keys='jian', values='zhi')
'translate biao jian zhi'
```

```python
>>> data = {'id': '1001', 'name': 'Jack', 'age': 22}
>>> data.keys()
dict_keys(['id', 'name', 'age'])
>>> data.values()
dict_values(['1001', 'Jack', 22])
>>> table = 'students'
>>> keys = ', '.join(data.keys())
>>> keys
'id, name, age'
>>> ['%s'] * 3           
['%s', '%s', '%s']
>>> values = ', '.join(['%s'] * len(data))  # str.join(iterable) 如果 iterable 中有任何非字符串值则抛出一个 TypeError
>>> values
'%s, %s, %s'
>>> 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
'INSERT INTO students (id, name, age) VALUES (%s, %s, %s)'
>>>
```

```python
>>> data = {'id': '1001', 'name': 'Jack', 'age': 22}
>>> [key for key in data] 
['id', 'name', 'age']
>>> [" {key} = %s".format(key=key) for key in data] 
[' id = %s', ' name = %s', ' age = %s']
>>> ','.join([" {key} = %s".format(key=key) for key in data])
' id = %s, name = %s, age = %s'
```

请参阅 [格式化字符串语法](https://docs.python.org/3/library/string.html#formatstrings) 了解有关可以在格式化字符串中指定的各种格式化选项的说明。

**注意：** 当使用 `n` 类型 (例如: `'{:n}'.format(1234)`) 来格式化数字 ([int](https://docs.python.org/3/library/functions.html#int), [float](https://docs.python.org/3/library/functions.html#float), [complex](https://docs.python.org/3/library/functions.html#complex), [decimal.Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal) 及其子类) 的时候，该函数会临时性地将 `LC_CTYPE` 区域设置为 `LC_NUMERIC` 区域以解码 `localeconv()` 的 `decimal_point` 和 `thousands_sep` 字段，如果它们是非 ASCII 字符或长度超过 1 字节，并且 `LC_NUMERIC` 区域与 `LC_CTYPE` 区域不一致时。 这个临时更改会影响其他线程。

*在 3.7 版更改:* 当使用 `n` 类型格式化数字时，该函数在某些情况下会临时性地将 `LC_CTYPE` 区域设置为 `LC_NUMERIC` 区域。

str.**join**(*iterable*)  
返回一个由 *iterable* 中的字符串串联而成的字符串。如果 *iterable* 中有任何非字符串值则抛出一个 [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError)，包括 [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes) 对象。元素之间的分隔符是提供这个方法的字符串。

```python
>>> a = ['apple', 'banana', 'cisco', 'decode']
>>> '*'.join(a)
'apple*banana*cisco*decode'
>>> ' '.join(a)
'apple banana cisco decode'
>>> ''.join(a)
'applebananaciscodecode'
>>>
```

str.**lower()**  
Return a copy of the string with all the cased characters [[4]](https://docs.python.org/3.6/library/stdtypes.html#id15) converted to lowercase.

The lowercasing algorithm used is described in section 3.13 of the Unicode Standard.

str.**replace**(*old*, *new*[, *count*])  
返回一个字符串的副本并将所有子串 *old* 替换为 *new*。如果指定了可选参数 *count*，则仅将前 *count* 个 *old* 替换为 *new*。

```python
>>> s = "tools for windows"
>>> s.replace('o', 'p')
'tppls fpr windpws'
>>> s.replace('o', 'p', 2)
'tppls for windows'
```

str.**rstrip([**_chars_**])**  
返回原字符串的副本，并移除末尾的字符。*chars* 参数是一个指定要移除的字符的集合的字符串。如果省略或为 `None`，则 *chars* 参数默认移除空格。实际上 *chars* 参数并非指定单个后缀；而是会移除参数值的所有组合:  

```python
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
>>>
```

要删除单个后缀字符串，而不是所有字符的集合，请参见 [str.removesuffix()](https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix) 方法。 例如:  

```python
>>> 'Monty Python'.rstrip(' Python')
'M'
>>> 'Monty Python'.removesuffix(' Python')
'Monty'
>>>
```

str.**split**(*sep=None, maxsplit=-1*)  
返回字符串中的一个单词列表，使用 *sep* 作为分隔字符串。If *maxsplit* is given, at most *maxsplit* splits are done (thus, the list will have at most `maxsplit+1` elements). If *maxsplit* is not specified or `-1`, then there is no limit on the number of splits (all possible splits are made).

如果指定 *sep*，连续的分隔符不会被聚集到一起而是被视为界定空串 (例如， `'1,,2'.split(',')` 返回 `['1', '', '2']`)。*sep* 参数可以包括多个字符 (例如，`'1<>2<>3'.split('<>')` 返回 `['1', '2', '3']`)。用一个指定的分隔符分隔一个空串返回 `['']`。

例如：

```python
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
```

如果 *sep* 没有指定或者为 `None`，则应用一个不同的分隔算法：连续的空白被作为一个分隔符，而且如果字符串有前导和尾随空白，输出结果的起始或结束位置将不包含空串。因此，当分隔符为 `None` 时，分隔一个空串或者仅由空白组成的字符串返回 `[]`。

例如：

```python
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']
```

str.**startswith**(*prefix*[, *start*[, *end*]])  
如果字符串以指定的 *prefix* 开始则返回 `True`，否则返回 `False`。*prefix* can also be a tuple of prefixes to look for. With optional *start*, test string beginning at that position. With optional *end*, stop comparing string at that position.

str.**title()**  
返回字符串的首字母大写版本，其中单词以大写字符开头，其余字符为小写。  

示例：  

```python
>>> 'Hello world'.title()
'Hello World'
>>>
```

str.**upper**()  
返回一个字符串的副本且将所有的 cased characters（Cased characters are those with general category property being one of “Lu” (Letter, uppercase), “Ll” (Letter, lowercase), or “Lt” (Letter, titlecase).）转换为大写字母。  
<br />  

#### 格式化字符串字面值（f-字符串）
**本小结的内容是在Python 3.13的标准库文档中增加的，本节的最后一个 Python 需要3.13及以上版本。** 

*在版本 3.6 中新增。* 

*在 3.7 版本发生变更：* [await](https://docs.python.org/zh-cn/3.13/reference/expressions.html#await) 和 [async for](https://docs.python.org/zh-cn/3.13/reference/compound_stmts.html#async-for) 可在 f-字符串内部的表达式中使用。

*在 3.8 版本发生变更：* 增加了调试运算符 (`=`) 

*在 3.12 版本发生变更：* 许多针对 f-字符串内部的表达式的限制已被移除。 例如，嵌套字符串、注释和反斜杠现在都是允许的。

*f-字符串* (正式名称为 *格式化字符串字面值*) 是带有 `f` 或 `F` 前缀的字符串字面值。 这种类型的字符串字面值允许将任意 Python 表达式嵌入到由花括号 (`{}`) 标记的 *替换字段* 内部。 这些表达式将在运行时被求值，这与 [str.format()](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#str.format) 类似，并被转换为常规的 [str](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#str) 对象。 例如： 

```python
>>> who = 'nobody'
>>> nationality = 'Spanish'
>>> f'{who.title()} expects the {nationality} Inquisition!'
'Nobody expects the Spanish Inquisition!'
>>> 
```

也可以使用包含多行的 f-字符串： 

```py
>>> f'''This is a string
... on two lines'''
'This is a string\non two lines'
>>> 
```

一个单独的左花括号，`'{'`，标记一个可包含任意 Python 表达式的 *替换字段*： 

```py
>>> nationality = 'Spanish'
>>> f'The {nationality} Inquisition!'
'The Spanish Inquisition!'
>>> 
```

要包括 `{` 或 `}` 字面值，请使用双花括号： 

```py
>>> x = 42
>>> f'{{x}} is {x}'
'{x} is 42'
>>> 
```

还可以使用函数，以及 [格式说明符](https://docs.python.org/zh-cn/3.13/library/string.html#formatstrings)： 

```py
>>> from math import sqrt
>>> f'√2 \N{ALMOST EQUAL TO} {sqrt(2):.5f}'
'√2 ≈ 1.41421'
>>> 
```

在默认情况下，任何非字符串表达式都将使用 [str()](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#str) 来转换： 

```py
>>> from fractions import Fraction
>>> f'{Fraction(1, 3)}'
'1/3'
>>> 
```

要使用显式转换，请使用 `!` (叹号) 运算符，后面跟任意的有效格式说明符，包括： 

转换符|含义 
-----|-----------------     
`!a` |[ascii()](https://docs.python.org/zh-cn/3.13/library/functions.html#ascii) 
`!r` |[repr()](https://docs.python.org/zh-cn/3.13/library/functions.html#repr) 
`!s` |[str()](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#str) 

例如: 

```py
>>> from fractions import Fraction
>>> f'{Fraction(1, 3)!s}'
'1/3'
>>> f'{Fraction(1, 3)!r}'
'Fraction(1, 3)'
>>> question = '¿Dónde está el Presidente?'
>>> print(f'{question!a}')
'\xbfD\xf3nde est\xe1 el Presidente?'
>>> 
``` 

在调试期间同时看到表达式和值会很有帮助，具体是在表达式后使用等号 (`=`)。 这将保留花括号内部的空格，并可以使用转换器。 在默认情况下，调试运算符使用 [repr()](https://docs.python.org/zh-cn/3.13/library/functions.html#repr) (`!r`) 转换器。 例如：

```py
>>> from fractions import Fraction
>>> calculation = Fraction(1, 3)
>>> f'{calculation=}'
'calculation=Fraction(1, 3)'
>>> f'{calculation = }'
'calculation = Fraction(1, 3)'
>>> f'{calculation = !s}'
'calculation = 1/3'
>>> 
```

输出一旦已被求值，就可以用 [格式说明符](https://docs.python.org/zh-cn/3.13/library/string.html#formatstrings) 后面跟一个冒号 (`':'`) 来格式化它。 在表达式已被求值，并可能被转换为字符串之后，就会调用结果的 \_\_format\_\_() 方法并附带该格式说明符，或者如果未给出格式说明符则附带空字符串。 随后将使用已格式化的结果作为替换字段最终的值。 例如： 

```py
>>> from fractions import Fraction
>>> f'{Fraction(1, 7):.6f}'    # require Python 3.12 and above
'0.142857'
>>> f'{Fraction(1, 7):_^+10}'  # require Python 3.13 and above
'___+1/7___'
>>> 
```  
<br />  

#### printf-style 字符串格式化
**注意：** 这里描述的格式化操作展示了一些导致若干常见错误的怪现象 (例如无法正确地显示元组和字典)。使用更新的[格式化字符串文字](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)，[str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) 接口，或者[模板字符串](https://docs.python.org/3/library/string.html#template-strings)可以帮助避免这些错误。这些替代选择每一个都提供了它们自己的权衡及简单，灵活，和/或可扩展性的好处。

字符串对象有一个唯一的内置运算： % 运算符 (模运算)。这也称为字符串*格式化*或*插值*运算符。给定 `format % values` (其中 *format* 是一个字符串)，`%` conversion specifications in *format* are replaced with zero or more elements of *values*. 效果与在C语言中使用 `sprintf()` 相似。

如果 *format* 要求一个单一参数，*values* 可以是一个单一的非元组对象。[\[5\]](https://docs.python.org/3/library/stdtypes.html#id16) 否则，*values* 必须是一个恰好带有由格式化字符串指定的项数的元组，或者一个单一的映射对象 (例如，一个字典)。

一个转换说明符包含2个或多个字符并拥有下面的组件，这些组件必须按下面的顺序出现：

1. `'%'` 字符，标识说明符的开始。
2. 映射键 (可选)，由一个圆括号括起来的字符序列组成 (例如， `(somename)` )。
3. 转换标志 (可选)，影响一些转换类型的结果。
4. 最小字段宽度 (可选)。If specified as an `'*'` (星号), the actual width is read from the next element of the tuple in *values*, and the object to convert comes after the minimum field width and optional precision.
5. 精度 (可选)，表示为一个 `'.'` (点) 后跟精度。If specified as `'*'` (一个星号)， the actual precision is read from the next element of the tuple in *values*, and the value to convert comes after the precision.
6. Length modifier (可选).
7. 转换类型。

当右边的参数是一个字典 (或者其它映射类型)时，则字符串中的 *formats* 必须包含一个圆括号括起来的映射键到那个字典且立即插入到 `'%'` 字符后面。映射键从映射中选择将被格式化的值。例如：

```python
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 22})
Python has 022 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 222})
Python has 222 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 2222})
Python has 2222 quote types.
>>>
```

转换标志字符是：

Flag   |Meaning
-------|------------------
`'0'`  |转换将为数值填充0。

转换类型是：

Conversion    |Meaning            |Notes
--------------|-------------------|------
`'d'`         |象征十进制整型数。   |
`'f'`         |浮点小数格式。       |(3)
`'s'`         |字符串（使用 [str()](https://docs.python.org/3/library/stdtypes.html#str) 转换任何Python对象）。  |(5)

注释：

3. 替代形式导致结果总是包含一个小数点，即使它后面没有数字。

   精度决定小数点后面的位数，默认为6位。

4. 

5. 如果精度是 `N`，则输出被截断为 `N` 个字符。

```python
>>> print('%(language).2s has %(number)03d quote types.' %
...       {"language": "Python", "number": 222})
Py has 222 quote types.
>>>
```

### 二进制序列类型 — 字节、字节数组、内存视图
操作二进制数据的核心内置类型是[字节](https://docs.python.org/3/library/stdtypes.html#bytes)和[字节数组](https://docs.python.org/3/library/stdtypes.html#bytearray)。 它们由 [memoryview](https://docs.python.org/3/library/stdtypes.html#memoryview) 支持，它使用[缓冲区协议](https://docs.python.org/3/c-api/buffer.html#bufferobjects)访问其他二进制对象的内存而无需复制。  

[array](https://docs.python.org/3/library/array.html#module-array) 模块支持基本数据类型（如 32 位整型数和 IEEE754 双精度浮点值）的高效存储。  

#### 字节和字节数组操作
字节和字节数组对象都支持[通用](https://docs.python.org/3.6/library/stdtypes.html#typesseq-common)序列操作。它们不仅可以与同类型的运算对象互操作，还可以与任何 [bytes-like 对象](https://docs.python.org/3.6/glossary.html#term-bytes-like-object)互操作。因为这种灵活性，它们可以自由地混合操作而不引起错误。然而，返回结果的类型可能依赖于操作数的顺序。

bytes.**decode**(*encoding="utf-8", errors="strict"*)  
bytearray.**decode**(*encoding="utf-8", errors="strict”*)  
从给定的字节返回一个解码的字符串。默认编码是 `'utf-8'`. `errors` 可以设置为一个不同的错误处理方案。`errors` 的默认值是 `'strict'`, 意为编码错误则抛出一个 [UnicodeError](https://docs.python.org/3.6/library/exceptions.html#UnicodeError). 其它可能的值是`'ignore'`, `'replace'` 和任何其它通过 [codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error) 注册的名字，参考[错误处理程序](https://docs.python.org/3.6/library/codecs.html#error-handlers)章节。对于可能的编码列表，请参考[标准编码](https://docs.python.org/3.6/library/codecs.html#standard-encodings)章节。

**Note:** Passing the *encoding* argument to [str](https://docs.python.org/3.6/library/stdtypes.html#str) allows decoding any [bytes-like object](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) directly, without needing to make a temporary bytes or bytearray object.

*在版本3.1中发生变化：* 新增对关键字参数的支持。  

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

### 映射类型 — 字典
一个[映射](https://docs.python.org/3.6/glossary.html#term-mapping) 对象映射 [可哈希的](https://docs.python.org/3.6/glossary.html#term-hashable) 值到任意对象。映射是可变对象。目前仅有一个标准映射类型，*字典*。 (其它容器请参考内置[列表](https://docs.python.org/3.6/library/stdtypes.html#list)，[集合](https://docs.python.org/3.6/library/stdtypes.html#set)和[元组](https://docs.python.org/3.6/library/stdtypes.html#tuple)类，以及 [collections](https://docs.python.org/3.6/library/collections.html#module-collections) 模块.)

字典的键 *几乎* 可以是任意值。不[可哈希的](https://docs.python.org/3.6/glossary.html#term-hashable)值，即值包含列表，字典或其它可变类型 (通过比较值而不是对象身份) 不能被用作键。  

*class* __dict__(_\*\*kwargs_)  
*class* __dict__(_mapping, \*\*kwargs_)  
*class* __dict__(_iterable, \*\*kwargs_)  
返回一个从一个可选位置参数和一组可能为空集的关键字参数初始化的新字典。  

这些是字典支持的操作 (因此，自定义映射类型也应该支持)：  

**list(d)**  
返回字典 *d* 中使用的所有键的列表。  

**len(d)**  
返回字典 *d* 中的项目数。  

**d[key]**  
用 key *key* 返回 *d* 中的项目。 如果 *key* 不在映射中，则抛出一个 KeyError。  

**d[key] = value**  
将 `d[key]` 设置为 *value*。  

**del d[key]**  
从 *d* 中移除 `d[key]`。如果 *key* 不在映射中，则抛出一个 [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)。

**key in d**  
如果 *d* 有一个键 *key* 则返回 True，否则返回 False。  

**key not in d**  
等同于 `not key in d`。  

**clear()**  
从字典中删除所有项。  

**get**(*key*[, *default*])  
如果 *key* 在字典中，则返回 *key* 的值，否则返回 *default*。If default is not given, it defaults to `None`, 所以这个方法永远不会抛出 [KeyError](https://docs.python.org/3.6/library/exceptions.html#KeyError)。

**items()**  
返回一个新的字典的元素的视图 (`(key, value)` pairs)。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

**keys()**  
返回一个字典的键的新的视图。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

**values()**  
返回一个字典的值的新的视图。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

#### 字典视图对象
[dict.keys()](https://docs.python.org/3.6/library/stdtypes.html#dict.keys), [dict.values()](https://docs.python.org/3.6/library/stdtypes.html#dict.values) 和 [dict.items()](https://docs.python.org/3.6/library/stdtypes.html#dict.items) 返回的对象是 *视图对象*。它们提供了一个关于字典条目的动态视图，这意味着当字典变化的时候，视图将反映这些变化。

字典视图用法的一个例子：

```python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()
>>> items = dishes.items()

>>> keys
dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
>>> values
dict_values([2, 1, 1, 500])
>>> items
dict_items([('eggs', 2), ('sausage', 1), ('bacon', 1), ('spam', 500)])

>>> type(keys)
<class 'dict_keys'>
>>> type(values)
<class 'dict_values'>
>>> type(items) 
<class 'dict_items'>

>>> # iteration
...
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

>>> # keys and values are iterated over in the same order
...
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]
>>> list(items)
[('eggs', 2), ('sausage', 1), ('bacon', 1), ('spam', 500)]

>>> # view objects are dynamic and reflect dict changes
...
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']
>>> list(values)
[1, 500]

>>> # set operations
...
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'}
{'juice', 'sausage', 'spam', 'bacon'}
```

### 上下文管理器类型
Python 的 [with](https://docs.python.org/3/reference/compound_stmts.html#with) 语句支持由上下文管理器定义的运行时上下文的概念。 这是使用一对允许用户定义的类定义运行时上下文的方法实现的，该运行时上下文在语句体执行之前进入并在语句结束时退出：  

contextmanager.**\_\_enter\_\_()**  
进入运行时上下文并返回此对象或关联到该运行时上下文的其他对象。 此方法的返回值会绑定到使用此上下文管理器的 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句的 `as` 子句中的标识符。  

一个返回其自身的上下文管理器的例子是 [文件对象](https://docs.python.org/3.8/glossary.html#term-file-object)。 文件对象会从 \_\_enter\_\_() 返回其自身，以允许 [open()](https://docs.python.org/3.8/library/functions.html#open) 被用作 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句中的上下文表达式。  

一个返回关联对象的上下文管理器的例子是 [decimal.localcontext()](https://docs.python.org/3.8/library/decimal.html#decimal.localcontext) 所返回的对象。 这些管理器会将活动的 decimal 上下文设为原始 decimal 上下文的一个副本并返回该副本。 这允许对 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句体中的当前 decimal 上下文进行更改，而不会影响 `with` 语句以外的代码。  

contextmanager.**\_\_exit\_\_(**_exc_type, exc_val, exc_tb_**)**  
退出运行时上下文并返回一个布尔值标识来表明所发生的任何异常是否应当被抑制。 如果在执行 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句体期间发生了异常，则参数会包含异常的类型、值以及回溯信息。 在其他情况下三个参数均为 `None`。  

从这个方法返回一个真值将导致 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句抑制该异常并继续执行紧随在 `with` 语句之后的语句。 否则该异常将在此方法结束执行后继续传播。 在此方法执行期间发生的异常将会取代 `with` 语句体中发生的任何异常。

传入的异常绝对不应当被显式地重新引发 —— 相反地，此方法应当返回一个假值以表明此方法已成功完成并且不希望抑制被引发的异常。 这允许上下文管理代码方便地检测 [\_\_exit\_\_()](https://docs.python.org/3.8/library/stdtypes.html#contextmanager.__exit__) 方法是否确实已失败。

Python 定义了几个上下文管理器来支持简单的线程同步、文件或其他对象的快速关闭，以及更方便地操作活动十进制算术上下文。 除了上下文管理协议的实现之外，不会对特定类型进行特殊处理。 请参阅 [contextlib](https://docs.python.org/3.8/library/contextlib.html#module-contextlib) 模块查看相关的示例。  

Python 的[生成器](https://docs.python.org/3.8/glossary.html#term-generator) 和 [contextlib.contextmanager](https://docs.python.org/3.8/library/contextlib.html#contextlib.contextmanager) 装饰器提供了实现这些协议的便捷方式。 如果使用 [contextlib.contextmanager](https://docs.python.org/3.8/library/contextlib.html#contextlib.contextmanager) 装饰器来装饰一个生成器函数，它将返回一个实现了必要的 [\_\_enter\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__) 和 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 方法的上下文管理器，而不再是由一个未经装饰的生成器函数所产生的迭代器。  

请注意，Python/C API 中 Python 对象的类型结构中并没有这些方法的特定槽位。 想要定义这些方法的扩展类型必须将它们作为普通的 Python 可访问方法来提供。 与设置运行时上下文的开销相比，单个类字典查找的开销可以忽略不计。  

### 特殊属性
The implementation adds a few special read-only attributes to several object types, where they are relevant. 其中有些不被内置函数[dir()](https://docs.python.org/3.6/library/functions.html#dir) 报道。

object.**\_\_dict\_\_**  
一个字典或其它映射对象，用于存储对象的(可写的)属性。

instance.**\_\_class\_\_**  
一个类实例属于哪个类。

class.**\_\_bases\_\_**  
一个类对象的基类元组。

class.**\_\_subclasses\_\_()**  
每个类都保持了一份它的直接子类的弱引用列表。这个方法返回一个所有仍然活跃的引用的列表。例如：

```python
>>> import io
>>> io.IOBase.__subclasses__()
[<class 'io.RawIOBase'>, <class 'io.BufferedIOBase'>, <class 'io.TextIOBase'>]
```

## 内置异常
在 Python 中，所有异常都必须是派生自 [BaseException](https://docs.python.org/3.8/library/exceptions.html#BaseException) 的类的实例。在带有提及特定类的 [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 子句的 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 语句中，该子句还处理从该类派生的任何异常类（但不处理派生*它*的异常类）。 通过子类化创建的两个不相关的异常类永远不会等价，即使它们具有相同的名称。  

下面列出的内置异常可以由解释器或内置函数生成。 除非另有说明，它们都有一个“关联值”，指示错误的详细原因。这可能是一个字符串或几项信息的元组（例如，错误代码和解释代码的字符串）。 关联值通常作为参数传递给异常类的构造函数。  

用户代码可以引发内置异常。 这可用于测试异常处理程序或报告错误情况，“就像”解释器引发相同异常的情况一样； 但请注意，没有什么可以阻止用户代码引发不适当的错误。  

内置的异常类可以被子类化以定义新的异常； 鼓励程序员从 [Exception](https://docs.python.org/3.8/library/exceptions.html#Exception) 类或其子类之一派生新的异常，而不是从 [BaseException](https://docs.python.org/3.8/library/exceptions.html#BaseException)。 有关定义异常的更多信息，请参阅 Python 教程中的[用户定义的异常](https://docs.python.org/3.8/tutorial/errors.html#tut-userexceptions)。  

当在 [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 或 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句中引发（或重新引发）异常时，\_\_context\_\_ 会被自动设置为最后一个捕获的异常； 如果未处理新异常，则最终显示的回溯将包括原始异常和最后的异常。  

当引发一个新的异常（而不是使用一个简单的 `raise` 来重新引发当前正在处理的异常）时，隐式的异常上下文可以通过使用带有 [raise](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 的 [from](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 来补充一个明确的原因：  

```python
raise new_exc from original_exc
```

[from](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 后面的表达式必须是异常或 `None`。 它将在引发的异常上被设置为 \_\_cause\_\_。 设置 \_\_cause\_\_ 还会隐式地将 \_\_suppress\_context\_\_ 属性设置为 `True`，因此使用 `raise new_exc from None` 可以有效地将旧异常替换为新异常以显示其目的（例如，将 [KeyError](https://docs.python.org/3.8/library/exceptions.html#KeyError) 转换为 [AttributeError](https://docs.python.org/3.8/library/exceptions.html#AttributeError)），同时让旧异常在 \_\_context\_\_ 中保持可用状态以便调试时进行内省。    

除了异常本身的回溯之外，默认的回溯显示代码还会显示这些串联的异常。 \_\_cause\_\_ 中的显式串联异常如果存在将总是显示。仅当 \_\_cause\_\_ 为 [None](https://docs.python.org/3.8/library/constants.html#None) 且 \_\_suppress\_context\_\_ 为 false 时，才会显示 \_\_context\_\_ 中的隐式串联异常。  

在任何一种情况下，异常本身总是显示在任何串联异常之后，因此回溯的最后一行总是显示引发的最后一个异常。  

### 基类
下列异常主要被用作其他异常的基类。  

*exception* **BaseException**  
所有内置异常的基类。它不应该被用户自定义类直接继承 (这种情况请使用 [Exception](https://docs.python.org/3.8/library/exceptions.html#Exception))。 如果在此类的实例上调用 [str()](https://docs.python.org/3.8/library/stdtypes.html#str)，则会返回实例的参数表示，或者当没有参数时返回空字符串。  

**args**  
传给异常构造器的参数元组。 某些内置异常 (例如 [OSError](https://docs.python.org/3.8/library/exceptions.html#OSError)) 期待特定数量的参数并赋予此元组中的元素特殊的含义，而其他异常通常只调用一个给出错误信息的单独字符串。    

*exception* **Exception**  
所有内置的、非系统退出的异常都派生自这个类。 所有用户定义的异常也应该从这个类派生。    

### 具体异常
下面的异常是经常被抛出的异常。  

*exception* **AttributeError**  
当属性引用 (参见 [属性引用](https://docs.python.org/3.8/reference/expressions.html#attribute-references)) 或赋值失败时将被引发。（当一个对象根本不支持属性引用或属性赋值时，将引发 [TypeError](https://docs.python.org/3.8/library/exceptions.html#TypeError)。）    

*exception* **IndexError**  
当序列下标超出范围时引发。（切片索引被静默截断以落在允许的范围内；如果索引不是整数，则引发 [TypeError](https://docs.python.org/3.8/library/exceptions.html#TypeError)。）  

*exception* **KeyError**  
当在现有键集合中找不到指定的映射（字典）键时将被引发。  

*exception* **KeyboardInterrupt**  
当用户按下中断键 (通常为 Control-C 或 Delete) 时将被引发。 在执行期间，会定期检测中断。 该异常继承自 [BaseException](https://docs.python.org/3.8/library/exceptions.html#BaseException) 以确保不会被捕获 [Exception](https://docs.python.org/3.8/library/exceptions.html#Exception) 的代码意外捕获，从而阻止解释器退出。  

*exception* **NameError**  
当某个局部或全局名称未找到时将被引发。此异常仅用于非限定名称。关联的值是一条错误信息，其中包含未找到的名称。  

*exception* **OSError([**arg**])**    
*exception* **OSError(**_errno, strerror_**[**, *filename***[**, *winerror***[**, *filename2***]]])**  
此异常在一个系统函数返回一个系统相关的错误时将被引发，此类错误包括 I/O 操作失败例如 "文件未找到" 或 "磁盘已满" （不包括非法参数类型或其他偶然性错误）。

构造器的第二种形式可设置如下所述的相应属性。 如果未指定这些属性则默认为 [None](https://docs.python.org/3.8/library/constants.html#None)。 为了能向下兼容，如果传入了三个参数，则 [args](https://docs.python.org/3.8/library/exceptions.html#BaseException.args) 属性将仅包含由前两个构造器参数组成的 2 元组。    

构造器实际返回的往往是 [OSError](https://docs.python.org/3.8/library/exceptions.html#OSError) 的某个子类，如下文 [OS exceptions](https://docs.python.org/3.8/library/exceptions.html#os-exceptions) 中所描述的。 具体的子类取决于最终的 [errno](https://docs.python.org/3.8/library/exceptions.html#OSError.errno) 值。 此行为仅在直接或通过别名来构造 [OSError](https://docs.python.org/3.8/library/exceptions.html#OSError) 时发生，并且在子类化时不会被继承。  

**errno**  
来自于 C 变量 `errno` 的数字错误代码。  

*exception* **SyntaxError**  
当解析器遇到语法错误时将被引发。 这可以发生在 [import](https://docs.python.org/3.8/reference/simple_stmts.html#import) 语句，对内置函数 [exec()](https://docs.python.org/3.8/library/functions.html#exec) 或 [eval()](https://docs.python.org/3.8/library/functions.html#eval) 的调用，或者读取原始脚本或标准输入（也包括交互模式）的时候。  

异常实例的 [str()](https://docs.python.org/3.8/library/stdtypes.html#str) 只返回错误消息。  

**filename**  
语法错误所在文件的名称。

**lineno**  
发生错误所在文件中的行号。 行号索引从 1 开始：文件中首行的 `lineno` 为 1。  

**offset**  
发生错误所在文件中的列号。 列号索引从 1 开始：行中首个字符的 `offset` 为 1。  

**text**  
错误所涉及的源代码文本。  
<br>  

*exception* **TypeError**  
当一个操作或函数被应用于类型不适当的对象时将被引发。 关联的值是一个字符串，给出有关类型不匹配的详情。  

此异常可以由用户代码引发，以表明尝试对某个对象进行的操作不受支持也不应当受支持。如果某个对象应当支持给定的操作但尚未提供相应的实现，所要引发的适当异常应为 [NotImplementedError](https://docs.python.org/3.8/library/exceptions.html#NotImplementedError)。  

传入参数的类型错误 (例如在要求 [int](https://docs.python.org/3.8/library/functions.html#int) 时却传入了 [list](https://docs.python.org/3.8/library/stdtypes.html#list)) 应当导致 [TypeError](https://docs.python.org/3.8/library/exceptions.html#TypeError)，但传入参数的值错误 (例如传入要求范围之外的数值) 则应当导致 [ValueError](https://docs.python.org/3.8/library/exceptions.html#ValueError)。
<br>  

*exception* **UnicodeError**  
当发生与 Unicode 相关的编码或解码错误时将被引发。 此异常是 [ValueError](https://docs.python.org/3.8/library/exceptions.html#ValueError) 的一个子类。  

[UnicodeError](https://docs.python.org/3.8/library/exceptions.html#UnicodeError) 具有一些描述编码或解码错误的属性。 例如 `err.object[err.start:err.end]` 会给出导致编解码器失败的特定无效输入。  

 **encoding**  
引发错误的编码名称。

**reason**  
描述特定编解码器错误的字符串。  

**object**  
编解码器试图要编码或解码的对象。  

**start**  
[object](https://docs.python.org/3.8/library/functions.html#object) 中无效数据的开始位置索引。  

**end**  
[object](https://docs.python.org/3.8/library/functions.html#object) 中无效数据的末尾位置索引（不含）。  
<br>

*exception* **UnicodeEncodeError**  
当在编码过程中发生与 Unicode 相关的错误时将被引发。 此异常是 [UnicodeError](https://docs.python.org/3.8/library/exceptions.html#UnicodeError) 的一个子类。  
<br>  

*exception* **UnicodeDecodeError**  
当在解码过程中发生与 Unicode 相关的错误时将被引发。 此异常是 [UnicodeError](https://docs.python.org/3.8/library/exceptions.html#UnicodeError) 的一个子类。  
<br>  

*exception* **ValueError**  
当操作或函数接收到具有正确类型但值不适合的参数，并且情况不能用更精确的异常例如 [IndexError](https://docs.python.org/3.8/library/exceptions.html#IndexError) 来描述时将被引发。  
<br>  

*exception* **ZeroDivisionError**  
当除法或取余运算的第二个参数为零时将被引发。 关联的值是一个字符串，指明操作数和运算的类型。  
<br>  

下面的异常是为了与之前的版本保持兼容；从Python 3.3开始，它们都是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的别名。  

*exception* **EnvironmentError**  

*exception* **IOError**  

*exception* **WindowsError**  
仅Windows下可用。

#### OS异常
下面的异常是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的子类，它们将根据系统错误代码被引发。  

*exception* **ConnectionError**  
连接相关的问题的基类。  

子类是 [BrokenPipeError](https://docs.python.org/3.6/library/exceptions.html#BrokenPipeError), [ConnectionAbortedError](https://docs.python.org/3.6/library/exceptions.html#ConnectionAbortedError), [ConnectionRefusedError](https://docs.python.org/3.6/library/exceptions.html#ConnectionRefusedError) 和 [ConnectionResetError](https://docs.python.org/3.6/library/exceptions.html#ConnectionResetError)。  
<br>  

*exception* **ConnectionResetError**  
[ConnectionError](https://docs.python.org/3.6/library/exceptions.html#ConnectionError) 的一个子类，当一个连接被对方重置时抛出。相当于 errno 为 `ECONNRESET`。  
<br>  

*exception* **FileNotFoundError**  
当所请求的文件或目录不存在时将被引发。 对应于 errno `ENOENT`。  
<br>  

*exception* **TimeoutError**  
当一个系统函数在系统级超时时将被引发。 对应于 errno `ETIMEDOUT`。  

*3.3 新版功能:* 添加了以上所有 [OSError](https://docs.python.org/3.8/library/exceptions.html#OSError) 的子类。  

参见： [PEP 3151](https://www.python.org/dev/peps/pep-3151) - 重写 OS 和 IO 异常的层次结构  

### 异常层次结构
内置异常的类层次结构如下：  

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```
<br>  

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

`\d`  
For Unicode (str) patterns:  
匹配任何 Unicode 十进制数字（即 Unicode 字符类别 [Nd] 中的任何字符）。 这包括 [0-9] 以及许多其他数字字符。如果使用 ASCII 标志，则仅匹配 [0-9]。  

For 8-bit (bytes) patterns:  
匹配任何十进制数字； 这相当于 [0-9]。  

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

编解码器         |别名         |语言
----------------|-------------|-----
ascii           |646, us-ascii|英语
cp1252          |windows-1252 |西欧
gb2312          |chinese, csiso58gb231280, euc-cn, euccn, eucgb2312-cn, gb2312-1980, gb2312-80, iso-ir-58 |简体中文
gbk             |936, cp936, ms936 |统一汉语
gb18030         |gb18030-2000 |统一汉语
hz              |hzgb, hz-gb, hz-gb-2312 |简体中文
latin_1         |iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1 |西欧  
shift_jis       |csshiftjis, shiftjis, sjis, s_jis  |日语  
shift_jis_2004  |shiftjis2004, sjis_2004, sjis2004  |日语  
shift_jisx0213  |shiftjisx0213, sjisx0213, s_jisx0213  |日语  
utf_8           |U8, UTF, utf8 |所有语言  

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

如果需要获取当前文件的路径名，建议使用 `os.path.abspath(__file__)` ，若直接使用 `__file__` ，在 Python3.7 中获取的路径名是相对路径名。 

```sh
➜  ~ cat temp.py 
#!/usr/bin/env python3
import os.path

print(__file__)
print(os.path.abspath(__file__))
➜  ~ 
➜  ~ python3.7 temp.py 
temp.py
/home/ywh/temp.py
➜  ~ 
➜  ~ python3.11 temp.py 
/home/ywh/temp.py
/home/ywh/temp.py
➜  ~ 
➜  ~ python3 --version
Python 3.7.0
➜  ~ ./temp.py 
./temp.py
/home/ywh/temp.py
➜  ~ 
➜  ~ pyenv global system
➜  ~ python3 --version
Python 3.11.2
➜  ~ ./temp.py 
/home/ywh/./temp.py
/home/ywh/temp.py
➜  ~ 
```

从上面的代码可以看出，通过 `__file__` 获取的路径名是变化的，并且很多时候是相对路径名，而通过 `os.path.abspath(__file__)` 获取的路径名始终如一。 

os.path.**basename(**_path_**)**  
返回路径名 *path* 的基本名称。这是将 *path* 传入函数 [split()](https://docs.python.org/3/library/os.path.html#os.path.split) 之后，返回的一对值中的第二个元素。请注意，此函数的结果与 Unix **basename** 程序不同。**basename** 在 `'/foo/bar/'` 上返回 `'bar'`，而 [basename()](https://docs.python.org/3/library/os.path.html#os.path.basename) 函数返回一个空字符串 `('')`。

*在 3.6 版更改:* 接受一个 [path-like 对象](https://docs.python.org/3/glossary.html#term-path-like-object)。

```python
>>> os.path.basename('/origin/tos/fbi')
'fbi'
>>>  
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

os.path.**isfile(**_path_**)** 
如果 *path* 是 [现有的](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.exists) 常规文件，则返回 `True`。本方法会跟踪符号链接，因此，对于同一路径，[islink()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.islink) 和 [isfile()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.isfile) 都可能为 `True`。 

*在 3.6 版本发生变更：* 接受一个 [path-like object](https://docs.python.org/zh-cn/3.13/glossary.html#term-path-like-object)。  

```python
>>> import sys
>>> sys.executable
'/usr/bin/python'
>>> import os.path
>>> os.path.isfile('/usr/bin/python')
True
>>> 
``` 
<br />  

os.path.**isdir(**_path_**)** 
如果 *path* 是 [现有的](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.exists) 目录，则返回 `True`。本方法会跟踪符号链接，因此，对于同一路径，[islink()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.islink) 和 [isdir()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.isdir) 都可能为 `True`。

*在 3.6 版本发生变更：* 接受一个 [path-like object](https://docs.python.org/zh-cn/3.13/glossary.html#term-path-like-object)。  

```python
>>> os.path.isdir('/usr/bin/')
True
>>> os.path.isdir('/usr/bin')
True
>>> 
``` 
<br />  

os.path.**join**(_path, *paths_)  
智能地连接一个或多个路径组件。返回值是 *path* 和所有 _*paths_ 成员的串联，且除了最后一个部分，每一个非空的部分后面都跟着一个正确的目录分隔符 (`os.sep`)，这意味着如果最后一个部分为空则结果将必定以一个分隔符结尾。如果一个组件是一个绝对路径，则所有前面的组件都被丢弃且连接从绝对路径组件继续。

在 Windows 平台，当遇到一个绝对路径组件 (如，`r'\foo'`) 时驱动器号不重置。如果一个组件包含一个驱动器号，则所有前面的组件被丢弃且驱动器号被重置。注意，因为每个驱动器都有一个当前目录，`os.path.join("c:", "foo")` represents a path relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`。

*在版本3.6中发生变化：* *path* 和 *paths* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

```sh
➜  ~ python --version
Python 3.11.2
➜  ~ 
➜  ~ cat temp.py 
import os.path

print(__file__)
print(os.path.abspath(__file__))
DIR_OF_THIS_SCRIPT = os.path.dirname(os.path.abspath(__file__))
print(DIR_OF_THIS_SCRIPT)
DIR_OF_GITHUB = os.path.join(DIR_OF_THIS_SCRIPT, 'github')
print(DIR_OF_GITHUB)
➜  ~ 
➜  ~ python temp.py
/home/pi/temp.py
/home/pi/temp.py
/home/pi
/home/pi/github
➜  ~ 
```

### glob --- Unix 风格的路径名模式扩展
**源代码:** [Lib/glob.py](https://github.com/python/cpython/tree/3.13/Lib/glob.py)

[glob](https://docs.python.org/zh-cn/3.13/library/glob.html#module-glob) 模块会按照 Unix shell 所使用的规则找出所有匹配特定模式的路径名称，但返回结果的顺序是不确定的。 波浪号扩展不会生效，但 `*`、`?` 以及用 `[]` 表示的字符范围将被正确地匹配。 这是通过配合使用 [os.scandir()](https://docs.python.org/zh-cn/3.13/library/os.html#os.scandir) 和 [fnmatch.fnmatch()](https://docs.python.org/zh-cn/3.13/library/fnmatch.html#fnmatch.fnmatch) 函数来实现的，而不是通过实际唤起子 shell。

请注意以点号 `(.)` 打头的文件只能用同样以点号打头的模式来匹配，这不同于 [fnmatch.fnmatch()](https://docs.python.org/zh-cn/3.13/library/fnmatch.html#fnmatch.fnmatch) 或 [pathlib.Path.glob()](https://docs.python.org/zh-cn/3.13/library/pathlib.html#pathlib.Path.glob)。（对于波浪号和 shell 变量扩展，请使用 [os.path.expanduser()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.expanduser) 和 [os.path.expandvars()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.expandvars)。）

对于字面值匹配，请将原字符用方括号括起来。 例如，`'[?]'` 将匹配字符 `'?'`。

[glob](https://docs.python.org/zh-cn/3.13/library/glob.html#module-glob) 模块定义了下列函数：

glob.**glob(**_pathname, \*, root_dir=None, dir_fd=None, recursive=False, include_hidden=False_**)** 
返回一个匹配 *pathname* 的可能为空的路径名列表，其中的元素必须为包含路径信息的字符串。 *pathname* 可以是绝对路径 (如 `/usr/src/Python-1.5/Makefile`) 或相对路径 (如 `../../Tools/*/*.gif`)，并可包含 shell 风格的通配符。 无效的符号链接也将包括在结果中 (如像在 shell 中一样)。 结果是否排序取决于具体文件系统。 如果某个符合条件的文件在调用此函数期间被移除或添加，是否包括该文件的路径是没有规定的。

如果 *root_dir* 不为 `None`，则它应当是指明要搜索的根目录的 [path-like object](https://docs.python.org/zh-cn/3.13/glossary.html#term-path-like-object)。 它用在 [glob()](https://docs.python.org/zh-cn/3.13/library/glob.html#module-glob) 上与在调用它之前改变当前目录有相同的效果。 如果 *pathname* 为相对路径，结果将包含相对于 *root_dir* 的路径。

本函数带有 *dir_fd* 参数，支持 [基于目录描述符的相对路径](https://docs.python.org/zh-cn/3.13/library/os.html#dir-fd)。

如果 `recursive` 为真值，则模式 `"**"` 将匹配目录中的任何文件以及零个或多个目录、子目录和符号链接。 如果模式加了一个 [os.sep](https://docs.python.org/zh-cn/3.13/library/os.html#os.sep) 或 [os.altsep](https://docs.python.org/zh-cn/3.13/library/os.html#os.altsep) 则将不匹配文件。

如果 *include_hidden* 为真值，`"**"` 模式将匹配隐藏目录。*include_hidden* 参数对隐藏文件也有效。 

`glob.glob` 带有参数 `pathname` 和 `recursive` 时引发一个 [审计事件](https://docs.python.org/3.13/library/sys.html#auditing)。

`glob.glob/2` 带有参数 `pathname`、`recursive`、`root_dir` 和 `dir_fd` 时引发一个 [审计事件](https://docs.python.org/3.13/library/sys.html#auditing)。

**备注：** 在一个较大的目录树中使用 `"**"` 模式可能会消耗非常多的时间。 
**备注：** 如果 *pathname* 包含多个 `"**"` 模式并且 *recursive* 为真值则此函数可能返回重复的路径名。 

在 3.5 版本发生变更: 支持使用 `"**"` 的递归 glob。

在 3.10 版本发生变更: 添加了 `root_dir` 和 `dir_fd` 形参。

在 3.11 版本发生变更: 增加了 `include_hidden` 形参。 

**例子** 
考虑一个包含以下文件的目录: `1.gif`, `2.txt`, `card.gif` 以及一个子目录 `sub` 且其中只包含一个文件 `3.txt`。 [glob()](https://docs.python.org/zh-cn/3.13/library/glob.html#module-glob) 将产生如下结果。 请注意路径的任何开头部件都将被保留。 

```python
>>> import subprocess
>>> print(subprocess.run('tree', capture_output=True, text=True).stdout)
.
├── 1.gif
├── 2.txt
├── card.gif
└── sub
    └── 3.txt

2 directories, 4 files

>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']
>>> 
```

如果目录包含以 `.` 打头的文件，它们默认将不会被匹配。 例如，考虑一个包含 `card.gif` 和 `.card.gif` 的目录:

```python
>>> print(subprocess.run(['tree', '-a'], capture_output=True, text=True).stdout)
.
├── .card.gif
└── card.gif

1 directory, 2 files

>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']
>>> glob.glob('*.gif', include_hidden=True)
['.card.gif', 'card.gif']
>>> 
```

|模式           |含义 
|---------------|-----------------------------------------
|`*`            |匹配当前目录下任意名称，不跨目录，不匹配 `/` 
|recursive=True |必须开启才能使用 `**` 
|`**`           |匹配目录中的任何文件以及零个或多个目录、子目录和符号链接 
|`**/`          |仅匹配目录，匹配任意层级的目录路径 

**参见：** [fnmatch](https://docs.python.org/zh-cn/3.13/library/fnmatch.html#module-fnmatch) 模块提供了 shell 风格的文件名（而非路径）扩展。 

**参见：** [pathlib](https://docs.python.org/zh-cn/3.13/library/pathlib.html#module-pathlib) 模块提供高级路径对象。 
<br />

## 文件格式
本章描述的模块解析各种既不是标记语言也与e-mail无关的其它文件格式。

### csv — CSV文件读写
**源代码：** [Lib/csv.py](https://github.com/python/cpython/tree/3.7/Lib/csv.py)

所谓的 CSV (Comma Separated Values) 格式是表和数据库最常见的导入和导出格式。

csv 模块的 [reader](https://docs.python.org/3/library/csv.html#csv.reader) 和 [writer](https://docs.python.org/3/library/csv.html#csv.writer) 对象读和写序列。程序员也可以使用 [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader) 和 [DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter) 类来读写字典形式中的数据。

#### 模块内容
[csv](https://docs.python.org/3/library/csv.html#module-csv) 模块定义了下列函数：

csv.**reader**(*csvfile, dialect='excel', \*\*fmtparams*)  
返回一个将遍历给定的 *csvfile* 文件中的行的 reader 对象。*csvfile* 可以是支持[迭代器](https://docs.python.org/3/glossary.html#term-iterator)协议及每次调用它的 `__next__()` 方法都返回一个字符串的任意对象 — [文件对象](https://docs.python.org/3/glossary.html#term-file-object) 和列表对象都是适合的。如果 *csvfile* 是一个文件对象，打开它时必须带有 `newline=''`。（如果没有指定 `newline=''`，新行嵌入引用字段后将不能被正确解释，且在以 `\r\n` 作为行结束符的平台会写入一个额外的 `\r`。总是指定 `newline=''` 应该是安全的，因为 csv 模块执行自己的 ([universal](https://docs.python.org/3/glossary.html#term-universal-newlines)) 新行处理方法。）

```sh
$ cat club.csv
113,菲比酒吧
114,哥弟KTV
```

```python
>>> import csv
>>> with open('club.csv', newline='') as csvfile:
...     content = csv.reader(csvfile)
...     for item in content:
...         print(item)
...
['113', '菲比酒吧']
['114', '哥弟KTV']
>>>
```

```python
>>> import csv
>>> with open('club.csv', newline='') as csvfile:
...     content = csv.reader(csvfile)
...     for id, name in content:
...         print(name)
...
菲比酒吧
哥弟KTV
>>>
```

```python
>>> _list = ['a', 'b', 'c']
>>> content = csv.reader(_list)
>>> for item in content:
...     print(item)
...
['a']
['b']
['c']
>>>
```

csv.**writer**(_csvfile, dialect='excel', \*\*fmtparams_)  
Return a writer object responsible for converting the user’s data into delimited strings on the given file-like object. *csvfile* 可以是带有一个 `write()` 方法的任意对象。如果 *csvfile* 是一个文件对象，打开它时必须带有 `newline=''`。（如果没有指定 `newline=''`，新行嵌入引用字段后将不能被正确解释，且在以 `\r\n` 作为行结束符的平台会写入一个额外的 `\r`。总是指定 `newline=''` 应该是安全的，因为 csv 模块执行自己的 ([universal](https://docs.python.org/3/glossary.html#term-universal-newlines)) 新行处理方法。）

```python
>>> import csv
>>> with open('school.csv', 'w', newline='') as csvfile:
...     writer = csv.writer(csvfile)
...     writer.writerow(['班级', '姓名', '学号'])
...     writer.writerow([181, '成龙', 20181801])
...     writer.writerow([181, '李连杰', 20181802])
...
10
17
18
>>>
```

[csv](https://docs.python.org/zh-cn/3.9/library/csv.html#module-csv) 模块定义了以下类：

*class* csv.**DictReader(**_f, fieldnames=None, restkey=None, restval=None, dialect='excel', \*args, \*\*kwds_**)**  
创建一个对象，该对象在操作上类似于常规 reader，但是将每行中的信息映射到一个 [字典](https://docs.python.org/zh-cn/3.9/library/stdtypes.html#dict)，该字典的键由 *fieldnames* 可选参数给出。

*fieldnames* 参数是一个 [序列](https://docs.python.org/zh-cn/3.9/glossary.html#term-sequence)。如果省略 *fieldnames*，则文件 *f* 第一行中的值将用作字段名。无论字段名是如何确定的，字典都将保留其原始顺序。

如果某一行中的字段多于字段名，则剩余数据会被放入一个列表，并与 *restkey* 所指定的字段名 (默认为 `None`) 一起保存。 如果某个非空白行的字段少于字段名，则缺失的值会使用 *restval* 的值来填充 (默认为 `None`)。

所有其他可选或关键字参数都传递给底层的 [reader](https://docs.python.org/zh-cn/3.9/library/csv.html#csv.reader) 实例。

*在 3.6 版更改:* 返回的行现在的类型是 OrderedDict。

*在 3.8 版更改:* 现在，返回的行是 [字典](https://docs.python.org/zh-cn/3.9/library/stdtypes.html#dict) 类型。

一个简短的用法示例:

```python
>>> import csv
>>> with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
... 
Baked Beans
Lovely Spam
Wonderful Spam
>>> print(row)
{'first_name': 'Wonderful', 'last_name': 'Spam'}
```

*class* csv.**DictWriter(**_f, fieldnames, restval='', extrasaction='raise', dialect='excel', \*args, \*\*kwds_**)**  
创建一个对象，该对象在操作上类似常规 writer，但会将字典映射到输出行。 *fieldnames* 参数是由键组成的 [序列](https://docs.python.org/zh-cn/3.9/library/collections.abc.html#module-collections.abc)，它指定字典中值的顺序，这些值会按指定顺序传递给 `writerow()` 方法并写入文件 *f*。 如果字典缺少 *fieldnames* 中的键，则可选参数 *restval* 用于指定要写入的值。 如果传递给 `writerow()` 方法的字典的某些键在 *fieldnames* 中找不到，则可选参数 *extrasaction* 用于指定要执行的操作。 如果将其设置为默认值 `'raise'`，则会引发 [ValueError](https://docs.python.org/zh-cn/3.9/library/exceptions.html#ValueError)。 如果将其设置为 `'ignore'`，则字典中多余的值将被忽略。 所有其他可选或关键字参数都传递给底层的 [writer](https://docs.python.org/zh-cn/3.9/library/csv.html#csv.writer) 实例。

注意，与 [DictReader](https://docs.python.org/zh-cn/3.9/library/csv.html#csv.DictReader) 类不同，[DictWriter](https://docs.python.org/zh-cn/3.9/library/csv.html#csv.DictWriter) 类的 *fieldnames* 参数不是可选参数。

一个简短的用法示例:

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```

#### Writer对象
`Writer` 对象 ([DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter) 实例和 [writer()](https://docs.python.org/3/library/csv.html#csv.writer) 函数返回的对象) 具有下列公共方法。对于 `Writer` 对象，*行* 必须是一组可迭代的字符串或数字。对于 [DictWriter](https://docs.python.org/3.9/library/csv.html#csv.DictWriter) 对象，*行* 必须是一个字典，这个字典将字段名映射为字符串或数字（数字要先经过 [str()](https://docs.python.org/3.9/library/stdtypes.html#str) 转换类型）。请注意，输出的复数会有括号包围。这可能导致其他程序读取 CSV 文件时会有一些问题（假设它们完全支持复数）。

csvwriter.**writerow**(*row*)  
将 *row* 参数写入到 writer 的文件对象中，并根据当前的 [Dialect](https://docs.python.org/3.9/library/csv.html#csv.Dialect) 进行格式化。

*在版本3.5中发生变化：* 支持任意可迭代对象。  

csvwriter.**writerows(**_rows_**)**  
将 *rows*（即上面描述的能迭代 *row* 的对象）中的所有元素写入 writer 的文件对象，并根据当前的 dialect 进行格式化。

Writer 对象具有以下公共属性：

csvwriter.**dialect**  
一个只读的 dialect 描述，供 writer 使用。

DictWriter 对象具有以下公共方法：

DictWriter.**writeheader()**  
在 writer 的文件对象中，写入一行字段名称（字段名称在构造函数中指定），并根据当前的 dialect 进行格式化。本方法的返回值就是内部调用的 [csvwriter.writerow()](https://docs.python.org/3.9/library/csv.html#csv.csvwriter.writerow) 的返回值。

*3.2 新版功能.*  

*在 3.8 版更改:* 现在 [writeheader()](https://docs.python.org/3.9/library/csv.html#csv.DictWriter.writeheader) 也返回其内部使用的 [csvwriter.writerow()](https://docs.python.org/3.9/library/csv.html#csv.csvwriter.writerow) 方法的返回值。  

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

os.**mkdir(**_path, mode=0o777, \*, dir_fd=None_**)**  
创建一个名为 *path* 的目录，并应用数字模式 *mode*。

如果目录已经存在， [FileExistsError](https://docs.python.org/3/library/exceptions.html#FileExistsError) 会被引发。如果路径中的父目录不存在，则会引发 [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError) 。

某些系统会忽略 *mode*。在使用它的地方，当前的 umask 值首先被屏蔽掉。 如果设置了最后 9 位以外的位（即 *mode* 的八进制表示的最后 3 位数），则它们的含义取决于平台。在某些平台上，它们会被忽略，您应该显式调用 [chmod()](https://docs.python.org/3/library/os.html#os.chmod) 来设置它们。

本函数也支持 [目录描述符的相对路径](https://docs.python.org/3/library/os.html#dir-fd)。

创建临时目录也是可能的，请参阅 [tempfile](https://docs.python.org/3/library/tempfile.html#module-tempfile) 模块的 [tempfile.mkdtemp()](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp) 函数。

`os.mkdir` 附带参数 `path`、`mode` 和 `dir_fd` 引发一个 [审计事件](https://docs.python.org/3/library/sys.html#auditing) 。

*3.3 新版功能:* *dir_fd* 参数。

*在 3.6 版更改:* 接受一个 [path-like 对象](https://docs.python.org/3/glossary.html#term-path-like-object)。


os.**remove(**_path, *, dir_fd=None_**)** 
移除（删除）文件 _path_。如果 _path_ 是目录，则会引发 [OSError](https://docs.python.org/zh-cn/3.13/library/exceptions.html#OSError)。请使用 [rmdir()](https://docs.python.org/zh-cn/3.13/library/os.html#os.rmdir) 来移除目录。 如果文件不存在，则会引发 [FileNotFoundError](https://docs.python.org/zh-cn/3.13/library/exceptions.html#FileNotFoundError)。

本函数支持 [基于目录描述符的相对路径](https://docs.python.org/zh-cn/3.13/library/os.html#dir-fd)。

在 Windows 上，尝试删除正在使用的文件会抛出异常。而在 Unix 上，虽然该文件的条目会被删除，但分配给文件的存储空间仍然不可用，直到原始文件不再使用为止。

本函数在语义上与 [unlink()](https://docs.python.org/zh-cn/3.13/library/os.html#os.unlink) 相同。

os.remove 包含参数 `path` 和 `dir_fd` 时引发一个 [审计事件](https://docs.python.org/3.13/library/sys.html#auditing)。 

在 3.3 版本发生变更: 添加了 _dir_fd_ 参数。

在 3.6 版本发生变更: 接受一个 [path-like 对象](https://docs.python.org/3.13/glossary.html#term-path-like-object)。 

```sh
➜  ~ ls
github  readme.txt  temp.py
➜  ~ cat temp.py 
import os.path
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, 'readme.txt')
os.remove(filename)
➜  ~ 
➜  ~ python temp.py 
➜  ~ ls
github  temp.py
➜  ~ 
```

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

#### 调度程序接口
这些函数用于控制操作系统如何为进程分配CPU时间，仅在某些Unix平台上可用。如需更详细的信息，请参考您的Unix手册页（manpages）。 

*在版本 3.3 中增加。* 

如果操作系统支持，以下调度策略将被公开。 

os.**SCHED_OTHER**  
默认调度策略。 

os.**sched_getaffinity(**_pid, /_**)** 
返回进程（PID为 _pid_）被限制使用的CPU集合。 

如果 _pid_ 为 0，则返回当前进程的调用线程被限制使用的 CPU 集合。 

另请参见 [process_cpu_count()](https://docs.python.org/3/library/os.html#os.process_cpu_count) 函数。 

```python
>>> import os
>>> os.sched_getaffinity(0)  # 返回当前线程可用的CPU核心的编号的集合（PI zero 2 w）
{0, 1, 2, 3}
>>> 
```

#### 各种各样的系统信息

下面的数据值被用于支持路径操作运算。这些是为所有平台定义。

高层次的路径名操作被定义在 [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path) 模块中。

os.**sep**  
操作系统用来分隔路径名组件的字符。POSIX 为 `'/'` 而 Windows 为 `'\\'`。Note that knowing this is not sufficient to be able to parse or concatenate pathnames — 使用 [os.path.split()](https://docs.python.org/3.6/library/os.path.html#os.path.split) 和 [os.path.join()](https://docs.python.org/3.6/library/os.path.html#os.path.join) — 但它偶尔是有用的。Also available via [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path)。  

```python
>>> import platform
>>> import os
>>> platform.system()
'Windows'
>>> os.sep
'\\'
>>> print(os.sep) 
\
>>> print('\\')
\
>>> 
```

```python
>>> import tushare as ts
>>> pro = ts.pro_api()
>>> df1 = pro.hk_hold(trade_date='20220527', exchange='SH')
>>> df2 = pro.hk_hold(trade_date='20220527', exchange='SZ')
>>> df1.to_excel('C:\\Users\\WHY\\Downloads\\SH.xlsx')  # 标准 Windows 路径分隔符
>>> df2.to_excel('C:/Users/WHY/Downloads/SZ.xlsx')      # 类 Unix 路径分隔符
>>>
```

### io --- 处理流的核心工具
**源代码:** [Lib/io.py](https://github.com/python/cpython/tree/3.9/Lib/io.py)  

#### 高阶模块接口
io.**open(**_file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None_**)**  
这是内置的 [open()](https://docs.python.org/zh-cn/3.9/library/functions.html#open) 函数的别名。

`open` 附带参数 `path`、`mode` 和 `flags` 会引发 [审计事件](https://docs.python.org/zh-cn/3.9/library/sys.html#auditing)。`mode` 和 `flags` 参数可能已被修改或从原始调用中推断出来。

**另请参见：**

[sys](https://docs.python.org/3/library/sys.html#module-sys)  
包含标准IO流：[sys.stdin](https://docs.python.org/3/library/sys.html#sys.stdin)，[sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout)，和 [sys.stderr](https://docs.python.org/3/library/sys.html#sys.stderr)。

#### 类层次结构
![class hierarchy](/img/tpsl_16_2_3_class_hierarchy.png)

下表总结了 [io](https://docs.python.org/3/library/io.html#module-io) 模块提供的抽象基类：  

抽象基类  |继承      |Stub Methods      |Mixin Methods and Properties  
---------|----------|------------------|----------------------------  
[IOBase](https://docs.python.org/3/library/io.html#io.IOBase)  |   |`fileno`, `seek` 和 `truncate`  |`close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable`, 和 `writelines`  
[RawIOBase](https://docs.python.org/3/library/io.html#io.RawIOBase)  |[IOBase](https://docs.python.org/3/library/io.html#io.IOBase)  |`readinto` 和 `write`  |继承 [IOBase](https://docs.python.org/3/library/io.html#io.IOBase) 方法，`read`, 和 `readall`  
[BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase)  |[IOBase](https://docs.python.org/3/library/io.html#io.IOBase)  |`detach`, `read`, `read1`, 和 `write`  |继承 [IOBase](https://docs.python.org/3/library/io.html#io.IOBase) 方法，`readinto`, 和 `readinto1`  
[TextIOBase](https://docs.python.org/3/library/io.html#io.TextIOBase)  |[IOBase](https://docs.python.org/3/library/io.html#io.IOBase)  |`detach`, `read`, `readline`, 和 `write`  |继承 [IOBase](https://docs.python.org/3/library/io.html#io.IOBase) 方法，`encoding`, `errors`, 和 `newlines`  

##### I/O 基类

*class* io.**IOBase**  
所有 I/O 类的抽象基类，作用于字节流。没有公共构造函数（constructor）。

从一个文件读取或写入二进制数据的基本类型是 [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes)。其它 [bytes-like object](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) 也可以作为方法参数被接受。在某些情况下，例如 [readinto()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readinto)，要求一个可写的对象如 [bytearray](https://docs.python.org/3.6/library/stdtypes.html#bytearray)。文本 I/O 类对 [str](https://docs.python.org/3.6/library/stdtypes.html#str) 数据有效。

[IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 也是一个上下文管理器，因此支持 [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) 声明。在这个例子中，*file* is closed after the [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) statement’s suite is finished——即使出现异常：

```python
>>> with open('spam.txt', 'w') as file:
...     file.write('Spam and eggs!')
...
14
>>> file.closed
True
```

[IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 提供这些数据属性和方法：

**closed**  
如果流是关闭的，则返回 `True`。

*class* io.**RawIOBase**  
原始二进制 I/O 的基类。它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的属性和方法，[RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 还提供下面的方法：

**read**(*size=-1*)  
Read up to *size* bytes from the object and return them. 为了方便起见，如果 *size* 没有指定或者为 -1, all bytes until EOF are returned. Otherwise, only one system call is ever made. Fewer than *size* bytes may be returned if the operating system call returns fewer than *size* bytes.

如果返回 0 字节，且 *size* 不是 0，this indicates end of file. If the object is in non-blocking mode and no bytes are available, `None` is returned.

默认实现遵守 [readall()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readall) 和 [readinto()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readinto)。

*class* io.**BufferedIOBase**  
支持某种缓冲的二进制流的基类。它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了那些从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法和属性，[BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 还提供或重写了这些方法和属性：

**read**(*size=-1*)  
Read and return up to *size* bytes. If the argument is omitted, `None`, or negative, data is read and returned until EOF is reached. An empty [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes) object is returned if the stream is already at EOF.

##### 原始文件 I/O
*class* io.**FileIO**(*name, mode='r', closefd=True, opener=None*)  
[FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO) 代表一个包含字节数据的操作系统级别的文件。它实现了 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 接口 (因此也实现了 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 接口)。

除了从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 和 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 继承的属性和方法，[FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO) 还提供下面的数据属性：

**mode**  
构造函数中指定的模式。

##### 缓冲流
缓冲 I/O 流比原始 I/O 流为 I/O 设备提供了一个更高层次的接口。

*class* io.**BytesIO**(**[**_initial_bytes_**]**)  
使用内存中的一个字节缓冲区实现一个流。它继承 [BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase)。当 [close()](https://docs.python.org/3/library/io.html#io.IOBase.close) 方法被调用时缓冲区被丢弃。

可选参数 *initial_bytes* 是一个包含初始化数据的 [bytes-like 对象](https://docs.python.org/3/glossary.html#term-bytes-like-object)。

除了那些从 [BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3/library/io.html#io.IOBase) 继承的方法，[BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO) 提供或重写了这些方法：

*class* io.**BufferedReader**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
除了那些从 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法，[BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 还提供或重写了这些方法：

**read**([*size*])  
读取并返回 *size* 字节，或者如果 *size* 没有给出或者是负数，until EOF or if the read call would block in non-blocking mode.

*class* io.**BufferedWriter**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
一个为可写的，连续的 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 对象提供更高层次访问的缓冲区。它继承 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase)。当向这个对象写数据时，数据通常被放进一个内部缓冲区。缓冲区在多种条件下将被写到底层的 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 对象，包括：

* 对所有挂起的数据来说，当缓冲区太小时；
* 当 [flush()](https://docs.python.org/3.6/library/io.html#io.BufferedWriter.flush) 被调用时；
* 当 seek() 被请求时(对于 [BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom) 对象);
* 当 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 对象被关闭或者销毁时。 

除了那些从 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法，[BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 还提供或重写了这些方法：

**write**(*b*)  
写入 [bytes-like 对象](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) *b*，并返回写入的字节数。When in non-blocking mode, a [BlockingIOError](https://docs.python.org/3.6/library/exceptions.html#BlockingIOError) is raised if the buffer needs to be written out but the raw stream blocks.

*class* io.**BufferedRandom**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
一个随机访问流的缓冲区接口。它继承 [BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 和 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter), and further supports seek() and tell() functionality.

The constructor creates a reader and writer for a seekable raw stream, given in the first argument. 如果 *buffer_size* 被省略，则它默认为 [DEFAULT_BUFFER_SIZE](https://docs.python.org/3.6/library/io.html#io.DEFAULT_BUFFER_SIZE)。

[BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom) 可以做任何 [BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 或者 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 能做的事。

```python
>>> import io
>>> issubclass(io.BufferedRandom, io.BufferedReader)
False
>>> issubclass(io.BufferedRandom, io.BufferedWriter)
False
```

Python官方文档里说 `io.BufferedRandom` 继承 `io.BufferedReader` 和 `io.BufferedWriter`，但不知为何 `issubclass(io.BufferedRandom, io.BufferedReader)` 和 `issubclass(io.BufferedRandom, io.BufferedWriter)` 的返回结果都是 `False`。

##### 文本 I/O
*class* io.**TextIOBase**  
文本流的基类。This class provides a character and line based interface to stream I/O. There is no readinto() method because Python’s character strings are immutable. 它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了那些从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的属性和方法，[TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase) 提供或重写了这些数据属性和方法：

**read**(*size*)  
从流中读取并返回至多 *size* 个字符作为一个单一 [str](https://docs.python.org/3.6/library/stdtypes.html#str)。如果 *size* 是负数或者 `None`, reads until EOF.

**write(**_s, /_**)**  
将字符串 *s* 写入流并返回写入的字符数。  

*class* io.**TextIOWrapper**(*buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False*)  
A buffered text stream over a [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) binary stream. 它继承 [TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase)。

*class* io.**StringIO**(*initial_value='', newline='\n'*)  
一个用于文本I/O的内存中的流。当 [close()](https://docs.python.org/3/library/io.html#io.IOBase.close) 方法被调用时文本缓冲区被丢弃。

缓冲区的初始值可以通过提供的 *initial_value* 参数继续设置。如果新行转化被启用，newlines will be encoded as if by [write()](https://docs.python.org/3/library/io.html#io.TextIOBase.write)。流被放在缓冲区的起始位置。  

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

### getopt — C-风格的命令行选项解析器
**Source code:** [Lib/getopt.py](https://github.com/python/cpython/tree/3.6/Lib/getopt.py)

这个模块提供2个函数和1个异常：

getopt.**getopt**(*args, shortopts, longopts=[]*)  
分析命令行选项和参数列表。*args* 是被分析的参数列表，不包含首部的正在运行的程序引用。通常，这意为 `sys.argv[1:]`。*shortopts* 是脚本想要识别的选项字母字符串，要求一个参数的选项后面跟随一个冒号(`':'`；也就是，Unix getopt() 使用的相同的格式)。

**注意：** 和 GUN `getopt()` 不同，在一个非选项参数之后，所有更远的参数也都被认为是非选项。这和非GUN Unix系统的工作方式相似。

*longopts*，如果指定，必须是一个应该被支持的长选项名称的字符串列表。前导字符 `'--'` 不应该包含在选项名中。要求一个参数的长选项后面应该跟随一个等号(`'='`)。不支持可选参数。如果仅接受长选项，则 *shortopts* 应该是一个空串。命令行中的长选项只要它们提供的选项名前缀可以精确地匹配一个可以接受的选项就能够被识别。例如，如果 *longopts* 是 `['foo', 'frob']`，则选项 `--fo` 将匹配为 `--foo`，但 `--f` 就不能唯一匹配了，所以将抛出 [GetoptError](https://docs.python.org/3.6/library/getopt.html#getopt.GetoptError)异常。

返回值由2个元素组成：the first is a list of `(option, value)` pairs; 第二个是选项列表被截取后余下的程序参数列表(这是 *args* 的尾部切片)。对于每一个返回的 option-and-value pair，选项作为它的第一个元素，用一个连字符作为短选项的前缀(例如, `'-x'`)或者两个连字符作为长选项的前缀(例如, `'--long-option'`)，选项参数作为它的第二个元素，如果选项没有参数，则用一个空串。选项出现在列表中的顺序与它们被发现的顺序相同，因此允许多次出现。长选项和短选项可以混合。

### logging --- Python 的日志记录工具
**源代码：** [Lib/logging/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.9/Lib/logging/__init__.py)

**重要**  

此页面仅包含 API 参考信息。教程信息和更多高级用法的讨论，请参阅

* [基础教程](https://docs.python.org/3.9/howto/logging.html#logging-basic-tutorial)  
* [进阶教程](https://docs.python.org/3.9/howto/logging.html#logging-advanced-tutorial)  
* [日志操作手册](https://docs.python.org/3.9/howto/logging-cookbook.html#logging-cookbook)  

这个模块为应用与库实现了灵活的事件日志系统的函数与类。

使用标准库模块提供的日志记录 API 的主要好处是所有 Python 模块都可以参与日志记录，因此您的应用程序日志可以包含您自己的消息与来自第三方模块的消息集成。

这个模块提供许多强大而灵活的功能。如果你对 logging 不太熟悉，掌握它最好的方式就是查看它对应的教程。

#### 日志级别
日志级别的数值已在下表给出。如果你想自定义级别这将是你最感兴趣的，它们必须有相对于预定义级别的特定的值。如果你使用相同的数值定义一个级别，它将覆盖预定义的值，且预定义的名称也将丢失。

|Level       |Numeric value  |
|------------|---------------|
|`CRITICAL`  |50             |
|`ERROR`     |40             |
|`WARNING`   |30             |
|`INFO`      |20             |
|`DEBUG`     |10             |
|`NOTSET`    |0              |

#### LogRecord属性
LogRecord有许多属性，大多数来源于构造函数的参数。(注意，LogRecord构造函数的参数名称与LogRecord属性名称之间并非总是正确对应。)这些属性可以用来合并由记录转换成格式化字符串的数据。下表列出了（按字母顺序）属性名称，它们的意义以及对应的 %-style 格式化字符串占位符。

如果你使用 {}-formatting ([str.format()](https://docs.python.org/3.6/library/stdtypes.html#str.format)), 那么在格式化字符串中你可以使用 `{attrname}` 作为占位符。如果你使用 \$-formatting ([string.Template](https://docs.python.org/3.6/library/string.html#string.Template)), 那么使用 `${attrname}` 形式。在这两种情况下，当然，用你实际要用的属性名称替换 `attrname`。

在使用 {}-formatting 的情况下，你可以通过在属性名称之后指定格式化标志，用冒号(:)分隔。例如：`{msecs:03d}` 占位符将格式化毫秒值 `4` 为 `004`。关于可用选项的全部细节请参考 [str.format()](https://docs.python.org/3.6/library/stdtypes.html#str.format) 文档。

|Attribute name  |Format                     |Description                     |
|----------------|---------------------------|--------------------------------|
|args            |你不必自己格式化这个          |参数元组结合 `msg` 以产生 `message`，或者一个字典的值用来结合<br> `msg`（当仅有一个参数，且它是一个字典）。
|levelname       |`%(levelname)s`            |消息的文本日志级别(`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`)                                |
|message         |`%(message)s`              |记录的消息，计算 `msg % args`。当 [Formatter.format()](https://docs.python.org/3.6/library/logging.html#logging.Formatter.format) 被<br>调用时，这个属性被设置。
|msg             |你不必自己格式化这个          |传递给原始日志调用的格式化字符串。与 `args` 合并以产生 <br>`message`，或者一个任意对象（参考[使用任意对象作为消息](https://docs.python.org/3.6/howto/logging.html#arbitrary-object-messages)）。    

#### 模块级别的函数
除了上面描述的类，还有一些模块级别的函数。

logging.**basicConfig**(_\*\*kwargs_)  
通过创建一个带一个默认 [Formatter](https://docs.python.org/3.6/library/logging.html#logging.Formatter) 的 [StreamHandler](https://docs.python.org/3.6/library/logging.handlers.html#logging.StreamHandler) 来为日志系统做基本配置，并将其添加到根记录器。如果没有为根记录器定义处理器，则函数 [debug()](https://docs.python.org/3.6/library/logging.html#logging.debug), [info()](https://docs.python.org/3.6/library/logging.html#logging.info), [warning()](https://docs.python.org/3.6/library/logging.html#logging.warning), [error()](https://docs.python.org/3.6/library/logging.html#logging.error) 和 [critical()](https://docs.python.org/3.6/library/logging.html#logging.critical) 将自动调用
[basicConfig()](https://docs.python.org/3.6/library/logging.html#logging.basicConfig)。

如果已经为根记录器配置了处理器，则这个函数什么也不做。

**注意：** 这个函数应该在其它线程启动以前由main线程调用。在Python版本2.7.1和3.2以前，如果这个函数被多线程调用，可能（尽管这种情况很少出现）会使处理器（handler）被多次添加到根记录器，这将导致意外结果，如日志中的消息重复。

支持下列关键字参数（keyword arguments）。  

|Format     |Description    |
|-----------|---------------|
`format`    |为处理器使用指定的格式化字符串  
`level`     |设置根记录器级别为指定的级别  

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

### ctypes --- Python 的外部函数库
[ctypes](https://docs.python.org/3.9/library/ctypes.html#module-ctypes) 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。

#### ctypes reference
##### 查找共享库
当用编译语言编程时，当编译或者链接一个程序及当程序运行时，共享库被访问。

The purpose of the find_library() function is to locate a library in a way similar to what the compiler or runtime loader does (在一个共享库有几个版本的平台上应该加载最新版本), while the ctypes library loaders act like when a program is run, and call the runtime loader directly.

ctypes.util 模块提供了一个函数可以帮助检测要加载的库。

ctypes.util.**find_library**(*name*)  
尝试查找一个库并返回一个路径名。*name* 是不带任何前缀像 `lib`，后缀像 `.so`，`.dylib` 或版本号的库名 (this is the form used for the posix linker option -l). 如果不能找到库则返回 `None`。

准确的功能依赖于系统。

在Linux中，find_library() 尝试运行外部程序 (`/sbin/ldconfig`, `gcc`, `objdump` 和 `ld`) 查找库文件。它返回库文件的文件名。

*在版本3.6中发生变化：* 在Linux中，当搜索库时环境变量 `LD_LIBRARY_PATH` 的值被使用，如果一个库不能通过任何其它方法找到。

这里有一些例子：  
在Linux上：

```python
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
```

在macOS上，find_library() 尝试几个预定义的名称方案和路径以定位库，并返回一个完整的路径名如果成功的话：

```python
>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>
```

在Windows上, find_library() 沿着系统搜索路径搜索，并返回完整的路径名，但因为没有预定义的名称方案一个像 `find_library("c")` 的调用将失败并返回 `None`。

```python
>>> from ctypes.util import find_library
>>> find_library("c")
>>> find_library("m")
>>> find_library("bz2")
>>> find_library("apphelp")
'C:\\WINDOWS\\system32\\apphelp.dll'
>>> find_library("aphostclient")
'C:\\WINDOWS\\system32\\aphostclient.dll'
>>> find_library("APHostClient")
'C:\\WINDOWS\\system32\\APHostClient.dll'
>>> find_library("xinstaller")
'C:\\WINDOWS\\xinstaller.dll'
>>>
```

If wrapping a shared library with [ctypes](https://docs.python.org/3/library/ctypes.html#module-ctypes), it *may* be better to determine the shared library name at development time, and hardcode that into the wrapper module instead of using find_library() to locate the library at runtime.

##### 实用函数
ctypes.util.**find_library**(*name*)  
尝试查找一个库并返回一个路径名。*name* 是不带任何前缀像 `lib`，后缀像 `.so`，`.dylib` 或版本号的库名 (this is the form used for the posix linker option -l). 如果不能找到库则返回 `None`。

准确的功能依赖于系统。

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

默认情况下标准输入、标准输出及标准错误的文件对象以二进制模式打开，而参数 text=True 的作用是以文本模式打开响应的文件。 

```python
>>> import subprocess
>>> result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True)
>>> result.stdout
b"temp=51.5'C\n"
>>> result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
>>> result.stdout
"temp=51.0'C\n"
>>> result.stdout.strip()
"temp=51.0'C"
>>> print(result.stdout.strip())
temp=51.0'C
>>> 
```

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

*在 3.12 版本发生变更:* 针对 `shell=True` 改变的 Windows shell 搜索顺序。 当前目录和 `%PATH%` 会被替换为 `%COMSPEC%` 和 `%SystemRoot%\System32\cmd.exe`。 因此，在当前目录中投放一个命名为 `cmd.exe` 的恶意程序不会再起作用。 
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
<br />

*exception* subprocess**.CalledProcessError** 
[SubprocessError](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.SubprocessError) 的子类，当一个由 [check_call()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.check_call), [check_output()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.check_output) 或 [run()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.run) (附带 `check=True`) 运行的进程返回了非零退出状态码时将被引发。

**returncode** 
子进程的退出状态。如果程序由一个信号终止，这将会被设为一个负的信号码。

**cmd** 
用于创建子进程的指令。

**output** 
子进程的输出，如果被 [run()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.run) 或 [check_output()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.check_output) 捕获。否则为 `None`。

**stdout** 
对 output 的别名，对应的有 [stderr](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.CalledProcessError.stderr)。

**stderr** 
子进程的标准错误输出，如果被 [run()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.run) 捕获。 否则为 `None`。

*在 3.5 版本发生变更:* 添加了 *stdout* 和 *stderr* 属性。 
<br /> 

##### 常用参数
为了支持丰富的使用案例， [Popen](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen) 的构造函数（以及方便的函数）接受大量可选的参数。对于大多数典型的用例，许多参数可以被安全地留以它们的默认值。通常需要的参数有：

*args* 被所有调用需要，应当为一个字符串，或者一个程序参数序列。提供一个参数序列通常更好，它可以更小心地使用参数中的转义字符以及引用（例如允许文件名中的空格）。如果传递一个简单的字符串，则 *shell* 参数必须为 [True](https://docs.python.org/zh-cn/3.13/library/constants.html#True) （见下文）或者该字符串中将被运行的程序名必须用简单的命名而不指定任何参数。

```python
>>> subprocess.run('uname')
Linux
CompletedProcess(args='uname', returncode=0)
>>> subprocess.run('uname -a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.11/subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/subprocess.py", line 1024, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib/python3.11/subprocess.py", line 1901, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'uname -a'
>>> subprocess.run('uname -a', shell=True)
Linux pizero2w 6.12.25+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.25-1+rpt1 (2025-04-30) aarch64 GNU/Linux
CompletedProcess(args='uname -a', returncode=0)
>>> 
```

从上面的代码可以看出，当 *agrs* 参数是一个简单的字符串时，如果没有 shell=True 参数，那么 subprocess 模块会把整个字符串当成是一个程序名，即有可执行文件的的名称是该字符串，而实际上，在 Linux 平台，没有哪一个命令是包含空格的，所以最终抛出了一个 *FileNotFoundError* 的异常。 

*stdin*, *stdout* 和 *stderr* 分别指定被执行程序的标准输入、标准输出和标准错误文件句柄。 合法的值包括 `None`, [PIPE](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.PIPE), [DEVNULL](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.DEVNULL), 现存的文件描述符（一个正整数），现存的具有合法文件描述符的 [文件对象](https://docs.python.org/zh-cn/3.13/glossary.html#term-file-object)。 当使用默认设置 `None` 时，将不会进行任何重定向。 [PIPE](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.PIPE) 表示应当新建一个连接子进程的管道。 [DEVNULL](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.DEVNULL) 表示将使用特殊文件 [os.devnull](https://docs.python.org/zh-cn/3.13/library/os.html#os.devnull)。 此外，*stderr* 还可以为 [STDOUT](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.STDOUT)，这表示来自子进程的 stderr 数据应当被捕获到与 *stdout* 相同的文件句柄中。

如果指定了 *encoding* 或 *errors*，或者 *text* (也称 *universal_newlines*) 为真，则文件对象 *stdin*、 *stdout* 与 *stderr* 将会使用在此次调用中指定的 *encoding* 和 *errors* 或者 [io.TextIOWrapper](https://docs.python.org/zh-cn/3.13/library/io.html#io.TextIOWrapper) 的默认值以文本模式打开。

当构造函数的 *newline* 参数为 `None` 时。对于 *stdin*， 输入的换行符 `'\n'` 将被转换为默认的换行符 [os.linesep](https://docs.python.org/zh-cn/3.13/library/os.html#os.linesep)。对于 *stdout* 和 *stderr*， 所有输出的换行符都被转换为 `'\n'`。更多信息，查看 [io.TextIOWrapper](https://docs.python.org/zh-cn/3.13/library/io.html#io.TextIOWrapper) 类的文档。

如果文本模式未被使用， *stdin*， *stdout* 和 *stderr* 将会以二进制流模式打开。没有编码与换行符转换发生。

*在 3.6 版本发生变更:* 增加了 *encoding* 和 *errors* 形参。

*在 3.7 版本发生变更:* 添加了 *text* 形参作为 *universal_newlines* 的别名。

**备注：** 文件对象 [Popen.stdin](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen.stdin) 、 [Popen.stdout](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen.stdout) 和 [Popen.stderr](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen.stderr) 的换行符属性不会被 [Popen.communicate()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen.communicate) 方法更新。

如果 *shell* 设为 `True`，则使用 shell 执行指定的指令。如果您主要使用 Python 增强的控制流（它比大多数系统 shell 提供的强大），并且仍然希望方便地使用其他 shell 功能，如 shell 管道、文件通配符、环境变量展开以及 `~` 展开到用户家目录，这将非常有用。但是，注意 Python 自己也实现了许多类似 shell 的特性（例如 [glob](https://docs.python.org/zh-cn/3.13/library/glob.html#module-glob), [fnmatch](https://docs.python.org/zh-cn/3.13/library/fnmatch.html#module-fnmatch), [os.walk()](https://docs.python.org/zh-cn/3.13/library/os.html#os.walk), [os.path.expandvars()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.expandvars), [os.path.expanduser()](https://docs.python.org/zh-cn/3.13/library/os.path.html#os.path.expanduser) 和 [shutil](https://docs.python.org/zh-cn/3.13/library/shutil.html#module-shutil)）。

*在 3.3 版本发生变更:* 当 *universal_newlines* 被设为 `True`，则类将使用 [locale.getpreferredencoding(False)](https://docs.python.org/zh-cn/3.13/library/locale.html#locale.getpreferredencoding) 编码格式来代替 `locale.getpreferredencoding()`。 关于它们的区别的更多信息，见 [io.TextIOWrapper](https://docs.python.org/zh-cn/3.13/library/io.html#io.TextIOWrapper)。

**备注:** 在使用 `shell=True` 之前， 请阅读 [安全考量](https://docs.python.org/zh-cn/3.13/library/subprocess.html#security-considerations) 段落。

这些选项以及所有其他选项在 [Popen](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen) 构造函数文档中有更详细的描述。 
<br /> 

#### 较旧的高阶 API
在 Python 3.5 之前，这三个函数组成了 subprocess 的高阶 API。 现在你可以在许多情况下使用 [run()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.run)，但有大量现在代码仍会调用这些函数。 

subprocess**.check_call(**_args, \*, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, \*\*other_popen_kwargs_**)** 
附带参数运行命令。 等待命令完成。 如果返回码为零则正常返回，否则引发 [CalledProcessError](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.CalledProcessError)。 [CalledProcessError](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.CalledProcessError) 对象将在 [returncode](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.CalledProcessError.returncode) 属性中保存返回码。 如果 [check_call()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.check_call) 无法开始进程则它将传播已被引发的异常。

需要捕获 stdout 或 stderr 的代码应当改用 [run()](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.run)：

```python
run(..., check=True)
```

要屏蔽 stdout 或 stderr，可提供 [DEVNULL](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.DEVNULL) 这个值。

上面显示的参数只是常见的一些。 完整的函数签名与 [Popen](https://docs.python.org/zh-cn/3.13/library/subprocess.html#subprocess.Popen) 构造器的相同 —— 此函数会将所提供的 *timeout* 之外的全部参数直接传递给目标接口。

**备注:** 请不要在此函数中使用 `stdout=PIPE` 或 `stderr=PIPE`。 如果子进程向管道生成了足以填满 OS 管理缓冲区的输出而管道还未被读取时它将会阻塞。 

*在 3.3 版本发生变更:* *timeout* 被添加

*在 3.12 版本发生变更:* 针对 `shell=True` 改变的 Windows shell 搜索顺序。 当前目录和 `%PATH%` 会被替换为 `%COMSPEC%` 和 `%SystemRoot%\System32\cmd.exe`。 因此，在当前目录中投放一个命名为 `cmd.exe` 的恶意程序不会再起作用。 
<br />  

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
这章描述的模块实现了互联网协议和相关技术的支持。它们在Python中全被实现了。大多数这些模块都要求系统相关的模块 [socket](https://docs.python.org/3/library/socket.html#module-socket) 存在，目前大多数流行的平台都支持 [socket](https://docs.python.org/3/library/socket.html#module-socket)。下面是一个概述：

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

### urllib.parse — 将URLs解析为组件
**源代码:** [Lib/urllib/parse.py](https://github.com/python/cpython/tree/3.7/Lib/urllib/parse.py)

这个模块定义了一个标准接口将统一资源定位符 (URL) 字符串分解为多个组件 (寻址方案，网络定位，路径等。)，将多个组件合并还原成一个 URL 字符串，以及根据一个给定的“基类URL”将一个“相对URL”转换成一个绝对URL。

#### URL解析
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

#### URL 转码
URL 转码函数专注于获取程序数据并通过转码特殊字符和适当地编码非 ASCII 文本使其安全地用作 URL 组件。它们还支持逆转此操作以便从作为 URL 组成部分的内容中重建原始数据，如果上述的 URL 解析函数还未覆盖此功能的话。

urllib.parse.**urlencode(**_query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus_**)**  
将一个包含有 [str](https://docs.python.org/3/library/stdtypes.html#str) 或 [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) 对象的映射对象或二元组序列转换为以百分号编码的 ASCII 文本字符串。 如果所产生的字符串要被用作 [urlopen()](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) 函数的 POST 操作的 *data*，则它应当被编码为字节串，否则它将导致 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)。

结果字符串是一系列 `key=value` 对，由 `'&'` 字符进行分隔，其中 *key* 和 *value* 都已使用 *quote_via* 函数转码。 在默认情况下，会使用 [quote_plus()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus) 来转码值，这意味着空格会被转码为 `'+'` 字符而 '/' 字符会被转码为 `%2F`，即遵循 GET 请求的标准 (`application/x-www-form-urlencoded`)。 另一个可以作为 *quote_via* 传入的替代函数是 [quote()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote)，它将把空格转码为 `%20` 并且不编码 '/' 字符。 为了最大程序地控制要转码的内容，请使用 `quote` 并指定 *safe* 的值。

当使用二元组序列作为 *query* 参数时，每个元组的第一个元素为键而第二个元素为值。 值元素本身也可以为一个序列，在那种情况下，如果可选的参数 *doseq* 的值为 `True`，则为键的值序列的每个元素生成单独的 `key=value` 对，以 `'&'` 分隔。 被编码的字符串中的参数顺序将与序列中的参数元组的顺序相匹配。

*safe*, *encoding* 和 *errors* 参数会被传递给 *quote_via* (*encoding* 和 *errors* 参数仅在查询元素为 [str](https://docs.python.org/3/library/stdtypes.html#str) 时才会被传递)。

为了反向执行这个编码过程，此模块提供了 [parse_qs()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs) 和 [parse_qsl()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qsl) 来将查询字符串解析为 Python 数据结构。

请参考 [urllib 示例](https://docs.python.org/3/library/urllib.request.html#urllib-examples) 来了解如何使用 [urllib.parse.urlencode()](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) 方法来生成 URL 的查询字符串或 POST 请求的数据。

*在 3.2 版更改:* *query* 支持字节和字符串对象。

*3.5 新版功能:* *quote_via* 参数。

```python
>>> from urllib.parse import urlencode
>>> params = {'since_id': '4774091682746723'}
>>> urlencode(params)
'since_id=4774091682746723'
>>> params = {'containerid': '1076032830678474', 'since_id': '4774091682746723'}
>>> urlencode(params)
'containerid=1076032830678474&since_id=4774091682746723'
>>>
```

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

### http.client — HTTP协议客户端
**源代码：** [Lib/http/client.py](https://github.com/python/cpython/tree/3.6/Lib/http/client.py)

这个模块定义实现HTTP和HTTPS协议客户端的类。它通常不被直接使用 — 模块 [urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request) 使用它处理HTTP和HTTPS URLs。

**另请参阅：** 更高层次的HTTP客户端接口推荐 [Requests package](http://docs.python-requests.org/)。

**注意：** 如果Python编译了SSL支持 (通过 [ssl](https://docs.python.org/3.6/library/ssl.html#module-ssl) 模块)，HTTPS支持才可用。

这个模块提供了下面的类：

*class* http.client.**HTTPConnection(**_host, port=None_, **[**_timeout_, **]**_source_address=None, blocksize=8192_**)**  
一个 [HTTPConnection](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection) 实例代表与 HTTP 服务器的一个连接事务。 它的实例化应当传入一个主机和可选的端口号。 如果没有传入端口号，如果主机字符串的形式为 `主机:端口` 则会从中提取端口，否则将使用默认的 HTTP 端口（80）。 如果给出了可选的 *timeout* 参数，则阻塞操作（例如连接尝试）将在指定的秒数之后超时（如果未给出，则使用全局默认超时设置）。 可选的 *source_address* 参数可以为一个 (主机, 端口) 元组，用作进行 HTTP 连接的源地址。 可选的 *blocksize* 参数以字节为单位设置缓冲区的大小，用来发送文件类消息体。

举个例子，以下调用都是创建连接到同一主机和端口的服务器的实例：

```python
>>> h1 = http.client.HTTPConnection('www.python.org')
>>> h2 = http.client.HTTPConnection('www.python.org:80')
>>> h3 = http.client.HTTPConnection('www.python.org', 80)
>>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)
```

*在 3.2 版更改:* 添加了 *source_address* 参数。

*在 3.4 版更改:* 删除了 *strict* 参数，不再支持 HTTP 0.9 风格的“简单响应”。

*在 3.7 版更改:* 添加了 *blocksize* 参数。

*class* http.client.**HTTPResponse**(*sock, debuglevel=0, method=None, url=None*)  
Class whose instances are returned upon successful connection. Not instantiated directly by user.

*在版本3.4中发生变化：* *strict* 参量被移除了。HTTP 0.9 风格 “Simple Responses” 不再支持。

#### HTTPConnection 对象
[HTTPConnection](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection) 实例拥有下列方法：

HTTPConnection.**request(**_method, url, body=None, headers={}, \*, encode_chunked=False_**)**  
这会使用 HTTP 请求方法 *method* 和选择器 *url* 向服务器发送请求。

如果给定 *body*，那么给定的数据会在信息头完成之后发送。它可能是一个 [字符串](https://docs.python.org/3/library/stdtypes.html#str)，一个 [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)，一个打开的 [文件对象](https://docs.python.org/3/glossary.html#term-file-object)，或者一个可迭代的 [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)。如果 *body* 是字符串，它会按 HTTP 默认的 ISO-8859-1 编码。如果是一个字节类对象，它会按原样发送。如果是 [文件对象](https://docs.python.org/3/glossary.html#term-file-object)，文件的内容会被发送，这个文件对象应该至少支持`read()` 方法。如果这个文件对象是一个 [io.TextIOBase](https://docs.python.org/3/library/io.html#io.TextIOBase) 实例，由 `read()` 方法返回的数据会按 ISO-8859-1 编码，否则由 `read()` 方法返回的数据会按原样发送。如果 *body* 是一个迭代器，迭代器中的元素会被发送，直到迭代器耗尽。

*headers* 参数应该是额外的随请求一起发送的 HTTP 信息头的字典。

如果 *headers* 既不包含 Content-Length 也没有 Transfer-Encoding，但存在请求正文，那么这些头字段中的一个会被自动设定。如果 *body* 是 `None`，那么对于要求 body 的方法 (`PUT`，`POST`，和 `PATCH`)，Content-Length 头会被设为 `0`。如果 *body* 是字符串或者类似字节的对象，并且也不是[文件](https://docs.python.org/3/glossary.html#term-file-object)，Content-Length 头会设为正文的长度。任何其他类型的 *body* （一般是文件或迭代器）会按块编码，这时会自动设定 Transfer-Encoding 头以代替 Content-Length。

在 *headers* 中指定 Transfer-Encoding 时， *encode_chunked* 是唯一相关的参数。如果 *encode_chunked* 为 `False`，HTTPConnection 对象会假定所有的编码都由调用代码处理。如果为 `True`，正文会按块编码。

**注解:** HTTP 协议在 1.1 版中添加了块传输编码。除非明确知道 HTTP 服务器可以处理 HTTP 1.1，调用者要么必须指定 Content-Length，要么必须传入一个 [str](https://docs.python.org/3/library/stdtypes.html#str) 或字节类对象，注意该对象不能是表示 body 的文件。

*3.2 新版功能:* *body* 现在可以是可迭代对象了。

*在 3.6 版更改:* 如果 Content-Length 和 Transfer-Encoding 都没有在 *headers* 中设置，文件和可迭代的 *body* 对象现在会按块编码。添加了 *encode_chunked* 参数。不会尝试去确定文件对象的 Content-Length。

HTTPConnection.**putheader(**_header, argument_**[**, ...**])**  
向服务器发送一个 RFC 822 格式的头部。它向服务器发送一行由头、一个冒号和一个空格以及第一个参数组成的数据。 如果还给出了其他参数，将在后续行中发送，每行由一个制表符和一个参数组成。

示例：

```python
HTTPConnection.putheader('Accept', 'text/html')
```

**源代码细节**  
header 会采用 ASCII 编码，argument 如果为字符串，则采用 latin-1（即 ISO-8859-1）编码，如果 argument 为 int 的实例，则先将其转换为字符串，再采用 ASCII 编码。  

根据源代码中的细节可知，headers 字典中无论是键还是值都不能包含中文，否则会出现 UnicodeEncodeError。类似于：`UnicodeEncodeError: 'latin-1' codec can't encode characters in position 59-60: ordinal not in range(256)`  

#### HTTPResponse对象
An [HTTPResponse](https://docs.python.org/3.6/library/http.client.html#http.client.HTTPResponse) instance wraps the HTTP response from the server. It provides access to the request headers and the entity body. The response is an iterable object and can be used in a with statement.

*在版本3.5中发生变化：* 现在实现了 [io.BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 接口，它的所有的读操作都支持。

HTTPResponse.**read**([*amt*])  
读取并返回响应正文，或者直到下一个 *amt* 字节。

HTTPResponse.**version**  
服务器使用的HTTP协议版本。HTTP/1.0 为 10，HTTP/1.1 为 11。

HTTPResponse.**status**  
服务器返回的状态代码。

实例属性：

**code**  
返回类型为int，返回HTTP Response状态代码

```python
>>> import http.client
>>> import urllib.error
>>> from urllib.request import urlopen
>>> dir(http.client.HTTPResponse)
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'close', 'closed', 'detach', 'fileno', 'flush', 'getcode', 'getheader', 'getheaders', 'geturl', 'info', 'isatty', 'isclosed', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> hasattr(http.client.HTTPResponse, 'code')
False
>>> type(urlopen('http://example.webscraping.com'))
<class 'http.client.HTTPResponse'>
>>> isinstance(urlopen('http://example.webscraping.com'), http.client.HTTPResponse)
True
>>> hasattr(urlopen('http://example.webscraping.com'), 'code')
True
>>> dir(urlopen('http://example.webscraping.com'))
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> type(urlopen('http://example.webscraping.com').code)
<class 'int'>
>>> urlopen('http://example.webscraping.com').code
200
>>> try:
...     print(urlopen('https://python.org/java').code)
... except urllib.error.HTTPError as e:
...     print(e.code)
...
404
>>>
```

### socketserver — 一个网络服务器框架
**Source code:** [Lib/socketserver.py](https://github.com/python/cpython/tree/3.6/Lib/socketserver.py)

[socketserver](https://docs.python.org/3.6/library/socketserver.html#module-socketserver) 模块简化了写网络服务器的任务。

有四个基本的具体的服务器类：

*class* socketserver.**TCPServer**(*server_address, RequestHandlerClass, bind_and_activate=True*)  
这个类使用在客户端与服务器之间提供连续的数据流的互联网TCP协议，如果 *bind_and_activate* 是 true, 则构造函数自动地尝试调用 [server_bind()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_bind) 和 [server_activate()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_activate)。其它参数（parameters）被传递给基类 [BaseServer](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer)。

#### 服务器对象
*class* socketserver.**BaseServer**(*server_address, RequestHandlerClass*)  
这是模块（socketserver）中所有服务器对象的超类。它定义了接口，如下，但大多数方法都没有实现，方法在子类中实现。两个参数（parameters）被分别存储在 [server_address](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_address) 和 [RequestHandlerClass](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.RequestHandlerClass) 属性中。

**serve_forever**(*poll_interval=0.5*)  
处理请求直到一个明确的 [shutdown()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.shutdown) 请求。每 *poll_interval* 秒投票关闭。忽略 [timeout](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.timeout) 属性。它也调用 [service_actions()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.service_actions)，`service_actions()` 可能被子类或混入类用来给一个给定的服务提供具体的动作。例如，[ForkingMixIn](https://docs.python.org/3.6/library/socketserver.html#socketserver.ForkingMixIn) 类使用 [service_actions()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.service_actions) 清理僵尸子进程。

*在3.3版本中发生变化：* 为 `serve_forever` 方法增加 `service_actions` 调用。

**service_actions()**  
这在 [serve_forever()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.serve_forever) 循环中被调用。这个方法可以被子类或混入类重写以便给一个给定的服务执行特定的动作，例如清理动作。

*版本3.3中新增。*

**shutdown()**  
Tell the [serve_forever()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.serve_forever) loop to stop and wait until it does.

**RequestHandlerClass**  
用户提供的请求处理程序类；每次请求都会创建一个该类的实例。

**server_address**  
服务器监听的地址。地址格式的变化依赖于协议族；详细信息请看 [socket](https://docs.python.org/3.6/library/socket.html#module-socket) 模块的文档。对于 Internet protocols (IP), 这是一个包含一个给定地址的字符串和一个整型数端口号的元组：`('127.0.0.1', 80)`, 例如。

### http.server — HTTP 服务器
**源代码:** [Lib/http/server.py](https://github.com/python/cpython/tree/3.6/Lib/http/server.py)

这个模块定义实现HTTP服务器（Web服务器）的类。

*class* http.server.**SimpleHTTPRequestHandler**(*request, client_address, server*)  
这个类为当前目录及其子目录下的文件服务，直接映射目录结构到HTTP请求。

很多工作，例如解析请求，由基类 [BaseHTTPRequestHandler](https://docs.python.org/3.6/library/http.server.html#http.server.BaseHTTPRequestHandler) 完成。这个类实现了 [do_GET()](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET) 和 [do_HEAD()](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_HEAD) 方法。

下面是定义为 [SimpleHTTPRequestHandler](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler) 类级别的属性：

**extensions_map**  
一个映射后缀到MIME类型的字典。默认值由空串表明，且被认为是 `application/octet-stream`。映射不区分大小写，所以应该仅包含小写键。

```python
from http.server import SimpleHTTPRequestHandler


SimpleHTTPRequestHandler.extensions_map = {
    '.html': 'text/html',
    '.sh': 'test/x-sh',
    '.js': 'application/javascript',
    '.pac': 'application/x-ns-proxy-autoconfig',
    '': 'application/octet/stream',
}

```

## Python运行时服务
### sys — 系统专用参量和函数
该模块提供了一些变量和函数。这些变量可能被解释器使用，也可能由解释器提供。这些函数会影响解释器。本模块总是可用的。

sys.**argv**  
传递给Python脚本的命令行参数列表。`argv[0]` 是脚本的名字 (是否是full pathname依赖于操作系统)。If the command was executed using the [-c](https://docs.python.org/3.6/using/cmdline.html#cmdoption-c) command line option to the interpreter, `argv[0]` 将被设置为字符串 `'-c'`。如果没有脚本名称传递给Python解释器，则 `argv[0]` 是空串。

循环处理（loop over）标准输入，或者命令行中给出的文件列表，参考 [fileinput](https://docs.python.org/3.6/library/fileinput.html#module-fileinput) 模块。

sys.**exc_info()**  
本函数返回的元组包含三个值，它们给出当前正在处理的异常的信息。返回的信息仅限于当前线程和当前堆栈帧。如果当前堆栈帧没有正在处理的异常，则信息将从下级被调用的堆栈帧或上级调用者等位置获取，依此类推，直到找到正在处理异常的堆栈帧为止。此处的“处理异常”指的是“执行一个 except 子句”。任何堆栈帧都只能访问当前正在处理的异常的信息。  

如果整个堆栈都没有正在处理的异常，则返回包含三个 None 值的元组。否则返回值为 `(type, value, traceback)`。它们的含义是：*type* 获取正在处理的异常类型（它是 [BaseException](https://docs.python.org/3.10/library/exceptions.html#BaseException) 的子类）；*value* 获取异常实例（异常类型的一个实例）；*traceback* 获取一个 [回溯对象](https://docs.python.org/3.10/reference/datamodel.html#traceback-objects)，该对象封装了最初发生异常时的调用堆栈。  

```python
>>> import sys
>>> import pandas as pd
>>> try:
...     df = pd.read_csv("US01 2022MarMonthlyUnifiedTransaction.csv")
... except Exception:
...     exc_type, exc_value, exc_traceback = sys.exc_info()
...     print(exc_type)
...     print(exc_value)
...     print(issubclass(exc_type, BaseException))
...     print(isinstance(exc_value, exc_type))
...
<class 'pandas.errors.ParserError'>
Error tokenizing data. C error: Expected 1 fields in line 8, saw 28

True
True
>>>
```
<br />

sys.**executable** 
一个字符串，提供 Python 解释器的可执行二进制文件的绝对路径，仅在部分系统中此值有意义。如果 Python 无法获取其可执行文件的真实路径，则 [sys.executable](https://docs.python.org/zh-cn/3.13/library/sys.html#sys.executable) 将为空字符串或 `None`。 

```python
>>> import sys
>>> sys.executable
'/usr/bin/python'
>>> 
``` 
<br />

sys.**exit**([*arg*])  
退出Python。

可选参数 *arg* 可以是给出退出状态的整型数 (默认为0)，或者另一种类型的对象。如果它是一个整型数，shells和与shells类似的认为0是"成功终止"，而任何非0的值被认为是"不正常的终止"。大多数系统要求它在0-127的范围内，否则将产生未定义的结果。一些系统对特定的退出代码分配特定的含义有一个约定，但这些通常是非充分开发的；Unix程序通常使用 2 表示命令行语法错误，而 1 表示所有其它类型的错误。如果传递的是另一种类型的对象，`None` 等价于传递 0，而任何其它对象则打印到 [stderr](https://docs.python.org/3.6/library/sys.html#sys.stderr) 并导致一个退出代码 1。特别是，当一个错误发生的时候，`sys.exit("some error message")` 是退出一个程序的一种快速的方式。

sys.**path**  
一个指定模块搜索路径的字符串列表。Initialized from the environment variable [PYTHONPATH](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONPATH), plus an installation-dependent default.

As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted *before* the entries inserted as a result of [PYTHONPATH](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONPATH).

程序为了自己的目的可以自由修改这个列表。只有 strings 和 bytes 可以被添加到 [sys.path](https://docs.python.org/3.6/library/sys.html#sys.path)；所有其它数据类型在导入期间被忽略。

sys.**version_info**  
一个包含版本号的5个组成部分的元组：*major*, *minor*, *micro*, *releaselevel*, and *serial*. 除了 *releaselevel* 所有值都是整型数；发行版级别是 `'alpha'`, `'beta'`, `'candidate'`, 或者 `'final'`. Python版本2.0对应的 `version_info` 值是 `(2, 0, 0, 'final', 0)`. 组件也可以通过名称来访问，如 `sys.version_info[0]` 等价于 `sys.version_info.major`。

*在版本3.1中发生了变化：* 增加了名称组件属性。  

### \_\_main\_\_ --- 顶层代码环境
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
<br>  

### traceback — 打印或检索堆栈回溯
源代码： [Lib/traceback.py](https://github.com/python/cpython/tree/3.8/Lib/traceback.py)  

该模块提供了一个标准接口来提取、格式化和打印 Python 程序的堆栈跟踪。它在打印堆栈跟踪时完全模仿 Python 解释器的行为。当您想要在程序控制下打印堆栈跟踪时，例如在解释器周围的“封装器”中，这是非常有用的。  

这个模块使用 traceback 对象 —— 这是存储在 [sys.last_traceback](https://docs.python.org/3.8/library/sys.html#sys.last_traceback) 变量中并作为 [sys.exc_info()](https://docs.python.org/3.8/library/sys.html#sys.exc_info) 的第三项被返回的对象类型。  

这个模块定义了以下函数：  
 
traceback.**print_exception(**_etype, value, tb, limit=None, file=None, chain=True_**)**  
从 traceback 对象 *tb* 将异常信息和堆栈跟踪条目打印到 *file*。这在以下方面与 [print_tb()](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.print_tb) 不同：  

* 如果 *tb* 不是 `None`，它将打印一个标题 `Traceback (most recent call last):`  
* 它在堆栈跟踪之后打印异常 *etype* 和 *value*  
* 如果 *type(value)* 是 [SyntaxError](https://docs.python.org/3.8/library/exceptions.html#SyntaxError) 并且 *value* 具有适当的格式，它会打印出现语法错误的行，并用插入符号指示错误的大致位置。  

可选的 *limit* 参数与 [print_tb()](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.print_tb) 的含义相同。 如果 *chain* 为真（默认值），那么链式异常（异常的 \_\_cause\_\_ 或 \_\_context\_\_ 属性）也将被打印，就像解释器本身在打印未处理的异常时所做的那样。  

*在 3.5 版中已更改：* *etype* 参数被忽略，然后从 *value* 的类型推断。  
<br>  

该模块还定义了以下类：  

#### TracebackException 对象
*3.5 版中的新功能。*  

[TracebackException](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.TracebackException) 对象是从实际异常创建的，以捕获数据以供以后以轻量级方式打印。  

*class* traceback.**TracebackException(**_exc_type, exc_value, exc_traceback, \*, limit=None, lookup_lines=True, capture_locals=False_**)**  
捕获异常以供以后渲染。 *limit*、*lookup_lines* 和 *capture_locals* 与 [StackSummary](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.StackSummary) 类相同。  

请注意，当 *locals* 被捕获时，它们也会显示在回溯中。  

**\_\_cause\_\_**  
原始 `__cause__` 的 [TracebackException](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.TracebackException)。  

**\_\_context\_\_**  
原始 `__context__` 的 [TracebackException](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.TracebackException)。  

**\_\_suppress\_context\_\_**  
来自原始异常的 `__suppress_context__` 值。  

**stack**  
表示回溯的 [StackSummary](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.StackSummary)。

**exc_type**  
原始回溯的类。  

**filename**  
对于语法错误 - 发生错误的文件名。  

**lineno**  
对于语法错误 - 发生错误的行号。  

**text**  
对于语法错误 - 发生错误的文本。  

**offset**  
对于语法错误 - 发生错误的文本中的偏移量。  

**msg**  
对于语法错误 - 编译器错误消息。  

*classmethod* **from_exception(**_exc, \*, limit=None, lookup_lines=True, capture_locals=False_**)**  
捕获异常以供以后渲染。 *limit*、*lookup_lines* 和 *capture_locals* 与 [StackSummary](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.StackSummary) 类相同。  

请注意，当 *locals* 被捕获时，它们也会显示在回溯中。  

**format(**_\*, chain=True_**)**  
格式化异常。  

如果 *chain* 不是 `True`，`__cause__` 和 `__context__` 将不会被格式化。  

返回值是一个字符串生成器，每个字符串都以一个换行符结尾，一些包含内部换行符。 [print_exception()](https://docs.python.org/3.8/library/traceback.html?highlight=exc_value#traceback.print_exception) 是这个方法的包装器，它只是将行打印到文件中。  

指示发生了哪个异常的消息始终是输出中的最后一个字符串。  

**format_exception_only()**  
格式化回溯的异常部分。  

返回值是一个字符串生成器，每个字符串都以一个换行符结尾。  

通常，生成器发出单个字符串； 但是，对于 [SyntaxError](https://docs.python.org/3.8/library/exceptions.html#SyntaxError) 异常，它会发出几行（当打印时）显示有关语法错误发生位置的详细信息。  

指示发生了哪个异常的消息始终是输出中的最后一个字符串。  
<br>  

# Python语言参考
## 3. 数据模型
### 3.2. 标准类型层次结构
**模块**  
　　模块是 Python 代码的基本组织单元，模块由 [import](https://docs.python.org/3/reference/simple_stmts.html#import) 语句 (参见 [import](https://docs.python.org/3/reference/simple_stmts.html#import))，或通过调用函数如 [importlib.import_module()](https://docs.python.org/3/library/importlib.html#importlib.import_module) 和内置的 [\_\_import\_\_()](https://docs.python.org/3/library/functions.html#__import__) 调用 [导入系统](https://docs.python.org/3/reference/import.html#importsystem) 所创建。每个模块对象都有一个通过一个字典对象实现的命名空间 (这就是模块中定义的函数的 `__globals__` 属性所引用的字典)。属性引用被转换为在字典中查找，例如，`m.x` 等同于 `m.__dict__["x"]`。模块对象不包含用于初始化模块的代码对象 (因为一旦初始化完成就不需要它了)。

属性赋值更新模块的命名空间字典，例如，`m.x = 1` 等价于 `m.__dict__["x"] = 1`。

预定义的 (可写) 属性： [\_\_name\_\_](https://docs.python.org/3/reference/import.html#__name__) 是模块的名字；\_\_doc\_\_ 是模块的文档字符串，如果没有则为 `None`；\_\_annotations\_\_ (可选的) 是一个包含模块正文执行期间收集的变量注释的字典；如果模块是从一个文件加载，则 [\_\_file\_\_](https://docs.python.org/3/reference/import.html#__file__) 是模块对应的被加载文件的路径名。某些类型的模块可能没有 `__file__` 属性，例如 C 模块是静态链接到解释器内部的; 对于从一个共享库动态加载的扩展模块来说该属性为该共享库文件的路径名。 

```sh
➜  ~ cat temp.py                                                                                
#!/usr/bin/env python3                                                                          
import os.path                                                                                                                          
print(__file__)                                                                                 
print(os.path.abspath(__file__))                                                                
➜  ~                                                                                            
➜  ~ python3.7 temp.py                                                                          
temp.py                                                                                         
/home/ywh/temp.py                                                                               
➜  ~  
➜  ~ python3.11 temp.py         
/home/ywh/temp.py                                       
/home/ywh/temp.py
➜  ~                   
``` 

在 Python3.7 中，`__file__` 返回的是模块对应的文件的相对路径名，而在 Python3.11 中 `__file__` 返回的是模块对应的文件的绝对路径名。 

特殊的只读属性：[\_\_dict\_\_](https://docs.python.org/3/library/stdtypes.html#object.__dict__) is the module’s namespace as a dictionary object.  

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

#### 3.3.6. 仿真可调用对象
object.**\_\_call\_\_**(*self*__\[__*, args...*__\]__)  
当实例作为一个函数被“调用”时调用；如果定义了这个方法，则 `x(arg1, arg2, ...)` 是 `x.__call__(arg1, arg2, ...)` 的缩写。  

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
<br>  

## 4. 执行模型
### 4.1. 程序的结构
Python 程序是由代码块构成的。 一个*代码块* 是被作为一个单元来执行的一段 Python 程序文本。 以下几个都是代码块：一个模块、一个函数体和一个类定义。 交互式输入的每条命令都是一个代码块。 一个脚本文件（作为标准输入发送给解释器或是作为命令行参数发送给解释器的文件）是一个代码块。 一条脚本命令（通过 [-c](https://docs.python.org/3.8/using/cmdline.html#cmdoption-c) 选项在解释器命令行中指定的命令）是一个代码块。 传递给内置函数 [eval()](https://docs.python.org/3.8/library/functions.html#eval) 和 [exec()](https://docs.python.org/3.8/library/functions.html#exec) 的字符串参数也是代码块。  

代码块在 *执行帧* 中被执行。 一个帧会包含某些管理信息（用于调试）并决定代码块执行完成后应前往何处以及如何继续执行。  
<br>  

### 4.3. 异常
异常是为了处理错误或其他异常情况而打破代码块的正常控制流的一种方法。异常会在错误被检测到的位置被 *引发*，它可以由周围的代码块或者由直接或间接调用发生错误的代码块的任何代码块来处理。  

Python 解析器会在检测到运行时错误（例如零作为被除数）的时候引发异常。 Python 程序也可以通过 [raise](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 语句显式地引发异常。 异常处理程序是通过 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) ... [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 语句来指定的。 该语句的 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句可被用来指定清理代码，它并不处理异常，而是无论之前的代码是否发生异常都会被执行。  

Python 使用错误处理的“终止”模型：异常处理程序可以找出发生了什么问题，并在外层继续执行，但它不能修复错误的根源并重试失败的操作（除非通过从顶层重新进入出错的代码片段）。  

当一个异常完全未被处理时，解释器会终止程序的执行，或者返回交互模式的主循环。 无论是哪种情况，它都会打印堆栈回溯，除了当异常是 [SystemExit](https://docs.python.org/3.8/library/exceptions.html#SystemExit) 的时候。  

异常由类实例来标识。 根据实例的类选择 [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 子句：它必须引用实例的类或其基类。 该实例可以由处理程序接收，并且可以携带有关异常情况的附加信息。  

**注意：** 异常消息不是 Python API 的一部分。 它们的内容可能会在没有警告的情况下从 Python 的一个版本升级为下一个版本时发生改变，并且不应该被需要在多版本解释器下运行的代码所依赖。    

另请参考 [try 语句](https://docs.python.org/3.8/reference/compound_stmts.html#try) 小节中对 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 语句的描述以及 [raise 语句](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 小节中对 [raise](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 语句的描述。  
<br>  

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

## 6. 表达式
### 6.14. lambda 表达式
**lambda_expr** ::= "lambda" [[parameter_list](https://docs.python.org/zh-cn/3.13/reference/compound_stmts.html#grammar-token-python-grammar-parameter_list)] ":" [expression](https://docs.python.org/zh-cn/3.13/reference/expressions.html#grammar-token-python-grammar-expression) 

lambda 表达式（有时称为 lambda 形式）被用于创建匿名函数。 表达式 `lambda parameters: expression` 会产生一个函数对象 。 该未命名对象的行为类似于用以下方式定义的函数: 

```python
def <lambda>(parameters):
    return expression
```

请参阅 [函数定义](https://docs.python.org/zh-cn/3.13/reference/compound_stmts.html#function) 了解有关参数列表的句法。 请注意通过 lambda 表达式创建的函数不能包含语句或注释。  

## 7. 简单语句
### 7.3. assert语句
将调试断言插入到一个程序中，assert 语句是一种方便的方式：

**assert_stmt** ::=  "assert" [expression](https://docs.python.org/3/reference/expressions.html#grammar-token-expression) \["," [expression](https://docs.python.org/3/reference/expressions.html#grammar-token-expression)\]

简单形式，`assert expression`，等同于

```python
if __debug__:
    if not expression: raise AssertionError
```

### 7.12. global语句
**global_stmt** ::=  "global" [identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-identifier) ("," [identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-identifier))*

[global](https://docs.python.org/3/reference/simple_stmts.html#global) 语句是一个适用于整个当前代码块的公告。它意味着global语句中的identifiers都将被解释为全局变量。

## 8. 复合语句
复合语句是包含其它语句（语句组）的语句；它们会以某种方式影响或控制其所包含的语句的执行。 通常，复合语句会跨越多行，虽然在某些简单形式下整个复合语句也可能包含于一行之内。  

[if](https://docs.python.org/3.8/reference/compound_stmts.html#if), [while](https://docs.python.org/3.8/reference/compound_stmts.html#while) 和 [for](https://docs.python.org/3.8/reference/compound_stmts.html#for) 语句用来实现传统的控制流结构。 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 为一组语句指定异常处理程序 和/或 清理代码，而 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句允许在一个代码块周围执行初始化和终结代码。 函数和类定义在语法上也属于复合语句。  

一个复合语句由一个或多个“子句”构成。一个子句由一个句头和一个“套件”构成。一个具体的复合语句的子句头拥有相同的缩进级别。每个子句头以一个唯一的标识关键字开始并以一个冒号结尾。一个套件是由一个子句控制的一组语句。一个套件可以是与句头处于同一行且位于句头的冒号之后的一个或多个由分号分隔的简单语句，或者它可以是随后的行中的一个或多个缩进的语句。只有后面这种形式的套件可以包含嵌套的复合语句；下面是非法的，主要是因为接下来的 [else](https://docs.python.org/3/reference/compound_stmts.html#else) 子句属于哪一个 [if](https://docs.python.org/3/reference/compound_stmts.html#if) 子句不清晰：

```python
if test1: if test2: print(x)
```

还要注意在这个上下文中分号比冒号捆绑得更紧密，所以在下面的例子中，要么所有的 [print()](https://docs.python.org/3/library/functions.html#print) 调用都被执行，要么一个都没有：

```python
if x < y < z: print(x); print(y); print(z)
```

总结：

**compound_stmt ::**=&nbsp;&nbsp;[if_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-if_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [while_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-while_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [for_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-for_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [try_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-try_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [with_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-with_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [funcdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-funcdef)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [classdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-classdef)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_with_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_with_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_for_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_for_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_funcdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_funcdef)  
**suite&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[stmt_list](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-stmt_list) NEWLINE | NEWLINE INDENT [statement](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-statement)+ DEDENT  
**statement&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[stmt_list](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-stmt_list) NEWLINE | [compound_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-compound_stmt)  
**stmt_list&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[simple_stmt](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-simple_stmt) (";" [simple_stmt](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-simple_stmt))* [";"]  

请注意语句总是以 `NEWLINE` 结尾，之后可能跟随一个 `DEDENT`。 还要注意可选的后续子句总是以一个不能作为语句开头的关键字作为开始，因此不会产生歧义（‘摇摆的 [else](https://docs.python.org/3.8/reference/compound_stmts.html#else)’问题在 Python 中是通过要求嵌套的 [if](https://docs.python.org/3.8/reference/compound_stmts.html#if) 语句必须缩进来解决的)。  

为了清晰易懂，以下各节中语法规则的格式将每个子句放在单独的行上。  
<br>  

### 8.4. try 语句
[try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 语句可为一组语句指定异常处理程序 和/或 清理代码：  

```python
try_stmt  ::=  try1_stmt | try2_stmt
try1_stmt ::=  "try" ":" suite
               ("except" [expression ["as" identifier]] ":" suite)+
               ["else" ":" suite]
               ["finally" ":" suite]
try2_stmt ::=  "try" ":" suite
               "finally" ":" suite
```

**注意：**  
第三行末尾的加号（“+”）的含义同正则表达式中的加号，表示一个 try 子句后面可以跟一个或多个 except 子句。  

The [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) clause(s) specify one or more exception handlers. （clause 后面的 '(s)' 也表明了一个 try 语句后面可以跟多个 except 子句）当 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 子句中没有发生异常时，没有任何异常处理程序会被执行。 当 `try` 套件中发生异常时，将启动对异常处理程序的搜索。 此搜索会逐一检查 except 子句直至找到与该异常相匹配的子句。 如果存在无表达式的 except 子句，它必须是最后一个；它将匹配任何异常。 对于带有表达式的 except 子句，该表达式会被求值，如果结果对象与发生的异常“兼容”则该子句将匹配该异常。
如果对象是异常对象的类或基类，或者包含一个异常对象的类或基类的项的元组，则对象与异常兼容。  

如果没有 except 子句与异常匹配，则在周围的代码和调用堆栈中继续搜索异常处理程序。（异常会被传导至调用堆栈，除非有一个 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句正好引发了另一个异常。 新引发的异常会导致旧异常丢失。）

```python
>>> import pandas as pd
>>> import sys
>>> try:
...     df = pd.read_csv("JP1 2022MarMonthlyTransaction.csv")
... except pd.errors.ParserError as e:
...     print(e)
... finally:
...     df = pd.read_csv("JP1 2022MarMonthlyTransaction.csv", encoding="shift_jis")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "D:\Program Files\Python310\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 1235, in _make_engine
    return mapping[engine](f, **self.options)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 75, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 544, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 633, in pandas._libs.parsers.TextReader._get_header
  File "pandas\_libs\parsers.pyx", line 847, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas\_libs\parsers.pyx", line 1952, in pandas._libs.parsers.raise_parser_error
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8f in position 8: invalid start byte

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "D:\Program Files\Python310\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 581, in _read
    return parser.read(nrows)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\readers.py", line 1254, in read
    index, columns, col_dict = self._engine.read(nrows)
  File "D:\Program Files\Python310\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 225, in read
    chunks = self._reader.read_low_memory(nrows)
  File "pandas\_libs\parsers.pyx", line 805, in pandas._libs.parsers.TextReader.read_low_memory
  File "pandas\_libs\parsers.pyx", line 861, in pandas._libs.parsers.TextReader._read_rows
  File "pandas\_libs\parsers.pyx", line 847, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas\_libs\parsers.pyx", line 1960, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 8, saw 28

>>>
```

```python
>>> try:
...     try:
...         df = pd.read_csv("JP1 2022MarMonthlyTransaction.csv")
...     except pd.errors.ParserError as e:
...         print(e)
...     finally:
...         df = pd.read_csv("JP1 2022MarMonthlyTransaction.csv", encoding="shift_jis")
... except:
...     print("outer print statement\n")
...     print(sys.exc_info())
...
outer print statement

(<class 'pandas.errors.ParserError'>, ParserError('Error tokenizing data. C error: Expected 1 fields in line 8, saw 28\n'), <traceback object at 0x000001E251C93400>)
>>>
```

如果在对 except 子句头中的表达式求值时引发了异常，则原来对处理程序的搜索会被取消，并在周边代码和调用堆栈上启动对新异常的搜索（它会被视作是整个 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 语句引发了异常）。  

当找到一个匹配的 except 子句时，该异常将被赋值给该 except 子句在 `as` 关键字之后指定的目标，如果存在此关键字的话，并且该 except 子句的套件将被执行。 所有 except 子句都必须有一个可执行的代码块。 当到达这个代码块的末尾时，通常会在整个 try 语句之后继续执行。 （这意味着如果对于同一异常存在着嵌套的两个处理程序，而异常发生于内层处理程序的 try 子句中，则外层处理程序将不会处理该异常。）  

当使用 `as target` 将一个异常赋值给 `target` 时，它将在 except 子句的末尾被清除。 这就好像  

```python
except E as N:
    foo
```  

被转换成  

```python
except E as N:
    try:
        foo
    finally:
        del N
```

这意味着异常必须赋值给一个不同的名称才能在 except 子句之后引用它。 异常被清除是因为附加了回溯的情况下，它们与堆栈帧形成一个引用循环，使该帧中的所有局部变量保持活动状态直到发生下一次垃圾回收。  

在一个 except 子句套件被执行之前，有关异常的详细信息存储在 [sys](https://docs.python.org/3.8/library/sys.html#module-sys) 模块中，可以通过 [sys.exc_info()](https://docs.python.org/3.8/library/sys.html#sys.exc_info) 来访问。
[sys.exc_info()](https://docs.python.org/3.8/library/sys.html#sys.exc_info) 返回一个由异常类、异常实例和回溯对象（参见[标准类型层次结构](https://docs.python.org/3.8/reference/datamodel.html#types)一节）组成的三元组，用于标识程序中发生异常的点。
当从处理异常的函数返回时 [sys.exc_info()](https://docs.python.org/3.8/library/sys.html#sys.exc_info) 的值将恢复为之前的值（调用前的）。  

如果控制流离开 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 套件时没有引发异常，并且没有 [return](https://docs.python.org/3.8/reference/simple_stmts.html#return), [continue](https://docs.python.org/3.8/reference/simple_stmts.html#continue) 或 [break](https://docs.python.org/3.8/reference/simple_stmts.html#break) 语句被执行 ，则可选的 `else` 子句将被执行。 `else` 语句中的异常不会被之前的 [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 子句处理。  

如果存在 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally)，它将指定一个‘清理’处理程序。 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 子句会被执行，包括任何 [except](https://docs.python.org/3.8/reference/compound_stmts.html#except) 和 `else` 子句。 如果在这些子句中发生任何未处理的异常，该异常会被临时保存。 `finally` 子句将被执行。 如果存在被保存的异常，它会在 `finally` 子句的末尾被重新引发。 如果 `finally` 子句引发了另一个异常，被保存的异常会被设为新异常的上下文。 如果 `finally` 子句执行了 [return](https://docs.python.org/3.8/reference/simple_stmts.html#return), [break](https://docs.python.org/3.8/reference/simple_stmts.html#break) 或 [continue](https://docs.python.org/3.8/reference/simple_stmts.html#continue) 语句，则被保存的异常会被丢弃:   

```python
>>> def f():
...     try:
...         1/0
...     finally:
...         return 42
...
>>> f()
42
```

在 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句执行期间，程序不能获取异常信息。  

当在 `try...finally` 语句的 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try) 套件中执行 [return](https://docs.python.org/3.8/reference/simple_stmts.html#return)、[break](https://docs.python.org/3.8/reference/simple_stmts.html#break) 或 [continue](https://docs.python.org/3.8/reference/simple_stmts.html#continue) 语句时，[finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句在“退出时”也会被执行。  

```python
>>> def foo():
...     try:
...         return 'try'
...     finally:
...         print('print finally')
...
>>> foo()
print finally
'try'
>>>
```

函数的返回值是由最后被执行的 [return](https://docs.python.org/3.8/reference/simple_stmts.html#return) 语句所决定的。 由于 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句总是被执行，因此在 `finally` 子句中被执行的 `return` 语句总是最后一个被执行的:  

```python
>>> def foo():
...     try:
...         return 'try'
...     finally:
...         return 'finally'
...
>>> foo()
'finally'
>>>
```

有关异常的更多信息可以在 [异常](https://docs.python.org/3.8/reference/executionmodel.html#exceptions) 一节找到，有关使用 [raise](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 语句生成异常的信息可以在 [raise 语句](https://docs.python.org/3.8/reference/simple_stmts.html#raise) 一节找到。  

*在 3.8 版本发生改变：* 在 Python 3.8 之前，[continue](https://docs.python.org/3.8/reference/simple_stmts.html#continue) 语句不允许在 [finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 子句中使用，这是因为具体实现存在一个问题。  
<br>  

### 8.5. with 语句
[with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句用于包装使用上下文管理器 (参见 [with 语句上下文管理器](https://docs.python.org/3.8/reference/datamodel.html#context-managers) 一节) 定义的方法块的执行。 这允许封装常见的 [try](https://docs.python.org/3.8/reference/compound_stmts.html#try)...[except](https://docs.python.org/3.8/reference/compound_stmts.html#except)...[finally](https://docs.python.org/3.8/reference/compound_stmts.html#finally) 使用模式以方便重用。  

**with_stmt ::=**&nbsp;&nbsp;"with" with_item ("," with_item)* ":" [suite](https://docs.python.org/3.6/reference/compound_stmts.html#grammar-token-suite)  
**with_item ::=**&nbsp;&nbsp;[expression](https://docs.python.org/3.6/reference/expressions.html#grammar-token-expression) \["as" [target](https://docs.python.org/3.6/reference/simple_stmts.html#grammar-token-target)\]

带有一个“项目”的 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句的执行过程如下:  

1. 对上下文表达式 (在 [with_item](https://docs.python.org/3.8/reference/compound_stmts.html#grammar-token-with-item) 中给出的表达式) 求值以获得一个上下文管理器。  
2. 载入上下文管理器的 [\_\_enter\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__) 以便后续使用。  
3. 载入上下文管理器的 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 以便后续使用。  
4. 调用上下文管理器的 [\_\_enter\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__) 方法。  
5. 如果 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句中包含一个 `target`，[\_\_enter\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__) 的返回值将被赋值给它。  

**注意：** [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句会保证如果 [\_\_enter\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__) 方法返回时未发生错误，则 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 将总是被调用。 因此，如果在对目标列表赋值期间发生错误，它会将其视为在套件内发生的错误。 参见下面的第 6 步。  

6. 执行套件。
7. 调用上下文管理器的 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 方法。 如果一个异常导致套件退出，则它的类型、值和回溯将被作为参数传递给 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__)。 其它情况下，将提供三个 [None](https://docs.python.org/3.8/library/constants.html#None) 参数。  

如果套件的退出是由异常导致的，并且 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 方法的返回值为假，则该异常会被重新引发。 如果返回值为真，则该异常会被抑制，并会继续执行 [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句之后的语句。

如果套件因异常以外的任何原因退出，则来自 [\_\_exit\_\_()](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__) 的返回值会被忽略，并在正常位置继续执行所采取的退出类型。  

下面的代码：  

```python
with EXPRESSION as TARGET:
    SUITE
```

在语义上等价于:  

```python
manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not exit(manager, *sys.exc_info()):
        raise
finally:
    if not hit_except:
        exit(manager, None, None, None)
```

当不止一个 with_item 时，上下文管理器的处理就好像有多个 [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) 语句嵌套似的。

```python
with A() as a, B() as b:
    suite
```

在语义上等同于

```python
with A() as a:
    with B() as b:
        suite
```

*在版本3.1中发生变化：* 支持多个上下文表达式。  

**另请参考：**

**[PEP 343](https://www.python.org/dev/peps/pep-0343) - "with" 语句**  
Python [with](https://docs.python.org/3.8/reference/compound_stmts.html#with) 语句的技术规范、背景和示例。  
<br>  

# Python 教程
## 2. 使用Python解释器
### 2.1. 调用解释器
Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. 如果无效，你可以通过输入下面的命令：`quit()` 退出解释器。

## 4. 更多控制流工具
Besides the [while](https://docs.python.org/3/reference/compound_stmts.html#while) statement just introduced, Python knows the usual control flow statements known from other languages, with some twists.

### 4.3. range() 函数
如果你需要遍历一个数字序列，内置函数 [range()](https://docs.python.org/3/library/stdtypes.html#range) 派得上用场。它生成等差数列：

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

给定的结束点永远都不是生成的序列的一部分；一个长度为10的序列的项的合法索引，`range(10)` 生成 10 个值。让 range 以另一个数开始是可能的，或者指定一个不同的增量(即使为负；有时这被称为 ‘step’):

```python
>>> range(5, 10)
range(5, 10)
>>> for i in range(5, 10):
...     print(i)
...
5
6
7
8
9
>>> for i in range(0, 10, 3):
...     print(i)
...
0
3
6
9
>>> for i in range(-10, -100, -30):
...     print(i)
...
-10
-40
-70
```

遍历一个序列的索引，你可以联合 [range()](https://docs.python.org/3/library/stdtypes.html#range) 和 [len()](https://docs.python.org/3/library/functions.html#len) 如下：

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
>>>
```

In most such cases, however, it is convenient to use the [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) function, 请看 [Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms)。

如果你仅打印一个range，将发生一件奇怪的事情：

```python
>>> print(range(0, 10))
range(0, 10)
>>>
```

在很多方面 [range()](https://docs.python.org/3/library/stdtypes.html#range) 返回对象的行为就好像它是一个列表，但实际上它不是。当你遍历它时，它是一个返回预期的序列中的连续的项的对象，但它实际上不制造列表，从而节省空间。

我们说这样的对象是*可迭代的*，也就是说，suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. 我们已经见过 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 语句就是这样一个*迭代器*。[list()](https://docs.python.org/3/library/stdtypes.html#list) 函数是另一个；它从可迭代对象创建列表：

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
>>>
```

稍后我们将看到更多返回可迭代对象和使用可迭代对象作为参数的函数。

### 4.4. break 和 continue 语句, 和循环中的 else 子句
[break](https://docs.python.org/3/reference/simple_stmts.html#break) 语句，与 C 中相似，摆脱封闭它的最内层的 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 或者 [while](https://docs.python.org/3/reference/compound_stmts.html#while) 循环。

循环语句可能含有一个 `else` 子句；当循环通过耗尽列表 (with [for](https://docs.python.org/3/reference/compound_stmts.html#for)) 或者当条件变为 false (with [while](https://docs.python.org/3/reference/compound_stmts.html#while)) 而结束时执行 else 子句，当循环被一个 [break](https://docs.python.org/3/reference/simple_stmts.html#break) 语句终止时则不执行 else 子句。通过下面这个搜索质数的循环来举例说明：

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>>
```

(是的，这是正确的代码。仔细看：`else` 子句属于 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 循环，**而不是** [if](https://docs.python.org/3/reference/compound_stmts.html#if) 语句。)

当与循环一起使用时，比起 [if](https://docs.python.org/3/reference/compound_stmts.html#if) 语句中的 `else` 子句，循环中的 `else` 子句与 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句中的 `else` 子句有更多的共同点：当没有异常发生时执行 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句的 `else` 子句，当没有 `break` 发生时执行循环的 `else` 子句。关于 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句和异常的更多信息，请看 [处理异常](https://docs.python.org/3/tutorial/errors.html#tut-handling)。

[continue](https://docs.python.org/3/reference/simple_stmts.html#continue) 语句，也是从 C 借鉴来的，继续循环的下一次迭代：

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print('Found an even number', num)
...         continue
...     print('Found a number', num)
...
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
>>>
```  

### 4.9. 函数定义详解
#### 4.9.6. Lambda 表达式
[lambda](https://docs.python.org/3.13/reference/expressions.html#lambda) 关键字用于创建小巧的匿名函数。`lambda a, b: a+b` 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是一个单一的表达式。在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量： 

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
... 
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
>>> 
```

上面的例子使用 lambda 表达式返回函数。 另一种用法是传入一个小函数作为参数。 例如，[list.sort()](https://docs.python.org/zh-cn/3.13/library/stdtypes.html#list.sort) 接受一个排序键函数 *key*，它可以是一个 lambda 函数: 

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> 
```

pairs 列表有 4 个元素，每个元素是一个元组，`pairs.sort(key=lambda pair: pair[1])` 表示按照元组的第二个元素的字母顺序对 pairs 列表的元素进行排序。 

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

## 7. 输入和输出
有几种方式呈现一个程序的输出；数据可以被以易于人阅读的形式打印出来，或者写入到一个文件中以备将来使用。这章将讨论一些可能性。

### 7.2. 读和写文件
[open()](https://docs.python.org/3/library/functions.html#open) 返回一个[文件对象](https://docs.python.org/3/glossary.html#term-file-object)，最常见的用法是带两个参数：`open(filename, mode)`。

```python
>>> f = open('workfile', 'w')
```

#### 7.2.1. 文件对象的方法
这节剩下的例子将假设一个名为 `f` 的文件对象已经被创建。

`f.write(string)` 写入 *string* 的内容到文件中，返回写入的字符数。

```python
>>> f = open('workfile', 'w')
>>> f.write('This is a test\n')
15
```

其它类型的对象在写入他们以前必须被转换成一个字符串 (文本模式) 或者一个字节对象 (二进制模式)：

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
>>> f.closed
False
>>> f.close()
>>> f.closed
True
>>> with open('workfile', 'r') as f:
...     f.read()
...
"This is a test\n('the answer', 42)"
>>> f.closed
True
>>> with open('workfile', 'r') as f:
...     print(f.read())
...
This is a test
('the answer', 42)
>>> f.closed
True
>>>
```  

## 8. 错误和异常
到目前为止，错误消息还没有被过多提及，但是如果您尝试过这些示例，您可能已经看到了一些错误信息。 有（至少）两种可区分的错误：*语法错误*和*异常*。  

### 8.1. 语法错误
语法错误又称解析错误，可能是你学习 Python 时最常见的错误：  

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

解析器会复现出现错误的代码行，并用小“箭头”指向行里检测到的第一个错误。错误是由箭头 *前面的* token 引起的（或至少在箭头处检测到）：本例中，在 [print()](https://docs.python.org/3.9/library/functions.html#print) 函数处检测到错误，因为在它前面缺少冒号（':'） 。打印文件名和行号，以便于万一输入来自一个脚本你也知道在哪里查看。  

### 8.2. 异常
即使语句或表达式在语法上是正确的，当试图执行它时仍可能触发错误。执行时检测到的错误称为 *异常*，并且不是无条件致命的：您很快就会学习如何在 Python 程序中处理它们。然而，大多数异常不是由程序处理的，并且会导致如下所示的错误消息：  

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

错误消息的最后一行表明发生了什么。异常有不同的类型，而类型会作为错误信息的一部分被打印出来：上述示例中的异常类型是：[ZeroDivisionError](https://docs.python.org/3.9/library/exceptions.html#ZeroDivisionError)， [NameError](https://docs.python.org/3.9/library/exceptions.html#NameError) 和 [TypeError](https://docs.python.org/3.9/library/exceptions.html#TypeError)。作为异常类型被打印的字符串是发生的内置异常的名称。对于所有内置异常都是如此，但对于用户定义的异常则不一定如此（尽管它是一个有用的惯例）。标准异常名称是内置标识符（不是保留关键字）。  

该行的其余部分根据异常类型及其原因提供详细信息。  

错误消息的前面部分以堆栈回溯的形式显示了发生异常的上下文。 一般来说，它包含一个堆栈回溯，列出源代码行； 但是，它不会显示从标准输入读取的行。  

[内置异常](https://docs.python.org/3.9/library/exceptions.html#bltin-exceptions) 列出了内置异常及其含义。  

### 8.3. 处理异常
可以编写程序处理选定的异常。 看下面的例子，它要求用户输入，直到输入一个有效的整数，但允许用户中断程序（使用 `Control-C` 或操作系统支持的任何东西）； 请注意，用户生成的中断是通过引发 [KeyboardInterrupt](https://docs.python.org/3.9/library/exceptions.html#KeyboardInterrupt) 异常来指示的。  

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops! That was no valid number. Try again...")
...
```

[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句的工作原理如下：

* 首先，执行 *try 子句* （[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 和 [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 关键字之间的语句）。  
* 如果没有触发异常，则跳过 *except 子句*，[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句执行完毕。  
* 如果执行 try 子句时发生了异常，则跳过该子句中剩下的部分。如果异常的类型与 [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 关键字后面的异常匹配，则执行 except 子句，然后，继续执行 [try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句之后的代码。  
* 如果发生的异常不匹配 except 子句中的异常，则将其传递给外部的 [try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句；如果没有找到处理程序，则它是一个 *未处理的异常*，语句执行将终止，并显示如上所示的消息。  

[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句可以有多个 except 子句，可为不同的异常指定相应的处理程序。但最多只会执行一个处理程序。处理程序只处理对应的 try 子句中发生的异常，而不处理同一 `try` 语句的其他处理程序中发生的异常。except 子句可以将多个异常命名一个括号内的元组，例如：  

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

如果 [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 子句中的类与异常是同一个类或是它的基类时，则异常与 except 子句中的类兼容（反之则不成立 --- except 子句列出的派生类与基类不兼容）。例如，下面的代码将依次打印 B, C, D：  

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

注意，如果颠倒 except 子句的顺序（把 `except B` 放到第一个），则输出 B，B，B --- 即触发第一个匹配的 except 子句。

最后的 except 子句可以省略异常名，以用作通配符。但应谨慎使用，因为这种方式很容易掩盖真正的编程错误！它还可用于打印错误消息，然后重新触发异常（同样允许调用者处理异常）：  

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to integer.")
except:
    print("Unexcepted error:", sys.exc_info()[0])
    raise
```

[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) ... [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 语句有一个可选的 *else 子句*，当出现的时候，该子句必须放在所有 except 子句之后。如果 try 子句没有触发异常，则必须执行一些代码时，这个子句很有用。例如：

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()
```

使用 else 子句比向 [try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 子句添加额外的代码要好，因为它可以避免意外捕获不是由 `try ... except` 语句保护的代码触发的异常。  

发生异常时，它可能有一个关联值，也称为异常的 *参数* 。参数的存在和类型取决于异常类型。

except 子句可以在异常名称后面指定一个变量。该变量绑定到一个异常实例，其的参数存储在 `instance.args` 中。为了方便起见，异常实例定义了 [\_\_str\_\_()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) ，因此可以直接打印参数而无需引用 `.args` 。也可以在抛出之前首先实例化异常，并根据需要向其添加任何属性。  

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))  # the exception instance
...     print(inst.args)   # arguments stored in .args
...     print(inst)        # __str__ allows args to be printed directly,
...                        # but may be overridden in exception subclasses
...     x, y = inst.args   # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

如果异常有参数，则它们将作为未处理异常的消息的最后一部分（'详细信息'）被打印。

异常处理程序不仅处理 try 子句中直接发生的异常，还处理 try 子句中调用（即使是间接地）的函数内部发生的异常。例如:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

### 8.4. 触发异常
[raise](https://docs.python.org/3.9/reference/simple_stmts.html#raise) 语句允许程序员强制触发指定的异常。例如：

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

[raise](https://docs.python.org/3.9/reference/simple_stmts.html#raise) 唯一的参数就是要触发的异常。这个参数必须是异常实例或异常类（派生自 [Exception](https://docs.python.org/3.9/library/exceptions.html#Exception) 类）。如果传递的是异常类，它将通过调用它的没有参数的构造函数来隐式实例化：

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

如果你只想判断是否触发了异常，但并不打算处理该异常，则可以使用形式更简单的 [raise](https://docs.python.org/3.9/reference/simple_stmts.html#raise) 语句重新触发异常：

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

### 8.5. 异常链
[raise](https://docs.python.org/3.9/reference/simple_stmts.html#raise) 语句允许一个可选的 [from](https://docs.python.org/3.9/reference/simple_stmts.html#raise) 子句，该子句用于启用链式异常。 例如：

```python
# exc must be exception instance or None
raise RuntimeError from exc
```

转换异常时，这种方式很有用。例如：

```python
>>> def func():
...     raise IOError
...
>>> try:
...     func()
... except IOError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

当在 [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 或 [finally](https://docs.python.org/3.9/reference/compound_stmts.html#finally) 子句中引发异常时，异常链会自动发生。 可以使用 `from None` 习惯用法禁用异常链：

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

异常链机制详见 [内置异常](https://docs.python.org/3.9/library/exceptions.html#bltin-exceptions)。
<br>  

### 8.6. 用户自定义异常
程序可以通过创建新的异常类来命名自己的异常（有关 Python 类的更多信息，请参见[类](https://docs.python.org/3.9/tutorial/classes.html#tut-classes)）。 异常通常应该直接或间接地从 [Exception](https://docs.python.org/3.9/library/exceptions.html#Exception) 类派生。

可以定义异常类，它可以做任何其他类可以做的任何事情，但通常保持简单，常常只提供一些属性，以允许异常处理程序提取有关错误的信息。  

大多数异常都使用以“Error”结尾的名称来定义，类似于标准异常的命名。

许多标准模块定义了它们自己的异常来报告它们定义的函数中可能发生的错误。 有关类的更多信息，请参见[类](https://docs.python.org/3.9/tutorial/classes.html#tut-classes)一章。  
<br>  

### 8.7. 定义清理操作
[try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作。例如：

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodby, world!')
... 
Goodby, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

如果存在 [finally](https://docs.python.org/3.9/reference/compound_stmts.html#finally) 子句，则 `finally` 子句将作为 [try](https://docs.python.org/3.9/reference/compound_stmts.html#try) 语句完成之前的最后一个任务执行。 无论 `try` 语句是否产生异常，`finally` 子句都会运行。 以下几点讨论了发生异常时更复杂的情况：  

* 如果执行 `try` 子句期间触发了某个异常，则某个 [except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 子句应处理该异常。如果该异常没有被 `except` 子句处理，则该异常在 `finally` 子句执行后会被重新触发。  
* `except` 或 `else` 子句执行期间也会触发异常。 同样，该异常会在 `finally` 子句执行之后被重新触发。  
* 如果 `finally` 子句执行了 [break](https://docs.python.org/3.9/reference/simple_stmts.html#break)、[continue](https://docs.python.org/3.9/reference/simple_stmts.html#continue) 或 [return](https://docs.python.org/3.9/reference/simple_stmts.html#return) 等语句，则异常将不会被重新引发。  
* 如果执行 `try` 语句时遇到了 [break](https://docs.python.org/3.9/reference/simple_stmts.html#break)、[continue](https://docs.python.org/3.9/reference/simple_stmts.html#continue) 或 [return](https://docs.python.org/3.9/reference/simple_stmts.html#return) 语句，则 `finally` 子句在执行 `break`、`continue` 或 `return` 语句之前执行。  
* 如果 `finally` 子句中包含 `return` 语句，则返回值来自 `finally` 子句的 `return` 语句的返回值，而不是来自 `try` 子句的 `return` 语句的返回值。  

例如：  

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
... 
>>> bool_return()
False
```

一个更复杂的例子：  

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
... 
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

如你所见，任何情况下都会执行 [finally](https://docs.python.org/3.9/reference/compound_stmts.html#finally) 子句。[except](https://docs.python.org/3.9/reference/compound_stmts.html#except) 子句不处理两个字符串相除触发的 [TypeError](https://docs.python.org/3.9/library/exceptions.html#TypeError)，因此会在 `finally` 子句执行后被重新触发。  

在实际应用程序中，[finally](https://docs.python.org/3.9/reference/compound_stmts.html#finally) 子句对于释放外部资源（例如文件或者网络连接）非常有用，无论资源的使用是否成功。  
<br>  

### 8.8. 预定义的清理操作
某些对象定义了不需要该对象时要执行的标准清理操作。无论使用该对象的操作是否成功，都会执行清理操作。比如，下例要打开一个文件，并输出文件内容到屏幕：

```python
for line in open("myfile.txt"):
    print(line, end="")
```

这个代码的问题在于，在这部分代码完成执行后，它会让文件在一段不确定的时间内处于打开状态。在简单脚本中这没有问题，但对于较大的应用程序来说可能会出问题。[with](https://docs.python.org/3.9/reference/compound_stmts.html#with) 语句允许像文件这样的对象以确保它们总是被及时和正确地清理的方式使用。  

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 *f*。像文件一样，提供预定义清理操作的对象将在其文档中指出这一点。   
<br>  

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
<br />

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
<br>  

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
