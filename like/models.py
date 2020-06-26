from django.db import models
from blog.models import Post
from django.conf import settings
# Create your models here.


class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
