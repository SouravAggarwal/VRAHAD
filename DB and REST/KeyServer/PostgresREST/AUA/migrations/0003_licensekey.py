# Generated by Django 2.0.1 on 2018-01-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AUA', '0002_delete_licensekey'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lk', models.CharField(max_length=64)),
                ('ts', models.CharField(default='1515360975', max_length=20)),
            ],
        ),
    ]
