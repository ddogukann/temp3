# Generated by Django 4.1.1 on 2022-10-28 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_perm_alter_sirket_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calisan',
            name='calisan_yetki_id',
        ),
    ]