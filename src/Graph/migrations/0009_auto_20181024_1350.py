# Generated by Django 2.1.2 on 2018-10-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graph', '0008_auto_20181024_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_id',
            field=models.IntegerField(),
        ),
    ]
