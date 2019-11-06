from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
def index(request):
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.all() # meta 클래스에 의해서 역순으로 정렬됨
    return render(request, 'articles/index.html', {'articles':articles})


def create(request):
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET : 기본 form으로 넘겨짐
    # 2. POST : 검증에 실패(is_valid -> False)한 form(오류 메세지를 포함))
    if request.method == 'POST':
        # 사용자가 ArticleForm으로 보낸 데이터를 받아서 form이라는 인스턴스를 생성
        # form의 type은 ArticleForm이라는 클래스의 인스턴스(request.POST는 QueryDict로 담긴다)
        form = ArticleForm(request.POST)
        # form이 유효한지 아닌지 확인
        if form.is_valid():
            # form.cleaned_data 데이터를 요청받은대로 처리함
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # create로 만들면 save() 필요 없음
            article = Article.objects.create(title=title, content=content)
            return redirect('articles:index')
    
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:index')
    else :    
        form = ArticleForm()
        return render(request, 'articles/new.html', {'form':form})

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    return render(request, 'articles/detail.html', {'article':article})

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else :
        return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect('articles:detail', article.pk)
    else :
        # ArticleForm을 초기화(이전에 DB에 저장된 데이터 입력값을 넣어둔 상태)
        form = ArticleForm(initial={'title':article.title, 'content':article.content})
        # 딕셔너리 자료형
        # form = ArticleForm(initial=article.__dict__)
    return render(request, 'articles/new.html', {'form':form})