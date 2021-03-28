# NSS Tutorial



| Field | Type |
| :--- | :--- |
| ukprn | varchar\(8\) |
| institution | varchar\(100\) |
| subject | varchar\(60\) |
| level | varchar\(50\) |
| question | varchar\(10\) |
| A\_STRONGLY\_DISAGREE | int\(11\) |
| A\_DISAGREE | int\(11\) |
| A\_NEUTRAL | int\(11\) |
| A\_AGREE | int\(11\) |
| A\_STRONGLY\_AGREE | int\(11\) |
| A\_NA | int\(11\) |
| CI\_MIN | int\(11\) |
| score | int\(11\) |
| CI\_MAX | int\(11\) |
| response | int\(11\) |
| sample | int\(11\) |
| aggregate | char\(1\) |

National Student Survey 2012

The National Student Survey [http://www.thestudentsurvey.com/](http://www.thestudentsurvey.com/) is presented to thousands of graduating students in UK Higher Education. The survey asks 22 questions, students can respond with STRONGLY DISAGREE, DISAGREE, NEUTRAL, AGREE or STRONGLY AGREE. The values in these columns represent PERCENTAGES of the total students who responded with that answer.

The table `nss` has one row per institution, subject and question.

### Contents

* [1Check out one row](https://sqlzoo.net/wiki/NSS_Tutorial#Check_out_one_row)
* [2Calculate how many agree or strongly agree](https://sqlzoo.net/wiki/NSS_Tutorial#Calculate_how_many_agree_or_strongly_agree)
* [3Unhappy Computer Students](https://sqlzoo.net/wiki/NSS_Tutorial#Unhappy_Computer_Students)
* [4More Computing or Creative Students?](https://sqlzoo.net/wiki/NSS_Tutorial#More_Computing_or_Creative_Students.3F)
* [5Strongly Agree Numbers](https://sqlzoo.net/wiki/NSS_Tutorial#Strongly_Agree_Numbers)
* [6Strongly Agree, Percentage](https://sqlzoo.net/wiki/NSS_Tutorial#Strongly_Agree.2C_Percentage)
* [7Scores for Institutions in Manchester](https://sqlzoo.net/wiki/NSS_Tutorial#Scores_for_Institutions_in_Manchester)
* [8Number of Computing Students in Manchester](https://sqlzoo.net/wiki/NSS_Tutorial#Number_of_Computing_Students_in_Manchester)





  
1.The example shows the number who responded for:

* question 1
* at 'Edinburgh Napier University'
* studying '\(8\) Computer Science'

Show the the percentage who STRONGLY AGREE

```sql
SELECT A_STRONGLY_AGREE
  FROM nss
 WHERE question='Q01'
   AND institution='Edinburgh Napier University'
   AND subject='(8) Computer Science'
```

  
2.Show the institution and subject where the **score** is at least 100 for question 15.

```sql
SELECT institution, subject
  FROM nss
 WHERE question='Q15'
   AND score >= 100;
```

3.Show the institution and score where the score for '\(8\) Computer Science' is less than 50 for question 'Q15'

```sql
SELECT institution,score
  FROM nss
 WHERE question='Q15'
   AND subject='(8) Computer Science'
   AND score < 50 
```

  
4.Show the subject and total number of students who responded to question 22 for each of the subjects '\(8\) Computer Science' and '\(H\) Creative Arts and Design'.

```sql
SELECT subject,SUM(response)
  FROM nss
 WHERE question='Q22'
GROUP BY subject
HAVING (subject='(8) Computer Science' OR subject='(H) Creative Arts and Design')
```

5.Show the subject and total number of students who A\_STRONGLY\_AGREE to question 22 for each of the subjects '\(8\) Computer Science' and '\(H\) Creative Arts and Design'.

```sql
SELECT subject, SUM(response*A_STRONGLY_AGREE/100)
FROM nss
WHERE question='Q22'
AND (subject='(8) Computer Science' 
OR subject =  '(H) Creative Arts and Design')
GROUP BY subject
```

  
6.Show the percentage of students who A\_STRONGLY\_AGREE to question 22 for the subject '\(8\) Computer Science' show the same figure for the subject '\(H\) Creative Arts and Design'.

Use the **ROUND** function to show the percentage without decimal places.

```sql
SELECT subject, ROUND(SUM(A_STRONGLY_AGREE * response) / SUM(response),0)
  FROM nss
  WHERE question='Q22'
    AND subject IN ('(8) Computer Science',
                    '(H) Creative Arts and Design')
  GROUP BY subject;
```

7.Show the average scores for question 'Q22' for each institution that include 'Manchester' in the name.

The column **score** is a percentage - you must use the method outlined above to multiply the percentage by the **response** and divide by the total response. Give your answer rounded to the nearest whole number.

```sql
SELECT institution,ROUND(SUM(score * response) / SUM(response),0)
  FROM nss
 WHERE question='Q22'
   AND (institution LIKE '%Manchester%')
GROUP BY institution
ORDER BY institution
```

8.Show the institution, the total sample size and the number of computing students for institutions in Manchester for 'Q01'.

```sql
SELECT institution,SUM(sample), 
(SELECT sample FROM nss y
WHERE subject='(8) Computer Science'
AND x.institution = y.institution
AND question='Q01')
  FROM nss x
 WHERE question='Q01'
   AND (institution LIKE '%Manchester%')
GROUP BY institution
```

