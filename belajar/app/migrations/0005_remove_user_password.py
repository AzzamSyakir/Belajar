# Generated by Django 4.1.4 on 2023-01-05 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
