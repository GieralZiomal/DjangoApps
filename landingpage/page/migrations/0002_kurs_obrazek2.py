# Generated by Django 4.1.2 on 2022-10-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurs',
            name='obrazek2',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]
