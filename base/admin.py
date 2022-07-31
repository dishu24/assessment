from django.contrib import admin

from base.models import Book, Transaction


class BookDataForm(admin.ModelAdmin):
    list_display = ['id','book_name','category','rent_per_day']
    list_filter = ['category']
    search_fields = ['book_name','category','rent_per_day']

admin.site.register(Book,BookDataForm)
admin.site.register(Transaction)
