# Generated by Django 2.2.5 on 2020-02-27 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('seats', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
