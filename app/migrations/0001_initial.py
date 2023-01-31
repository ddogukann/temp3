# Generated by Django 4.1.1 on 2022-10-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hesaplama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otuzbesvergidilimi', models.FloatField(default=0)),
                ('yirmiyedivergidilimi', models.FloatField(default=0)),
                ('yirmivergidilimi', models.FloatField(default=0)),
                ('onbesvergidilimi', models.FloatField(default=0)),
                ('ocakhaziranasgari', models.FloatField(default=0)),
                ('temmuzagustosasgari', models.FloatField(default=0)),
                ('birinciderece', models.FloatField(default=0)),
                ('ikinciderece', models.FloatField(default=0)),
                ('ucuncuderece', models.FloatField(default=0)),
                ('sgkkesintiorani1', models.FloatField(default=0)),
                ('emeklisgkorani', models.FloatField(default=0)),
                ('issizlikkesintiorani', models.FloatField(default=0)),
                ('gelirvergioran1', models.FloatField(default=0)),
                ('gelirvergioran2', models.FloatField(default=0)),
                ('gelirvergioran3', models.FloatField(default=0)),
                ('gelirvergioran4', models.FloatField(default=0)),
                ('egitim1geliroran', models.FloatField(default=0)),
                ('egitim2geliroran', models.FloatField(default=0)),
                ('egitim3geliroran', models.FloatField(default=0)),
                ('damgavergiorani', models.FloatField(default=0)),
                ('indirimorani5510', models.FloatField(default=0)),
                ('sgkkesintiorani', models.FloatField(default=0)),
                ('isverenissizlikoran', models.FloatField(default=0)),
                ('issizlikisverenoran', models.FloatField(default=0)),
                ('ocakasgari', models.FloatField(default=0)),
                ('subatasgari', models.FloatField(default=0)),
                ('martasgari', models.FloatField(default=0)),
                ('nisanasgari', models.FloatField(default=0)),
                ('mayisasgari', models.FloatField(default=0)),
                ('haziranasgari', models.FloatField(default=0)),
                ('temmuzasgari', models.FloatField(default=0)),
                ('agustosasgari', models.FloatField(default=0)),
                ('eylulasgari', models.FloatField(default=0)),
                ('ekimasgari', models.FloatField(default=0)),
                ('kasimasgari', models.FloatField(default=0)),
                ('aralikasgari', models.FloatField(default=0)),
                ('asgaritavanorani', models.FloatField(default=0)),
                ('asgarimatrahorani', models.FloatField(default=0)),
            ],
        ),
    ]
