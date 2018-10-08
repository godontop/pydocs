* [导航](#导航)
* [Markdown](#markdown)
* [数据库](#数据库)
	* [MongoDB](#mongodb)
		* [文档](#文档)
		* [mongo Shell](#mongo-shell)
			* [配置mongo Shell](#配置mongo-shell)
	* [MySQL](#mysql)
		* [MySQL Workbench](#mysql-workbench)
		* [UPDATE语法](#update语法)
* [vim](#vim)
	* [vim插件](#vim插件)
		* [YouCompleteMe](#youcompleteme)

# 导航
DistroWatch  
[https://distrowatch.com](https://distrowatch.com)  
Linux发行版排名统计

StackEdit  
[https://stackedit.io/app](https://stackedit.io/app)  
支持GFM的Markdown在线编辑器

w3school 在线教程  
[http://www.w3school.com.cn](http://www.w3school.com.cn)  
中文版的w3school

# Markdown
要在Markdown中显示`<`和`>`，必须使用使用转义字符`&lt;`和`&gt;`。

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

### mongoexport
**选项**  
--db &lt;database&gt;, -d &lt;database&gt;  
  指定数据库的名字

--collection &lt;collection&gt;, -c &lt;collection&gt;  
  指定要导出的collection

--fields &lt;field1[,field2]&gt;, -f &lt;field1[,field2]&gt;  
指定要导出的字段，如果有多个字段，使用逗号分隔

--type &lt;string&gt;  
  默认值：json  
  在版本3.0中新增  
  指定要导出的格式。为CSV格式指定csv，为JSON格式指定json。  
  如果指定csv，则你必须使用--fields或--fieldFile选项来声明要从collection中导出的字段。

--out &lt;file&gt;, -o &lt;file&gt;  
  指定一个文件以写入导出的数据。如果没有指定文件名，mongoexport会将数据写到标准输出。


**用法**  
*在版本3.0中发生变化：* mongoexport删除了--csv选项。使用--type=csv选项来为输出指定CSV格式。

以csv格式导出cache数据库的twentythreads collection的_id字段

```sh
mongoexport --db cache --collection twentythreads --type=csv --fields _id --out url.csv
```

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