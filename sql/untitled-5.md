# Window LAG

  
1.The example uses a WHERE clause to show the cases in 'Italy' in March.

Modify the query to show data from Spain

```sql
SELECT name, DAY(whn),
 confirmed, deaths, recovered
 FROM covid
WHERE name = 'Spain'
AND MONTH(whn) = 3
ORDER BY whn
```

  
2.The **LAG** function is used to show data from the preceding row or the table. When lining up rows the data is partitioned by country name and ordered by the data **whn**. That means that only data from Italy is considered.

Modify the query to show **confirmed** for the day before.

```sql
SELECT name, DAY(whn), confirmed,
--lag 参数类型就是col是哪一个
   LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) as dbf 
 FROM covid
WHERE name = 'Italy'
AND MONTH(whn) = 3
ORDER BY whn
```

3.The number of confirmed case is cumulative - but we can use LAG to recover the number of new cases reported for each day.

Show the number of new cases for each day, for Italy, for March.

```sql

-- 直接做数学计算
SELECT name, DAY(whn) as day, confirmed - LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) as new
 FROM covid
WHERE name = 'Italy'
AND MONTH(whn) = 3
```

4.The data gathered are necessarily estimates and are inaccurate. However by taking a longer time span we can mitigate some of the effects.

You can filter the data to view only Monday's figures **WHERE WEEKDAY\(whn\) = 0**.

Show the number of new cases in Italy for each week - show Monday only.

```sql
SELECT name,convert(varchar(12), whn, 126), confirmed
 FROM covid
WHERE name = 'Italy'
AND DATENAME(weekday, whn) = 'Monday'
ORDER BY whn

```



6.The query shown shows the number of confirmed cases together with the world ranking for cases.

United States has the highest number, Spain is number 2...

Notice that while Spain has the second highest confirmed cases, Italy has the second highest number of deaths due to the virus.

Include the ranking for the number of deaths in the table.

```sql
SELECT 
   name,
   confirmed,
   RANK() OVER (ORDER BY confirmed DESC) rc1,
   deaths,
   RANK() OVER (ORDER BY deaths DESC) rc2
   FROM covid
WHERE whn = '2020-04-20'
ORDER BY confirmed DESC
```

8.For each country that has had at last 1000 new cases in a single day, show the date of the peak number of new cases.

```sql
select *
from (
    select 
        t.*, 
        rank() over(partition by name order by new_cases desc) rn
    from (
        select 
            t.*,
            confirmed - lag(confirmed, 1, 0) over(partition by name order by whn) new_cases
        from covid t
    ) t
    where new_cases > 1000
) t
where rn = 1
```











