# Generated by Django 4.1.1 on 2022-12-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_sirket_sirket_nace_kodu'),
    ]

    operations = [
        migrations.CreateModel(
            name='vergidairesi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vd_adi', models.CharField(max_length=50, verbose_name='Vergi Dairesi Adı')),
                ('vd_kodu', models.CharField(max_length=50, verbose_name='Vergi Dairesi Kodu')),
                ('vd_sehir', models.CharField(max_length=50, verbose_name='Vergi Dairesi Şehir')),
            ],
            options={
                'verbose_name_plural': 'Vergi Daireleri',
            },
        ),
    ]
