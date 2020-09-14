# Generated by Django 2.0.13 on 2020-09-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200914_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='a_da',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_blind',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='post',
            name='num_like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='num_read',
        ),
        migrations.RemoveField(
            model_name='post',
            name='num_reply',
        ),
        migrations.RemoveField(
            model_name='post',
            name='p_dp',
        ),
        migrations.RemoveField(
            model_name='post',
            name='prob_slang',
        ),
        migrations.RemoveField(
            model_name='post',
            name='temp',
        ),
        migrations.AddField(
            model_name='post',
            name='prob_dp',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='prob_n',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='prob_p',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='temperature',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
