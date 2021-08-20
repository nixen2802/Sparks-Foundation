from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('transactions/', views.transactions, name='transactions'),
    path('transfers/', views.transfers, name='transfers'),
    path('transfers/<int:pk>/', views.transfer_detail, name='transfer_detail'),
    path('tran/',views.transfers, name='transfers')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)