# Generated by Django 3.2.12 on 2022-04-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zion', '0002_auto_20220324_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_linkes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_url', models.CharField(blank=True, max_length=50)),
                ('url', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]