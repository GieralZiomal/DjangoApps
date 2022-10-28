from django.shortcuts import render
from .models import kurs

# Create your views here.
def home(request):
    kurs1 = kurs.objects.get()
    context = {

        "kurs": kurs1

    }
    return render(request, 'index.html', context)