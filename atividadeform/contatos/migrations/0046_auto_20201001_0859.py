# Generated by Django 3.1 on 2020-10-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0045_auto_20200928_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='valor_de_terceiros',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
