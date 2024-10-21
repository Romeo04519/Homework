from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Settings
from .forms import ContactForm
# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')
def choose_(request):
    post_num_fin = Settings.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post_num_rec = form.cleaned_data['post_number']
            post_num_fin.post_num = post_num_rec
            post_num_fin.save()
    return render(request, 'choose_numb.html')

def index(request):
    post_num_fin = Settings.objects.get(id=1)
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, post_num_fin.post_num)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    context = {
        'page_posts': page_posts,
    }

    return render(request, 'index.html',context)

