# Generated by Django 4.2.6 on 2023-10-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
