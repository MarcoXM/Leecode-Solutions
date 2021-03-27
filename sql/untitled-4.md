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

2.Give year of 'Citizen Kane'.

```sql
SELECT yr
FROM movie 
WHERE title = 'Citizen Kane'
```

3.List all of the Star Trek movies, include the **id**, **title** and **yr** \(all of these movies include the words Star Trek in the title\). Order results by year.

```sql
SELECT id, title , yr
FROM movie 
WHERE title like '%Star Trek%'
ORDER BY yr
```

  
4.What **id** number does the actor 'Glenn Close' have?

```sql
SELECT id
FROM actor 
WHERE name = 'Glenn Close' 
```

  
5.What is the **id** of the film 'Casablanca'

```sql
SELECT id
FROM movie
WHERE title = 'Casablanca'
```

  
6.Obtain the cast list for 'Casablanca'.what is a cast list?

The cast list is the names of the actors who were in the movie.

Use **movieid=11768**, \(or whatever value you got from the previous question\)

{% tabs %}
{% tab title="SQL" %}
```sql
SELECT name
FROM actor 
JOIN casting
ON id = actorid 
WHERE movieid = 27;
```
{% endtab %}

{% tab title="SQL" %}
```sql
SELECT name
FROM actor, casting
WHERE id=actorid AND movieid =27
```
{% endtab %}
{% endtabs %}

  
7.Obtain the cast list for the film 'Alien'

```sql
SELECT name
FROM actor 
JOIN casting
ON id = actorid 
WHERE movieid = (SELECT id FROM movie WHERE title = 'Alien');
```

  
8.List the films in which 'Harrison Ford' has appeared

```sql
SELECT title
FROM movie 
JOIN casting
ON id = movieid AND actorid = (SELECT id FROM actor WHERE name = 'Harrison Ford');
```

  
9.List the films where 'Harrison Ford' has appeared - but not in the starring role. \[Note: the **ord** field of casting gives the position of the actor. If ord=1 then this actor is in the starring role\]

```sql
SELECT title
FROM movie 
JOIN casting
ON id = movieid AND actorid = (SELECT id FROM actor WHERE name = 'Harrison Ford' AND ord != 1);
```

  
10.List the films together with the leading star for all 1962 films.

```sql
SELECT title,name
FROM movie
JOIN casting 
ON movie.id = casting.movieid 
JOIN actor
ON actor.id = casting.actorid AND ord = 1
WHERE yr = 1962;
```

11.Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies

```sql
SELECT yr,COUNT(title) FROM
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id
WHERE name='Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 2
```

  
12.List the film title and the leading actor for all of the films 'Julie Andrews' played in.

```sql
SELECT title,name
FROM movie
JOIN casting 
ON movie.id = casting.movieid
JOIN actor
ON actor.id = casting.actorid
WHERE casting.ord = 1 AND movie.id IN (SELECT movieid FROM casting
WHERE actorid = (
  SELECT id FROM actor 
  WHERE name='Julie Andrews'))
```

  
13.Obtain a list, in alphabetical order, of actors who've had at least 15 **starring** roles.

```sql
SELECT name
FROM actor
JOIN casting
ON id = actorid
WHERE ord = 1
GROUP BY name
HAVING COUNT(name) >= 15
```

  
14.List the films released in the year 1978 ordered by the number of actors in the cast, then by title.

```sql
SELECT title,COUNT(actorid)
FROM movie
JOIN casting
ON id = casting.movieid
WHERE yr = 1978
GROUP BY title
ORDER BY COUNT(actorid) DESC ,title
```

  
15.List all the people who have worked with 'Art Garfunkel'.

```sql
SELECT name
FROM actor
JOIN casting
ON id = actorid AND actorid != (SELECT id FROM actor WHERE name = 'Art Garfunkel')
WHERE movieid in (
SELECT movieid
FROM movie
JOIN casting
ON movie.id = casting.movieid
WHERE actorid = (SELECT id FROM actor WHERE name = 'Art Garfunkel'))


```





