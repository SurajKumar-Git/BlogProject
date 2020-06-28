from django.urls import path
from comment.views import post_comments

app_name = "comment"
urlpatterns = [
    path("<int:post_id>/", post_comments, name="post_comments")
]
