# SELECT within SELECT



| name | continent | area | population | gdp |
| :--- | :--- | :--- | :--- | :--- |
| Afghanistan | Asia | 652230 | 25500100 | 20343000000 |
| Albania | Europe | 28748 | 2831741 | 12960000000 |
| Algeria | Africa | 2381741 | 37100000 | 188681000000 |
| Andorra | Europe | 468 | 78115 | 3712000000 |
| Angola | Africa | 1246700 | 20609294 | 100990000000 |
| ... |  |  |  |  |



1. **Bigger than Russia**

```sql
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')
```



2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

```sql
SELECT name FROM world
  WHERE continent = 'Europe'
    and GDP/population >
     (SELECT GDP/population FROM world
      WHERE name='United Kingdom')
```

3. List the **name** and **continent** of countries in the continents containing either **Argentina** or **Australia**. Order by name of the country.

```sql
SELECT name, continent FROM world
  WHERE continent in 
     (SELECT continent FROM world
      WHERE name ='Argentina' or name ='Australia')
```

4. Which country has a population that is more than Canada but less than Poland? Show the name and the population.

```sql
SELECT name, population FROM world
  WHERE population > 
     (SELECT population FROM world
      WHERE name ='Canada') and population < (SELECT population FROM world
      WHERE name ='Poland')
```

5. Germany \(population 80 million\) has the largest population of the countries in Europe. Austria \(population 8.5 million\) has 11% of the population of Germany.

Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

```sql
SELECT  name, CONCAT(ROUND(population * 100/(SELECT population FROM world WHERE name = 'Germany'),0), '%')
FROM world
WHERE continent = 'Europe'


```

6. Which countries have a GDP greater than every country in Europe? \[Give the **name** only.\] \(Some countries may have NULL gdp values\)

```sql

SELECT name
FROM world
WHERE gdp >= ALL(SELECT gdp FROM world WHERE gdp >=0 AND continent = 'Europe') AND continent != 'Europe'
```

7. Largest in each continent

```sql
SELECT continent, name, area FROM world x
  WHERE area >= ALL
    (SELECT area FROM world y
        WHERE y.continent=x.continent
          AND area>0)
```

8.List each continent and the name of the country that comes first alphabetically.

```sql
SELECT continent, name
FROM world x
WHERE name <= ALL(SELECT name FROM world y WHERE y.continent = x.continent)
```

9.Find the continents where all countries have a population &lt;= 25000000. Then find the names of the countries associated with these continents. Show **name**, **continent** and **population**.

```sql
SELECT name, continent, population
FROM world x
WHERE 25000000  > ALL(SELECT population FROM world y WHERE x.continent = y.continent AND y.population > 0)

```

10.Some countries have populations more than three times that of any of their neighbours \(in the same continent\). Give the countries and continents.

```sql
SELECT name, continent
FROM world x
WHERE population > ALL(SELECT population*3 FROM world y WHERE x.continent = y.continent AND population > 0 AND y.name != x.name)
```

















