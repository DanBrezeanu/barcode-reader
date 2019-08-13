from django.db import models

# Create your models here.

class Barcodes(models.Model):
    barcode = models.ImageField()
    barcodeText = models.TextField()
