from django.db import models

# Create your models here.

class Mobil(models.Model):
  tahun = models.IntegerField()
  kilometer = models.FloatField()
  pajak = models.FloatField()
  mpg = models.FloatField()
  engineSize = models.FloatField()
  harga = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.tahun} {self.merek} {self.model}"
