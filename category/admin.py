from django.contrib import admin
from .models import CategoryModel

# Register your models here.
class AdminCategoryModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "slug"]
    
admin.site.register(CategoryModel, AdminCategoryModel)