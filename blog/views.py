from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

posts=[
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1', 
        'content':'First post content',
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
    }
]
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})

# Create your views here.
