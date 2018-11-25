import psycopg2


def queries_SQL(question_num, query):
    db = psycopg2.connect(dbname="news")  # , user="postgres", password="1234"
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    print("The solution for question number ", question_num, " is: ")
    for result in results:
        print("{}".format(result[0]), "{}".format(result[1]))
    db.close()


query_1 = '''
    SELECT  articles.title, COUNT(*) AS views FROM log, articles
    WHERE articles.slug=SUBSTRING(log.path FROM 10)
    GROUP BY log.path,  articles.title
    ORDER BY views DESC LIMIT 3;
    '''


query_2 = '''
    CREATE view AuthorsVa AS
    SELECT articles.author, articles.title,
    COUNT(*) AS views FROM log, articles
    WHERE articles.slug = SUBSTRING(log.path FROM 10)
    GROUP BY log.path, articles.title, articles.author
    ORDER BY views;
    SELECT authors.name, AuthorsVa.author,
    SUM(views) AS totalviews
    FROM AuthorsVa, authors
    WHERE AuthorsVa.author=authors.id
    GROUP BY AuthorsVa.author, authors.id, authors.name
    ORDER BY totalviews DESC;
    '''


query_3 = '''
    CREATE VIEW fratedays AS
    SELECT DATE(time) AS days, status,
    COUNT(*) * 100 / SUM(COUNT(*)) OVER() AS frate
    FROM log WHERE status != '200 OK'
    GROUP BY status, DATE(time) ORDER BY frate;
    SELECT frate, days FROM fratedays
    WHERE frate >= 1 ORDER BY frate DESC;
    '''


queries_SQL(1, query_1)
queries_SQL(2, query_2)
queries_SQL(3, query_3)
