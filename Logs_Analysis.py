#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

def get_pop_art():
  #Return 3 most popular articles from the 'database', based on views.
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(*) as views from articles, log where log.path like concat('%',articles.slug) group by title order by views desc limit 3; ")
  row = c.fetchall()
  print("\n3 Most Popular Articles")
  for i in row:
    print("\nArticle: {:} \nViews: {:}" .format(i[0], i[1]))
  db.close

def get_pop_auth():
  #Return 3 most popular authors from the 'database', based on total articles views.
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select authors.name, count(*) as views from authors, articles, log where authors.id = articles.author and log.path like concat('%',articles.slug) group by authors.name order by views desc;")
  row = c.fetchall()
  print("\nMost Popular Authors")
  for i in row:
    print("\nAuthor: {:} \nViews: {:}" .format(i[0], i[1]))
  db.close

def get_error_days():
  #Return days that greater than 1% of errors occurred.
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("WITH error_count as ("SELECT date(time), count(status) as total
FROM log
where status not like '200%'
group by date(time)
),
status_total as (SELECT date(time), count(status) as total
FROM log group by date(time)
)
SELECT error_count.date, (count(*) * 100 / (select count(*) FROM error_count)) as percentage FROM error_count, status_total where error_count.date = status_total.date group by error_count.date;")
  row = c.fetchall()
  print("\nDays with > 1% errors")
  for i in row:
    print("\nDate {:} \nPercentage: {:}" .format(i[0], i[1]))
  db.close

if __name__ == "__main__":
    get_pop_art()
    get_pop_auth()
    get_error_days()