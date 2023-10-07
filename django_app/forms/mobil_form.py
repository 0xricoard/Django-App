from django import forms

class MobilForm(forms.Form):
    YEAR_CHOICES = [
        (2013, '2013'),
        (2014, '2014'),
        (2015, '2015'),
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
    ]

    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Semi-Auto', 'Semi-Auto'),
    ]

    FUEL_TYPE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    mileage = forms.FloatField()
    tax = forms.FloatField()
    mpg = forms.FloatField()
    engineSize = forms.FloatField()
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    fuelType = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)
