from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/student', methods = ['POST', 'GET'])
def student():
    if request.method == 'POST':
        code = request.form['code']
        if code == '1':
            return render_template('qp1.html')
        else:
            return render_template('qp2.html')

@app.route('/success',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #ans1 = request.form['ans1']
      #ans2 = request.form['ans2']
      ans = request.form
      return render_template("success.html",ans = ans)

@app.route('/enternew')
def new_student():
   return render_template('student1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result1.html",msg = msg)
         con.close()

'''@app.route('/enternew')
def new_student():
   return render_template('student.html')'''

'''@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("RQP.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()'''

if __name__ == '__main__':
   app.run(debug = True)