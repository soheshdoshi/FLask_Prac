from flask import Flask, render_template, request, json
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
   return render_template('signup.html')

@app.route('/userRegistration', methods=['POST'])
def signUp():
   _firstname=request.form['firstname']
   _lastname=request.form['lastname']
   _email=request.form['email']
   _gender=request.form['gender']
   _city=request.form['city']
   Add_User_Dat(_firstname,_lastname,_email,_gender,_city)
   return render_template('login.html')


def Add_User_Dat(firstname,lastname,email,gender,city):
    con=sql.connect('static/user.db')
    create_user_table="""CREATE TABLE IF NOT EXISTS user(
        id integer primary key AUTOINCREMENT,
        firstname text,
        lastname text,
        email text,
        gender text,
        city text
    );
    """
    with con:
        cur=con.cursor()
        cur.execute(create_user_table)
        cur.execute("insert into user(firstname,lastname,email,gender,city) values (?,?,?,?,?)",(firstname,lastname,email,gender,city))
        con.commit()
        print("recoed add")
    con.close()

if __name__ == "__main__":
    app.run(debug=True)
