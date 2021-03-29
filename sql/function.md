# Function



RANK\(\) OVER \(ORDER BY f DESC\) returns the rank position relative to the expression f.

```sql
  RANK() OVER (ORDER BY f DESC) 
```

1.In this example we show the ranking, by population of those countries with a population of over 180 million.

```sql
SELECT name,population,
       RANK() OVER (ORDER BY population DESC) AS rank_population
FROM world WHERE population>180000000
ORDER BY name


for i in rank(1, len(rows)):
    rank[i] = dit_rank(population values)
```





2. You can see view the RANK according to continent. This shows the biggest country

```sql
SELECT
 name,population,
 RANK() OVER (ORDER BY population DESC) AS world_rank,
 RANK() OVER (PARTITION BY continent ORDER BY population DESC) AS local_rank
FROM world WHERE population > 100000000
ORDER BY name
```



