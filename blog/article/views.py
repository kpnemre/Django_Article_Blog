from django.shortcuts import render, HttpResponse

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
    