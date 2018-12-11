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
            print("{article} -- {views1} views"
                  .format(article=result[0], views1=result[1]))
    elif question_num == 2:
        print("\n\n2. Who are the most popular article authors of all time?")
        for result in results:
            print("{author} -- {views2} views"
                  .format(author=result[0], views2=result[1]))
    elif question_num == 3:
        print('\n\n')
        print("3. On which days did more than 1% of requests lead to errors?")
        for result in results:
            print("on {day} there was {errors} % errors"
                  .format(day=result[1], errors=result[0]))
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
    SELECT name, totalviews from totals;
    '''

query3_extra = '''
    SELECT ROUND((ratio.sumstatus * 100 / errorlogs.alllogs), 2) AS errorRate,
    errorlogs.day FROM errorlogs, ratio
    WHERE ratio.day = errorlogs.day AND ratio.status != '200 OK'
    AND (ratio.sumstatus * 100 / errorlogs.alllogs) > 1;

'''

if __name__ == '__main__':
    queries_SQL(1, query_1)
    queries_SQL(2, query_2)
    queries_SQL(3, query3_extra)

else:
    print('Import')
