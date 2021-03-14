# SELECT from WORLD



| name | continent | area | population | gdp |
| :--- | :--- | :--- | :--- | :--- |
| Afghanistan | Asia | 652230 | 25500100 | 20343000000 |
| Albania | Europe | 28748 | 2831741 | 12960000000 |
| Algeria | Africa | 2381741 | 37100000 | 188681000000 |
| Andorra | Europe | 468 | 78115 | 3712000000 |
| Angola | Africa | 1246700 | 20609294 | 100990000000 |
| ... |  |  |  |  |

### 1. Introduction

1.[Read the notes about this table.](https://sqlzoo.net/wiki/Read_the_notes_about_this_table.) Observe the result of running this SQL command to show the name, continent and population of all countries

```sql
SELECT name, continent, population FROM world
```

**2. Large Countries**

[How to use WHERE to filter records.](https://sqlzoo.net/wiki/WHERE_filters) Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.

```sql
SELECT name
  FROM world
 WHERE population > 1000000000
```

**3.** Per capita GDP

Give the `name` and the **per capita GDP** for those countries with a `population` of at least 200 million.

```sql
SELECT  name, gdp/population
FROM world
WHERE population > 200000000
```

4**. South America In millions**

Show the `name` and `population` in millions for the countries of the `continent` 'South America'. Divide the population by 1000000 to get population in millions.

```sql
SELECT name, population/1000000 as population
FROM world
WHERE continent = 'South America'
```

5. **France, Germany, Italy**

Show the `name` and `population` for France, Germany, Italy

```sql
SELECT name, population
FROM world
WHERE name in ('France','Germany','Italy');
```

**6.United**

Show the countries which have a `name` that includes the word 'United'

```sql
SELECT name
FROM world
WHERE name like 'United%'
```

**7. Two ways to be big**

Two ways to be big: A country is **big** if it has an area of more than 3 million sq km or it has a population of more than 250 million.

Show the countries that are big by area or big by population. Show name, population and area.

```sql
SELECT name, population, area
FROM world 
WHERE area > 3000000 or population >250000000;
```



