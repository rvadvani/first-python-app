# Generated by Django 5.0 on 2024-01-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_employee_technologies'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
