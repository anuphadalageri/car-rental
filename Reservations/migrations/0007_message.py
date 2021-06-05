# Generated by Django 3.1.3 on 2021-01-13 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservations', '0006_auto_20210109_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('reciever', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Reservations.visitor')),
            ],
        ),
    ]