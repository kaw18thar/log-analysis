# sql-log-analysis
## How to run this file:
in your vagrant terminal type `python loganalysis.py` and you should see the output of these three SQL queries run against the news database:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 
## Views created to handle the database:
* `AuthorsVa`: this view summs the number of views for each article belongs to every author the news database have. We make use of this view to sum all the views for all articles that are written by each author.
* `fratedays`: this view sums the failure rates of each day alone( i.e. how many http requests did not get the '200 OK' success response.
## Special thanks to the writer of this Stack Overflow answer:
[How to calculate percentage with a SQL statement](https://stackoverflow.com/a/772439)
