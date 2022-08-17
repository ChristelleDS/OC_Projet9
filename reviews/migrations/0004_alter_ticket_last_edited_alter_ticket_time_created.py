# Generated by Django 4.0.6 on 2022-08-17 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_ticket_image_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='last_edited',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
