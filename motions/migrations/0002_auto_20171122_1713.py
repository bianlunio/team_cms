# Generated by Django 2.0rc1 on 2017-11-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motion',
            name='comment',
            field=models.TextField(blank=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='description',
            field=models.TextField(blank=True, verbose_name='题解'),
        ),
    ]
