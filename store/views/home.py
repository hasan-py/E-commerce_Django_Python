from django.shortcuts import render,redirect
from django.views import View
from store.models import Product
from store.models import Category

class Home(View):

	def get(self,request):
		cart = request.session.get('cart')
		categories = Category.getAllCategory()
		products = Product.getAllProduct().order_by('-id')

		if request.GET.get('id'):
			filterProductById = Product.objects.get(id=int(request.GET.get('id')))
			return render(request, 'productDetail.html',{"product":filterProductById,"categories":categories})

		if not cart:
			request.session['cart'] = {}

		if request.GET.get('category_id'):
			filterProduct = Product.getProductByFilter(request.GET['category_id'])
			return render(request, 'home.html',{"products":filterProduct,"categories":categories})

		return render(request, 'home.html',{"products":products,"categories":categories})

	def post(self,request):
		product = request.POST.get('product')

		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		print(cart)
		request.session['cart'] = cart
		return redirect('cart')