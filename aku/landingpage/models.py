from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField ()
    
    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150,blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "{}.{}.{}.{}".format(self.nama, self.kodebrg ,self.stok ,self.harga)
class Transaksi(models.Model):
    kodetrans = models.CharField(max_length=8)
    tgltrans = models.DateTimeField(auto_now_add=True)
    total = models.BigIntegerField()
    

    def __str__(self):
        return "{}.{}.{}".format(self.kodetrans, self.tgltrans ,self.total)

class DetailTrans(models.Model):
    kodebrg = models.CharField(max_length=8)
    kodetrans = models.CharField(max_length=8)
    tgltrans = models.DateTimeField(auto_now_add=True)
    subtotal = models.BigIntegerField()
    

    def __str__(self):
        return "{}.{}.{}.{}".format(self.kodetrans, self.kodebrg ,self.tgltrans ,self.subtotal)