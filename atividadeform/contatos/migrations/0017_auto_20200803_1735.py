# Generated by Django 2.1.3 on 2020-08-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0016_auto_20200507_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='nome',
            field=models.CharField(max_length=300),
        ),
    ]
