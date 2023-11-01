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
        ('Other', 'Other'),
    ]

    FUEL_TYPE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Other', 'Other'),
    ]

    ENGINE_SIZE_CHOICES = [
        (1.0, '1.0'),
        (1.2, '1.2'),
        (1.3, '1.3'),
        (1.4, '1.4'),
        (1.5, '1.5'),
        (1.6, '1.6'),
        (1.8, '1.8'),
        (2.0, '2.0'),
        (2.2, '2.2'),
        (2.4, '2.4'),
        (2.5, '2.5'),
        (2.8, '2.8'),
        (3.0, '3.0'),
        (4.2, '4.2'),
        (4.5, '4.5'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Tahun Produksi")
    mileage = forms.IntegerField(label="Jarak Tempuh (mil)")
    tax = forms.IntegerField(label="Pajak")
    mpg = forms.FloatField(label="Miles Per Gallon (MPG)")
    engineSize = forms.ChoiceField(choices=ENGINE_SIZE_CHOICES, label="Ukuran Mesin")
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES, label="Transmisi")
    fuelType = forms.ChoiceField(choices=FUEL_TYPE_CHOICES, label="Jenis Bahan Bakar")
