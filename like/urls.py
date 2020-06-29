from django.urls import path
from like.views import LikePost

app_name = "like"
urlpatterns = [
    path("<int:post_id>/", LikePost.as_view(), name="like_post")
]
