from django.shortcuts import render
from .models import Musicid
from django.db.models import Q
import requests



# Create your views here.
def home(request):
    musicinfo = Musicid.objects.all()
    context = {

        "musiclist": musicinfo
    }
    return render(request, 'index.html', context)




def search(request):
    if request.method == 'POST':
        musictitle = request.POST.get('artistormusic')
        venues = Musicid.objects.filter(Q(title__contains=musictitle) | Q(artist__contains=musictitle))
        context = {

            "musiclist": venues

        }
        return render(request, 'search.html', context)
        #return render(request, 'notfound.html')


