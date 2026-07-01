from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.db import models
from .models import BlogPost, PostStream
from personal_site.form_tools.rich_text import RichTextWidget


class PostStreamAdminForm(forms.ModelForm):
    posts = forms.ModelMultipleChoiceField(
        queryset=BlogPost.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("posts", is_stacked=False),
    )

    class Meta:
        model = PostStream
        fields = "__all__"


@admin.register(PostStream)
class PostStreamAdmin(admin.ModelAdmin):
    form = PostStreamAdminForm
    prepopulated_fields = {"slug": ("title",)}


class BlogPostAdminForm(forms.ModelForm):
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3, "style": "width: 100%;"}),
    )
    post_streams = forms.ModelMultipleChoiceField(
        queryset=PostStream.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("post streams", is_stacked=False),
    )

    class Meta:
        model = BlogPost
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["post_streams"].initial = self.instance.poststream_set.all()
        elif not self.is_bound:
            max_sort_order = (
                BlogPost.objects.aggregate(models.Max("sort_order"))["sort_order__max"]
                or 0
            )
            self.fields["sort_order"].initial = max_sort_order + 1


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = (
        "title",
        "sort_order",
        "created_at",
        "updated_at",
    )
    list_editable = ("sort_order",)
    ordering = ("sort_order", "-updated_at")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {
            "widget": RichTextWidget(attrs={"editor_height": "90vh"}),
        }
    }

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        post_streams = form.cleaned_data.get("post_streams")
        if post_streams is not None:
            form.instance.poststream_set.set(post_streams)

    class Media:
        js = ("/static/app.min.js",)
        css = {
            "all": ["https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css"],
        }
