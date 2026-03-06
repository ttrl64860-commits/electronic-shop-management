from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model with Role
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    min_stock = models.IntegerField()

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Invoice Model
class Invoice(models.Model):

    PAYMENT_METHOD = (
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('card', 'Card')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    status = models.CharField(max_length=50, default='paid')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id}"


# Invoice Items (Products inside invoice)
class InvoiceItem(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
      
    
