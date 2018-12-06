
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

CREATE VIEW fratedays AS 
SELECT DATE(time) AS days, status, COUNT(*) AS alllogs 
FROM log WHERE  DATE(time) = DATE(time) 
GROUP BY status, DATE(time); 