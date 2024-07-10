from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
from django import forms
from .models import  *


class List_form (forms.ModelForm):
    
    class Meta:
        model=List
        fields=["Title","Detail"]


    def __init__(self,id=None,*args,**kwargs):
        super(List_form,self).__init__(*args,**kwargs)

        self.fields['Title'].widget.attrs['class']='form-control'
        self.fields['Detail'].widget.attrs['class']='form-control'

        if id!=None:
            self.fields['Title'].widget.attrs['value']=List.objects.get(id=id).Title
            self.fields['Detail'].widget.attrs['value']=List.objects.get(id=id).Detail