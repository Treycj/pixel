
from rest_framework import serializers

from pixel.models import Admin, Cart, Content_owner, Customer, Orders, Payment, Product, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','birth_year','role')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user_name','user')

class Content_ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content_owner
        fields = ('user_name','user')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('user_name','user')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','image','isSelected')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('quantity','total_price','product')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_date','order_time','users')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('mode_of_payment','payment_date','payment_time','details')

class Payment_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('user','payment','telephone_number','card_number')