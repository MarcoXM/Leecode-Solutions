## SQL 

--------------------------

### SQL标准命令

------

 与关系数据库交互的标准SQL命令是创建、选择、插入、更新、删除和删除，简单分为以下几组：

总的来说，SQL语言定义了这么几种操作数据库的能力：

**DDL：Data Definition Language**

DDL允许用户定义数据，也就是创建表、删除表、修改表结构这些操作。通常，DDL由数据库管理员执行。

**DML：Data Manipulation Language**

DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。

**DQL：Data Query Language**

DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。

#### DDL（数据定义语言）

 数据定义语言用于改变数据库结构，包括创建、更改和删除数据库对象。用于操纵表结构的数据定义语言命令有：

- `CREATE TABLE`-- 创建（在数据库中创建新表、表视图或其他对象）
- `ALTER TABLE`-- 更改 （修改现有的数据库对象，如表）
- `DROP TABLE`-- 删除 （删除数据库中的整个表、表或其他对象的视图）

#### DML（数据操纵语言）

 数据操纵语言用于检索、插入和修改数据，数据操纵语言是最常见的SQL命令。

 数据操纵语言命令包括：

- `INSERT`-- 插入 （创建记录）
- `DELETE`-- 删除 （删除记录）
- `UPDATE`-- 修改（修改记录）
- `SELECT` -- 检索 （从一个或多个表检索某些记录）

#### DCL（数据控制语言）

 数据控制语言为用户提供权限控制命令。

 用于权限控制的命令有：

- `GRANT`-- 授予权限
- `REVOKE`-- 撤销已授予的权限



表的每一行称为记录（Record），记录是一个逻辑意义上的数据。

表的每一列称为字段（Column），同一个表的每一行记录都拥有相同的若干字段。

字段定义了数据类型（整型、浮点型、字符串、日期等），以及是否允许为`NULL`。注意`NULL`表示字段数据不存在。一个整型字段如果为`NULL`不表示它的值为`0`，同样的，一个字符串型字段为`NULL`也不表示它的值为空串`''`。

作为**主键**最好是完全业务无关的字段，我们一般把这个字段命名为`id`。常见的可作为`id`字段的类型有：

1. 自增整数类型：数据库会在插入数据时自动为每一条记录分配一个自增整数，这样我们就完全不用担心主键重复，也不用自己预先生成主键；
2. 全局唯一GUID类型：使用一种全局唯一的字符串作为主键，类似`8f55d96b-8acc-4636-8cb8-76bf8abc2f57`。GUID算法通过网卡MAC地址、时间戳和随机数保证任意计算机在任意时间生成的字符串都是不同的，大部分编程语言都内置了GUID算法，可以自己预算出主键。

对于大部分应用来说，通常自增类型的主键就能满足需求。我们在`students`表中定义的主键也是`BIGINT NOT NULL AUTO_INCREMENT`类型。

 如果使用INT自增类型，那么当一张表的记录数超过2147483647（约21亿）时，会达到上限而出错。使用BIGINT自增类型则可以最多约922亿亿条记录。





## SQL Analyst

### SQL SELECT TOP, LIMIT, ROWNUM

------

- SELECT TOP 子句用于指定要返回的记录数量。
- SELECT TOP子句在包含数千条记录的大型表上很有用。返回大量记录会影响性能。

> **注：**并不是所有的数据库系统都支持SELECT TOP子句。MySQL支持LIMIT子句来选择有限数量的记录，而Oracle使用ROWNUM。

##### SQL Server / MS Access 语法

```sql
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;
```

##### **MySQL语法：**

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```

###### 实例

```sql
SELECT *
FROM Persons
LIMIT 5;
```

##### Oracle 语法

```sql
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
```

###### 实例

```sql
SELECT *
FROM Persons
WHERE ROWNUM <=5;
```





### SQL LIKE 运算符

------

在WHERE子句中使用LIKE运算符来搜索列中的指定模式。

有两个通配符与LIKE运算符一起使用：

- `％` - 百分号表示零个，一个或多个字符
- `_` - 下划线表示单个字符

**注意：** MS Access使用问号（`?`）而不是下划线（`_`）。

百分号和下划线也可以组合使用！

##### SQL LIKE 语法

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

**提示**：您还可以使用AND或OR运算符组合任意数量的条件。

| LIKE 运算符                     | 描述                                 |
| ------------------------------- | ------------------------------------ |
| WHERE CustomerName LIKE 'a%'    | 查找以“a”开头的任何值                |
| WHERE CustomerName LIKE '%a'    | 查找以“a”结尾的任何值                |
| WHERE CustomerName LIKE '%or%'  | 在任何位置查找任何具有“or”的值       |
| WHERE CustomerName LIKE '_r%'   | 在第二个位置查找任何具有“r”的值      |
| WHERE CustomerName LIKE 'a_%_%' | 查找以“a”开头且长度至少为3个字符的值 |
| WHERE ContactName LIKE 'a%o'    | 找到以"a"开头，以"o"结尾的值         |



### SQL IN 运算符

------

IN运算符允许您在WHERE子句中指定多个值。IN运算符是多个OR条件的简写。

##### SQL IN 语法

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

##### 或者

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```



### SQL BETWEEN 运算符

------

BETWEEN运算符用于选取介于两个值之间的数据范围内的值。

BETWEEN运算符选择给定范围内的值。值可以是数字，文本或日期。

BETWEEN运算符是包含性的：包括开始和结束值，且开始值需小于结束值。

##### SQL BETWEEN 语法

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

要否定BETWEEN运算符的结果，可以添加NOT运算符：

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name NOT BETWEEN value1 AND value2;
```



### SQL 连接（Joins）

------

SQL JOIN 子句用于把来自两个或多个表的行结合起来，基于这些表之间的共同字段。

简单地说，就是先确定一个主表作为结果集，然后，把其他表的行有选择性地“连接”在主表结果集上。

最常见的 JOIN 类型：**SQL INNER JOIN（简单的 JOIN）**。 SQL INNER JOIN 从多个表中返回满足 JOIN 条件的所有行。

让我们看看选自 "Orders" 表的数据：

| OrderID | CustomerID | OrderDate  |
| :------ | :--------- | :--------- |
| 10308   | 2          | 1996-09-18 |
| 10309   | 37         | 1996-09-19 |
| 10310   | 77         | 1996-09-20 |

然后，看看选自 "Customers" 表的数据：

| CustomerID | CustomerName                       | ContactName    | Country |
| :--------- | :--------------------------------- | :------------- | :------ |
| 1          | Alfreds Futterkiste                | Maria Anders   | Germany |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Mexico  |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mexico  |

请注意，"Orders" 表中的 "CustomerID" 列指向 "Customers" 表中的客户。上面这两个表是通过 "CustomerID" 列联系起来的。

然后，如果我们运行下面的 SQL 语句（包含 INNER JOIN）：

### 实例

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

运行结果如下所示：

| OrderID | CustomerName                       | OrderDate  |
| :------ | :--------------------------------- | :--------- |
| 10308   | Ana Trujillo Emparedados y helados | 1996-09-18 |

值得注意的是，连接是在WHERE子句中执行的。

可以使用几个操作符连接表，例如=、<、>、<=、>=、！=、BETWEEN、LIKE、 和NOT。

##### 不同的 SQL JOIN

------

在我们继续讲解实例之前，我们先列出您可以使用的不同的 SQL JOIN 类型：

- **INNER JOIN**：如果表中有至少一个匹配，则返回行
- **LEFT JOIN**：即使右表中没有匹配，也从左表返回所有的行
- **RIGHT JOIN**：即使左表中没有匹配，也从右表返回所有的行
- **FULL JOIN**：只要其中一个表中存在匹配，则返回行
- **SELF JOIN**：用于将表连接到自己，就好像该表是两个表一样，临时重命名了SQL语句中的至少一个表
- **CARTESIAN JOIN**：从两个或多个连接表返回记录集的笛卡儿积

###### SQL INNER JOIN 关键字（内部连接）

------

内部链接INNER JOIN关键字选择两个表中具有匹配值的记录。

######## SQL INNER JOIN 语法

```text
SELECT column_name(s)
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name;
```

**注释：**INNER JOIN 与 JOIN 是相同的。

######## 加入三张表

------

以下SQL语句选择包含客户和货运单信息的所有订单：

**代码示例：**

```sql
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
```

###### SQL 左连接 LEFT JOIN 关键字

------

SQL左链接LEFT JOIN关键字返回左表（表1）中的所有行，即使在右表（表2）中没有匹配。如果在正确的表中没有匹配，结果是NULL。

######## SQL LEFT JOIN 语法

```text
SELECT column_name(s)                
FROM table1                
LEFT JOIN table2                
ON table1.column_name=table2.column_name;       
```

或：

```text
SELECT column_name(s)                
FROM table1                
LEFT OUTER JOIN table2                
ON table1.column_name=table2.column_name;      
```

> **注释：**在一些数据库中，LEFT JOIN称为LEFT OUT ER JOIN。



###### SQL右连接 RIGHT JOIN 关键字

------

SQL右链接 RIGHT JOIN 关键字返回右表（table2）的所有行，即使在左表（table1）上没有匹配。如果左表没有匹配，则结果为NULL。

######## SQL RIGHT JOIN 语法

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2 ON table1.column_name = table2.column_name;
```

> **注释：**在一些数据库中，RIGHT JOIN 称为 RIGHT OUTER JOIN。
>

###### SQL FULL OUTER JOIN 关键字

------

当左（表1）或右（表2）表记录匹配时，FULL OUTER JOIN关键字将返回所有记录。

**注意：** FULL OUTER JOIN可能会返回非常大的结果集！

###### SQL FULL OUTER JOIN 语法

```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;
```

 ![SQL FULL OUTER JOIN]

###### SQL自连接

------

自联接是一种常规联接，但表本身是连接的。

###### Self JOIN语法

```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

演示数据库

------

在本教程中，我们将使用着名的Northwind示例数据库。

以下是"Customers"表中的选择：

| CustomerID | CustomerName                       | ContactName    | Address                       | City        | PostalCode | Country |
| ---------- | ---------------------------------- | -------------- | ----------------------------- | ----------- | ---------- | ------- |
| 1          | Alfreds Futterkiste                | Maria Anders   | Obere Str. 57                 | Berlin      | 12209      | Germany |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitución 2222 | México D.F. | 05021      | Mexico  |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mataderos 2312                | México D.F. | 05023      | Mexico  |


######  SQL Self JOIN示例

------

以下SQL语句匹配来自同一城市的客户：

###### 代码示例

```sql
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City 
ORDER BY A.City;
```

### SQL UNION 运算符

------

UNION运算符用于组合两个或更多SELECT语句的结果集，而不返回任何重复的行。

- UNION中的每个SELECT语句必须具有相同的列数
- 这些列也必须具有相似的数据类型
- 每个SELECT语句中的列也必须以相同的顺序排列
- 每个SELECT语句必须有相同数目的列表达式
- 但是每个SELECT语句的长度不必相同

##### SQL UNION 语法1

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

> **注释：**默认情况下，UNION 运算符选择一个不同的值。如果允许重复值，请使用 UNION ALL。

##### SQL UNION 语法2

```sql
SELECT column_name(s) FROM table1
[WHERE condition]

UNION
SELECT column_name(s) FROM table2
[WHERE condition];
```

给定的条件可以是基于您的需求的任何给定表达式。

##### SQL UNION ALL 语法1

UNION All运算符用于组合两个SELECT语句(包括重复行)的结果。

适用于UNION子句的相同规则将适用于UNION All操作符。

```sql
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```

> **注释：**UNION结果集中的列名总是等于UNION中第一个SELECT语句中的列名。

##### SQL UNION ALL 语法2

```sql
SELECT column_name(s) FROM table1
[WHERE condition]
UNION ALL
SELECT column_name(s) FROM table2
[WHERE condition];
```

### SQL explain extend 



