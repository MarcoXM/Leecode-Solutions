# Window functions



General Elections were held in the UK in 2015 and 2017. Every citizen votes in a **constituency**. The candidate who gains the most votes becomes MP for that constituency.

All these results are recorded in a table **ge**

| yr | firstName | lastName | constituency | party | votes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2015 | Ian | Murray | S14000024 | Labour | 19293 |
| 2015 | Neil | Hay | S14000024 | Scottish National Party | 16656 |
| 2015 | Miles | Briggs | S14000024 | Conservative | 8626 |
| 2015 | Phyl | Meyer | S14000024 | Green | 2090 |
| 2015 | Pramod | Subbaraman | S14000024 | Liberal Democrat | 1823 |
| 2015 | Paul | Marshall | S14000024 | UK Independence Party | 601 |
| 2015 | Colin | Fox | S14000024 | Scottish Socialist Party | 197 |
| 2017 | Ian | MURRAY | S14000024 | Labour | 26269 |
| 2017 | Jim | EADIE | S14000024 | SNP | 10755 |
| 2017 | Stephanie Jane Harley | SMITH | S14000024 | Conservative | 9428 |
| 2017 | Alan Christopher | BEAL | S14000024 | Liberal Democrats | 1388 |

### Contents

* [1Warming up](https://sqlzoo.net/wiki/Window_functions#Warming_up)
* [2Who won?](https://sqlzoo.net/wiki/Window_functions#Who_won.3F)
* [3PARTITION BY](https://sqlzoo.net/wiki/Window_functions#PARTITION_BY)
* [4Edinburgh Constituency](https://sqlzoo.net/wiki/Window_functions#Edinburgh_Constituency)
* [5Winners Only](https://sqlzoo.net/wiki/Window_functions#Winners_Only)
* [6Scottish seats](https://sqlzoo.net/wiki/Window_functions#Scottish_seats)



  
1.Show the **lastName**, **party** and **votes** for the **constituency** 'S14000024' in 2017.

```sql
SELECT lastName, party, votes
  FROM ge
 WHERE constituency = 'S14000024' AND yr = 2017
ORDER BY votes DESC
```

2.You can use the RANK function to see the order of the candidates. If you RANK using \(ORDER BY votes DESC\) then the candidate with the most votes has rank 1.Show the party and RANK for constituency S14000024 in 2017. List the output by party

```sql
SELECT party, votes, --- rank 是个class
       RANK() OVER (ORDER BY votes DESC) as posn
  FROM ge
 WHERE constituency = 'S14000024' AND yr = 2017
ORDER BY party
```

































