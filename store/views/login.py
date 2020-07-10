from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from store.models import Customer

class Login(View):
	return_url = None

	def get(self,request):
		Login.return_url = request.GET.get('return_url')
		return render(request,'login.html')

	def post(self,request):
		userData = request.POST
		customerEmail = Customer.emailExits(userData["email"])
		if customerEmail:
			if check_password(userData["password"],customerEmail.password):
				request.session["customer"] = customerEmail.id
				if Login.return_url:
					return HttpResponseRedirect(Login.return_url)
				else:
					Login.return_url = None
					return redirect('home')
			else:
				return render(request,'login.html',{"userData":userData,"error":"Email or password doesn't match"})
		else:
			return render(request,'login.html',{"userData":userData,"error":"Email or password doesn't match"})



def logout(request):
	request.session.clear()
	return redirect('home')