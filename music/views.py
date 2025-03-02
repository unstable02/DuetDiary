from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

def home(request):
    song = Song.objects.first()  # Ek hi song hoga
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            if song:  # Pehle song ko delete karo
                song.delete()
            form.save()
            return redirect("home")
    else:
        form = SongForm()

    return render(request, "music/home.html", {"song": song, "form": form})

