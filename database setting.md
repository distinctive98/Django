- 데이터베이스 테이블 구축

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
```



- migrations 생성

```bash
$ python manage.py makemigrations
```



- 파이썬과 데이터베이스 연결

```bash
$ python manage.py migrate
```



- 쉘 접속

```bash
$ python manage.py shell
```



- 쉘에서 QuerySet 확인하기

```python
>>> from articles.models import Article
>>> Article.objects.all()
<QuerySet []>
>>> exit()
```



- 쉘에서 데이터 삽입하기

```python
#첫 번째 방법
>>> from articles.models import Article
>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django'
>>> article.save()
>>> article
<Article: Article object (1)>
    
#두 번째 방법
>>> article = Article(title='second', content='edition')
>>> article.save()
>>> article
<Article: Article object (2)>
    
#세 번째 방법
>>> Article.objects.create(title='third', content='eye')
<Article: Article object (3)>
    
#전체 확인
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```



- 쉘에서 데이터 선택하기

```python
>>> Article.objects.filter(title='first')
>>> Article.objects.filter(title='first').first()
>>> Article.objects.filter(title='first').last()
>>> Article.objects.get(pk=1)
>>> Article.objects.all()[2]
>>> Article.objects.all()[1:3] #2, 3번글 select
>>> Article.objects.order_by('pk') #오름차순
>>> Article.objects.order_by('-pk')
>>> Article.objects.filter(title__contains='fir') #와일드카드
>>> Article.objects.filter(title__startswith='f')
```



- 슈퍼유저 생성하기

```bash
$ python manage.py createsuperuser
```



