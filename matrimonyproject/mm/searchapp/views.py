from django.shortcuts import render
from songapp.models import  Song
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    songs=None
    query=None
    if 'q'in request.GET:
        query=request.GET.get('q')
        songs=Song.objects.all().filter(Q(title__contains=query) | Q(artist__contains=query))
    return render(request,'search.html',{'query':query,'songs':songs})