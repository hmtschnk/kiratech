# Generated by Django 4.0.5 on 2022-06-25 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='author',
            new_name='suuplier',
        ),
    ]
