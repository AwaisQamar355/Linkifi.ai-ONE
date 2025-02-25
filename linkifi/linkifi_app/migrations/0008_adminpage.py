# Generated by Django 3.2.25 on 2024-09-25 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import linkifi_app.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkifi_app', '0007_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='platform_images/', validators=[linkifi_app.validators.validate_svg])),
                ('date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
