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

    ENGINE_SIZE_CHOICES = [
        (1.0, '1.0'),
        (1.1, '1.1'),
        (1.2, '1.2'),
        (1.3, '1.3'),
        (1.4, '1.4'),
        (1.5, '1.5'),
        (1.6, '1.6'),
        (1.7, '1.7'),
        (1.8, '1.8'),
        (1.9, '1.9'),
        (2.0, '2.0'),
        (2.1, '2.1'),
        (2.2, '2.2'),
        (2.3, '2.3'),
        (2.4, '2.4'),
        (2.5, '2.5'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    mileage = forms.IntegerField()
    tax = forms.IntegerField()
    mpg = forms.FloatField()
    engineSize = forms.ChoiceField(choices=ENGINE_SIZE_CHOICES)
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    fuelType = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)
