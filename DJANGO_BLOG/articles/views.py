from django.shortcuts import render, redirect
from .models import Article, Comment
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    return render(request, 'articles/index.html', {'articles':articles})

def new(request):
    return render(request, 'articles/new.html')

@login_required
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
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html')

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments})

def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else :
        return redirect('article:detail', article.pk)

@login_required
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/edit.html', {'article':article})

def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
    #     return redirect('articles:detail', article.id)
    # else:
    #     return redirect('articles:detail', article.id)
    return redirect('articles:detail', article_id)
    
def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect('articles:detail', article_id)
