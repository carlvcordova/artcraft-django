from django.db import models
from django.db.models.fields import AutoField, IntegerField

# Create your models here.


class Artist(models.Model):
    artistID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Artwork(models.Model):
    artworkID = models.AutoField(primary_key=True)
    year = models.DateField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    orderPrice = models.IntegerField() # there will be a shipping fee teehee
    orderDate = models.DateField(max_length=20)
    artworkID = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
