from tkinter import Widget
from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields="__all__"
        # fields=['','']
        widgets={
            'esim':forms.TextInput(attrs={'class':'fname'}),
            'slug':forms.Textarea(attrs={'class':'fname','cols':50,  'rows':1}),
            'nomer':forms.NumberInput(attrs={'class':'fname'}),
            'kala':forms.TextInput(attrs={'class':'fname'}),
            'email':forms.EmailInput(attrs={'class':'fname'}),
            'pochta':forms.EmailInput(attrs={'class':'fname'}),
            'poshta':forms.EmailInput(attrs={'class':'fname'}),
            'is_published':forms.CheckboxInput(attrs={'class':'fname'}),
                    }
