# Generated by Django 4.1.3 on 2023-03-22 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym_website',
            name='address',
        ),
    ]