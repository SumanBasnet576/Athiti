from Accounts.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter
from .models import Post
from django.db.models import Q
from .forms import UpdateBlogPostForm
from django.http import HttpResponse

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import CreateBlogPostForm

POSTS_PER_PAGE = 10


# Create your views here.
# web part

def home_screen_view(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, "poem/home.html", context)


def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    context['form'] = form
    return render(request, 'poem/create.html', context)


def detail_blog_view(request, slug):
    context = {}
    blog_post = get_object_or_404(Post, slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'poem/detail_post.html', context)


def delete_post(request, slug=None):
    user = request.user
    post_to_delete = Post.objects.get(slug=slug)
    if post_to_delete.author != user:
        return HttpResponse("you are not author")
    post_to_delete.delete()
    return redirect('home')


def edit_blog_view(request, slug):
    context = {}
    user = request.user
    blog_post = get_object_or_404(Post, slug=slug)
    if blog_post.author != user:
        return HttpResponse("You are not author")
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )
    context['form'] = form
    return render(request, 'poem/edit_post.html', context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(
            Q(title__contains=q) |
            Q(body__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))
