# Generated by Django 4.0.1 on 2022-01-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='model_image',
            field=models.ImageField(default='default.jpg', upload_to='model_images/'),
        ),
    ]
