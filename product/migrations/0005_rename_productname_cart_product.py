# Generated by Django 3.2.12 on 2022-05-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='productName',
            new_name='product',
        ),
    ]