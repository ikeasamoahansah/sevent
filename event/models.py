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
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=32, default="COE")
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=3)
    date = models.DateField()
    time = models.TimeField(auto_now=False, default='1:45')
    is_over = models.BooleanField()
    
    def __str__(self):
        return f"{self.title}"

# Create your models here.
class EventRegistration(models.Model):
    
    f_name = models.CharField(blank=False, max_length=64)
    l_name = models.CharField(blank=False, max_length=64)
    email = models.EmailField(blank=False, max_length=256)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.email} | {self.event}"


