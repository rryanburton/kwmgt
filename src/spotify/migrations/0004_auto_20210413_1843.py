# Generated by Django 3.2 on 2021-04-13 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_auto_20210413_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='followers_url',
            new_name='followers_href',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='followers_count',
            new_name='followers_total',
        ),
    ]
