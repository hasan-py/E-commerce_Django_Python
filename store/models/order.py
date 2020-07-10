from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	date = models.DateField(default=datetime.datetime.today)
	address = models.CharField(max_length=255,blank=True)
	phone = models.CharField(max_length=15,blank=True)
	completed = models.BooleanField(default=False)

	
	def __str__(self):
		return self.customer.email