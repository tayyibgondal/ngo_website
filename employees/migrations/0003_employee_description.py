# Generated by Django 4.1.4 on 2022-12-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
