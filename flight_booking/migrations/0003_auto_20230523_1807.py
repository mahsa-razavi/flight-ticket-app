# Generated by Django 2.2.12 on 2024-01-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0002_auto_20230523_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='country',
            new_name='state',
        ),
    ]
