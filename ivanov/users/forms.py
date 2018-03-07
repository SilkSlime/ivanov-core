from django import forms
from django.contrib.auth.models import User



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if len(User.objects.filter(username=username)) == 0:
            raise forms.ValidationError({'username': "No such user: " + username}, code='invalid')
        
        return cleaned_data
        
        