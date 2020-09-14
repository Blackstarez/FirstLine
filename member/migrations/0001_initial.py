# Generated by Django 2.0.13 on 2020-09-14 04:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(max_length=3)),
                ('sex', models.IntegerField(max_length=1)),
                ('email', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('offerInfoAgree', models.IntegerField(max_length=1)),
                ('offerInfoAgreeDay', models.CharField(max_length=14)),
                ('creationDate', models.CharField(max_length=14)),
                ('classification', models.IntegerField(max_length=1)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
