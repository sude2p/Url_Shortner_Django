# Generated by Django 5.0.2 on 2024-03-01 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0004_alter_url_short_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='url',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
