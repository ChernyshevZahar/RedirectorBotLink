# Generated by Django 5.1.6 on 2025-03-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('getlink', models.CharField(max_length=100)),
                ('postLink', models.CharField(max_length=100)),
            ],
        ),
    ]
