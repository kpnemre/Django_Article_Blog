from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
# Create your views here.
def index(request):
    # return HttpResponse("Anasayfa")
    context= {
        'number':7
    }
    return render(request, 'index.html',context)
    # return render(request, 'article/index.html')
    
def about(request):
    return render(request, 'about.html')

# def detail(request,id):
#     return HttpResponse("Anasayfa" +str(id))

def dashboard(request):
    articles= Article.objects.filter(author=request.user)
    context ={
        'articles':articles
    }
    return render(request, 'dashboard.html', context)

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article= form.save(commit=False)
        article.author= request.user
        article.save()
        
        messages.success(request, "Article is created successfully..")
        redirect("index")
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
    
