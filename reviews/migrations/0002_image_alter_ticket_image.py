# Generated by Django 4.0.6 on 2022-08-09 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.image'),
        ),
    ]
