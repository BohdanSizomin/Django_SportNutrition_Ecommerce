# Generated by Django 3.2.9 on 2021-12-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_variation'),
        ('orders', '0003_auto_20211216_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='home.Variation'),
        ),
    ]