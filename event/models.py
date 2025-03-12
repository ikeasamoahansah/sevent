from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=64)
    desc = models.TextField(blank=False)
    pic = models.ImageField(blank=False, upload_to="images/")
    created_at = models.DateTimeField(auto_add_now=True)
    date = models.DateField()
    is_over = models.BooleanField()
    
    def __str__(self):
        return f"{self.author}, {self.title}"

# Create your models here.
class EventRegistration(models.Model):
    
    f_name = models.CharField(blank=False)
    l_name = models.CharField(blank=False)
    email = models.CharField(blank=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.f_name} | {self.email}"


