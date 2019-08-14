from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BarcodeForm
from .functions.functions import handle_uploaded_file
import cv2
from pyzbar import pyzbar
from django.http import JsonResponse
import glob
from django.utils import timezone
from BarcodeDatabase.models import Barcodes
# Create your views here.

def index(request):
    if request.method == 'POST':
        barcode = BarcodeForm(request.POST, request.FILES)
        if barcode.is_valid():
            filename, barcodeData = handle_uploaded_file(request.FILES['photo'])
            return render(request, "index.html", {'form': barcode, 'barcodeurl': '/' + filename, 'barcodeData' : barcodeData})
    else:
        barcode = BarcodeForm()
        return render(request, "index.html", {'form': barcode})

    return HttpResponse("")

def savephoto(request):
    tmp_photo = cv2.imread(glob.glob('media/tmp-barcode.*')[0])
    extension = glob.glob('media/tmp-barcode*')[0].split('.')[-1]

    barcodes = pyzbar.decode(tmp_photo)

    response = {'response': False, 'barcodes': []}

    for barcode in barcodes:
        barcode_filename = 'media/barcodes/' + barcode.data.decode('utf-8') + '-' + str(timezone.now().strftime('%y%m%d%H%M')) + '.' + extension

        barcode_image = tmp_photo[barcode.rect.top : barcode.rect.top + barcode.rect.height,
                              barcode.rect.left : barcode.rect.left + barcode.rect.width]
        cv2.imwrite(barcode_filename, barcode_image)

        b = Barcodes(barcodeImage = barcode_filename, barcodeData = barcode.data)
        b.save()

        response['barcodes'].append({'name': barcode_filename, 'value': barcode.data.decode('utf-8')})

    response['response'] = True
    return JsonResponse(response)
