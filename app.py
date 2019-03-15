from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student', methods = ['POST', 'GET'])
def student():
    if request.method == 'POST':
        return render_template('qp1.html')

@app.route('/success',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("success.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)