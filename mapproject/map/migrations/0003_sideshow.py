# Generated by Django 2.0.3 on 2018-04-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20180416_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sideshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_by', models.CharField(max_length=30)),
                ('publish_date', models.DateField(verbose_name='Publication date')),
                ('article_synopsis', models.TextField(max_length=1000)),
                ('url', models.URLField()),
            ],
        ),
    ]
