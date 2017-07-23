#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

#try:
  #conn = psycopg2.connect(database=DBNAME)
  #print("I am able to connect to the database")
#except:
    #print("I am unable to connect to the database")

def get_popular():
  #"""Return 3 most popular articles from the 'database', based on views."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select name, id from authors order by name desc;")
  return c.fetchall()
  db.close

print (get_popular())