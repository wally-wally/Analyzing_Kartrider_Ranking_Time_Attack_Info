from django import forms
from .models import DataPage

class DataPageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'nickname'}))
    speed = forms.CharField(widget=forms.TextInput(attrs={'class': 'speed'}))
    img_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'img_url'}))
    created_at = forms.CharField(widget=forms.TextInput(attrs={'class': 'created_at'}))
    
    class Meta:
        model = DataPage
        fields = '__all__'