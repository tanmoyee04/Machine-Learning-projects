from django.shortcuts import render
#from .ReMusic import dd

# Create your views here.

def index(request):
    songname=''
    genre=None
    if request.method=="POST":
        songname=request.POST.get('songID')
        genre=dd.process(songname)
        #genre='MELODY'
    context={'songname':songname,'genre': genre}
    return render(request,'index.html',context)