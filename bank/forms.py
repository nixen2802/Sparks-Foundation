from django import forms
from .models import Transactions, Customer

class TransferForm(forms.ModelForm):
    class Meta:
        model=Transactions
        fields=['sender_name', 'recipient_name', 'amount', 'status', 'date_of_transfer']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['cust_id', 'cust_name', 'cust_email', 'balance']
