from django.urls import path
from .views import Home,Signup,Login,logout,Cart,Checkout,OrderView
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
]
