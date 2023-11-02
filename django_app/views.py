import joblib
from django.shortcuts import render
from .forms.mobil_form import MobilForm
from .utils import convert_currency as currency, input_binarizer as binarizer, create_dataset as dataset

model = joblib.load('django_app/models/model-regression-knn.pkl')

def home(request):
    context = {
        'title': 'Beranda - Solusi Tepat untuk Memperkirakan Harga Mobil Bekas - Cari Harga yang Pas untuk Spesifikasi Mobil Bekas',
        'params': '/'
    }
    return render(request, 'home.html', context)

def guide(request):
    context = {
      'title': 'Panduan - Baca Panduan Agar Tidak Bingung Saat Menggunakannya - Cari Harga yang Pas untuk Spesifikasi Mobil Bekas',
      'params': '/docs'  
    }
    return render(request, 'guide.html', context)

def handling_404(request):
    context = {
        'title': 'Halaman Tidak Ditemukan - 404 Error Not Found - Cari Harga yang Pas untuk Spesifikasi Mobil Bekas',
        'params': '/404'
    }
    return render(request, '404.html', context)

def estimasi_harga(request):
    result = None
    car_specification = None
    year = 0
    mileage = 0
    tax = 0
    mpg = 0
    enginesize = 0
    transmission = 0
    fueltype = 0

    if request.method == 'POST':
        form = MobilForm(request.POST)

        if form.is_valid():
            user_input = form.cleaned_data

            year = int(user_input['year'])
            mileage = int(user_input['mileage'])
            tax = currency.convert_idr_to_gpb(int(user_input['tax']))
            mpg = float(user_input['mpg'])
            enginesize = float(user_input['engineSize'])
            transmission = user_input['transmission']
            fueltype = user_input['fuelType']

            car_specification = dataset.car_dataset(year, mileage, tax, mpg, enginesize, binarizer.transmission(transmission), binarizer.fueltype(fueltype))

            prediction = model.predict([car_specification])
            result = prediction[0]  # Ambil hasil prediksi pertama
    else:
        form = MobilForm()

    context = {
        'title': 'Estimasi - Cari Harga yang Pas sesuai Spesifikasi Mobil Bekas tersebut',
        'form': form, 
        'estimasi': result,
        'estimasi_rupiah': currency.convert_gbp_to_idr(result),
        'params': '/estimate',
        'user_input': car_specification
    }
    return render(request, 'estimasi_harga.html', context)
