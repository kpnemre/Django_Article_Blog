from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from .models import Comment
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
    comments= article.comment.all()
    # print(article)
    context= {
        'article':article,
        'comments':comments
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
    
@login_required(login_url='user:login')   
def articles(request):
    keyword =request.GET.get("keyword")
    if keyword:
        articles= Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles":articles})
        
    articles =Article.objects.all()  
    print(type(articles))
    context={
        'articles':articles
    }
    return render(request, "articles.html",context)

def comment(request,id):
    article = get_object_or_404(Article, id=id)
    if request.method =="POST":
        comment_author= request.POST.get("comment_author") #html deki input name den alıyoruz
        comment_content=request.POST.get("comment_content")
        
        newCommment =Comment( comment_author=comment_author,comment_content= comment_content)
        newCommment.article=article # comment modelindeki article içine yukarıdaki article ı ekledik
        # print(newCommment)
        newCommment.save()
        # return redirect("article/article/"+ str(id))
    return redirect(reverse("article:detail",kwargs={'id':id}))
        
    
    
    