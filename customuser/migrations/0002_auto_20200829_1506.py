# Generated by Django 3.0.8 on 2020-08-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.TextField(blank=True, max_length=12),
        ),
    ]
