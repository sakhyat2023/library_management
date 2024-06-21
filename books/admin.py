from django.contrib import admin
from .models import BooksModel, ReviewModel

# Register your models here.
admin.site.register(BooksModel)
admin.site.register(ReviewModel)