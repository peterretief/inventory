from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
#        exclude = ['author','arrival_date', 'establishment', 'guestname', 'departure_date']
