# Generated by Django 2.0.13 on 2020-09-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='classification',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='offerInfoAgree',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='sex',
            field=models.IntegerField(max_length=1),
        ),
    ]
