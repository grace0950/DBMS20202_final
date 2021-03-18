from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(db_path)
db = SQLAlchemy(app)


class ExamData(db.Model):
    tablename = 'ExamData'
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer)
    model_Name = db.Column(db.String(255))
    value_without = db.Column(db.Float)
    time = db.Column(db.Float)


@app.route('/', methods=['GET', 'POST'])
def all_persons():
    EID = db.session.query(ExamData.eid).distinct()  # 取得所有EID
    model_Name = db.session.query(ExamData.model_Name).distinct()  # 取得所有model_Name
    if 'eid' in request.form and 'model_Name' in request.form:
        result = ExamData.query.filter_by(eid=int(request.form.get("eid")), model_Name=request.form.get("model_Name"))
        return render_template("index.html", EID=EID, model_Name=model_Name, result=result)
    return render_template("index.html", EID=EID, model_Name=model_Name)



if __name__ == '__main__':
    if not os.path.exists(db_path):
        db.create_all()
        db.session.add(ExamData(eid=50, model_Name='Multiple Regression', 
                        value_without=0.5781, time=13.03))
        db.session.add(ExamData(eid=50, model_Name='Logistic Regression',
                        value_without=0.587, time=10.93))
        db.session.add(ExamData(eid=51, model_Name='Multiple Regression',
                        value_without=0.5158, time=10.98))
        db.session.add(ExamData(eid=51, model_Name='Logistic Regression',
                        value_without=0.572, time=10.16))

        db.session.commit()

    app.run()

