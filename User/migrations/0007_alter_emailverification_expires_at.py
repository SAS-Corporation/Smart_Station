# Generated by Django 4.2.18 on 2025-02-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_emailverification_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
