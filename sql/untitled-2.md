# SELECT from Nobel



| nobel |  |  |
| :--- | :--- | :--- |
| yr | subject | winner |
| 1960 | Chemistry | Willard F. Libby |
| 1960 | Literature | Saint-John Perse |
| 1960 | Medicine | Sir Frank Macfarlane Burnet |
| 1960 | Medicine | Peter Madawar |
| ... |  |  |

**1.Winners from 1950**

Change the query shown so that it displays Nobel prizes for 1950.

```sql
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950
```

**2. 1962 Literature**

```sql
SELECT winner
  FROM nobel
 WHERE yr = 1962
   AND subject = 'Literature'
```

**3.** Albert Einstein

```sql
SELECT yr, subject 
FROM NOBEL
WHERE winner = 'Albert Einstein';
```

4.Recent Peace Prizes

```sql
SELECT winner
FROM nobel
WHERE subject = 'Peace' and yr >= 2000
```

5. Literature in the 1980's

```sql
SELECT *
FROM nobel
WHERE subject = 'Literature' and yr BETWEEN 1980 AND 1989;
```

6.Only Presidents

Show all details of the presidential winners:

* Theodore Roosevelt
* Woodrow Wilson
* Jimmy Carter
* Barack Obama

```sql
SELECT * FROM nobel
 WHERE winner IN ('Theodore Roosevelt',
                  'Woodrow Wilson',
                  'Jimmy Carter',
                  'Barack Obama')
```

7.John

```sql
SELECT winner FROM nobel
WHERE winner like 'john %';
```

8. Chemistry and Physics from different years

```sql
SELECT yr, subject, winner
FROM nobel
WHERE (subject = 'Physics' and yr = 1980) or
      (subject = 'Chemistry' and yr = 1984);
```

9.Exclude Chemists and Medics

```sql
SELECT yr,subject,winner
FROM nobel
WHERE yr = 1980 and subject not in ('Chemistry','Medicine')
```

10. Early Medicine, Late Literature

 Show year, subject, and name of people who won a 'Medicine' prize in an early year \(before 1910, not including 1910\) together with winners of a 'Literature' prize in a later year \(after 2004, including 2004\)

```sql
SELECT *
FROM nobel
WHERE (yr < 1910 and subject = 'Medicine') 
  or (yr >=2004 and subject = 'Literature')
```

  
11.Find all details of the prize won by PETER GRÜNBERG

```sql
SELECT *
FROM nobel
WHERE winner LIKE 'peter gr%nberg'
```

12. Find all details of the prize won by EUGENE O'NEILL

```sql
SELECT *
FROM nobel
WHERE winner LIKE 'EUGENE O''NEILL'
```

  
13.List the winners, year and subject where the winner starts with **Sir**. Show the the most recent first, then by name order.

```sql
SELECT winner, yr, subject
FROM nobel
WHERE winner like 'sir%'
ORDER BY yr DESC, winner;
```

14. Chemistry and Physics last

```sql
SELECT 
  winner, subject
FROM 
  nobel
WHERE 
  yr = 1984
ORDER BY 
  CASE WHEN subject IN ('Physics','Chemistry') THEN 1 ELSE 0 END, 
  subject, 
  winner
```





