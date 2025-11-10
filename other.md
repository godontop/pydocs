* [HTML](#html)
* [JS 参考](#js-参考)
    * [Window](#window)
        * [Window 对象](#window-对象)
    * [HTML DOM](#html-dom)
        * [HTML 元素](#html-元素)
* [Markdown](#markdown)
* [Python2](#python2)
    * [Python 2 语言参考](#python-2-语言参考)
        * [3. 数据模型](#3-数据模型-1)
            * [3.4. 特殊方法名](#34-特殊方法名)
                * [3.4.1. 基本自定义](#341-基本自定义)
                * [3.4.6. 仿真容器类型](#346-仿真容器类型)
* [Windows](#windows)
	* [PowerShell](#powershell)


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

## HTML 注释  
注释标签 \<!-- 与 --> 用于在 HTML 插入注释。  

**实例**  

```html
<!-- 在此处写注释 -->
```

# JS 参考
## Window
### Window 对象
**Window 对象** 
窗口对象表示浏览器中的一个打开的窗口。

如果一个文档包含框架（`<iframe>` 标签），浏览器会为 HTML 文档创建一个窗口对象，并为每个框架创建一个额外的窗口对象。 

**Window 对象方法**  
方法            |描述        
---------------|--------------------------------- 
alert()        |显示一个带有消息和“确定”按钮的警告框 
scrollTo()     |将文档滚动到指定的坐标 

## HTML DOM
### HTML 元素
**元素对象** 
在 HTML DOM 中，**元素对象** 代表一个 HTML 元素，例如 P、DIV、A、TABLE 或任何其它的 HTML 元素。 

**属性和方法** 
下面的属性和方法可以被用于所有 HTML 元素：

属性/方法        |描述 
----------------|------------------------------
scrollHeight    |返回元素的完整高度，包括 padding 
scrollWidth     |返回元素的完整宽度，包括 padding 


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

如果要在一个单元格内的两行之间插入一个空行，可以使用两个连续的 `<br>` 标签。 

标签             |效果 
----------------|--------------------------------------------------- 
2个 `<br>` 标签  |第一行<br><br>第二行，我与第一行之间有两个连续的 `<br>` 标签 

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
