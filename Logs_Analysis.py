#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def get_pop_art():
    # Return 3 most popular articles from the 'database', based on views.
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT title, count(*) AS views FROM articles, log
                 WHERE log.path LIKE concat('%',articles.slug)
                 GROUP BY title ORDER BY views DESC LIMIT 3;''')
    row = c.fetchall()
    print("\n3 Most Popular Articles")
    for i in row:
        print("\nArticle: {:} \nViews: {:}" .format(i[0], i[1]))
    db.close


def get_pop_auth():
    # Return 3 most popular authors from the 'database',
    # based on total articles views.
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT authors.name, count(*) AS views
                 FROM authors, articles, log
                 WHERE authors.id = articles.author AND log.path
                 LIKE concat('%',articles.slug)
                 GROUP BY authors.name ORDER BY views DESC;''')
    row = c.fetchall()
    print("\nMost Popular Authors")
    for i in row:
        print("\nAuthor: {:} \nViews: {:}" .format(i[0], i[1]))
    db.close


def get_error_days():
    # Return days where greater than 1% of errors occurred.
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''WITH error_count AS (
                 SELECT date(time), count(status) AS total
                 FROM log WHERE status NOT LIKE '200%'
                 GROUP BY date(time)
                 ),
                 status_total AS (SELECT date(time), count(status) AS total
                 FROM log
                 GROUP BY date(time)
                 ),
                 combined_percent AS (SELECT error_count.date
                 AS error_date, error_count.total * 100.0/ status_total.total
                 AS percentage
                 FROM error_count, status_total
                 WHERE error_count.date = status_total.date
                 GROUP BY error_count.date, percentage
                 )
                 SELECT to_char(error_date, 'Month, DD, YYYY')
                 AS error_day, to_char(percentage,  '999.99%')
                 AS error_percent
                 FROM combined_percent WHERE percentage > 1;''')
    row = c.fetchall()
    print("\nDays with > 1% errors")
    for i in row:
        print("\nDate {:} \nPercentage: {:}" .format(i[0], i[1]))
    db.close

if __name__ == "__main__":
    get_pop_art()
    get_pop_auth()
    get_error_days()
