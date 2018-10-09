from django.shortcuts import render, redirect
from post.models import Post
from math import ceil

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
    if request.method =='POST':
        # 找到需要修改的那一条数据
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)
        # 修改内容并保存
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)# 把id传到read
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(pk=post_id)
        return render(request, 'edit_post.html', {'post': post})


def read_post(request):
    # 拿到刚刚传过来的id
    post_id = int(request.GET.get('post_id'))
    # 拿到库中的对象id
    post = Post.objects.get(pk=post_id)
    return render(request, 'read_post.html', {'post': post})


def delete_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(pk=post_id).delete()
    return redirect('/')


def post_list(request):
    page = int(request.GET.get('page', 1))  # 当前页码
    total = Post.objects.count()         # 文章总数
    per_page = 10                        # 每页帖子数
    pages = ceil(total / per_page)       # 总页数

    start = (page - 1) * per_page        # 当前页开始的索引
    end = start + per_page               # 当前页结束的索引
    # 拿到全部
    posts = Post.objects.all()[start:end]
    return render(request, 'post_list.html', {'posts': posts, 'pages': range(pages)})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})

