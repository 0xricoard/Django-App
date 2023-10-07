from django import forms

class MobilForm(forms.Form):
    # Definisikan pilihan untuk variabel tahun, transmisi, dan tipe bahan bakar
    YEAR_CHOICES = [
        (1998, '1998'),
        (1999, '1999'),
        (2000, '2000'),
        (2001, '2001'),
        (2002, '2002'),
        (2003, '2003'),
        (2004, '2004'),
        (2005, '2005'),
        (2006, '2006'),
        (2007, '2007'),
        (2008, '2008'),
        (2009, '2009'),
        (2010, '2010'),
        (2011, '2011'),
        (2012, '2012'),
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
    mileage = forms.IntegerField()
    tax = forms.IntegerField()
    mpg = forms.FloatField()
    engineSize = forms.FloatField()
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    fuelType = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)
