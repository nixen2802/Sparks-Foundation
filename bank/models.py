from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):   
    cust_id = models.IntegerField()
    cust_name = models.CharField(max_length=50)
    cust_email= models.CharField(max_length=50)
    balance = models.FloatField()
    class Meta:
        db_table = "customers"


class Transactions(models.Model):
    sender_name=models.CharField(max_length=50)
    recipient_name=models.CharField(max_length=50)
    amount=models.FloatField()
    status=models.CharField(max_length=25)
    date_of_transfer=models.CharField(max_length=100)
    class Meta:
        db_table = "transactions"