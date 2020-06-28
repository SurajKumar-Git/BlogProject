from django import forms
from blog.models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.text import slugify


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "description", "content",
                  "status", "category", "image"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', "rows": "4"}),
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '700px'}}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'author': forms.Select(attrs={"display": "hidden"})
        }
        help_texts = {
            "image": "Image size should be less than 1 MB"
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not self.initial:
            slug = slugify(title)
            if Post.objects.filter(slug=slug).exists():
                raise forms.ValidationError(
                    "Title already exists", code="Invalid")
        return title

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > (1048576):  # 1 MB
            raise forms.ValidationError("Image size greater than 1 MB")
        return image
