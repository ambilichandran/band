# Generated by Django 5.1.1 on 2024-10-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='venue',
            field=models.TextField(null=True),
        ),
    ]
