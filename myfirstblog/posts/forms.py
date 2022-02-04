from django import forms
from posts.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "your Title"}
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "your Body"}
            ),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "your Title"}
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "your Body"}
            ),
        }
