from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} > {self.name}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="articles", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    video_url = models.URLField(null=True, blank=True, help_text="Make sure to use the embed link!")  

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
        self.slug = slugify(self.question)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
