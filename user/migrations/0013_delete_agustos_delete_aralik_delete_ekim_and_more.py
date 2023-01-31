# Generated by Django 4.1.1 on 2022-11-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_maas_calisan_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='agustos',
        ),
        migrations.DeleteModel(
            name='aralik',
        ),
        migrations.DeleteModel(
            name='ekim',
        ),
        migrations.DeleteModel(
            name='eylul',
        ),
        migrations.DeleteModel(
            name='haziran',
        ),
        migrations.DeleteModel(
            name='kasim',
        ),
        migrations.DeleteModel(
            name='mart',
        ),
        migrations.DeleteModel(
            name='mayis',
        ),
        migrations.DeleteModel(
            name='nisan',
        ),
        migrations.DeleteModel(
            name='ocak',
        ),
        migrations.DeleteModel(
            name='subat',
        ),
        migrations.DeleteModel(
            name='temmuz',
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_arge_gun',
            field=models.FloatField(default=0, verbose_name='Haziran Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Haziran Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Haziran Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Haziran Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Haziran Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_brut',
            field=models.FloatField(default=0, verbose_name='Haziran Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Haziran Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Haziran Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Haziran Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Haziran Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Haziran Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Haziran İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Haziran İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Haziran İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Haziran İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Haziran İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Haziran Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Haziran Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_net_ucret',
            field=models.FloatField(default=0, verbose_name='Haziran Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Haziran Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Haziran Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Haziran Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Haziran SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Haziran SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Haziran SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Haziran Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Haziran Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Haziran Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='haziran_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Haziran Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_arge_gun',
            field=models.FloatField(default=0, verbose_name='Mart Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mart Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mart Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Mart Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Mart Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_brut',
            field=models.FloatField(default=0, verbose_name='Mart Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Mart Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Mart Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mart Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Mart Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mart Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mart İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Mart İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Mart İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mart İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mart İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Mart Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Mart Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_net_ucret',
            field=models.FloatField(default=0, verbose_name='Mart Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Mart Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Mart Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Mart Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mart SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mart SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Mart SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Mart Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mart Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Mart Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mart_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Mart Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_arge_gun',
            field=models.FloatField(default=0, verbose_name='Mayıs Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mayıs Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mayıs Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Mayıs Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Mayıs Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_brut',
            field=models.FloatField(default=0, verbose_name='Mayıs Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Mayıs Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Mayıs Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mayıs Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Mayıs Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mayıs Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mayıs İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Mayıs İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Mayıs İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mayıs İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mayıs İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Mayıs Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Mayıs Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_net_ucret',
            field=models.FloatField(default=0, verbose_name='Mayıs Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Mayıs Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Mayıs Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Mayıs Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Mayıs SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mayıs SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Mayıs SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Mayıs Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Mayıs Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Mayıs Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='mayis_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Mayıs Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_arge_gun',
            field=models.FloatField(default=0, verbose_name='Nisan Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Nisan Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Nisan Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Nisan Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Nisan Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_brut',
            field=models.FloatField(default=0, verbose_name='Nisan Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Nisan Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Nisan Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Nisan Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Nisan Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Nisan Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Nisan İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Nisan İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Nisan İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Nisan İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Nisan İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Nisan Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Nisan Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_net_ucret',
            field=models.FloatField(default=0, verbose_name='Nisan Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Nisan Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Nisan Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Nisan Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Nisan SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Nisan SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Nisan SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Nisan Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Nisan Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Nisan Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='nisan_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Nisan Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_arge_gun',
            field=models.FloatField(default=0, verbose_name='Ocak Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ocak Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ocak Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Ocak Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Ocak Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_brut',
            field=models.FloatField(default=0, verbose_name='Ocak Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Ocak Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ocak Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ocak Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ocak Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ocak Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ocak İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Ocak İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Ocak İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ocak İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ocak İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Ocak Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Ocak Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_net_ucret',
            field=models.FloatField(default=0, verbose_name='Ocak Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ocak Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ocak Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Ocak Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ocak SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ocak SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Ocak SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Ocak Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ocak Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Ocak Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ocak_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Ocak Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_arge_gun',
            field=models.FloatField(default=0, verbose_name='Şubat Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Şubat Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Şubat Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Şubat Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Şubat Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_brut',
            field=models.FloatField(default=0, verbose_name='Şubat Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Şubat Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Şubat Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Şubat Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Şubat Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Şubat Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Şubat İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Şubat İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Şubat İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Şubat İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Şubat İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Şubat Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Şubat Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_net_ucret',
            field=models.FloatField(default=0, verbose_name='Şubat Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Şubat Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Şubat Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Şubat Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Şubat SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Şubat SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Şubat SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Şubat Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Şubat Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Şubat Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='subat_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Şubat Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_brut',
            field=models.FloatField(default=0, verbose_name='Temmuz Brüt'),
        ),
    ]
