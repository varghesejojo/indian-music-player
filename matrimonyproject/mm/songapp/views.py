from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .models import Song, Favourite


def add_song(request):
    if request.method=='POST':
        title=request.POST.get('title',)
        artist=request.POST.get('artist',)
        image=request.FILES['image']
        audio_file=request.FILES['audio_file']
        duration=request.POST.get('duration',)
        songs=Song(title=title,artist=artist,image=image,audio_file=audio_file,duration=duration)
        songs.save()
    return render(request, 'about.html')

def home(request):
    songs=Song.objects.all()
    return render(request,'home.html',{'songs':songs})

def playsong(request, id):
    obj = Song.objects.get(id=id)
    is_favourite = Favourite.objects.filter(user=request.user).filter(song=id).values('is_fav')
    if 'add-fav' in request.POST:
        is_fav = True
        query = Favourite(user=request.user, song=obj, is_fav=is_fav)
        print(f'query: {query}')
        query.save()
        messages.success(request, "Added to favorite!")
        return redirect('songapp:play', id=id)
    elif 'rm-fav' in request.POST:
        is_fav = True
        query = Favourite.objects.filter(user=request.user, song=obj, is_fav=is_fav)
        print(f'user: {request.user}')
        print(f'song: {id} - {obj}')
        print(f'query: {query}')
        query.delete()
        messages.success(request, "Removed from favorite!")
        return redirect('songapp:play', id=id)

    return render(request, 'playsong.html',{'song':obj,'is_favourite': is_favourite})


def favourite(request):
    songs = Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct()
    print(f'songs: {songs}')

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        favourite_song = Favourite.objects.filter(user=request.user, song__id=song_id, is_fav=True)
        favourite_song.delete()
        messages.success(request, "Removed from favourite!")
    context = {'songs': songs}
    return render(request, 'favourite.html', context=context)