from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [('D', 'Draft'), ('P', 'Published')]

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=statuses, default='D')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories")
    image = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
