# Generated by Django 5.0 on 2023-12-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_technology_department_created_at_employee_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='technologies',
            field=models.ManyToManyField(to='users.technology'),
        ),
    ]
