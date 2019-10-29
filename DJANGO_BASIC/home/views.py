from django.shortcuts import render, HttpResponse
import random
import requests
import json
from datetime import datetime

def index(request) : 
    #return HttpResponse('Welcome to Django')
    return render(request, 'home/index.html')

def hola(request) :
    #return HttpResponse('hola~')
    return render(request, 'home/hola.html')

def dinner(request):
    menus = ['피자', '치킨', '족발']
    dinner = random.choice(menus)
    #return HttpResponse(f'오늘의 저녁 메뉴는 {dinner}입니다.')
    return render(request, 'dinner.html', {'menus':menus, 'dinner':dinner})

def lotto(request):
    URL = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=819'
    lotto_819 = []
    res = requests.get(URL)
    info = res.json()
    for i in range(1,7):
        lotto_819.append(info[f'drwtNo{i}'])

    numbers = range(1,46)
    match = {}
    count = 0
    while(len(match) != 6):
        lotto_my = random.sample(numbers, 6)
        match = set(lotto_my) & set(lotto_819) #교집합을 match에 저장(list)
        count += 1

    return HttpResponse(count)
    #return HttpResponse(f'오늘의 로또 추천번호는 {my_lotto}입니다.')


def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'home/introduce.html', {'name':name, 'age':age})

def multifly(request, num1, num2):
    return render(request, 'home/multifly.html', {'multifly':num1*num2})

def image(request):
    return render(request, 'home/image.html')

def isbirth(request):
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    return render(request, 'home/isbirth.html', {'result':result})

def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    return render(request, 'home/ispal.html', {'word':word, 'result':result})

def throw(request):
    return render(request, 'home/throw.html')

def catch(request):
    message = request.GET.get('message')
    return render(request, 'home/catch.html', {'message':message})

def word(request):
    return render(request, 'home/word.html')

def palin(request):
    drome = request.GET.get('word')
    if drome == drome[::-1]:
        result = True
    else:
        result = False
    return render(request, 'palin.html', {'drome':drome, 'result':result})

def user_new(request):
    return render(request, 'home/user_new.html')

def user_create(request):
    user_name = request.POST.get('name')
    user_password = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'user_name':user_name, 'user_password':user_password})

def static_example(request):
    return render(request, 'home/static_example.html')