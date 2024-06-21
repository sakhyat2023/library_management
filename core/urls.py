from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path(
        "category/<slug:cta_name>", views.HomeTemplateView.as_view(), name="book_list"
    ),
    path("book/<int:book_id>", views.BookDetailsView.as_view(), name="book_details")
]
