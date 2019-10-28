# django

## 기초

- Project 생성

```bash
$ django-admin startproject first_app
```

- App 생성

```bash
$ django-admin startapp pages
```

- Server 실행

```bash
$ python manage.py runserver
```



## HTML

- POST 방식의 경우 아래를 필수적으로 작성해야 함

```html
{% csrf_token %}
```

- static 파일을 사용할 경우 아래를 상단에 작성해야 함

```html
{% load static %}
```



