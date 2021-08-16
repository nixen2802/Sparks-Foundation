from django import forms
from .models import Transactions

class TransferForm(forms.ModelForm):
    class Meta:
        model=Transactions
        fields=['sender_name', 'recipient_name', 'amount', 'status', 'date_of_transfer']
