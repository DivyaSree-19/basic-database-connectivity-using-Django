# Generated by Django 5.0.2 on 2024-03-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=' ', max_length=20)),
                ('Age', models.IntegerField(default=' ')),
                ('Address', models.CharField(default=' ', max_length=20)),
        
                ('Mail', models.CharField(default=' ', max_length=50)),
            ],
        ),
    ]
