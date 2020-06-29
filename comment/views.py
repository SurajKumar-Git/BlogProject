from django.shortcuts import render, get_object_or_404
from blog.models import Post
from comment.models import Comment
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from comment.forms import CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# Create your views here.


class PostCommentCreateView(CreateView):
    model = Comment
    fields = ['message']

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.set_post(post)
        form.instance.set_user(self.request.user)
        self.object = form.save()
        comments_count = post.get_post_comments_count()
        if self.request.is_ajax():
            context = {'comment': self.object}
            comment_html = render_to_string("comment/comment.html",
                                            context, request=self.request)
            return JsonResponse({"comment_html": comment_html, "comments_count": comments_count}, status=200)


class PostCommentUpdateView(UpdateView):
    model = Comment
    fields = ['message']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        comment_form_html = render_to_string("comment/comment_form.html",
                                             context, request=self.request)
        return JsonResponse({"comment_form_html": comment_form_html}, status=200)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        self.object = form.save()
        if self.request.is_ajax():
            context = {'comment': self.object}
            comment_html = render_to_string("comment/update_comment.html",
                                            context, request=self.request)
            return JsonResponse({"comment_html": comment_html}, status=200)


class PostCommentDeleteView(DeleteView):
    model = Comment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object.get_post()
        self.object.delete()
        comments_count = post.get_post_comments_count()
        if self.request.is_ajax():
            return JsonResponse({"comments_count": comments_count}, status=200)
