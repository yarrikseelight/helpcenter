from django.contrib import admin
from .models import Category, Subcategory, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "subcategory", "video_url"]
    list_filter = ["subcategory"]
    readonly_fields = ["slug"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ["slug"]

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]
    readonly_fields = ["slug"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)
