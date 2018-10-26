# Generated by Django 2.1.2 on 2018-10-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Graph', '0005_auto_20181024_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Graph.Group'),
        ),
        migrations.AlterField(
            model_name='node',
            name='parent_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Graph.Group'),
        ),
    ]