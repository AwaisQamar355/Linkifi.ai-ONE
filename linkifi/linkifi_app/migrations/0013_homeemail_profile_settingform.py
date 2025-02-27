# Generated by Django 3.2.25 on 2024-09-25 05:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkifi_app', '0012_orderproduct_urladmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeemail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Settingform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settingurl', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='shop/images')),
                ('selected_picture', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
