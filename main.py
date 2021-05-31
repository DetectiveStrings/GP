from flask import Flask
from flask import request
import dataBaseHandel
from flaskext.mysql import MySQL
import hashlib
import sys
import tasks

app = Flask(__name__)

task = tasks.Tasks()

userDB = dataBaseHandel.DBHelp(app , 'testuser' , 'test1234', 'localhost' ,'AppTest' )

AdminPassHash = hashlib.md5((sys.argv[1]).encode()).hexdigest()
E_mail = sys.argv[2]
phone = sys.argv[3]

print(type(AdminPassHash))

#creat the db tables and default values
userDB.creatTable("test" , str(AdminPassHash) , E_mail , phone )




@app.route("/user")
def user():
	try :
		suported = task.IsMobileUser(request) 
		user , PassHash , E_Mail , Phone = task.sginInData(request) 

		submit = userDB.Insertuser("Admins" , user  ,PassHash ,E_Mail ,Phone )
		return submit 
	except:
		return "your device is not supported"
    



if __name__ == "__main__":
    # Only for debugging while developing
		app.run(host='0.0.0.0', debug=True, port=444  )
