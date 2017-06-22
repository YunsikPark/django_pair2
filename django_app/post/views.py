from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .form import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        post.delete()
    return redirect('post_list')


def post_modify(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'post_modify.html', context)


def post_create(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)
