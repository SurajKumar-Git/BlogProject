from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models import Count

# Create your models here.


class CategoryQuerySet(models.QuerySet):

    def get_posts_count(self, category_id):
        return self.get(id=category_id).post_category.filter(status="P").count()


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    # Model Monagers
    objects = models.Manager()
    categories = CategoryQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_slug(self, slug):
        self.slug = slug

    def get_slug(self):
        return self.slug

    def __str__(self):
        return self.name

    def get_no_of_posts(self):
        return Category.categories.get_posts_count(self.id)


class PostQuerySet(models.QuerySet):  # Custom Model Manager

    def published_posts(self):
        return self.filter(status="P")

    def draft_posts(self):
        return self.filter(status="D")

    def author_posts(self, author_id):
        return self.filter(author__id=author_id)

    def category_posts(self, category_slug):
        return self.filter(category__slug=category_slug)

    def top_liked_post(self, top):
        return self.annotate(like_count=Count('post_likes')).order_by("-like_count")[:top]


class Post(models.Model):
    statuses = [('D', 'Draft'), ('P', 'Published')]

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=statuses, default='D')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post_category")
    image = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Model Monagers
    objects = models.Manager()
    posts = PostQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.set_slug(slugify(self.title))
        super().save(*args, **kwargs)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def set_status(self, status):
        if status in ("D", "P"):
            self.status = status
        else:
            raise ValueError    # Need to Add more info on setters

    def get_status(self):
        return self.status

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def set_slug(self, slug):
        self.slug = slug

    def get_slug(self):
        return self.slug

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def __str__(self):
        return self.title

    def get_post_like_count(self):
        return self.post_likes.all().count()
        # return Like.likes.get_post_like_count(self.id)

    def get_post_comments(self):
        return self.post_comments.all()

    def get_post_comments_count(self):
        return self.get_post_comments().count()

    def get_post_like(self, user):
        return self.post_likes.filter(user=user)

    def is_liked_post(self, user):
        return self.get_post_like(user).exists()
