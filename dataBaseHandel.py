from flaskext.mysql import MySQL




class DBHelp():
	mysql = MySQL()
	app = "" 
	def __init__(self ,app , user , password , host , db ):
		self.app = app

		self.app.config['MYSQL_DATABASE_USER'] = user 
		self.app.config['MYSQL_DATABASE_PASSWORD'] = password
		self.app.config['MYSQL_DATABASE_HOST'] = host
		self.app.config['MYSQL_DATABASE_DB'] = db
		self.app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor'
		self.mysql.init_app(self.app)
		print('DONE!')  
###################SELECT####################
	def select(self ,TBName , whatToSelect , condetion , valueOfCondetion ):

		comm = self.mysql.connect()
		cur = comm.cursor()
		payload = "SELECT "+ whatToSelect + " from "+ TBName+ " WHERE " + condetion + " = " + str(valueOfCondetion)
		print(payload)
		x = cur.execute(payload)

		return x 
#********************noWhere****************#
	def selectNoWhere(self ,TBName , whatToSelect):
		comm = self.mysql.connect()
		cur = comm.cursor()
		payload = "SELECT "+ whatToSelect + " from "+ TBName 
		
		x = cur.execute(payload)

################creatTable###################		
	def creatTable(self ,name, PassHash , E_mail , Phone ):
        
		comm = self.mysql.connect()
		cur = comm.cursor() 

	#creat admins table
		cur.execute("CREATE TABLE IF NOT EXISTS `Admins` (`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT, `name` VARCHAR(20), `PassHash` VARCHAR(33), `E_Mail` VARCHAR(50),`Phone` VARCHAR(13));")
        
		admin_found = self.select("Admins" , "*" , "id" , 1)
		if not admin_found :
 		#set default admin account 
			self.Insertuser('Admins' ,  name , PassHash , E_mail , Phone )
			

		return 'TaBLE created'

    #incert data
	def Insertuser(self , tbName , name , PassHash , E_Mail , Phone ):
		comm = self.mysql.connect()
		cur = comm.cursor()
		
		payload = "INSERT INTO Admins (name , PassHash , E_Mail , Phone ) VALUES ('"+name+"','"+PassHash+"','"+E_Mail+"','"+str(Phone)+"')"
        
		cur.execute(payload)
		comm.commit()
		return "incertDONE!!"

 #   def updateTable()
