from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models import Customer

class Signup(View):

	def get(self,request):
		return render(request,'signup.html')
			
	def post(self,request):
		userData = request.POST
		# validate
		error = self.validateData(userData)
		if error :
			return render(request,'signup.html',{"error":error,"userData":userData})
		else:
			if Customer.emailExits(userData['email']):
				error["emailExits_error"] = "Email Already Exits"
				return render(request,'signup.html',{"error":error,"userData":userData})
			else:
				customer = Customer(
					name=userData['name'],
					email=userData['email'],
					phone=userData['phone'],
					password=make_password(userData['password']),
				)
				customer.save()
				return redirect('home')

	# Validate form method
	def validateData(self,userData):
		error = {}
		if not userData['name'] or not userData['email']  or not userData['phone']  or not userData['password'] or not userData['confirm_password']:
			error["field_error"] = "All field must be required"
		elif len(userData['password'])<8 and len(userData['confirm_password'])<8 :
			error['minPass_error'] = "Password must be 8 char"
		elif len(userData['name']) > 25 or len(userData['name']) < 3 :
			error["name_error"] = "Name must be 3-25 charecter"
		elif len(userData['phone']) != 11:
			error["phoneNumber_error"] = "Phone number must be 11 charecter."
		elif userData['password'] != userData['confirm_password']:
			error["notMatch_error"] = "Password doesn't match"	

		return error

	