from django.urls import path
from blog.views import baseview, HomeView, BlogFilterByCategory, BlogDetailView

app_name = "blog"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<slug:slug>", BlogFilterByCategory.as_view(),
         name="category_filter"),
    path("blog/<slug:slug>", BlogDetailView.as_view(), name="blog_detail"),
]
