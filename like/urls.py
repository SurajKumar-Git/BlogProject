from django.urls import path
from like.views import like_post

app_name = "like"
urlpatterns = [
    path("<int:post_id>/", like_post, name="like_post")
]
