# Generated by Django 5.1.1 on 2024-10-28 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ['-nomeCidade']},
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='nome',
            new_name='nomeCidade',
        ),
    ]