import joblib
from django.shortcuts import render
from .forms.mobil_form import MobilForm
from .utils import convert_currency as currency

model = joblib.load('django_app/models/model_knn.pkl')

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

    if request.method == 'POST':
        form = MobilForm(request.POST)

        if form.is_valid():
            user_input = form.cleaned_data

            # Ubah variabel-variabel ke tipe data numerik
            spesifikasi_mobil_bekas = [
                [
                    int(user_input['year']), 
                    int(user_input['mileage']), 
                    float(currency.convert_idr_to_gpb(int(user_input['tax']))),
                    float(user_input['mpg']), 
                    float(user_input['engineSize'])
                ]
            ]

            prediction = model.predict(spesifikasi_mobil_bekas)
            result = prediction[0]  # Ambil hasil prediksi pertama
    else:
        form = MobilForm()

    context = {
        'title': 'Estimasi - Cari Harga yang Pas sesuai Spesifikasi Mobil Bekas tersebut',
        'form': form, 
        'estimasi': result, 
        'estimasi_rupiah': currency.convert_gbp_to_idr(result),
        'params': '/estimate'
    }
    return render(request, 'estimasi_harga.html', context)
