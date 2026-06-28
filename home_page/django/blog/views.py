from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import PostStream, BlogPost
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "This is a test page. It is not meant to be used in production."
    )


def all_stream(
    request: HttpRequest, start: int = 0, count: int | None = None
) -> HttpResponse:
    end = start + count if count is not None else None
    posts = BlogPost.objects.all()[start:end].values(
        "slug", "title", "description", "updated_at"
    )
    return JsonResponse(list(posts), safe=False, encoder=DjangoJSONEncoder)


def stream(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post_stream = PostStream.objects.get(slug=slug)
    except PostStream.DoesNotExist:
        return JsonResponse({"error": "Post stream not found."}, status=404)

    start: int = int(request.GET.get("start", 0))
    count_str: str | None = request.GET.get("count")
    count: int | None = int(count_str) if count_str is not None else None

    end = start + count if count is not None else None

    posts = post_stream.posts.all()[start:end].values(
        "slug", "title", "description", "updated_at"
    )
    return JsonResponse(list(posts), safe=False, encoder=DjangoJSONEncoder)


def post(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return HttpResponseNotFound("Post not found.")

    context = {
        "title": post.title,
        "description": post.description,
        "content": post.content,
        "created_at": post.created_at.date(),
        "tags": post.poststream_set.values_list("title", flat=True),  # pyright: ignore[reportAttributeAccessIssue]
    }

    if post.created_at.date() != post.updated_at.date():
        context["updated_at"] = post.updated_at.date()

    return render(
        request,
        "Blog Post.html",
        context,
    )
