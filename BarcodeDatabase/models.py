from django.db import models

# Create your models here.

class Barcodes(models.Model):
    barcodeImage = models.ImageField()
    barcodeData = models.TextField()
