# Generated by Django 3.1 on 2020-09-17 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0040_projeto_valor_infra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listamaterial',
            name='projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contatos.projeto'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='fabricante',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
