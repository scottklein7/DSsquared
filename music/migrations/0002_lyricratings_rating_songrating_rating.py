# Generated by Django 4.0.3 on 2022-03-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyricratings',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songrating',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
