# Generated by Django 4.1.3 on 2023-01-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_advert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('speaker', models.CharField(max_length=200)),
                ('event_img', models.ImageField(upload_to='static/images/events')),
            ],
        ),
    ]
