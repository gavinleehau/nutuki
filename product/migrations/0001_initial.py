# Generated by Django 3.2.7 on 2022-01-09 15:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=100, verbose_name='Nhà cung cấp')),
                ('name', models.CharField(max_length=100, verbose_name='Tên gói')),
                ('storage', models.CharField(choices=[('30_GB', '30 GB'), ('2_TB', '2 TB'), ('5_TB', '5 TB'), ('Unlimited', 'Unlimited')], max_length=20, verbose_name='Dung lượng')),
                ('descriptions', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Mô tả')),
                ('old_pricing', models.DecimalField(decimal_places=0, max_digits=100, null=True, verbose_name='Giá tiền cũ')),
                ('pricing', models.DecimalField(decimal_places=0, max_digits=100, verbose_name='Giá tiền')),
                ('shareDrive', models.CharField(choices=[('unfinished', 'Chưa hoàn thành'), ('finished', 'Hoàn thành')], default='', max_length=20, verbose_name='Trạng thái đơn hàng')),
            ],
            options={
                'db_table': 'email business',
            },
        ),
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên gói')),
                ('storage', models.CharField(choices=[('1_GB', '1 GB'), ('2_GB', '2 GB'), ('5_GB', '5 GB')], max_length=10, verbose_name='Dung lượng')),
                ('bandwidth', models.CharField(default='Không giới hạn băng thông', max_length=100, verbose_name='Dung lượng')),
                ('freeDomain', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Miễn phí domain')),
                ('template', models.CharField(choices=[('Theo mẫu', 'Theo mẫu'), ('Theo yêu cầu', 'Theo yêu cầu')], max_length=20, verbose_name='Giao diện website')),
                ('descriptions', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Mô tả')),
                ('old_pricing', models.DecimalField(decimal_places=0, max_digits=100, null=True, verbose_name='Giá tiền cũ')),
                ('pricing', models.DecimalField(decimal_places=0, max_digits=100, verbose_name='Giá tiền')),
                ('shareDrive', models.CharField(choices=[('finished', 'Hoàn thành'), ('unfinished', 'Chưa hoàn thành')], default='', max_length=20, verbose_name='Trạng thái đơn hàng')),
            ],
            options={
                'db_table': 'website',
            },
        ),
        migrations.CreateModel(
            name='Checkout_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_domain', models.CharField(max_length=100, null=True, verbose_name='Tên miền đăng ký: ')),
                ('used_time', models.CharField(max_length=20, verbose_name='Thời gian sử dụng: ')),
                ('number_of_users', models.CharField(max_length=12, null=True, verbose_name='Số lượng người dùng: ')),
                ('selected_email_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.emailbusiness')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Họ tên: ')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email: ')),
                ('phone', models.CharField(max_length=12, null=True, verbose_name='Số điện thoại: ')),
                ('message', models.TextField(null=True, verbose_name='Nội dung')),
                ('selected_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.website')),
            ],
        ),
    ]