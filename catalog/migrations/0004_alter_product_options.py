# Generated by Django 4.2.14 on 2024-07-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_edit_category', 'Can edit category'), ('can_edit_description', 'Can edit description')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
