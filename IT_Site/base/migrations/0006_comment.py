# Generated by Django 4.1.3 on 2023-01-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
