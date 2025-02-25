# Generated by Django 3.2.25 on 2024-09-25 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkifi_app', '0009_shopee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopeurlone', models.CharField(max_length=600)),
                ('title', models.TextField(max_length=600)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=600)),
                ('selected_picture', models.CharField(blank=True, max_length=255, null=True)),
                ('profileimage', models.ImageField(blank=True, null=True, upload_to='shop/images')),
                ('date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
