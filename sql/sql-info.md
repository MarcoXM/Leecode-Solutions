# SQL-Info

## SQL 查漏补缺

### **1. State the differences between HAVING and WHERE clauses.**

| **Basis for Comparison** | **WHERE** | **HAVING** |
| :--- | :--- | :--- |
| Implemented in | Row operations | Column operations |
| Applied to | A single row | The summarized row or groups |
| Used for | Fetching specific data from specific rows according to the given condition | Fetching the entire data and separating according to the given condition |
| Aggregate functions | Cannot have them | Can have them |
| Statements | Can be used with **SELECT, UPDATE, and DELETE** | Cannot be used without a SELECT statement |
| GROUP BY clause | Comes after the WHERE clause | Comes before the HAVING clause |

Where 不能用在group by 的结果. Where 相当与是一个filter 的作用. 这也就是为啥你会看到 np有where . 同时where 也会有更广阔的使用空间

### **2. What is SQL?**

SQL stands for ‘Structured Query Language’ and is used for communicating with the databases. According to ANSI, SQL is the standard query language for Relational Database Management Systems \(RDBMS\) that is used for maintaining them and also for performing different operations of data manipulation on different types of data. **Basically, it is a database language that is used for the creation and deletion of databases,** and it can be used to fetch and modify the rows of a table and also for multiple other things.

### **3. Explain the different types of SQL commands.**

![different types of SQL commands](https://intellipaat.com/blog/wp-content/uploads/2015/09/different-types-of-SQL-commands.png)

* Data Definition Language

  : DDL is that part of SQL which defines the data structure of the database in the initial stage when the database is about to be created. It is mainly used to create and restructure database objects. Commands in DDL are:

  * Create table
  * Alter table
  * Drop table

* **Data Manipulation Language**: DML is used to manipulate the already existing data in the database. That is, it helps users retrieve and manipulate the data. It is used to perform operations like inserting data into the database through the **insert** command, updating the data with the **update** command, and deleting the data from the database through the **delete** command.
* **Data Control Language:** DCL is used to control access to the data in the database. DCL commands are normally used to create objects related to user access and also to control the distribution of privileges among users. The commands that are used in DCL are **Grant** and **Revoke**.
* **Transaction Control Language:** It is used to control the changes made by DML commands. It also authorizes the statements to assemble in conjunction into logical transactions. The commands that are used in TCL are **Commit**, **Rollback**, **Savepoint**, **Begin**, and **Transaction**.

### 4. **What is a default constraint?**

Constraints are used to specify some sort of rules for processing data and limiting the type of data that can go into a table. Now, let’s understand the default constraint.

Code Example:

```sql
-- 我们建一个表,然后给student 成绩设定初始值 50
create table stu1(s_id int, s_name varchar(20), s_marks int default 50)
select *stu1
```

```sql
-- insert 的时候我们就没有给mark 赋值
insert into stu1(s_id,s_name) values(1,’Sam’)
insert into stu1(s_id,s_name) values(2,’Bob’)
insert into stu1(s_id,s_name) values(3,’Matt’)
select * x`from stu1
```

## SQL 约束有哪几种？

> SQL 约束有哪几种？

* NOT NULL: 用于控制字段的内容一定不能为空（NULL）。
* UNIQUE: 控件字段内容不能重复，一个表允许有多个 Unique 约束。
* PRIMARY KEY: 也是用于控件字段内容不能重复，但它在一个表只允许出现一个。
* FOREIGN KEY: 用于预防破坏表之间连接的动作，也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。
* CHECK: 用于控制字段的值范围。

### **5. What is a unique constraint?**

**Unique constraints** ensure that all the values in a column are different. For example, if we assign a unique constraint to the e\_name column in the below table, then every entry in this column should have a unique value.

First, we will create a table.

```sql
-- 当然这里我习惯会是用serial not unique
create table stu2(s_id int unique, s_name varchar(20))
```

Now, we will insert the records.

```sql
insert into stu2 values(1,’Julia’)
insert into stu2 values(2,’Matt’)
insert into stu2 values(3,’Anne’)
```

### **6. How would you find the second highest salary from the below table?**

![How would you find the second highest salary from the below table](https://intellipaat.com/blog/wp-content/uploads/2015/09/How-would-you-find-the-second-highest-salary-from-the-below-table.png) **Code**:

```sql
select * from employee
select max(e_salary) from employee 
where e_salary not in (select max(e_salary) from employee);
-- 非常巧妙的做法,排除了original_max 然后再 得到new_max
```

### **7. What is a Primary Key?**

A primary key is used to uniquely identify all table records. It cannot have NULL values, and it must contain unique values. A table can have only one primary key that consists of single or multiple fields.

Now, we will write a query for demonstrating the use of a primary key for the Employee table:

```sql
CREATE TABLE Employee (
ID int NOT NULL,
Employee_name varchar(255) NOT NULL,
Employee_designation varchar(255),
Employee_Age int,
PRIMARY KEY (ID)
);

-- 建表时候也可以定义
CREATE TABLE e1(
id serial PRIMARY KEY, -- 在这里
Employee_name varchar(255) NOT NULL,
Employee_designation varchar(255),
Employee_Age int 
);
```

### **8. What is a Foreign Key?**

A foreign key is an attribute or a set of attributes that references to the primary key of some other table. So, basically, it is used to link together two tables.

Let’s create a foreign key for the below table:

![What is a Foreign Key](https://intellipaat.com/blog/wp-content/uploads/2015/09/What-is-a-Foreign-Key.png)

```sql
CREATE TABLE Orders (
OrderID int PRIMARY KEY NOT NULL,
OrderNumber int NOT NULL,
PersonID int,
FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) -- 这里就连 table(pri-key)
)
```

### **9. What is an Index?**

Indexes help speed up searching in the database. If there is no index on any column in the **WHERE clause**, then the SQL server has to skim through the entire table and check each and every row to find matches, which might result in slow operation on large data.

Indexes are used to find all rows matching with some columns and then to skim through only those subsets of the data to find the matches.

加速查询的进程, 我的理解是hash-map,没有index 的话就要这个表逐行扫描, 这不就是list 里头找元素的index嘛.

所以如果里面的元素分布越广,这样效率会更高.

**Syntax**:

```sql
CREATE INDEX INDEX_NAME ON TABLE_NAME (COLUMN)
```

### **10. Explain the types of Indexes.**

![Explain the types of Indexes.](https://intellipaat.com/blog/wp-content/uploads/2015/09/Explain-the-types-of-Indexes..png)

* Single-column Indexes

  : A single-column index is created for **only one column of a table**.

  * **Syntax**:

```sql
CREATE INDEX index_name
ON table_name(column_name);
```

* Composite-column Indexes

  : A composite-column index is an index created for **two or more columns of the table.**

  * **Syntax**: 就是table\(\) 传参的时候放两个或者以上嘛

```sql
CREATE INDEX index_name
ON table_name (column1, column2)
```

* Unique Indexes

  : Unique indexes are used for maintaining the data integrity of the table. They don’t allow multiple values to be inserted into the table.

  * **Syntax**: 这个我就只能想到天配 primary key

```sql
CREATE UNIQUE INDEX index
ON table_name(column_name)
```

Now, let’s move on to the next question in this ‘Top SQL Interview Questions’ blog.

### **11. State the differences between Clustered and Non-clustered indexes.**

* **Clustered index**: It is used to sort the rows of data by their key values. A clustered index is like the contents of a phone book. We can open the book at ‘David’ \(for ‘David, Thompson’\) and find information for all Davids right next to each other. Since the data is located next to each other, it helps a lot in fetching data based on range-based queries. Also, the clustered index is actually related to how the data is stored. There is only one clustered index possible per table. 只能有一个index, 在一个table,与内存有关,
* **Non-clustered index**: It stores data at one location and indexes at some other location. The index has pointers that point to the location of the data. As the index in the non-clustered index is stored in different places, there can be many non-clustered indexes for a table. 这个就是一个pointer  指向数据位置

Now, we will see the major differences between clustered and non-clustered indexes:

| **Parameters** | **Clustered Index** | **Non-clustered Index** |
| :--- | :--- | :--- |
| Used for | Sorting and storing records physically in memory | Creating a logical order for data rows. Pointers are used for physical data files |
| Methods for storing | Stores data in the leaf nodes of the index | Never stores data in the leaf nodes of the index |
| Size | Quite large | Comparatively, small |
| Data accessing | Fast | Slow |
| Additional disk space | Not required | Required to store indexes separately |
| Type of key | **By default, the primary key of a table is a clustered index** | It can be used with the unique constraint on the table that acts as a composite key |
| Main feature | Improves the performance of data retrieval | **Should be created on columns used in Joins** |

### **13. What do you understand by a Character Manipulation function?**

Character manipulation functions are used for the **manipulation of character data types.**

Some of the character manipulation functions are:

* UPPER:

  It returns the string in uppercase.

  * **Syntax**:

  ```sql
  UPPER(‘string’)
  ```

  * **Example**:

  ```sql
  SELECT UPPER(‘demo string’) from String;
  ```

  * **Output**:

  ```sql
  DEMO STRING
  ```

* LOWER:

  It returns the string in lowercase.

  * **Syntax**:

  ```sql
  LOWER(‘STRING’)
  ```

  * **Example**:

  ```sql
  SELECT LOWER (‘DEMO STRING’) from String
  ```

  * **Output**:

  ```sql
  demo string
  ```

* INITCAP:

It converts the first letter of the string to uppercase and retains others in lowercase.

* **Syntax**:

  ```sql
  Initcap(‘sTRING’)
  ```

* **Example**:

  ```sql
  SELECT Initcap(‘dATASET’) from String
  ```

* **Output**:

  ```sql
  Dataset
  ```

* CONCAT:

  It is used to concatenate two strings.

  * **Syntax**:

  ```sql
  CONCAT(‘str1’,’str2’)
  ```

  * **Example**:

  ```sql
  SELECT CONCAT(‘Data’,’Science’) from String
  ```

  * **Output**:

  ```sql
  Data Science
  ```

* LENGTH:

It is used to get the length of a string.

* **Syntax**:

  ```sql
  LENGTH(‘String’)
  ```

* **Example**:

  ```sql
  SELECT LENGTH(‘Hello World’) from String
  ```

* **Output**:

  ```sql
  11
  ```

  Going ahead with this blog on ‘Top SQL Interview Questions,’ we will see the next question.

### **14. What is AUTO\_INCREMENT?**

**AUTO\_INCREMENT** is used in SQL to automatically generate a unique number whenever a new record is inserted into a table. 自增是非常基本的概念在CS

Since the primary key is unique for each record, we add this primary field as the AUTO\_INCREMENT field so that it is incremented when a new record is inserted.

The AUTO-INCREMENT value is by default starts from 1 and incremented by 1 whenever a new record is inserted.

**Syntax:**

```sql
CREATE TABLE Employee(
Employee_id int NOT NULL AUTO-INCREMENT,
Employee_name varchar(255) NOT NULL,
Employee_designation varchar(255)
Age int,
PRIMARY KEY (Employee_id)
)
```

### **15. What is the difference between DELETE and TRUNCATE commands?**

* **DELETE**: This query is used to delete or remove one or more existing tables.
* **TRUNCATE**: This statement deletes all the data from inside a table.

![What is the difference between DELETE and TRUNCATE commands](https://intellipaat.com/blog/wp-content/uploads/2015/09/What-is-the-difference-between-DELETE-and-TRUNCATE-commands.png)The difference between DELETE and TRUNCATE commands are as follows:

* TRUNCATE is a DDL command, and DELETE is a DML command. delete 只修改数据,不会改结构
* With TRUNCATE, we can’t really execute and trigger, **while with DELETE we can accomplish a trigger.**
* If a table is referenced by foreign key constraints, then TRUNCATE won’t work. So, if we have a foreign key, then we have to use the DELETE command.

**The syntax for the DELETE command**:

```sql
DELETE FROM table_name
[WHERE condition];
```

* **Example**:

```sql
select * from stu
```

* **Output**:

  ![output 5](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-5.png)

```sql
delete from stu where s_name=’Bob’
-- 将bob删掉
```

* **Output**:

  ![output 6](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-6.png)

**The syntax for the TRUNCATE command**:

```sql
TRUNCATE TABLE
Table_name;
```

* **Example**:

```sql
select * from stu1
```

* **Output**:

![output 7](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-7.png)

```sql
truncate table stu1
-- 清空表了
```

* **Output**:

![output 8](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-8.png)

This deletes all the **records** from the table. 表还是存在的

### **16. What is COALESCE function?**

COALESCE function takes a set of inputs and returns the first non-null value.

这就是排除null值的好方法,null 用这个添加替换值,然后再保存

**Syntax**:

```text
COALESCE(val1,val2,val3,……,nth val)
```

**Example**:

```text
SELECT COALESCE(NULL, 1, 2, ‘MYSQL’)
```

**Output**:

```text
1
```

### **17. What do you understand by Normalization and Denormalization?**

**Normalization and denormalization are basically two methods used in databases.**

![What do you understand by Normalization and De-normalization](https://intellipaat.com/blog/wp-content/uploads/2015/09/What-do-you-understand-by-Normalization-and-De-normalization.png)

Normalization is used in **reducing data redundancy and dependency by organizing fields and tables in databases.** It involves constructing tables and setting up relationships between those tables according to certain rules. The redundancy and inconsistent dependency can be removed using these rules to make it more flexible.

1. Each table cell should contain a single value.

   Each record needs to be unique.

2. Single Column Primary Key
3. Has no transitive functional dependencies

   增加了sql 使用时的成本,不仅要写复杂的code, 同时还有运算时间

   第一范式（1NF）：数据库表中的字段都是单一属性的，不可再分。这个单一属性由基本类型构成，包括整型、实数、字符型、逻辑型、日期型等。

   第二范式（2NF）：数据库表中不存在非关键字段对任一候选关键字段的部分函数依赖（部分函数依赖指的是存在组合关键字中的某些字段决定非关键字段的情况），也即所有非关键字段都完全依赖于任意一组候选关键字。 第三范式（3NF）：在第二范式的基础上，数据表中如果不存在非关键字段对任一候选关键字段的传递函数依赖则符合第三范式。所谓传递函数依赖，指的是如果存在"A → B → C"的决定关系，则C传递函数依赖于A。因此，满足第三范式的数据库表应该不存在如下依赖关系： 关键字段 → 非关键字段x → 非关键字段y

Denormalization is contrary to normalization. In this, we basically add redundant data to speed up complex queries involving multiple tables to join. Here, we attempt to optimize the read performance of a database by adding redundant data or by grouping the data.

### **18. What is wrong with the below-given SQL query?**

```sql
SELECT gender, AVG(age) 
FROM employee 
WHERE AVG(age)>30 
GROUP BY gender
```

When we execute this command, we get the following error:

```text
Msg 147, Level 16, State 1, Line 1
```

Aggregation may not appear in the WHERE clause unless it is in a subquery contained in a HAVING clause or a select list, the column being aggregated is an outer reference.

```sql
Msg 147, Level 16, State 1, Line 1
Invalid column name ‘gender’.
```

**This basically means that whenever we are working with aggregate functions and we are using GROUP BY, we can’t use the WHERE clause. Therefore, instead of the WHERE clause, we should use the HAVING clause.**

Also, when we are using the HAVING clause, GROUP BY should come first and HAVING should come next.

```sql
SELECT e_gender, avg(e_age) 
FROM employee 
GROUP BY e_gender 
HAVING AVG(e_age)>30
```

**Output**:

![Output 9](https://intellipaat.com/blog/wp-content/uploads/2015/09/Output-9.png)

### **19. What do you know about the stuff\(\) function?**

The stuff function deletes a part of the **string and then inserts** another part into the string starting at a specified position.

**Syntax**:

```sql
STUFF(String1, Position, Length, String2)
```

Here, **String1** is the one that would be overwritten. **Position** indicates the starting location for overwriting the string. **Length** is the length of the substitute string, and **String2** is the string that would overwrite String1.

**Example**:

```sql
select stuff(‘SQL Tutorial’,1,3,’Python’)
```

This will change ‘SQL Tutorial’ to ‘Python Tutorial’ 这里和 index 替换有点像

**Output**:

```sql
Python Tutorial
```

### **20. What are Views? Give an example.**

Views are virtual tables used to limit the tables that we want to display, and these are nothing but the result of a SQL statement that has a name associated with it. Since views are not virtually present, they take **less space to store.**

类比的话view 也可以说是table, 但是和table又会有不一样的区别.

![What are Views](https://intellipaat.com/blog/wp-content/uploads/2015/09/What-are-Views.png)

Let’s consider an example. In the below employee table, say, we want to perform multiple operations on the records with **gender ‘Female’**. We can create a view-only table for the female employees from the entire employee table.

Now, let’s implement it on the SQL server.

Below is our employee table:

```sql
select * from employee -- 实际上这个操作不要用,要的话自己给个top 5
```

![output 10](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-10.png)

Now, we will write the syntax for view.

**Syntax**:

```sql
    CREATE VIEW female_employee AS SELECT * 
FROM employee 
WHERE e_gender=’Female’

SELECT * FROM female_employee
```

**Output**:

![output 11](https://intellipaat.com/blog/wp-content/uploads/2015/09/output-11.png)

视图是一种基于数据表的一种虚表

（1）视图是一种虚表 （2）视图建立在已有表的基础上, 视图赖以建立的这些表称为基表 （3）**向视图提供数据内容的语句为 SELECT 语句,可以将视图理解为存储起来的 SELECT 语句** （4）视图向用户提供基表数据的另一种表现形式 （5）视图没有存储真正的数据，真正的数据还是存储在基表中 （6）程序员虽然操作的是视图，但最终视图还会转成操作基表 （7）一个基表可以有0个或多个视图

### **24. State the differences between Views and Tables.**

| **Views** | **Tables** |
| :--- | :--- |
| It is a **virtual table** that is extracted from a database. | A table is structured with a set number of columns and a boundless number of rows. |
| Views do not hold data themselves. | Table contains data and stores the data in databases. |
| A view is also utilized to query certain information contained in a few distinct tables. | A table holds fundamental client information and the cases of a characterized object. |
| In a view, we will get frequently queried information. | In a table, changing the information in the database changes the information that appears in the view |

### **21. What is a stored procedure? Give an example.**

A stored procedure is a prepared SQL code that can be **saved and reused**. In other words, we can consider a stored procedure to be **a function consisting of many SQL statements to access the database system**. We can consolidate several SQL statements into a stored procedure and execute them whenever and wherever required.

**A stored procedure can be used as a means of modular programming**, i.e., we can create a stored procedure once, store it, and call it multiple times as required. This also supports faster execution when compared to executing multiple queries.

**Syntax**:

```sql
--------------创建存储过程-----------------

CREATE PROC [ EDURE ] procedure_name [ ; number ]
    [ { @parameter data_type }
        [ VARYING ] [ = default ] [ OUTPUT ]
    ] [ ,...n ]

[ WITH
    { RECOMPILE | ENCRYPTION | RECOMPILE , ENCRYPTION } ]

[ FOR REPLICATION ]

AS sql_statement [ ...n ]

--------------调用存储过程-----------------

EXECUTE Procedure_name '' --存储过程如果有参数，后面加参数格式为：@参数名=value，也可直接为参数值value

--------------删除存储过程-----------------

drop procedure procedure_name    --在存储过程中能调用另外一个存储过程，而不能删除另外一个存储过程
```

**Example**:

```sql
-- 无参数存储过程, 选出Student表中的所有信息,这里可以是任何操作,类比seed_everything
create proc StuProc
as      //此处 as 不可以省略不写
begin   //begin 和 end 是一对，不可以只写其中一个，但可以都不写
select S#,Sname,Sage,Ssex 
from student
end
go
```

### **有参数存储过程**

**全局变量**

全局变量也称为外部变量，是在函数的外部定义的，它的作用域为从变量定义处开始，到本程序文件的末尾。

选出指定姓名的学生信息:

```sql
create proc StuProc
@sname varchar(100)   
as 
begin
select S#,Sname,Sage,Ssex 
from student 
where sname=@sname -- 将这人民传到sql
end
go

exec StuProc '赵雷'   //执行语句
```

上面是在外部给变量赋值，也可以在内部直接给变量设置默认值

```sql
create proc StuProc
@sname varchar(100)='赵雷'
as 
begin
select S#,Sname,Sage,Ssex from student where sname=@sname
end
go

exec StuProc
```

也可以把变量的内容输出，使用output

```sql
create proc StuProc
@sname varchar(100),
@IsRight int  output -- 先定义变量,类型
as 
if exists (select S#,Sname,Sage,Ssex from student where sname=@sname)
set @IsRight =1 -- set 赋值
else
set @IsRight=0
go

declare @IsRight int 
exec StuProc '赵雷' , @IsRight output
select @IsRight
```

以上是全局变量，下面来了解局部变量

**局部变量**

局部变量也称为内部变量。局部变量是在函数内作定义说明的。其作用域仅限于函数内部，离开该函数后再使用这种变量是非法的。

**局部变量的定义**

必须先用Declare命令定以后才可以使用，declare{@变量名 数据类型}

**局部变量的赋值方法**

set{@变量名=表达式}或者select{@变量名=表达式}

**局部变量的显示**

类比go !!! 函数里面 `:=`才能用这个

```sql
create proc StuProc
as 
declare @sname varchar(100)
set @sname='赵雷'
select S#,Sname,Sage,Ssex from student where sname=@sname
go

exec StuProc --这里不就是封装了,但是能换人吗?
```

那如果是要把局部变量的数据显示出来怎么办呢？

```sql
create proc StuProc
as 
declare @sname varchar(100)
set @sname=(select Sname from student where S#=01)
select @sname -- 通过赋值然后select 拉出来
go

exec StuProc
```

比如，在SQL Server查询编辑器窗口中用CREATE PROCEDURE语句创建存储过程PROC\_InsertEmployee，用于实现向员工信息表（tb\_Employee）中添加信息，同时生成自动编号。其SQL语句如下：

```sql
IF EXISTS (SELECT name  
   FROM   sysobjects  
   WHERE  name = 'Proc_InsertEmployee'  
   AND          type = 'P') 
DROP PROCEDURE Proc_InsertEmployee 
GO  -- 排除重复
CREATE PROCEDURE Proc_InsertEmployee 
@PName nvarchar(50), 
@PSex nvarchar(4), 
@PAge int, 
@PWage money 
AS 
begin 
   declare @PID nvarchar(50) -- 内部变量来源于table 本身
   select @PID=Max(员工编号) from tb_Employee 
   if(@PID is null) 
       set @PID='P1001' 
   else 
       set @PID='P'+cast(cast(substring(@PID,2,4) as int)+1 as nvarchar(50)) 
   begin 
       insert into tb_Employee values(@PID,@PName,@PSex,@PAge,@PWage) 
   end 
end 
go
```

### **26. Explain the difference between OLTP and OLAP.**

![Explain the difference between OLTP and OLAP](https://intellipaat.com/blog/wp-content/uploads/2015/09/Explain-the-difference-between-OLTP-and-OLAP.png)**OLTP:** It basically stands for **Online Transaction Processing** and we can consider it to be a category of software applications that is efficient for supporting **transaction-oriented programs.** One of the important attributes of the OLTP system is its potentiality to keep up the consistency.

这是区别data engineer 和data analst 的区别

The OLTP system often follows decentralized planning to keep away from single points of failure. **This system is generally designed for a large audience of end-users to perform short transactions**. Also, queries involved in such databases are generally simple, need fast response time, and in comparison, it returns only a few records. So, the number of transactions per second acts as an effective measure for those systems.

**OLAP:** OLAP stands for **Online Analytical Processing** and it is a category of software programs that are identified by a comparatively lower frequency of online transactions. For OLAP systems, the efficacy computing depends highly on the response time. Hence, such systems are generally **used for data mining or maintaining aggregated historical data**, and they are usually used in multi-dimensional schemas.

目标是不一样的,OLTP 你就要不断地保持数据一致,准确 定时的讲OLTP &gt;&gt;&gt;&gt; OLAP

### **27. What do you understand by Self Join?**

Self Join in SQL is used for joining a table with itself. Here, depending upon some conditions, each row of the table is joined with itself and with other rows of the table.

**Syntax**:

```text
SELECT a.column_name, b.column_name
FROM table a, table b
WHERE condition
```

**Example**: Consider the customer table given below.

| **ID** | **Name** | **Age** | **Address** | **Salary** |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Anand | 32 | Ahmedabad | 2,000.00 |
| 2 | Abhishek | 25 | Delhi | 1,500.00 |
| 3 | Shivam | 23 | Kota | 2,000.00 |
| 4 | Vishal | 25 | Mumbai | 6,500.00 |
| 5 | Sayeedul | 27 | Bhopal | 8,500.00 |
| 6 | Amir | 22 | MP | 4,500.00 |
| 7 | Arpit | 24 | Indore | 10,000.00 |

We will now join the table using Self Join:

```sql
SQL> SELECT a.ID, b.NAME, a.SALARY
   FROM CUSTOMERS a, CUSTOMERS b
   WHERE a.SALARY < b.SALARY;
```

**Output**:

| **ID** | **Name** | **Salary** |
| :--- | :--- | :--- |
| 2 | Anand | 1,500.00 |
| 2 | Abhishek | 1,500.00 |
| 1 | Vishal | 2,000.00 |
| 2 | Vishal | 1,500.00 |
| 3 | Vishal | 2,000.00 |
| 6 | Vishal | 4,500.00 |
| 1 | Sayeedul | 2,000.00 |
| 2 | Sayeedul | 1,500.00 |
| 3 | Sayeedul | 2,000.00 |
| 4 | Sayeedul | 6,500.00 |
| 6 | Sayeedul | 4,500.00 |
| 1 | Amir | 2,000.00 |
| 2 | Amir | 1,500.00 |
| 3 | Amir | 2,000.00 |
| 1 | Arpit | 2,000.00 |
| 2 | Arpit | 1,500.00 |
| 3 | Arpit | 2,000.00 |
| 4 | Arpit | 6,500.00 |
| 5 | Arpit | 8,500.00 |
| 6 | Arpit | 4,500.00 |

### **28. Using auto increament column as index .**

在使用InnoDB存储引擎时，如果没有特别的需要，请永远使用一个与业务无关的自增字段作为主键。如果从数据库索引优化角度看，使用InnoDB引擎而不使用自增主键绝对是一个糟糕的主意。

InnoDB使用聚集索引，数据记录本身被存于主索引（一颗B+Tree）的叶子节点上。这就要求同一个叶子节点内（大小为一个内存页或磁盘页）的各条数据记录按主键顺序存放，因此每当有一条新的记录插入时，MySQL会根据其主键将其插入适当的节点和位置，如果页面达到装载因子（InnoDB默认为15/16），则开辟一个新的页（节点）。如果表使用自增主键，那么每次插入新的记录，记录就会顺序添加到当前索引节点的后续位置，当一页写满，就会自动开辟一个新的页。如下：

![image-20200505190631414](https://github.com/MarcoXM/Leecode-Solutions/tree/b85a0d7c5257f054f03d52b7b035f98ce302a46b/home/marco/.config/Typora/typora-user-images/image-20200505190631414.png)

### **28. Using ①②用 `>=` 替代 `>` .**

```sql
      低效：
      SELECT * FROM EMP WHERE DEPTNO > 3   
      首先定位到DEPTNO=3的记录并且扫描到第一个DEPT大于3的记录
      高效：
      SELECT * FROM EMP WHERE DEPTNO >= 4  
      直接跳到第一个DEPT等于4的记录
```

### **29. MySQL joins: ON vs. USING vs. Theta-style**

What is the difference between the following three syntaxes?

> ```sql
> SELECT * FROM film JOIN film_actor ON (film.film_id = film_actor.film_id)
> SELECT * FROM film JOIN film_actor USING (film_id)
> SELECT * FROM film, film_actor WHERE film.film_id = film_actor.film_id
> ```

The difference is mostly syntactic sugar, but with a couple interesting notes.

To put names, the first two are called **"ANSI-style"** while the third is called **"Theta-style"**.

#### Theta styleF

On the **FROM** clause, tables are listed as if with Cartesian products, and the **WHERE** clause specifies how the join should take place.

This is considered to be the "old" style. It is somewhat confusing to read. Consider the following query:

> ```sql
> SELECT * FROM film, film_actor WHERE film.film_id = film_actor.film_id AND actor_id = 17 AND film.length > 120
> ```

烦乱,把所有的都塞到了where

The above lists films over **120** minutes in length, in which actor **\#17** plays. Never mind the results; what about the query? Being just one part of the **WHERE** clause, a one out of three elements in the **AND** expression, the join equation gets lost. It is difficult to find and isolate the terms which make for table joins as opposed to terms which filter out rows. In the above example it is still relatively easy to point out. How about a query with **5** tables and a **20** terms **WHERE** clause?

#### ANSI style: ON

With **JOIN** ... **ON**, one separates the join terms from the filtering terms. Rewriting the previous example:

> ```text
> SELECT * FROM film JOIN film_actor ON (film.film_id = film_actor.film_id) WHERE actor_id = 17 AND film.length > 120
> ```

It is quite clear now what belongs to what.

Note: the parenthesis are not strictly required in the **ON** clause. I personally like to use them: it makes for an even greater distinction between query parts. SQL syntax is such a mess!

#### ANSI style: USING

Is the special case where we join tables on columns of the same name, we can make a shortcut and use **USING**:

> ```text
> SELECT * FROM film JOIN film_actor USING (film_id) WHERE actor_id = 17 AND film.length > 120
> ```

This time the parenthesis are required \(I'm not sure why the difference on that part\).

This is mainly a nicety, less words to type, and a resulting prettified query. But also note a couple differences:

#### USING vs. ON

The following is valid:

> ```text
> SELECT film.title, film_id FROM film JOIN film_actor USING (film_id) WHERE actor_id = 17 AND film.length > 120;
> ```

But the following is not:

> ```text
> SELECT film.title, film_id FROM film JOIN film_actor ON (film.film_id = film_actor.film_id) WHERE actor_id = 17 AND film.length > 120;
> ERROR 1052 (23000): Column 'film_id' in field list is ambiguous
> ```

