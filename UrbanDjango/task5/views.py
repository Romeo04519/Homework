from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ContactForm

def sign_up_by_html(request):
    users = ['leo', 'tiger']
    info = {}
    context={
        'info': info,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветствуем, {username}!')
        if username in users:
            info['error'] = 'Пользователь уже существует'
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

    return render(request, 'registration_page.html', context)

def sign_up_by_django(request):
    users = ['leo', 'tiger']
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
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                info['error'] = 'Пользователь уже существует'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
    return render(request, 'registration_page.html', context)
