# Generated by Django 3.1.6 on 2021-02-27 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0003_auto_20210227_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
