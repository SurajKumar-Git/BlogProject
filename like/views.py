from django.shortcuts import render, get_object_or_404
from blog.models import Post
from like.models import Like
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_like = post.get_post_like(request.user)
    if post_like:
        post_like.delete()
        is_liked = False
    else:
        Like.objects.create(post=post, user=request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'like_count': post.get_post_like_count()
    }
    if request.is_ajax():
        form_html = render_to_string("like/like_section.html",
                                     context, request=request)
        return JsonResponse({"form": form_html})
