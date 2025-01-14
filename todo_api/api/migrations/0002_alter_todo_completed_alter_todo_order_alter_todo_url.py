# Generated by Django 5.1.4 on 2025-01-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
