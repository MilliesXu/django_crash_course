from django.shortcuts import render

from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, 'post_list.html', context)
