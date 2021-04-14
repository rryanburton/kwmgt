# Generated by Django 3.2 on 2021-04-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_auto_20210413_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='followers',
            new_name='followers_count',
        ),
        migrations.AddField(
            model_name='artist',
            name='followers_url',
            field=models.URLField(null=True),
        ),
    ]
