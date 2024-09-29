from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

def books(request):
    first = 'Граф Монте-Кристо'
    second = 'Отверженные'
    third = 'Гордость и предубеждения'
    context={
        'first': first,
        'second': second,
        'third': third,
    }
    return render(request, 'books.html', context)

def about_us(request):
    return render(request, 'about_us.html')

