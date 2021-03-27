# More JOIN operations

This tutorial introduces the notion of a join. The database consists of three tables `movie` , `actor` and `casting` .

| movie |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **id** | title | yr | director | budget | gross |

| actor |  |
| :--- | :--- |
| **id** | name |

| casting |  |  |
| :--- | :--- | :--- |
| **movieid** | **actorid** | **ord** |

[![Movie2-er.png](https://sqlzoo.net/w/images/5/50/Movie2-er.png)](https://sqlzoo.net/wiki/File:Movie2-er.png)



1.List the films where the **yr** is 1962 \[Show **id**, **title**\]

```sql
SELECT id, title
 FROM movie
 WHERE yr=1962
```











