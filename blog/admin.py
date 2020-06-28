from django.contrib import admin
from blog.models import Category, Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
