from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'dataanalyst',
    'location':'benguluru',
    'salary':1
  },
  {
    'id':2,
  'title':'datascient',
  'location':'hyderabad',
  'salary':2
  },
  {
    'id':3,
    'title':'frontend engineer',
    'location':'delhi',
  },
  {
    'id':4,
    'title':'backende',
    'location':'up',
    'salary':4
  }

]
@app.route("/")
def helloworld():
  return render_template('home.html',jobs=JOBS)
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
    
