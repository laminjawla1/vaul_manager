# Generated by Django 4.1.7 on 2023-10-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_remove_profile_has_return'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ledger',
        ),
    ]
