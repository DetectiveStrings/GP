from flask import request

class Tasks():
	def __init__(self):
		x= 1 

		
	def sginInData(self , request):

		user = request.args.get('username' , default = '*' ,type = str) 
		PassHash = request.args.get('password' , default = '*'  , type = str)
		E_Mail = request.args.get("email", default = '*'  , type = str)
		Phone = request.args.get("phone" ,  default = '*'  , type = int)

		return user , PassHash , E_Mail , Phone


	def IsMobileUser(self , request ):
		agent = request.headers.get('User-Agent')

		is_suported = (agent.lower()).index("android")
		return is_suported 

