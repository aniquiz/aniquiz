# Generated by Django 3.0.6 on 2020-10-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
