# Generated by Django 4.0.3 on 2022-03-18 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inncomapp', '0002_remove_company_createdtime_alter_company_companycode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='createdTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]