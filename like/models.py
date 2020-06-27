from django.db import models
from blog.models import Post
from django.conf import settings
# Create your models here.


class LikeQuerySet(models.QuerySet):

    def post_like_count(self, post_id):
        return self.filter(post__id=post_id).count()


class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    objects = models.Manager()
    likes = LikeQuerySet.as_manager()

    def set_post(self, post):
        self.post = post

    def get_post(self):
        return self.post

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def __str__(self):
        return f"{self.post} {self.user}"
