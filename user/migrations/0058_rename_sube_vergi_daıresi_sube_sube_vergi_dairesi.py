# Generated by Django 4.1.1 on 2023-01-24 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0057_alter_iskur_iskur_no_alter_iskur_iskur_sifre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sube',
            old_name='sube_vergi_daıresi',
            new_name='sube_vergi_dairesi',
        ),
    ]
