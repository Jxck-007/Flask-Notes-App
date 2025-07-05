from flask import Flask, request, jsonify,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Notesdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class  Notes (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    content=db.Column(db.String(200),default=0)
    date_time=db.Column(db.DateTime,default=datetime.utcnow)



@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        ntitle=request.form['title']
        ncontent=request.form['content']
        new_note=Notes(title=ntitle,content=ncontent)
        try:
            db.session.add(new_note)
            db.session.commit()
            notes=Notes.query.order_by(Notes.date_time).all()
            return render_template('index.html',notes=notes)
        except:
            return "A Error Occured"
    return render_template('index.html')
@app.route('/notes/<int:id>',methods=['DELETE'])
def delete_note(id):
    note_to_delete=Notes.query.get_or_404(id)
    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'An Error Occured While Deteling your note'
    
@app.route('/notes/<int:id>',methods=["PUT"])
def update_note(id):
    title=request.json['title']
    content=request.json['content']
    note_to_update=Notes.query.get_or_404(id)
    note_to_update.title=title
    note_to_update.content= content
    db.session.commit()
    return"Updated Successfully"

@app.route('/welcome/<user>')
def welcome(user):
    return(f"Welcome To The Notes App {user}")


if __name__=='__main__':
    app.run(debug=True)