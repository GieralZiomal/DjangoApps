# Generated by Django 4.1.2 on 2022-10-26 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articles_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='data',
        ),
    ]