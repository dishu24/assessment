from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from base.models import Book, Transaction
from datetime import datetime
from datetime import date

# Create your views here.

def home(request):
    if request.method =='POST':
        book_name = request.POST['book_name']
        category = request.POST['category']
        rent_per_day = request.POST['rent_per_day']
        book = Book(book_name=book_name, category=category, rent_per_day=rent_per_day)
        book.save()
        return redirect('home')
    books = Book.objects.all()
    return render(request,'home.html',{'books':books})

def transactionrecord(request,id):
    books = Book.objects.get(pk=id)
    rent = int(books.rent_per_day)
    # print(type(rent))

    total_amount=0

    if request.method =='POST':
        person_name = request.POST['person_name']
        book = request.POST['book']
        issued_date = request.POST['issued_date']
        return_date = request.POST['return_date']
        # print(person_name,issued_date,book,return_date)
        print(issued_date)

        # date convert
        if return_date != '':

            ymd_date_1 = (issued_date)
            ymd_date_2 = (return_date)
            # Creates actual date objects from our string values.
            date_1 = date.fromisoformat(ymd_date_1)
            date_2 = date.fromisoformat(ymd_date_2)
            diff = abs(date_1 - date_2).days

            total_amount = rent * diff
        else:
            return_date = None
        trans = Transaction(person_name=person_name,book=Book.objects.get(pk=id,book_name=book), issued_date=issued_date,return_date=return_date,total_rent=total_amount)
        print(trans)
        trans.save()
        # return redirect('alltransaction')
        
    return render(request,'transaction.html',{'books':books})
    
def alltransactions(request):
    transactions = Transaction.objects.all()

    if request.method == "GET":
        person_name = request.GET.get('person_name')
        book = request.GET.get('book')
        issued_date_to = request.GET.get('issued_date_to')
        issued_date_end = request.GET.get('issued_date_end')
        
        if person_name != '':
            form = Transaction.objects.filter(person_name=person_name)
        
        if book != '':
            form = Transaction.objects.filter(book__book_name=book,)
        
        if issued_date_to != None or issued_date_end != None:
            form = Transaction.objects.filter(issued_date__gte=issued_date_to , issued_date__lte=issued_date_end)


    return render(request,'alltransaction.html',{'transactions':transactions,'form':form})
    
def searchbook(request):
    books = Book.objects.all()
    
    if request.method == "GET":
        book_name = request.GET.get('book_name')
        category = request.GET.get('category')
        rent = request.GET.get('rent_per_book')
        min_rent = request.GET.get('min_range')
        max_rent = request.GET.get('max_range')
        # print(min_rent)
        if book_name !="":
            forms = Book.objects.filter(book_name=book_name)
        if rent !="":
            forms = Book.objects.filter(rent_per_day = rent)
        if category != "":
            forms = Book.objects.filter(category=category)
        if (min_rent != None) or (max_rent != None):
            forms = Book.objects.filter(rent_per_day__gte=min_rent , rent_per_day__lte=max_rent)
            
    return render(request,'searchbook.html',{'forms':forms})

def updateTransaction(request,id):
    obj = Transaction.objects.get(pk=id)
    book_issued_date = str(obj.issued_date)
    total_amount=0
    if request.method =='POST':
        person_name = request.POST['person_name']
        book_id = request.POST['book_id']
        book = request.POST['book']
        issued_date = book_issued_date
        return_date = request.POST['return_date']
        
        books = Book.objects.get(pk=id)
        rent = int(books.rent_per_day)
        # date convert        
        if return_date != '':
            ymd_date_1 = (issued_date)
            ymd_date_2 = (return_date)
            # Creates actual date objects from our string values.
            date_1 = date.fromisoformat(ymd_date_1)
            date_2 = date.fromisoformat(ymd_date_2)
            diff = abs(date_1 - date_2).days
            total_amount = rent * diff
        else:
            return_date = None
        trans = Transaction(pk=obj.id,person_name=person_name,book=Book.objects.get(pk=book_id,book_name=book), issued_date=issued_date,return_date=return_date,total_rent=total_amount)
        print(trans)
        trans.save()
        return redirect('alltransactions')
    return render(request,'updatetransaction.html',{'obj':obj})