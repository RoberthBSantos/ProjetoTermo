# Generated by Django 3.0.4 on 2021-03-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0063_auto_20210321_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='subitem',
            name='quantidade',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
