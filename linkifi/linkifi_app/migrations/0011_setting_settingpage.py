# Generated by Django 3.2.25 on 2024-09-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkifi_app', '0010_shopproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seotitle', models.CharField(max_length=500)),
                ('seodescription', models.CharField(max_length=400)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SettingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pexiid', models.IntegerField()),
                ('api', models.CharField(max_length=500)),
                ('googleid', models.CharField(max_length=400)),
                ('date', models.DateField()),
            ],
        ),
    ]
