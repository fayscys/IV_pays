from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class MobileServiceProvider(models.Model):
    name = models.CharField(max_length=100)  
    logo = models.ImageField(upload_to='provider_logos/')  

    def __str__(self):
        return self.name

class MobileTopUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(MobileServiceProvider, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.provider.name} - {self.phone_number}"

class BillCategory(models.Model):
    name = models.CharField(max_length=100)  # Name of the bill category (e.g., "Electricity")

    def __str__(self):
        return self.name

class BillPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.due_date}"

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class MoneyTransfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transfers')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} sent {self.amount} to {self.recipient.name}"


class PaymentCategory(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

class FrequentPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(PaymentCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    next_payment_date = models.DateField()
    frequency = models.CharField(max_length=20, choices=[("monthly", "Monthly"), ("quarterly", "Quarterly"), ("annually", "Annually")])

    def __str__(self):
        return f"{self.user.username} - {self.category.name}"


