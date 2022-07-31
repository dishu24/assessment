from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=150,null=False, blank=False )
    rent_per_day = models.CharField(max_length=150,null=False, blank=False )

    def __str__(self):
        return self.book_name

class Transaction(models.Model):
    person_name = models.CharField(max_length=150,null=True, blank=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=False, auto_now_add=False, null=True,blank=True)
    return_date = models.DateField(auto_now=False, auto_now_add=False, null=True,blank=True)
    total_rent = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return f'Book : ({self.book}) , person : {self.person_name} , issue date : {self.issued_date}'