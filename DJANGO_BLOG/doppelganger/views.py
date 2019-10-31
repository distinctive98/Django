from django.shortcuts import render
from faker import Faker
from .models import Doppelganger

# Create your views here.
def main(request):
    return render(request, 'doppelganger/main.html')

def confirm(request):
    # # DB에 이름이 있는지 확인
    # name = request.POST.get('name')
    # doppelganger = Doppelganger.objects.filter(name=name).first() #get()은 없을 경우 error 발생
    
    # #NULL이 아니면 True 반환
    # if doppelganger : 
    # else :
    
    fake = Faker('ko-KR')
    d_name = fake.name()
    d_job = fake.job()
    d_address = fake.address()
    
    doppelganger = Doppelganger(name=d_name, address=d_address, job=d_job)
    doppelganger.save()

    return render(request, 'doppelganger/confirm.html', {'doppelganger':doppelganger})