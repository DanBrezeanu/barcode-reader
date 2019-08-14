import cv2
from pyzbar import pyzbar
from BarcodeDatabase.models import Barcodes
from django.utils import timezone

def handle_uploaded_file(f):
    filename = 'media/photos/' + f.name
    extension = f.name.split('.')[-1]

    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    image = cv2.imread(filename)
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        print("No barcodes found")
        return (barcode_filename, "No barcodes found")
    else:
        barcode_filename = 'media/tmp-barcode.' + extension
        cv2.imwrite(barcode_filename, image)
        for barcode_idx, barcode in enumerate(barcodes):
            print(barcode.data)
        return (barcode_filename, "".join(barData.data.decode("utf-8") for barData in barcodes))
