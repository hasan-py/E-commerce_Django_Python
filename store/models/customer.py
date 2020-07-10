from django.db import models
from .category import Category

class Customer(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=15)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.name


	@staticmethod
	def emailExits(userEmail):
		try:
			email = Customer.objects.get(email=userEmail)
			return email
		except:
			return False
