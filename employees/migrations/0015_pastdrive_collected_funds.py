# Generated by Django 4.1.2 on 2022-12-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_pitch_phone_no_alter_volunteer_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastdrive',
            name='collected_funds',
            field=models.IntegerField(default=2345),
            preserve_default=False,
        ),
    ]
