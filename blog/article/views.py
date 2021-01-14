from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    # return HttpResponse("Anasayfa")

    return render(request, 'index.html')
    # return render(request, 'article/index.html')
    
def about(request):
    return render(request, 'about.html')

# def detail(request,id):
#     return HttpResponse("Anasayfa" +str(id))

@login_required(login_url='user:login')   
def dashboard(request):
    articles= Article.objects.filter(author=request.user)
    context ={
        'articles':articles
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='user:login')   
def addArticle(request):
    # form = ArticleForm(request.POST or None)
    form = ArticleForm(request.POST or None, request.FILES or None)
    # print(form)
    if form.is_valid():
        article= form.save(commit=False)
        article.author= request.user
        article.save()
        
        messages.success(request, "Article is created successfully..")
        return redirect("article:dashboard")
    context= {
        'form':form
    }
    return render(request, 'addarticle.html', context)

def detail(request,id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    # print(article)
    context= {
        'article':article
    }
    return render(request, 'detail.html', context)

@login_required(login_url='user:login')        
def update(request,id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article= form.save(commit=False)
        article.author= request.user
        article.save()
        
        messages.success(request, "Article is updated successfully..")
        return redirect("article:dashboard")
    context= {
        'form':form
    }
    return render(request, 'update.html', context)

@login_required(login_url='user:login')   
def delete(request,id):
    article = get_object_or_404(Article, id=id)

    article.delete()
        
    messages.success(request, "Article is deleted successfully..")
    return redirect("article:dashboard")
    
    