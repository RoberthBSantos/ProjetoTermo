# Generated by Django 2.1.3 on 2021-03-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0054_auto_20210226_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='sub_item',
            field=models.ManyToManyField(blank=True, null=True, related_name='_produtos_sub_item_+', to='contatos.Produtos'),
        ),
    ]
