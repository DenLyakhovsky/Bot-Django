from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50, label='Імʼя')
    last_name = forms.CharField(max_length=50, label='Прізвище')
