from django.shortcuts import render,redirect
from django.http import HttpResponse
from bank.models import Customer,Transactions
from bank.forms import TransferForm
import datetime
from collections import OrderedDict

def home(request):
    return render(request, 'bank/home.html', {'nbar':'home'})

def customers(request):
    customers_info=Customer.objects.all()
    return render(request, 'bank/customers_view.html', {'nbar':'customers_page', 'customers': customers_info})

def transactions(request):
    transactions_info=reversed(Transactions.objects.all())
    return render(request, 'bank/transactions_view.html', {'nbar':'transactions_page', 'transactions': transactions_info})

def transfers(request):
    customers=Customer.objects.all()
    transactions_info=Transactions.objects.all()
    if(request.method=='POST'):
        if(request.POST.get('sender')=='Select Customer' or request.POST.get('receiver')=='Select Customer'):
            return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': "not selected customer"})
        elif(request.POST.get('sender')==request.POST.get('receiver')):
            return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': "same selected customer"})
        else:
            trans_insert=Transactions()
            flag=0
            for c in customers:
                if(c.cust_id==int(request.POST.get('sender'))):
                    trans_insert.sender_name=c.cust_name
                    if(c.balance<float(request.POST.get('amount'))):
                        flag=1
                if(c.cust_id==int(request.POST.get('receiver'))):
                    trans_insert.recipient_name=c.cust_name
            if(flag==0):
                trans_insert.amount=request.POST.get('amount')
                if(float(request.POST.get('amount'))<0):
                    trans_insert.amount=request.POST.get('amount')
                    trans_insert.status="Failure"
                    trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                    trans_insert.save()
                    return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': "negative balance"})
                else:
                    trans_insert.status="Success"
                    trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                    deduction=Customer.objects.get(cust_id=request.POST.get('sender'))
                    deduction.balance=deduction.balance-float(request.POST.get('amount'))
                    credetion=Customer.objects.get(cust_id=request.POST.get('receiver'))
                    credetion.balance=credetion.balance+float(request.POST.get('amount'))
                    deduction.save()
                    credetion.save()
                    trans_insert.save()
                    return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': "Success"})
            else:
                trans_insert.amount=request.POST.get('amount')
                trans_insert.status="Failure"
                trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                trans_insert.save()
                return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': "insufficient balance"})
    else:
        return render(request, 'bank/transfers_view.html', {'nbar':'transfers_page', 'customers': customers, 'message': ""})

def customer_detail(request, pk):
    single_customer = Customer.objects.get(cust_id=pk)
    return render(request, 'bank/single_customers_view.html',{'nbar':'customers_page', 'single_customer': single_customer})

def transfer_detail(request, pk):
    single_customer = Customer.objects.get(cust_id=pk)
    customers=Customer.objects.all()
    transactions_info=Transactions.objects.all()
    if(request.method=='POST'):
        if(request.POST.get('sender')=='Select Customer' or request.POST.get('receiver')=='Select Customer'):
            return render(request, 'bank/money_transfer_view.html',{'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': "not selected customer"})
        elif(request.POST.get('sender')==request.POST.get('receiver')):
             return render(request, 'bank/money_transfer_view.html',{'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': "same selected customer"})
        else:
            trans_insert=Transactions()
            flag=0
            for c in customers:
                if(c.cust_id==int(request.POST.get('sender'))):
                    trans_insert.sender_name=c.cust_name
                    if(c.balance<float(request.POST.get('amount'))):
                        flag=1
                if(c.cust_id==int(request.POST.get('receiver'))):
                    trans_insert.recipient_name=c.cust_name
            if(flag==0):
                if(float(request.POST.get('amount'))<0):
                    trans_insert.amount=request.POST.get('amount')
                    trans_insert.status="Failure"
                    trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                    trans_insert.save()
                    return render(request, 'bank/money_transfer_view.html', {'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': "negative balance"})
                else:
                    trans_insert.amount=request.POST.get('amount')
                    trans_insert.status="Success"
                    trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                    deduction=Customer.objects.get(cust_id=int(request.POST.get('sender')))
                    deduction.balance=deduction.balance-float(request.POST.get('amount'))
                    credetion=Customer.objects.get(cust_id=int(request.POST.get('receiver')))
                    credetion.balance=credetion.balance+float(request.POST.get('amount'))
                    deduction.save()
                    credetion.save()
                    trans_insert.save()
                    return render(request, 'bank/money_transfer_view.html', {'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': "Success"})
            else:
                trans_insert.amount=request.POST.get('amount')
                trans_insert.status="Failure"
                trans_insert.date_of_transfer= datetime.datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
                trans_insert.save()
                return render(request, 'bank/money_transfer_view.html', {'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': "insufficient balance"})
    else:
        return render(request, 'bank/money_transfer_view.html',{'nbar':'transfers_page', 'single_customer': single_customer, 'customers': customers, 'message': ""})
    

