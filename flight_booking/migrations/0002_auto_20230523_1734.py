# Generated by Django 2.2.12 on 2024-01-10 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='bookead_seat',
            new_name='booked_seats',
        ),
    ]
