from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name