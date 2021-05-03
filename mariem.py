from flask import Flask ,render_template, request, url_for , redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:mariem123@localhost/form'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://bzlfelvdwcgaby:86c3ecfc7379ca196aa4954d3f5c943be26cb629a0aa04745cafb2c206db30fb@ec2-52-44-31-100.compute-1.amazonaws.com:5432/d785e2cdg9eu6j'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db =SQLAlchemy(app)

class favquotes(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    author =db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result= favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/a',methods=['POST','GET'])
def after():
    if request.method =='POST' :
        a = request.form['author']
        q = request.form['quote']
        quotedata = favquotes(author=a , quote=q)
        db.session.add(quotedata)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method=='GET' :
        return render_template('after.html')






@app.route('/<m>' , methods=['GET','POST'])
def before(m):
    if request.method=='POST' :
        return render_template('before.html')
    else :
        return render_template('before.html')
