from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html', {'articles':articles})

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # article = Article(title=title, content=content)
    # article.save()

    if request.method == 'POST':    
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else :
        return redirect('article:detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/edit.html', {'article':article})