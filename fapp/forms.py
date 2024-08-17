from django import forms
from .models import *
class mform(forms.ModelForm):
    class Meta():
        model=addproduct
        fields='__all__'


class myform(forms.ModelForm):
    class Meta():
        model=user
        fields=['address','phonenumber','image']