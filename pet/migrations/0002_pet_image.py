# Generated by Django 2.2.6 on 2019-12-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='get_image_path/'),
        ),
    ]
