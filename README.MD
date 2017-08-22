# Udacity_FSND_Project3  - **LOGS ANALYSIS POSTGRESQL QUERY PROJECT** by Jason M. Hester
==============================

## Required Libraries and Dependencies
-----------------------------------
This program runs on Python 3 and requires a working Linux Virtual Server with PostgreSQL 9.6 or later installed locally.
        (see: https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
This program also requires the newsdata.sql file to be stored under the /vagrant directory.
        (see: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## How to Run Project
------------------
1. Download the newsdata.sql library, unzip, and install in a folder of your choosing under the /vagrant directory.
2. Download the "Logs_Analysis.py" file to the same vagrant folder which houses your newsdata.sql file.
3. Open a Terminal and run the following commands:
        vagrant ssh
        cd vagrant/<your chosen folder>
        psql -d news -f newsdata.sql
        python3 Logs_Analysis.py

## Description
-----------
This program uses python to run a set of postgreSQL queries which answer the following questions:
        1. What are the most popular three articles of all time?
        2. Who are the most popular article authors of all time?
        3. On which days did more than 1% of requests lead to errors?
This programs outputs the answers in a Terminal in plain text fromat.

### Accessibility
-------------
While this back-end program outputs plain text which is inherently accessible, care must be taken to ensure further formatting on the front-end remains accessible and usable by persons with disabilities using assistive technologies such as screen-readers.
