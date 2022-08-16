from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False,max_length=50)
    password = models.CharField(max_length=50)
    birth_year = models.DateField()
    role = models.CharField(max_length=100,blank=True)


class Customer(models.Model):
    user_name = models.CharField(max_length=30,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Content_owner(models.Model):
    user_name = models.CharField(max_length=30,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    user_name = models.CharField(max_length=30,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    isSelected = models.BooleanField(null=True)

class Cart(models.Model):
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Orders(models.Model):
    order_date = models.DateField()
    order_time = models.TimeField()
    users = models.ManyToManyField(User)

class Payment(models.Model):
    mode_of_payment = models.CharField(max_length= 100)
    payment_date = models.DateField()
    payment_time = models.TimeField()
    details = models.ManyToManyField(User, through='Payment_Details')

class Payment_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    telephone_number = models.IntegerField()
    card_number = models.CharField(blank= True,max_length= 30)









