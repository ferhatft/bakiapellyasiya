from django.shortcuts import render

# Create your views here.
from .models import ClientopinionModel

def anasayfa(request):

    clien_opinion = ClientopinionModel.objects.all()
    
            
    context = {
        'clien_opinion':clien_opinion,
    }
    return render(request, "index.html", context)


def about(request):
    
    clien_opinion = ClientopinionModel.objects.all()
    
   
    
    context = {
        'clien_opinion' :clien_opinion,
    }
    return render(request, "about.html", context)
