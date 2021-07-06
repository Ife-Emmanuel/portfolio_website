from django import forms
from .models import GroupDescription

class GroupDescriptionForm(forms.ModelForm):
    model = GroupDescription
    field = ['text']
    labels = {'text' : 'description'}
