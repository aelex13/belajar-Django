# Generated by Django 2.2.12 on 2022-10-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_barang_waktu_posting'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('kodetrans', models.CharField(max_length=8)),
                ('tgltrans', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=8)),
                ('tgltrans', models.DateTimeField(auto_now_add=True)),
                ('total', models.BigIntegerField()),
            ],
        ),
    ]
