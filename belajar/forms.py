from django import forms

class MobilForm(forms.Form):
    year = forms.IntegerField()
    mileage = forms.FloatField()
    tax = forms.FloatField()
    mpg = forms.FloatField()
    engineSize = forms.FloatField()
