# Generated by Django 3.1.3 on 2020-12-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
