# Generated by Django 2.0 on 2021-08-11 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Product_Id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='seller_Id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
