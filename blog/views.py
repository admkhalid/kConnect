from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/model_<viewtype.html>
    #in the home() view above we are calling the post objects as 'posts' in
    #the context. but by default a ListView will call that variable object_list
    #instead. we can change that by adding one more variable
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    #this class expects the template's name to be <modelname>_form.html.
    #in our case post_form.html

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})