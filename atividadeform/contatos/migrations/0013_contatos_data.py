# Generated by Django 2.1.3 on 2020-05-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0012_contatos_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
