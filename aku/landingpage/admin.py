from django.contrib import admin

# Register your models here.
from .models import Barang,Jenis
from .models import Transaksi
from .models import DetailTrans
class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields= ['kodebrg','nama']
    list_filter= ('jenis',)
    list_per_page= 5

admin.site.register(Barang,kolomBarang)
admin.site.register(Transaksi)
admin.site.register(DetailTrans)
admin.site.register(Jenis)