# Generated by Django 3.2.25 on 2024-09-25 05:49

from django.db import migrations, models
import linkifi_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('linkifi_app', '0005_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='platform_images/', validators=[linkifi_app.validators.validate_svg])),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlatformFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='platform_images/', validators=[linkifi_app.validators.validate_svg])),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Platformone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='platform_images/', validators=[linkifi_app.validators.validate_svg])),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlatformThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='platform_images/', validators=[linkifi_app.validators.validate_svg])),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
