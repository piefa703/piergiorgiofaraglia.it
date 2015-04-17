Title: Come scrivere il risultato di una query su file csv
Slug: come-scrivere-risultato-query-su-file-csv
Lang: it
Date: 2015-04-17 15:00
Modified: 2015-04-17 15:00
Category: mysql
Tags: howto,query,csv,sql
Authors: Piergiorgio Faraglia
Summary: Comandi per scrivere direttamente su csv il risultato di una query sql

Sarà capitato a tutti di dover eseguire una query sql da riga di comando e
dover mostrare il risultato della query su un file csv (che con estrema
facilità può essere aperto con programmi quali LibreOffice).

Il file csv potrà essere creato da un terminal bash o dalla console di mysql.

## Creazione da terminale

Eseguire il seguente comando:

    mysql -u YOUR_USERNAME -p YOUR_DB -B -e "YOUR_QUERY" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g'

al posto dei placeholder mettere il proprio username, db, e query nell'ordine.

## Creazione da console mysql

Per creare un file csv dalla console di mysql eseguire:

    mysql -u YOUR_USER -p YOUR_DATABASE
    SELECT * INTO OUTFILE 'YOUR_CSV_ABS_PATH' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '\\' LINES TERMINATED BY '\n' FROM table WHERE 1
