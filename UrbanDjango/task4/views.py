from lib2to3.fixes.fix_input import context

from django.shortcuts import render


# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def books(request):
    list_ = ['Граф Монте-Кристо', 'Отверженные', 'Гордость и предубеждения', 'Портрет Дориана Грея']
    context = {
        'list': list_
    }
    return render(request, 'books.html', context)


def about_us(request):
    return render(request, 'about_us.html')
