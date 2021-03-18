# 電影院售票系統

這是一個利用國賓影城的電影資料所建立的電影院售票系統。售票網頁會依照用戶選擇的心情來推薦電影類型，並顯示當期電影供用戶選擇，用戶可以自由選擇觀看電影、戲院與日期時間下訂電影。除此之外，用戶還可以在訂票後還輸入用戶資訊，進行退票動作。

### Prerequisites

Postgres SQL

```
# postgres as database
apt-get install postgresql postgresql-contrib
```

Flask & Psycopg2
```
# flask as connection to postgres
pip3 install flask flask_sqlalchemy flask_migrate flask_bootstrap flask_wtf

# psycopg as python3 to postgres API
pip3 install psycopg2
```

Beautifulsoup
```
# beautifulsoup4 for getting data
pip3 install beautifulsoup4
```

### DEMO

![](demo.gif)

### Installing

If you are using OSX system, run the config bash script:
```
./mac_config.sh
```

For downloading the data from [國賓影城](https://www.ambassador.com.tw/home/MovieList?Type=1), use the bash script:
```
# ./update_no_merge [mmdd-mmdd]
# the website only have data throughout a week from now on
# the first mmdd is today and the second is one week later
./update_no_merge 0620-0627
```
It will create a folder named [mmdd-mmdd]csvs and all data inside are formatted for use.

## Deployment

For running our website, we need to make sure the database is working:
```
# run postgresql with user "postgres"
$ sudo -iu postgres

# build postgresql database with target user and database name
postgres@linux:~$ psql
postgres=# CREATE database DBMS_movie;
postgres=# \q
postgres@linux:~$ psql -U postgres -d DBMS_movie

# check user and database
DBMS_movie=# \c
You are now connected to database "DBMS_movie" as user "postgres"

# create table and load data from sql command at 'path/to/our/project/createtable.sql'
DBMS_movie=# CREATE TABLE actors(
...
);
...
DBMS_movies=# COPY actors FROM '/path/to/our/project/0620-0627csvs/actor_data0620-0627.csv' DELIMITER ',' CSV;
...

# check our database connections
$ pg_isready
/var/run/postgresql:5433 -accepting connections
$ pg_isready -h localhost -p 5433
localhost:5433 - accepting connections

# set environment variables to locate the database
$ export POSTGRES_URL="127.0.0.1:5433"
$ export POSTGRES_USER="postgres"
$ export POSTGRES_PW="dbpw"
$ export POSTGRES_DB="DB_movies"
```

After setting the database, run the python code to build the website:
```
if mac:
python main.py password_for_postgresql
if ubuntu:
$ python3 web/main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 596-310-633
```

Open the website with browser(https://127.0.0.1:5000/ in this case)

Finally Done!

## Authors 

* **資科二 秦嘉佑** - *data crawl & format, scripting, README* - [absnormal](https://github.com/absnormal)  
  **資科二 龔琳甯** - *backend & frontend*  
  **資科四 彭嵩寧** - *backend & frontend*  
  **資科二 邱品硯** - *backend & frontend*  
  **資科二 黃昱涵** - *frontend & pdf*  
**add yours profile and work part here**

See also the list of [contributors](https://github.com/SabrinaKung/DBMS20202_final/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

