from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')

def books(request):
    return render(request, 'books.html')

def about_us(request):
    return render(request, 'about_us.html')

