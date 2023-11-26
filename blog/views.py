from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import generic
from django.views.decorators.csrf import requires_csrf_token
from .models import Post
from . import models
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def mypost(request):
    posts = Post.objects.filter(author = request.user)
    return render(request , "mypost.html" , {'posts':posts})

def signout(request):
    logout(request)
    return redirect('/')

def newpost(request):
    if request.method=="POST":
        # author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('desc')
        slug= request.POST.get('slug')
        slug=request.POST.get('slug').strip()
        # date = request.POST.get('date')
        # en = Post(author=request.user , title=title , desc=desc , date=date)
        en = models.Post(title=title , content = content ,author = request.user,slug=slug)
        en.save()
        return redirect("/home")
    return render(request , "create_post.html")

@requires_csrf_token
def loginn(request):
    if request.method=="POST":
        uname = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(username=uname , password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            return redirect("/")
    return render(request , "login.html")

@requires_csrf_token
def signup(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = User.objects.create_user(username=name , email=email , password=password)
        newuser.save()
        return redirect("/")
    return render(request , "signup.html")