from django.contrib import admin
from .models import Category, Article

# Register your models here.


           
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ["category"]
    readonly_fields = ["slug"]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","parent_category"]
    list_filter = ["parent_category"]
    readonly_fields = ["slug"]
    
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
    



