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
    else:
        for barcode_idx, barcode in enumerate(barcodes):
            print(barcode.data)
            barcode_filename = 'media/barcodes/' + barcode.data.decode('utf-8') + '-' + str(timezone.now().strftime('%y%m%d%H%M')) + '.' + extension

            barcode_image = image[barcode.rect.top : barcode.rect.top + barcode.rect.height,
                                  barcode.rect.left : barcode.rect.left + barcode.rect.width]
            cv2.imwrite(barcode_filename, barcode_image)

            b = Barcodes(barcodeImage = barcode_filename, barcodeData = barcode.data)
            b.save()
