#!/usr/bin/env python3
import psycopg2


def queries_SQL(question_num, query):
    db = psycopg2.connect(dbname="news")  # , user="postgres", password="1234"
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    if question_num == 1:
        print("\n\n1. What are the most popular three articles of all time?")
        for result in results:
            print("{}".format(result[0]), "{}".format(result[1]), " views")
    elif question_num == 2:
        print("\n\n2. Who are the most popular article authors of all time?")
        for result in results:
            print("{}".format(result[0]), "{}".format(result[1]), " views")
    elif question_num == 3:
        print('\n\n')
        print("3. On which days did more than 1% of requests lead to errors?")
        for result in results:
            print("{}".format(result[1]), "{}".format(result[0]), "% errors")
    else:
        print("Wrong question no. please revise your code. ")
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
    SELECT authors.name, AuthorsVa.views,
    SUM(views) AS totalviews
    FROM AuthorsVa, authors
    WHERE AuthorsVa.author=authors.id
    GROUP BY AuthorsVa.author, authors.id, authors.name,
    AuthorsVa.views
    ORDER BY totalviews DESC;
    '''


query_3 = '''
    CREATE VIEW fratedays AS
    SELECT DATE(time) AS days, status,
    COUNT(*) * 100 / SUM(COUNT(*)) OVER() AS frate
    FROM log WHERE status != '200 OK' AND DATE(time) = DATE(time)
    GROUP BY status, DATE(time) ORDER BY frate;
    SELECT ROUND(frate, 2), days FROM fratedays
    WHERE frate >= 1 ORDER BY frate DESC;
    '''

if __name__ == '__main__':
    # code goes here
    queries_SQL(1, query_1)
    queries_SQL(2, query_2)
    queries_SQL(3, query_3)

else:
    print('Import')
