# Generated by Django 2.1.3 on 2020-05-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0013_contatos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
