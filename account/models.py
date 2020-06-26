from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.


class User(AbstractUser):
    pic = models.ImageField(blank=True)
    bio = models.TextField(max_length=300, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        slug_str = "%s-%s" % (self.get_full_name(), self.id)
        self.slug = slugify(slug_str)
        # self.pic = make_thumbnail(self.pic, size=(200, 200))
        super().save(*args, **kwargs)
