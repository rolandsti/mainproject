# Generated by Django 2.2.2 on 2019-06-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='destription',
            field=models.TextField(default='this is cool'),
        ),
    ]