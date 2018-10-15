* [导航](#导航)
* [Markdown](#markdown)
* [Python](#python)
    * [Python标准库](#python标准库)
        * [内置类型](#内置类型)
            * [数值类型 — int, float, complex](#数值类型--int-float-complex)
                * [整型数类型的按位运算](#整型数类型的按位运算)
        * [并行执行](#并行执行)
            * [threading — 基于线程的并行](#threading--基于线程的并行)
                * [线程对象](#线程对象)
        * [互联网协议与支持](#互联网协议与支持)
            * [urllib.parse — 将URLs解析为组件](#urllibparse--将urls解析为组件)
                * [URL解析](#url解析)
    * [Python语言参考](#python语言参考)
        * [3. 数据模型](#3-数据模型)
            * [3.3. 特殊方法名](#33-特殊方法名)
                * [3.3.1. 基本自定义](#331-基本自定义)
                * [3.3.7. 仿真容器类型](#337-仿真容器类型)
    * [PyPI](#pypi)
        * [PyMongo](#pymongo)
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
	* [MySQL](#mysql)
		* [MySQL Workbench](#mysql-workbench)
        * [LOAD DATA INFILE语法](#load-data-infile语法)
        * [SELECT语法](#select语法)
		* [UPDATE语法](#update语法)
        * [比较函数与运算符](#比较函数与运算符)
* [vim](#vim)
	* [vim插件](#vim插件)
		* [YouCompleteMe](#youcompleteme)

# 导航
DistroWatch  
[https://distrowatch.com](https://distrowatch.com)  
Linux发行版排名统计

Markdown  
[http://tool.oschina.net/markdown](http://tool.oschina.net/markdown)  
开源中国的在线Markdown编辑器

MongoDB文档  
[https://docs.mongodb.com](https://docs.mongodb.com)

MongoDB Reference  
[https://docs.mongodb.com/manual/reference/](https://docs.mongodb.com/manual/reference/)

PyMongo  
[http://api.mongodb.com/python/current/index.html](http://api.mongodb.com/python/current/index.html)

StackEdit  
[https://stackedit.io/app](https://stackedit.io/app)  
支持GFM的Markdown在线编辑器

w3school 在线教程  
[http://www.w3school.com.cn](http://www.w3school.com.cn)  
中文版的w3school

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

### 并行执行
#### threading — 基于线程的并行
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
### PyMongo
使用 [find_one()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one) 获取一个单一的文档

在MongoDB中可以被执行的最基本的查询类型是 [find_one()](http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one)。这个方法返回一个匹配查询的单一的文档 (或者 `None` 如果没有文档被匹配)。这很有用当你知道那里仅有一个匹配文档，或者仅对第一个匹配有兴趣。

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
upsert     |布尔  |可选的。与 **update** 字段一起使用。

当为 **真** 时，[findAndModify()](https://docs.mongodb.com/manual/reference/method/db.collection.findAndModify/#db.collection.findAndModify) either:

* 如果没有文档匹配**查询**则创建一个新的文档。详细信息请看 [upsert behavior](https://docs.mongodb.com/manual/reference/method/db.collection.update/#upsert-behavior)。
* 更新一个匹配**查询**的单一的文档。

为避免多次 upserts，请确保**查询**字段是[唯一索引的](https://docs.mongodb.com/manual/core/index-unique/#index-type-unique)。

默认值为 **false**。

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
$ne   |匹配所有不等于指定值的值。

## MySQL
将ID表的MARKET字段的长度改为10

```sql
mysql> alter table ID modify column MARKET varchar(10);
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

### SELECT语法

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

# vim
在vim中输入下面的指令，看vim是否支持python或python3，返回1则表示支持

```vim
:echo has('python') || has('python3')
```

显示当前文件的文件类型

```vim
:set ft?
```

**查找**  
在Normal模式下按下`/`，然后输入要查找的字符并按下回车键，vim便会跳转到第一个匹配位置，按`n`查找下一个，按`N`查找上一个。

## vim插件
### YouCompleteMe
#### 命令
**`:YcmDebugInfo`**  
可以查看用于当前文件的编译命令