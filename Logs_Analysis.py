#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

def get_popular():
  #"""Return 3 most popular articles from the 'database', based on views."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(*) as views from articles, log where log.path like concat('%',articles.slug,'%') group by title order by views desc limit 3; ")
  row = c.fetchall()
  print("\n3 Most Popular Articles")
  for i in row:
    print("\nArticle: {:} \nViews: {:}" .format(i[0], i[1]))
  db.close

if __name__ == "__main__":
    get_popular()