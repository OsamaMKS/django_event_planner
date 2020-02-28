# Generated by Django 2.2.5 on 2020-02-28 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_booking', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
