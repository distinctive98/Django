from django.shortcuts import render, HttpResponse
import random
import requests
import json

def index(request) : 
    #return HttpResponse('Welcome to Django')
    return render(request, 'index.html')

def hola(request) :
    #return HttpResponse('hola~')
    return render(request, 'hola.html')

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
    return render(request, 'hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'introduce.html', {'name':name, 'age':age})

def multifly(request, num1, num2):
    return render(request, 'multifly.html', {'multifly':num1*num2})