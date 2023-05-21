from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    slug  = models.SlugField(max_length=100, unique=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories')

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
