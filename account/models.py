from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.


class User(AbstractUser):
    pic = models.ImageField(blank=True, default="ava.png")
    bio = models.TextField(max_length=300, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    REQUIRED_FIELDS = ['email', 'fist_name', 'last_name']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        slug_str = "%s-%s" % (self.get_full_name(), self.id)
        self.set_slug(slugify(slug_str))
        # self.pic = make_thumbnail(self.pic, size=(200, 200))
        super().save(*args, **kwargs)

    def set_pic(self, pic):
        self.pic = pic

    def get_pic(self):
        return self.pic

    def set_bio(self, bio):
        self.bio = bio

    def get_bio(self):
        return self.bio

    def set_slug(self, slug):
        self.slug = slug

    def get_slug(self):
        return self.slug
