from django import template
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
	keys = cart.keys()
	for id in keys:
		if int(id) == product.id:
			return True
	return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
	keys = cart.keys()
	for id in keys:
		if int(id) == product.id:
			return cart.get(id)
	return 0

@register.filter(name='price_subtotal')
def price_subtotal(product,cart):
	keys = cart.keys()
	for id in keys:
		if int(id) == product.id:
			return int(cart.get(id))*product.price

@register.filter(name='price_total')
def price_total(products,cart):
	total = 0
	for p in products:
		total += price_subtotal(p,cart)

	return total

@register.filter(name="currency")
def currency(number):
	return "৳"+str(number)


@register.filter(name="multipy")
def multipy(num,num2):
	return num*num2
