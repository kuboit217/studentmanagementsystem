# Generated by Django 3.1.6 on 2021-02-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentmanagementapp.courses'),
        ),
    ]