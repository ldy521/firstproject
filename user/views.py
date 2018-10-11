from django.shortcuts import render,redirect
from user.forms import RegisterForm
from user.models import User
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

            return redirect('/user/login/')
        else:
            return render(request,'register.html',{'error':form.errors})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname').strip()
        password = request.POST.get('password').strip()
        # 检查用户是否存在
        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error':'用户不存在'})
        # 检查密码是否正确
        if check_password(password,user.password):
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            request.session['avatar'] = user.icon.url
            return redirect('/user/info/')
        else:
            return render(request, 'login.html', {'error':'密码错误'})
    else:
        return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def user_info(request):
    uid = request.session.get('uid')
    user = User.objects.get(pk=uid)

    return render(request, 'user_info.html', {'user':user})




