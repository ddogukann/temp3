# Generated by Django 4.1.1 on 2022-11-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_delete_agustos_delete_aralik_delete_ekim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bordro',
            name='agustos_arge_gun',
            field=models.FloatField(default=0, verbose_name='Ağustos Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ağustos Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ağustos Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Ağustos Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Ağustos Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_brut',
            field=models.FloatField(default=0, verbose_name='Ağustos Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Ağustos Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ağustos Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ağustos Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ağustos Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ağustos Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ağustos İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Ağustos İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Ağustos İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ağustos İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ağustos İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Ağustos Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Ağustos Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_net_ucret',
            field=models.FloatField(default=0, verbose_name='Ağustos Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ağustos Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ağustos Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Ağustos Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ağustos SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ağustos SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Ağustos SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Ağustos Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ağustos Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Ağustos Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='agustos_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Ağustos Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_arge_gun',
            field=models.FloatField(default=0, verbose_name='Aralık Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Aralık Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Aralık Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Aralık Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Aralık Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_brut',
            field=models.FloatField(default=0, verbose_name='Aralık Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Aralık Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Aralık Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Aralık Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Aralık Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Aralık Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Aralık İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Aralık İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Aralık İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Aralık İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Aralık İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Aralık Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Aralık Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_net_ucret',
            field=models.FloatField(default=0, verbose_name='Aralık Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Aralık Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Aralık Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Aralık Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Aralık SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Aralık SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Aralık SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Aralık Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Aralık Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Aralık Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='aralik_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Aralık Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_arge_gun',
            field=models.FloatField(default=0, verbose_name='Ekim Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ekim Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ekim Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Ekim Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Ekim Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_brut',
            field=models.FloatField(default=0, verbose_name='Ekim Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Ekim Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ekim Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ekim Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ekim Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ekim Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ekim İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Ekim İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Ekim İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ekim İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ekim İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Ekim Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Ekim Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_net_ucret',
            field=models.FloatField(default=0, verbose_name='Ekim Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Ekim Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Ekim Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Ekim Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Ekim SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ekim SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Ekim SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Ekim Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Ekim Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Ekim Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='ekim_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Ekim Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_arge_gun',
            field=models.FloatField(default=0, verbose_name='Eylül Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Eylül Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Eylül Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Eylül Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Eylül Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_brut',
            field=models.FloatField(default=0, verbose_name='Eylül Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Eylül Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Eylül Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Eylül Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Eylül Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Eylül Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Eylül İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Eylül İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Eylül İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Eylül İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Eylül İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Eylül Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Eylül Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_net_ucret',
            field=models.FloatField(default=0, verbose_name='Eylül Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Eylül Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Eylül Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Eylül Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Eylül SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Eylül SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Eylül SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Eylül Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Eylül Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Eylül Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='eylul_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Eylül Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_arge_gun',
            field=models.FloatField(default=0, verbose_name='Kasım Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Kasım Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Kasım Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Kasım Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Kasım Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_brut',
            field=models.FloatField(default=0, verbose_name='Kasım Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Kasım Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Kasım Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Kasım Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Kasım Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Kasım Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Kasım İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Kasım İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Kasım İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Kasım İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Kasım İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Kasım Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Kasım Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_net_ucret',
            field=models.FloatField(default=0, verbose_name='Kasım Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Kasım Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Kasım Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Kasım Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Kasım SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Kasım SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Kasım SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Kasım Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Kasım Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Kasım Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='kasim_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Kasım Vergi Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_arge_gun',
            field=models.FloatField(default=0, verbose_name='Temmuz Arge Günü'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_asgari_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Temmuz Asgari Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_asgari_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Temmuz Asgari Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_asgari_vergi',
            field=models.FloatField(default=0, verbose_name='Temmuz Asgari Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_bordroyaesasbrut',
            field=models.FloatField(default=0, verbose_name='Temmuz Bordro Yasağa Esas Brüt'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_calisilan_gun',
            field=models.FloatField(default=0, verbose_name='Temmuz Çalışılan Gün'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Temmuz Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_damga_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Temmuz Damga Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Temmuz Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_gelir_vergisi_istisnasi',
            field=models.FloatField(default=0, verbose_name='Temmuz Gelir Vergisi İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Temmuz İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_istisna_oncesi_damga',
            field=models.FloatField(default=0, verbose_name='Temmuz İstisna Öncesi Damga'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_istisna_oncesi_gelir',
            field=models.FloatField(default=0, verbose_name='Temmuz İstisna Öncesi Gelir'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_isveren_issizlik_kesintisi',
            field=models.FloatField(default=0, verbose_name='Temmuz İşveren İşsizlik Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_isveren_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Temmuz İşveren SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_kumulatif_asgari',
            field=models.FloatField(default=0, verbose_name='Temmuz Kumulatif Asgari'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_kumulatif_vergi',
            field=models.FloatField(default=0, verbose_name='Temmuz Kumulatif Vergi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_net_ucret',
            field=models.FloatField(default=0, verbose_name='Temmuz Net Ücret'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_odenecek_damga_vergisi',
            field=models.FloatField(default=0, verbose_name='Temmuz Ödenecek Damga Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_odenecek_gelir_vergisi',
            field=models.FloatField(default=0, verbose_name='Temmuz Ödenecek Gelir Vergisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_odenecek_sgk',
            field=models.FloatField(default=0, verbose_name='Temmuz Ödenecek SGK'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_sgk_istisnasi',
            field=models.FloatField(default=0, verbose_name='Temmuz SGK İstisnası'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Temmuz SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_sgk_matrahi',
            field=models.FloatField(default=0, verbose_name='Temmuz SGK Matrahi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_toplam_maliyet',
            field=models.FloatField(default=0, verbose_name='Temmuz Toplam Maliyet'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_toplam_sgk_kesintisi',
            field=models.FloatField(default=0, verbose_name='Temmuz Toplam SGK Kesintisi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_vergi_dilimi',
            field=models.FloatField(default=0, verbose_name='Temmuz Vergi Dilimi'),
        ),
        migrations.AddField(
            model_name='bordro',
            name='temmuz_vergi_matrahi',
            field=models.FloatField(default=0, verbose_name='Temmuz Vergi Matrahi'),
        ),
    ]