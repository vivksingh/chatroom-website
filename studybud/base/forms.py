from django.forms import ModelForm
from . models import Room
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class Roomform(ModelForm):
    class Meta:
        model=Room
        fields= '__all__'
        exclude=['host','participants']