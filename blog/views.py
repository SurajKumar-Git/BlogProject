from django.shortcuts import render
from blog.models import Post, Category
from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from blog.forms import PostForm
from django.db.models import Q

# Create your views here.


def baseview(request):
    return render(request, "blog/blog_detail.html")


class HomeView(generic.ListView):
    model = Post
    queryset = Post.posts.published_posts()
    context_object_name = 'posts'
    template_name = "blog/index.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_post_count'] = Post.posts.published_posts().count()
        context['categories'] = Category.objects.all()
        context['popular_posts'] = Post.posts.published_posts().top_liked_post(
            3)  # Gets top 3 liked posts
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
        post = context.get("post")
        context["related_blogs"] = Post.posts.published_posts().category_posts(
            post.get_category().get_slug()).exclude(id=post.id)[:4]
        if self.request.user.is_authenticated:
            context['is_liked'] = post.is_liked_post(self.request.user)
        context["like_count"] = post.get_post_like_count()
        context["comments"] = post.get_post_comments().order_by(
            "-date_modified")
        context["comments_count"] = post.get_post_comments_count()
        return context


class AddBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic.CreateView):
    permission_required = ('blog.add_post',)
    form_class = PostForm
    model = Post
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy('account:profile')
    extra_context = {"Add_Update": "Add Blog"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    permission_required = ('blog.change_post',)
    form_class = PostForm
    model = Post
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy('account:profile')
    extra_context = {"Add_Update": "Update Blog"}

    # Update should not be accessible by other authors
    def test_func(self):
        return self.request.user == Post.objects.get(slug=self.kwargs["slug"]).author


class DeleteBlogPost(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    permission_required = ('blog.delete_post',)
    model = Post
    success_url = reverse_lazy('account:profile')
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


# To show blogs to author, both draft and published
class AuthorBlogsDetailView(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, mixins.UserPassesTestMixin, BlogDetailView):
    permission_required = ('blog.view_post',)
    queryset = None

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def test_func(self):
        return self.request.user == Post.objects.get(slug=self.kwargs["slug"]).author


class SearchBlogs(HomeView):
    def get_queryset(self):
        search = self.request.GET.get("query")
        return Post.objects.filter(
            Q(status="P"),
            Q(title__icontains=search) | Q(content__icontains=search)
        )
