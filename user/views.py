from django.shortcuts import render,redirect
from user.forms import RegisterForm
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.i



def register(request):
    if request.method == 'POST':
        # 可以传两个  有一个特殊的上传图片，不能用POST
        form = RegisterForm(request.POST, request.FILES)
        # 如果正常保存数据 不正常报错
        if form.is_valid():
            # django封装好的方法, commit=False 先生成对象并不提交
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

            return i
        else:
            return render(request,'register.html',{'error':form.errors})
    else:
        return render(request, 'register.html')


def login(request):

    return render(request, 'login.html', {})


def logout(request):

    return redirect('/')


def user_info(request):

    return render(request, 'user_info.html', {})




