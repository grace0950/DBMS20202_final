# main.py
from flask import Flask, render_template, request, redirect, url_for,jsonify
#from view_form import UserForm
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from form import FormRegister
import os
import sys
from form2 import FormDelete

app = Flask(__name__)

def get_env_variable(name):
     try:
         return os.environ[name]
     except KeyError:
         message = "Expected environment variable '{}' not set.".format(name)
         raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")
postgresurl = POSTGRES_URL.split(":")
POSTGRES_HOST = postgresurl[0]
POSTGRES_PORT = postgresurl[1]

DB_URL = 'postgresql+psycopg2:///{user}:{pw}@{url}/{db}'.format(user = POSTGRES_USER,
                                                                pw = POSTGRES_PW,
                                                                url = POSTGRES_URL,
                                                                db = POSTGRES_DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

bootstrap = Bootstrap(app)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

conn = psycopg2.connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PW,
                        host=POSTGRES_HOST,
                        port=POSTGRES_PORT)

def inserttable(c_name, c_phone, c_id, c_list, m_name, m_theater, m_day, m_time, m_row, m_column):
    #sql_cmd = "INSERT INTO %s (id, name, model,doors) VALUES (%d,%s,%s,%d)" % (table_name, ID, name, model, doors)

    sql_cmd = "INSERT INTO customer (c_name,c_phone,c_id,c_list,m_name,m_theater,m_day,m_time,m_row,m_column) VALUES (%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)" % (c_name, c_phone, c_id, c_list, m_name, m_theater, m_day, m_time, m_row, m_column)
    #sql_cmd = "INSERT INTO cars (id, name, model,doors) VALUES (191912,'bmw','car',4)"
    return sql_cmd


#c_name, c_phone, c_id, c_list, m_name, m_theater, m_day, m_time, m_row, m_column
@app.route('/', methods=['GET', 'POST'])
def index():
    #if form.validate_on_submit():
    # print(f"state = {}")
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def BO():
    return render_template('testbooking.html')

@app.route('/superbooking/<moviename>/<movietheater>/<day>/<time>',methods=['GET', 'POST'])
def SUPER(moviename, movietheater, day, time):

    day = day[0:2] + '/' + day[2:]
    if request.method == 'POST':
        totle = int(request.values['adults']) + int(request.values['children'])
        conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
        cur = conn.cursor()


        sql = 'select s_column,s_row from seat where m_name = %r and t_name = %r and day = %r and s_time = %r and has_someone = false order by s_column,s_row' % (moviename, movietheater, day, time)


        cur.execute(sql)
        u = cur.fetchall()
        print(f"len = {len(u)}")
        if len(u) < totle:
            return render_template('fail.html')
        x = 0
        #print(f"{moviename} {movietheater} {day} {time} {request.values['username']}
        #{request.values['userphone']} {request.values['userid']} {request.values['adults']} {request.values['children']}")
        for i in u:
            if x < totle:
                print(f"seat = {i[0]} {i[1]} x = {x}")
                sql = 'UPDATE seat SET has_someone = true WHERE m_name = %r and t_name = %r and day = %r and s_time = %r and s_column = %r and s_row = %r' % (moviename, movietheater, day, time, i[0], i[1])
                cur.execute(sql)

                hash_hash = request.form.get('userid')+moviename+movietheater+day+time+i[0]+i[1]

                sql_cmd = "INSERT INTO customer (c_name,c_phone,c_id,c_list,m_name,m_theater,m_day,m_time,m_row,m_column) VALUES (%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)" % (request.values['username'], request.values['userphone'], request.values['userid'], hash(hash_hash), moviename, movietheater, day, time, i[1], i[0])
                cur.execute(sql_cmd)
                conn.commit()
                x = x+1
            else:
                print(f"x={x}")
                break;

        conn.close()
    return render_template('success.html')

@app.route('/user/<past_val>', methods=['GET', 'POST'])
def getuserinfo(past_val):
    form = FormDelete()
    x = str(past_val)
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT c_name,c_list,m_name,m_theater,m_day,m_time,m_row,m_column FROM customer where c_id = %r" % x
    cur.execute(sql)
    u = cur.fetchall()
    if form.submit.data or form.validate_on_submit():
        ticket_id = request.form.get('c_list')
        desql = "UPDATE seat SET has_someone = false from customer where customer.c_list = %r and customer.m_name = seat.m_name and customer.m_theater = seat.t_name and customer.m_day = seat.day and customer.m_time =seat.s_time and customer.m_column  = seat.s_column and customer.m_row = seat.s_row" % ticket_id
        cur.execute(desql)
        conn.commit()
        sql="DELETE FROM customer WHERE c_list=%r" % ticket_id
        cur.execute(sql)
        sql = "SELECT c_name,c_list,m_name,m_theater,m_day,m_time,m_row,m_column FROM customer where c_id = %r" % x
        cur.execute(sql)
        u = cur.fetchall()

        conn.commit()
        conn.close()
        print(f"u = {u} id = {x}")
        return render_template('user.html',u=u,T=x, form=form)
    return render_template('user.html', u=u, T=x,form = form)


"""
@app.route('/user/<past_val>',methods = ['GET','POST'])
def getuserinfo(past_val):
    form = FormDelete()
    x = str(past_val)
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT c_name,c_list,m_name,m_theater,m_day,m_time,m_row,m_column FROM customer where c_id = %r" %x
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    print(f"u = {u}")
    print(f"past_value = {x} ")
    return render_template('user.html', u=u, T=x,form = form)
"""
@app.route('/order',methods = ['GET','POST'])
def order():
    return render_template('qwe.html')

@app.route('/index/emovion/<past_val>')
def getmovielist(past_val):
    x = str(past_val)
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT movie_name,url FROM movie_type where type_name = %r" % x
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('movie_list.html', u=u, T=x)
@app.route('/index/movieinfo/<moviename>')
def getmovieinfo(moviename):
    x = str(moviename)
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT url FROM movie_type where movie_name = %r" % x
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()

    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT distinct theater FROM movie where movie_name = %r" % x
    cur.execute(sql)
    t = cur.fetchall()
    conn.close()

    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT info FROM movie_type where movie_name = %r" % x
    cur.execute(sql)
    info = cur.fetchall()
    conn.close()
    if len(t) == 0:
        return render_template('comingsoon.html', U=u, T=x, t=(("即將上映",),), I=info)
    return render_template('movie.html', U=u, T=x, t=t, I=info)

@app.route('/index/movieinfo/<moviename>/<movietheater>')
def getmovietime(moviename, movietheater):
    x = str(moviename)
    y = str(movietheater)
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='06/27'" % (x, y)
    cur.execute(sql)
    d20 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='06/28'" % (x, y)
    cur.execute(sql)
    d21 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='06/29'" % (x, y)
    cur.execute(sql)
    d22 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='06/30'" % (x, y)
    cur.execute(sql)
    d23 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='07/01'" % (x, y)
    cur.execute(sql)
    d24 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='07/02'" % (x, y)
    cur.execute(sql)
    d25 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='07/03'" % (x, y)
    cur.execute(sql)
    d26 = cur.fetchall()
    sql = "SELECT movie_time FROM movie where movie_name = %r and theater = %r and movie_day='07/04'" % (x, y)
    cur.execute(sql)
    d27 = cur.fetchall()
    conn.close()

    return render_template('movie_time.html', d20=d20, d21=d21, d22=d22, d23=d23, d24=d24, d25=d25, d26=d26, d27=d27, T=y, N=x)

@app.route('/index/movieinfo/<moviename>/<movietheater>/<day>/<time>', methods=["GET", "POST"])
def booking(moviename, movietheater, day, time):
    return render_template('testbooking.html', m_n=moviename, m_t=movietheater, day=day, time=time)

@app.route('/excited_type')
def excited_type():
    return render_template('excited_type.html')

@app.route('/index/excited',methods = ['GET','POST'])
def index_excited():
    return render_template('excited_type.html')

@app.route('/index/boring',methods = ['GET','POST'])
def index_boring():
    return render_template('boring_type.html')

@app.route('/index/angry',methods = ['GET','POST'])
def index_angry():
    return render_template('argry_type.html')

@app.route('/index/happy',methods = ['GET','POST'])
def index_happy():
    return render_template('happy_type.html')

@app.route('/index/sad',methods = ['GET','POST'])
def index_sad():
    x ="https://github.com/smpss92118/DBMS20202_final/blob/master/data/image/Documentary.png?raw=true"
    return render_template('sad_type.html', u=x)

@app.route('/index/movie/<state>')
def index_movie(state):
    #x = "https://www.ambassador.com.tw/assets/img/movies/BLADERUNNERTHEFINALCUT_180x270_Poster.jpg"

    #x = "https://github.com/smpss92118/DBMS20202_final/blob/master/LIFEOFPI2020_180x270_Poster.jpg?raw=true"
    x = "https://github.com/SabrinaKung/DBMS20202_final/blob/master/0529-0604movie/%E4%BD%A0%E7%9A%84%E9%B3%A5%E5%85%92%E6%9C%83%E5%94%B1%E6%AD%8C.jpg?raw=true"
    return render_template('movie_info.html', u=x)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =FormRegister()
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT movie_name FROM movie_type "
    cur.execute(sql)
    movie = cur.fetchall()
    conn.close()
    movieArr = []
    for mv in movie:
        movieArr.append((mv, mv[0]))
    form.m_name.choices = movieArr

    if form.submit.data or form.validate_on_submit():
        c_name = request.form.get('c_name')
        c_phone = request.form.get('c_phone')
        c_id = request.form.get('c_id')
        c_list = request.form.get('c_list')
        m_name = request.form.get('m_name')
        print(f"mname = {m_name[2:-3]}")
        m_theater = request.form.get('m_theater')
        m_day = request.form.get('m_day')
        m_time = request.form.get('m_time')
        m_row = request.form.get('m_row')
        m_column = request.form.get('m_column')
        sql_cmd = inserttable(c_name, c_phone, c_id, c_list, m_name[2:-3], m_theater, m_day, m_time, m_row, m_column)
        query_data = db.engine.execute(sql_cmd)
        return render_template('index.html')
    return render_template('register.html', form=form)

@app.route('/movieType/<state>')
def ty_pe(state):
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    ss = str(state[2:-3])
    sql = "SELECT movie_name FROM movie_type where type_name = %r" % ss
    cur.execute(sql)
    movie = cur.fetchall()
    conn.close()
    movieArr = []
    for mv in movie:
        mobj = {}
        mobj['id'] = mv
        mobj['name'] = mv[0]
        movieArr.append(mobj)
    return jsonify({'movie': movieArr})
"""
@app.route('/user', methods=['GET', 'POST'])
def user():
    form =FormDelete()
    if form.submit.data or form.validate_on_submit():
        conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
        cur = conn.cursor()
        ticket_id = request.form.get('c_list')
        print(f"id={ticket_id}")

        sql = "DELETE FROM customer WHERE c_list=%r" % ticket_id
        #sql = "DELETE FROM customer WHERE c_list='987654321'"
        cur.execute(sql)
        conn.commit()
        conn.close()
    return render_template('user.html', form=form)
"""

@app.route('/movie_type')
def type():
    conn = psycopg2.connect(database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PW, host=POSTGRES_HOST, port=POSTGRES_PORT)
    cur = conn.cursor()
    sql = "SELECT * FROM movie_type"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('movie_type.html', u=u)


if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = '123123'
    app.run()
