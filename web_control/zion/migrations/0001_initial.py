# Generated by Django 3.2.12 on 2022-03-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passport_series', models.CharField(blank=True, max_length=10)),
                ('Passport_number', models.CharField(blank=True, max_length=40)),
                ('Passport_received', models.CharField(blank=True, max_length=60)),
                ('Location', models.CharField(blank=True, max_length=30)),
                ('School_name', models.CharField(blank=True, max_length=60)),
                ('School_class', models.CharField(blank=True, max_length=10)),
                ('Birth_date', models.DateField(blank=True, null=True)),
                ('Phone', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(blank=True, max_length=10)),
                ('id_stepik', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
