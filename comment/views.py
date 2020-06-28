from django.shortcuts import render, get_object_or_404
from blog.models import Post
from comment.models import Comment
from django.views.generic import FormView
from comment.forms import CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.set_post(post)
        comment_form.instance.set_user(request.user)
        comment_form.save()
    else:
        comment_form = CommentForm()
    comments = post.get_post_comments().order_by('-date_modified')
    comments_count = post.get_post_comments_count()
    context = {
        'post': post,
        "comments": comments
    }

    if request.is_ajax():
        form_html = render_to_string("comment/comments.html",
                                     context, request=request)
        return JsonResponse({"form": form_html, 'comments_count': comments_count})
