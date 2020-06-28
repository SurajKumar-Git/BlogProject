from django.shortcuts import render
from blog.models import Post, Category
from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from blog.forms import PostForm

# Create your views here.


def baseview(request):
    return render(request, "blog/blog_detail.html")


class HomeView(generic.ListView):
    model = Post
    queryset = Post.posts.published_posts()
    context_object_name = 'posts'
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class BlogFilterByCategory(HomeView):

    def get_queryset(self):
        return Post.posts.published_posts().category_posts(self.kwargs['slug'])


class BlogDetailView(generic.DetailView):
    model = Post
    queryset = Post.posts.published_posts()
    context_object_name = 'post'
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AddBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = ('blog.add_post',)
    form_class = PostForm
    model = Post
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy('blog:home')
    extra_context = {"Add_Update": "Add Blog"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    permission_required = ('blog.change_post',)
    form_class = PostForm
    model = Post
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy('blog:home')
    extra_context = {"Add_Update": "Update Blog"}

    # Update should not be accessible by other authors
    def test_func(self):
        return self.request.user == Post.objects.get(slug=self.kwargs["slug"]).author


class DeleteBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    permission_required = ('blog.delete_post',)
    model = Post
    success_url = reverse_lazy('blog:home')
    template_name = "blog/delete_blog_post.html"
    context_object_name = "post"

    def test_func(self):
        return self.request.user == Post.objects.get(slug=self.kwargs["slug"]).author


class AuthorBlogs(generic.ListView):
    model = Post
    context_object_name = 'author_posts'
    template_name = None

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)  # Modify query set


class AuthorBlogsPublished(generic.ListView):
    model = Post
    context_object_name = 'published_author_posts'

    def get_queryset(self):
        # Modify query set
        return super().get_queryset().filter(author__slug=self.kwargs["slug"], status="P")
