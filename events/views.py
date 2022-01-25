from django.shortcuts import render
from .models import Event

# Create your views here.

def home(request):
<<<<<<< HEAD
	events = Event.objects
	return render(request, 'events/home.html', {'events': events})
=======
	return render(request, 'events/home.html')
>>>>>>> c7bce7816e4a2acac17d70bd3d4b1aea577abcec
