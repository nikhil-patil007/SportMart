# Generated by Django 3.0 on 2021-09-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='xyz@12', max_length=100)),
                ('Upassword', models.CharField(default='password', max_length=255)),
            ],
        ),
    ]
