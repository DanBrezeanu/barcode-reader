# Generated by Django 2.2.3 on 2019-08-13 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BarcodeDatabase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barcodes',
            old_name='barcodeText',
            new_name='barcodeData',
        ),
        migrations.RenameField(
            model_name='barcodes',
            old_name='barcode',
            new_name='barcodeImage',
        ),
    ]
