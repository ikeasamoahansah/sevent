import os
from .models import *

def get_and_del(request):
    if request.method == "POST":
        event_id = request.POST.get("event-id")
        post = Event.objects.filter(id=event_id).first()
        if post and post.author == request.user:
            post.delete()
            os.remove(post.pic.path)
