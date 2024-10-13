from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ContactForm
from .models import *

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def games(request):
    games_ = Game.objects.all()
    context = {
        'games_': games_,
    }
    return render(request, 'games.html', context)


def about_us(request):
    return render(request, 'about_us.html')

def sign_up_by_django(request):
    byuers_ = Buyer.objects.all()
    users = []
    for i in byuers_:
        users.append(i.name)
    form = ContactForm()
    info = {}
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name = username, balance = 500, age = age)
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                info['error'] = 'Пользователь уже существует'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
    return render(request, 'registration_page.html', context)
