# Generated by Django 2.1.2 on 2018-10-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleus', '0002_repo_saved_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
