# Generated by Django 3.2.4 on 2021-08-20 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='costField',
        ),
    ]
