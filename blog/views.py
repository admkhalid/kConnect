from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    # posts = [
    #     {
    #         'title': 'Post1',
    #         'author': 'admkhalid',
    #         'date_posted': '28 June 2019',
    #         'content': 'dummy content'
    #     },
    #     {
            
    #         'title': 'Post2',
    #         'author': 'Jane Doe',
    #         'date_posted': '29 June 2019',
    #         'content': 'dummy content 2'
    #     }
    # ]
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})