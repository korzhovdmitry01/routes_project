from django import forms
from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='City', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a city'
    }))

    class Meta:
        model = City
        fields = ('name', )


