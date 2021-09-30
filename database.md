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
