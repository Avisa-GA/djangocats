# Generated by Django 4.0.3 on 2022-04-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_cattoy'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='cattoys',
            field=models.ManyToManyField(to='main_app.cattoy'),
        ),
    ]
