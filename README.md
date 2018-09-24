* [导航](#导航)
* [数据库](#数据库)
	* [MongoDB](#mongodb)

# 导航
w3school 在线教程  
[http://www.w3school.com.cn](http://www.w3school.com.cn)  
中文版的w3school

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

```
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

字段的值可以是任意的BSON [数据类型](https://docs.mongodb.com/manual/reference/bson-types/)，包括其它文档，数组，和文档数组。例如，下面的文档包含各种类型的值：

```
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
