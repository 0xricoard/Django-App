#from django.shortcuts import render

# Create your views here.
import joblib
from django.shortcuts import render
from .forms import MobilForm

# Muat model saat tampilan dimuat
model = joblib.load('model_knn.pkl')

def estimasi_harga(request):
    estimasi = None
    estimasi_rupiah = None
    if request.method == 'POST':
        form = MobilForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data
            # Lakukan prediksi harga menggunakan model yang telah dimuat
            data_mobil_bekas = [[input_data['year'], input_data['mileage'], input_data['tax'], input_data['mpg'], input_data['engineSize']]]
            prediction = model.predict(data_mobil_bekas)
            estimasi = prediction[0]  # Ambil hasil prediksi pertama
            # Konversi estimasi ke Rupiah
            estimasi_rupiah = estimasi * 19110 * 1e-6
    else:
        form = MobilForm()

    return render(request, 'estimasi_harga.html', {'form': form, 'estimasi': estimasi, 'estimasi_rupiah': estimasi_rupiah})
