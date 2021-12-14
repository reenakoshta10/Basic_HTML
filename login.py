from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def home():
  return render_template("login.html")

@app.route("/home", methods=['GET','POST'])
def login():
  if request.method == 'POST':
    user_name = request.form["uname"]
    password = request.form['password']
  else:
    user_name = request.args.get('uname')
    password = request.args.get('password')
  return render_template("home.html", user_name=user_name)

if __name__=='__main__':
  app.run()