# Generated by Django 3.0.14 on 2022-11-25 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='body',
        ),
    ]
