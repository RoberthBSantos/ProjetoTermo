# Generated by Django 2.1.3 on 2020-05-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0011_contatos_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='modelo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
