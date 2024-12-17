from django.db import models

class DimCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField()

class DimWallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(DimCustomer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField()

class DimTransactionType(models.Model):
    transaction_type_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=50)

class DimTime(models.Model):
    date_key = models.DateField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    quarter = models.IntegerField()
    weekday = models.IntegerField()

class FactTransactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField()
    customer = models.ForeignKey(DimCustomer, on_delete=models.CASCADE)
    wallet = models.ForeignKey(DimWallet, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
