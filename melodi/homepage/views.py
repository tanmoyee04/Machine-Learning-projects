from django.shortcuts import render
from .dd import process

# Create your views here.

def index(request):
    songname=''
    genre=None
    if request.method=="POST":
        songname=request.POST.get('songID')
        genre=process(songname)
    context={'songname':songname,'genre': genre}
    return render(request,'index.html',context)