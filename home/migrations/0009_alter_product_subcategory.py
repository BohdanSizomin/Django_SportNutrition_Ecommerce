# Generated by Django 3.2.9 on 2021-12-27 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.subcategory'),
        ),
    ]
