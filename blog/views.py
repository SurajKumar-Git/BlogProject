from django.shortcuts import render
from blog.models import Post, Category
from django.views import generic

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
