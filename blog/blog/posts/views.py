from django.shortcuts import render
from .models import Post

def iindex(request):
    posts=Post.objects.all()
    return render(request,'iindex.html',{'posts':posts})
def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})

# Create your views here.
