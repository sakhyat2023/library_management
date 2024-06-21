from django.db import models
from django.contrib.auth.models import User
from category.models import CategoryModel


# Create your models here.
class BooksModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    borrowing_price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="books"
    )
    is_borrow_book = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title
    
class ReviewModel(models.Model):
    review = models.ForeignKey(
        BooksModel, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.review.title)
