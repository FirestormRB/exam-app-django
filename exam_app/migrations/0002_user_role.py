# Generated by Django 2.0 on 2019-07-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(2, 'Student'), (1, 'Super Admin'), (3, 'Teacher')], default=1),
        ),
    ]
