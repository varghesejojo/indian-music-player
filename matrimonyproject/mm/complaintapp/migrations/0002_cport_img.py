# Generated by Django 4.1.5 on 2023-03-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cport',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='com/'),
        ),
    ]