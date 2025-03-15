from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .helper_functions import *

# Create your views here.

def home(request):
    return render(request, "event/home.html", {"events": Event.objects.all().order_by('-created_at')})

@login_required(login_url='/admin')
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = EventForm()
    return render(request, 'event/add.html', {"form":form})


def view_event(request, event_id):
    event= get_object_or_404(Event, id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'event/view.html', context)


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.event = event
            reg.save()
            return redirect("/")
    else:
        form = EventRegistrationForm()
    return render(request, 'event/registration.html', {"form":form, "event": event})


def logout_view(request):
    logout(request)
    return redirect('/')
