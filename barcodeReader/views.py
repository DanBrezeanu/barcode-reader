from django.shortcuts import render
from django.http import HttpResponse
from .forms import BarcodeForm
from .functions.functions import handle_uploaded_file
# Create your views here.

def index(request):
    if request.method == 'POST':
        barcode = BarcodeForm(request.POST, request.FILES)
        if barcode.is_valid():
            handle_uploaded_file(request.FILES['photo'])
            return render(request, "index.html", {'form':barcode})
    else:
        barcode = BarcodeForm()
        return render(request, "index.html", {'form':barcode})
