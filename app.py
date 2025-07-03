from flask import Flask, request, jsonify,render_template
 
app=Flask(__name__)

notes=[]

@app.route('/')
@app.route('/frontend')
def frontend():
    return render_template('index.html')

@app.route('/notes',methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes',methods=['POST'])
def add_notes():
    data=request.json
    notes.append(data)
    return jsonify(data),201



if __name__=='__main__':
    app.run(debug=True)