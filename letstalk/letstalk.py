from flask import Flask, request, render_template
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)

#specify app configurations for database 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'lData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#intiialize mysql database object
mysql.init_app(app)

 
@app.route("/")
def hello():
	render_template('home.html')
	return "Welcome to your space!"
 



#Methods to sign up, sign in, and authenticate sign in
@app.route('/SignUp')
def showSignUp():
	return render_template('signup.html')


@app.route('/Signin')
def showSignin():
	return render_template('signin.html')


@app.route('/NewAccount')

def createNewAccount():
	try:
		name = request.form('inputName')
		username = request.form('inputEmail')
		password = request.form('inputPassword')
		cursor.callproc('spCreateUser',(_userEmail,_userPassword))
		data = cursor.fetchall()
	if len(data) is 0:
   		conn.commit()
   		return {'StatusCode':'200','Message': 'User creation success'}
	else:
		return {'StatusCode':'1000','Message': str(data[0])}


	except Exception as e:
		return "Username taken, please try again!"






@app.route("/Authenticate", methods = ['POST'])

#Authenticate login requests
def Authenticate():
	try:
		username = request.form('inputEmail')
		password = request.form('inputPassword')
		cursor = mysql.connect().cursor() #object to handle database communication
		cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
		data = cursor.fetchone()
		if data is None:
			return "Invalid Username/Password"
		else:
			return "login succcesful!"

	except Exception as e:
		return "User does not exist - please try again!"

if __name__ == "__main__":
	app.run()
