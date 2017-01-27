from flask import Flask, request, render_template
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)

#specify app configurations for database 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'blogs'
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
		username = request.form('inputEmail')
		password = request.form('inputPassword')

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

	except Exception as e:
		return "User does not exist - please try again!"

if __name__ == "__main__":
	app.run()