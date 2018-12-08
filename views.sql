
CREATE view AuthorsVa AS 
SELECT articles.author, articles.title, COUNT(*) AS views 
FROM log, articles WHERE articles.slug = SUBSTRING(log.path FROM 10) AND  articles.author =  articles.author
GROUP BY log.path, articles.title, articles.author ORDER BY views; 

CREATE VIEW totals AS
SELECT authors.name AS name, AuthorsVa.author,
SUM(views) AS totalviews
FROM AuthorsVa, authors
WHERE AuthorsVa.author=authors.id
GROUP BY authors.name, AuthorsVa.author
ORDER BY totalviews DESC;


CREATE VIEW ratio AS
SELECT to_char(time, 'Month dd, yyyy') as day,
status, count(*) AS sumstatus
FROM log
WHERE to_char(time, 'Month dd, yyyy') = to_char(time, 'Month dd, yyyy')
GROUP BY to_char(time, 'Month dd, yyyy'), status;

CREATE VIEW errorlogs as
SELECT  SUM(sumstatus) AS alllogs, day FROM ratio
WHERE day = day group by  ratio.day ;

