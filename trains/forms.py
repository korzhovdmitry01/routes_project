from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Name of train', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a train"s name'
    }))
    travel_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time'
    }))
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Train
        fields = '__all__'


