# sql-log-analysis
## How to run this file:
### Prerequisits:
first you need to have installed [Python](https://www.python.org) and [Psycopg2 v2.7.5](http://initd.org/psycopg/download/) to deal with PostgreSQL.
1. download and install vagrant [version 1.9.5](https://releases.hashicorp.com/vagrant/1.9.5/) is the one that works without problems
2. download and install virtual box [version 5.2.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2)
3. download and install postgreSQL [version 9.5](https://www.postgresql.org/download/) 
### Instructions:
* Create an empty folder to hold your project folders and files; name this folder `log-analysis-dir`. Inside `log-analysis-dir` download the vagrant file (https://goo.gl/wLBxDA). Create another folder named `log-analysis-project` and place it next to the vagrant file inside the `log-analysis-dir` this folder will share files with the virtual machine.
* Until now, our project folder should look like this:
\ `log-analysis-dir`
  --vagrant file
  --`log-analysis-project`
* Go to `log-analysis-project` folder or `cd` to it in your terminal. Here, create the loganalysis.py file and download and unzip the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database file. Now your project folder should look like this: 
<dl>
  <code>/log-analysis-dir</code> 
 <dt> <code>//vagrant file</code> </dt> 
  <dt><code>//log-analysis-project</code></dt>
 <dd>//------ newsdata.sql </dd>
 <dd>//------ loganalysis.py </dd>
  
  

Go to `log-analysis-dir` folder and git bash there, run these commands:

- `vagrant up` and wait till the virtual machine is created. 
- Then `vagrant ssh`, which will make the terminal prompt turn into something like: `vagrant@vagrant:`.
- Then, `cd /vagrant`, which will take us to the directory shared between the virtual machine and our computer.
- Here, we use `cd log-analysis-project` command 
- use the command `psql -d news -f newsdata.sql` and then `psql -d news` to connect to the news database. Note: we can skip to the command `psql -d news` directly once we have already connected to the database.
- run these two SQL select statements necessary to run our loganalysis python app:
`    CREATE view AuthorsVa AS
    SELECT articles.author, articles.title,
    COUNT(*) AS views FROM log, articles
    WHERE articles.slug = SUBSTRING(log.path FROM 10)
    GROUP BY log.path, articles.title, articles.author
    ORDER BY views;`
and
`
    CREATE VIEW fratedays AS
    SELECT DATE(time) AS days, status,
    COUNT(*) * 100 / SUM(COUNT(*)) OVER() AS frate
    FROM log WHERE status != '200 OK' AND DATE(time) = DATE(time)
    GROUP BY status, DATE(time) ORDER BY frate;`
    now we can see that there are two views created by vagrant in our terminal:
    `
      news=> \dv
                List of relations
       Schema |   Name    | Type |  Owner
      --------+-----------+------+---------
       public | authorsva | view | vagrant
       public | fratedays | view | vagrant
      (2 rows)
       `
- Now run our python file which contains our code using `python loganalysis.py`
- We should see the output of these three SQL queries run against the news database:
    1. What are the most popular three articles of all time? 
    2. Who are the most popular article authors of all time? 
    3. On which days did more than 1% of requests lead to errors? 
 
 
 
## Views created to handle the database:
* `AuthorsVa`: this view summs the number of views for each article belongs to every author the news database have. We make use of this view to sum all the views for all articles that are written by each author.
* `fratedays`: this view sums the failure rates of each day alone( i.e. how many http requests did not get the '200 OK' success response.


## Special thanks to the writer of this Stack Overflow answer:
[How to calculate percentage with a SQL statement](https://stackoverflow.com/a/772439)
