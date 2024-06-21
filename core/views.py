from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from books.models import BooksModel
from category.models import CategoryModel
from books.forms import UserCommentFrom
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

# Create your views here.
class HomeTemplateView(TemplateView):
    model = BooksModel
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("cta_name")
        if category_slug:
            category = CategoryModel.objects.get(slug=category_slug)
            context["books"] = BooksModel.objects.filter(category=category)
        else:
            context["books"] = BooksModel.objects.all()
        context["categories"] = CategoryModel.objects.all()
        return context
    
class BookDetailsView(LoginRequiredMixin, FormMixin, DetailView):
    model = BooksModel
    form_class = UserCommentFrom
    template_name = "book_details.html"
    pk_url_kwarg = "book_id"
    context_object_name = "book"
    
    def get_success_url(self):
        return reverse_lazy("book_details", kwargs={"book_id": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.instance.review = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    
    
    



