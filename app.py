from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sc.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Sc(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Sc(title=title, desc= desc)
        db.session.add(todo)
        db.session.commit()
    
    alltodo = Sc.query.all()
    return render_template('index.html', alltodo=alltodo)

# @app.route('/show')
# def product():
#     alltodo = Sc.query.all()
#     print(alltodo)
#     return 'proddd'

@app.route('/update/<int:sno>' , methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Sc.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/') 
        
    todo = Sc.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)
    db.session.delete(alltodo)
    db.session.commit()
    return redirect("/")

@app.route('/delete/<int:sno>')
def delete(sno):
    alltodo = Sc.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,port=8000)