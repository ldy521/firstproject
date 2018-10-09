from django.shortcuts import render, redirect
from post.models import Post
# Create your views here.
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 直接创建出post 保存
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%d' % post.id)# 把id传到read
    else:
        return render(request, 'create_post.html', {})


def edit_post(request):
    return render(request, 'edit_post.html', {})


def read_post(request):
    # 拿到刚刚传过来的id
    post_id = int(request.GET.get('post_id'))
    # 拿到库中的对象id
    post = Post.objects.get(pk=post_id)
    return render(request, 'read_post.html', {'post':post})


def delete_post(request):
    return render(request, 'delete_post.html', {})


def post_list(request):
    return render(request, 'post_list.html', {})


def search(request):
    return render(request, 'search.html', {})

