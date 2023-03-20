from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("formPost.html")
  
@app.route('/login',methods = ['POST'])
def login():
  Username = request.form['Username']
  password = request.form['password']
  if Username == "admin" and password == "xxx123##":
    return render_template("login.html", Username=Username)
  else:
    return render_template("errore.html", password=password)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)