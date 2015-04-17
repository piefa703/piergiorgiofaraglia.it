Title: How to output query on csv
Slug: how-to-output-query-on-csv
Lang: en
Date: 2015-04-17 15:00
Modified: 2015-04-17 15:00
Category: mysql
Tags: howto,query,csv,sql
Authors: Piergiorgio Faraglia
Summary: Commands to output query directly to csv

Sometimes happen to have to perform sql query, from command line, and show
results directly on csv.

Such a file would be created both form bash command line and from mysql command
line.

## Creazion from bash command line

Execute following command:

    mysql -u YOUR_USERNAME -p YOUR_DB -B -e "YOUR_QUERY" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g'

sustitute placeholders with your username, db, and query to execute.

## Creation from mysql command line

In order to create csv from mysql console, execute:

    mysql -u YOUR_USER -p YOUR_DATABASE
    SELECT * INTO OUTFILE 'YOUR_CSV_ABS_PATH' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '\\' LINES TERMINATED BY '\n' FROM table WHERE 1
