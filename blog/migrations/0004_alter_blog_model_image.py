# Generated by Django 4.0.1 on 2022-01-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='model_image',
            field=models.ImageField(default='', upload_to='model_images/'),
        ),
    ]
