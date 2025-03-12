from django import forms
from .models import Event, EventRegistration


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ["title", "desc", "pic"]



class EventRegistrationForm(forms.ModelForm):

    class Meta:
        model = EventRegistration
        fields =  ["f_name", "l_name", "email"]
