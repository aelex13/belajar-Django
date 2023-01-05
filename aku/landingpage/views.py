from django.shortcuts import render
from landingpage.forms import FormBarang

# Create your views here.

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html', konteks)