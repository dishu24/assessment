from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/issued/<str:id>/', views.transactionrecord, name='transactionrecord'),
    path('books/all/transactions/', views.alltransactions, name='alltransactions'),
    path('search/books/', views.searchbook, name='searchbook'),
    path('books/transaction/update/<str:id>/', views.updateTransaction, name='updatetransaction'),
]
