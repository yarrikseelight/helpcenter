from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from .models import Article, Category, Subcategory
from django.shortcuts import get_object_or_404

# Create your views here.


class HelpcenterView(View):
    def get(self, request):
        form = SearchForm()
        categories = Category.objects.all
        return render(request, "helpcenterapp/helpcenter.html", {"form":form, "categories":categories})
    
       
class ArticlesView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        subcategories = category.subcategories.all()
        return render(request, "helpcenterapp/articles.html", {"category" : category, "subcategories":subcategories})
       
    
class ArticleView(View):
    def get(self, request, slug, slug2):
        article = get_object_or_404(Article, slug=slug2)  
        subcategory = article.subcategory 
        category = subcategory.category 
        return render(request, "helpcenterapp/article.html", {
            "article": article,
            "category": category,
            "subcategory": subcategory  
        })
    
    