# Generated by Django 4.1.7 on 2023-03-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_project_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
