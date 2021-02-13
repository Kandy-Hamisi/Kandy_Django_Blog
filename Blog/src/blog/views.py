''' Django views are python functions that receive a web request and returns a web response'''

from django.shortcuts import render
from django .views import generic
from .models import Post

# Create your views here.
''' ListView is a subclass of generic class_based views'''
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')#the (-) sign signifies the latest post would be at the top
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'