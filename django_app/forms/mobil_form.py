from django import forms

class MobilForm(forms.Form):
    # Definisikan pilihan untuk variabel tahun, transmisi, dan tipe bahan bakar
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
    mileage = forms.CharField()  # Gunakan CharField untuk memastikan input adalah string
    tax = forms.CharField()
    mpg = forms.CharField()
    engineSize = forms.CharField()
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    fuelType = forms.ChoiceField(choices=FUEL_TYPE_CHOICES)

    def clean(self):
        cleaned_data = super().clean()

        # Ubah variabel-variabel tertentu ke tipe data float
        try:
            cleaned_data['mileage'] = float(cleaned_data['mileage'])
            cleaned_data['tax'] = float(cleaned_data['tax'])
            cleaned_data['mpg'] = float(cleaned_data['mpg'])
            cleaned_data['engineSize'] = float(cleaned_data['engineSize'])
        except ValueError:
            # Tangani kesalahan jika nilai tidak dapat diubah menjadi float
            raise forms.ValidationError("Masukkan angka yang valid.")

        return cleaned_data
