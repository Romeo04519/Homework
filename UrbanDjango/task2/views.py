from django.shortcuts import render

# Create your views here.

def c_templ(request):
    return render(request, 'class_template.html')

def f_templ(request):
    return render(request, 'func_template.html')
