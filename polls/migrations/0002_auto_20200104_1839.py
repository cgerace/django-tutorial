# Generated by Django 3.0.2 on 2020-01-04 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pug_date',
            new_name='pub_date',
        ),
    ]
