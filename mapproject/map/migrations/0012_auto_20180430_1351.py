# Generated by Django 2.0.3 on 2018-04-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20180430_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='articles',
            field=models.ManyToManyField(blank=True, to='map.Article'),
        ),
    ]
