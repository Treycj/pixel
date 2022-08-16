from multiprocessing import context
from django.http.response import JsonResponse

from django.shortcuts import render

from rest_framework import viewsets,status
from pixel.models import Admin, Cart, Content_owner, Customer, Orders, Payment, Payment_Details, Product, User
from pixel.serializers import AdminSerializer, CartSerializer, Content_ownerSerializer, CustomerSerializer, OrdersSerializer, Payment_DetailsSerializer, PaymentSerializer, ProductSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer

class Content_ownerViewSet(viewsets.ModelViewSet):
   queryset = Content_owner.objects.all()
   serializer_class = Content_ownerSerializer

class AdminViewSet(viewsets.ModelViewSet):
   queryset = Admin.objects.all()
   serializer_class = AdminSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
   queryset = Cart.objects.all()
   serializer_class = CartSerializer

class OrdersViewSet(viewsets.ModelViewSet):
   queryset = Orders.objects.all()
   serializer_class = OrdersSerializer

class PaymentViewSet(viewsets.ModelViewSet):
   queryset = Payment.objects.all()
   serializer_class = PaymentSerializer

class Payment_DetailsViewSet(viewsets.ModelViewSet):
   queryset = Payment_Details.objects.all()
   serializer_class = Payment_DetailsSerializer

