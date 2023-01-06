# Generated by Django 4.1.3 on 2023-01-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/course'),
        ),
        migrations.AddField(
            model_name='course',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='module_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/module'),
        ),
        migrations.RemoveField(
            model_name='module',
            name='course',
        ),
        migrations.AlterField(
            model_name='module',
            name='staff_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/staff'),
        ),
        migrations.AddField(
            model_name='module',
            name='course',
            field=models.ManyToManyField(to='base.course'),
        ),
    ]
