# Generated by Django 3.2.7 on 2022-01-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220110_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='storage',
            field=models.CharField(choices=[('500_MB', '500 MB'), ('1_GB', '1 GB'), ('2_GB', '2 GB'), ('5_GB', '5 GB')], max_length=10, verbose_name='Dung lượng'),
        ),
    ]
