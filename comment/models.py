from django.db import models
from django.conf import settings
from blog.models import Post
# Create your models here.


class CommentQuerySet(models.QuerySet):

    def post_comments(self, post_id):
        return self.filter(post__id=post_id)


class Comment(models.Model):

    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    comments = CommentQuerySet.as_manager()

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_post(self, post):
        self.post = post

    def get_post(self):
        return self.post

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def __str__(self):
        return self.message
