# Generated by Django 3.2.7 on 2021-12-31 07:25

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Câu Hỏi: ')),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(default='', null=True, verbose_name='Câu trả lời: ')),
            ],
            options={
                'db_table': 'qustions',
                'ordering': ['-id'],
            },
        ),
    ]