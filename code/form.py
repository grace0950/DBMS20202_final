from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
import sys
import psycopg2
from flask import request



#def getmovie():
 #   mm = request.form.get('m_name')
  #  return mm
#def movie_name():
#    IN = sys.argv
#    IN1 = str(IN[1])
#    conn = psycopg2.connect(database="DBMS_movie", user="postgres", password=IN1, host="127.0.0.1", port="5432")
#    cur = conn.cursor()
#    sql = "SELECT DISTINCT movie_name FROM movie_type"
#    cur.execute(sql)
#    u = cur.fetchall()
#    conn.close()
#    return u
#
#MV = []
#for x in movie_name():
#    MV.append((x, x[0]))
#
#print(getmovie())


MV = []
class FormRegister(Form):
    """依照Model來建置相對應的Form
    password2: 用來確認兩次的密碼輸入相同
    """
    c_name = StringField('UserName', validators=[
        validators.DataRequired(),
    ])
    c_phone = StringField('Phone', validators=[
        validators.DataRequired(),
    ])
    c_id = PasswordField('ID', validators=[
        validators.DataRequired(),
        validators.Length(5, 12),
        validators.EqualTo('c_id2', message='ID NEED MATCH')
    ])
    c_id2 = PasswordField('Confirm ID', validators=[
        validators.DataRequired()
    ])
    c_list = StringField('list',default = '0', validators=[
        validators.DataRequired(),
    ])
    m_type = SelectField('MovieType', default = '0',validators=[
    ])
    m_name = SelectField('MovieName',  validators=[
    ])
    m_theater = StringField('theaterName', validators=[
        validators.DataRequired(),
    ])
    m_day = StringField('Day', validators=[
        validators.DataRequired(),
    ])
    m_time = StringField('Time', validators=[
        validators.DataRequired(),
    ])
    m_row = StringField('ROW', validators=[
        validators.DataRequired(),
    ])
    m_column = StringField('COLUMN', validators=[
        validators.DataRequired(),
    ])
    submit = SubmitField('Register New Account')
    def __init__(self):
        form = self
        super(FormRegister, self).__init__()
        self.m_type.choices = self._movie_type()
        self.m_name.choices = self._movie_name()
        #ee = request.form.get('m_name')
        #print(ee)
    def _movie_name(self):
        IN = sys.argv
        IN1 = str(IN[1])
        conn = psycopg2.connect(database="DBMS_movie", user="postgres", password=IN1, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        sql = "SELECT DISTINCT movie_name FROM movie_type"
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        MV = []
        for x in u:
            MV.append((x,x[0]))
        return MV

    def _movie_type(self):
        IN = sys.argv
        IN1 = str(IN[1])
        conn = psycopg2.connect(database="DBMS_movie", user="postgres", password=IN1, host="127.0.0.1", port="5432")
        cur = conn.cursor()
        sql = "SELECT DISTINCT type_name FROM movie_type"
        cur.execute(sql)
        t = cur.fetchall()
        conn.close()
        MT = []
        for x in t:
            MT.append((x, x[0]))
        return MT
