# Create your views here.
import joblib
from django.shortcuts import render
from .forms.mobil_form import MobilForm

model = joblib.load('django_app/models/model_knn.pkl')

def home(request):
  context = {
    'title': 'Beranda - Solusi Tepat untuk Memperkirakan Harga Mobil Bekas | Estimasi Harga Mobil Bekas',
    'params': '/'
  }

  return render(request, 'home.html', context)

def estimasi_harga(request):
  estimasi = None
  estimasi_rupiah = None

  if request.method == 'POST':
    form = MobilForm(request.POST)

    if form.is_valid():
      user_input = form.cleaned_data

      # Lakukan prediksi harga menggunakan model yang telah dimuat
      spesifikasi_mobil_bekas = [[user_input['year'], user_input['mileage'], user_input['tax'],user_input['mpg'], user_input['engineSize']]]

      prediction = model.predict(spesifikasi_mobil_bekas)

      estimasi = prediction[0]  # Ambil hasil prediksi pertama

      # Konversi estimasi ke Rupiah
      to_idr = estimasi * 19110
      estimasi_rupiah = '{:,.0f}'.format(to_idr)
  else:
    form = MobilForm()

  context = {
    'title': 'Estimasi | Estimasi Harga Mobil Bekas',
    'form': form, 
    'estimasi': estimasi, 
    'estimasi_rupiah': estimasi_rupiah,
    'params': '/estimate'
  }

  return render(request, 'estimasi_harga.html', context)
