from django.urls import path
from comment.views import PostCommentCreateView, PostCommentUpdateView, PostCommentDeleteView

app_name = "comment"
urlpatterns = [
    path("post/<int:post_id>/", PostCommentCreateView.as_view(), name="post_comments"),
    path("<int:pk>/edit/",
         PostCommentUpdateView.as_view(), name="comment_edit"),
    path("<int:pk>/delete/", PostCommentDeleteView.as_view(), name="comment_delete")

]
