# Generated by Django 5.1.1 on 2024-10-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_produto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='dataVencimento',
            field=models.DateField(blank=True, null=True, verbose_name='data'),
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
