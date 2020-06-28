from django.urls import path
from blog.views import baseview, HomeView, BlogFilterByCategory, BlogDetailView, AddBlogPost, UpdateBlogPost, DeleteBlogPost, AuthorBlogsDetailView

app_name = "blog"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<slug:slug>", BlogFilterByCategory.as_view(),
         name="category_filter"),
    path("blog/add", AddBlogPost.as_view(), name="add_blog_post"),
    path("blog/<slug:slug>", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<slug:slug>/update",
         UpdateBlogPost.as_view(), name="update_blog_post"),
    path("blog/<slug:slug>/delete",
         DeleteBlogPost.as_view(), name="delete_blog_post"),
    path("blog/<slug:slug>/view", AuthorBlogsDetailView.as_view(),
         name="view_author_blog_detail"),
]
