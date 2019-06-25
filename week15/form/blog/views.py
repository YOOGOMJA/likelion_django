from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator

# 블로그 포스트 불러오기 
from .form import BlogPost


# Create your views here.

def home(request):
    blogs=Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'home.html', {'blogs':blogs, 'posts':posts})

def detail(request,blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'details':details})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))


def blogpost(request):
    
    if request.method == "POST" :
        # 1. 입력된 내용을 처리하는 기능 
        form = BlogPost(request.POST)
        if form.is_valid():
            # 1.1. 입력된 내용이 모두 올바른 경우 
            # 모델객체를 가져오되 저장은 아직 하지 않음
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            # 데이터 처리가 모두 끝났으니 홈으로 리다이렉트
            return redirect('home')
    else :
        # 2. 빈 페이지를 띄워주는 기능
        form = BlogPost()
        return render(request , 'new.form.html' , { 'form' : form })

