# Generated by Django 3.2.18 on 2023-04-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0006_alter_userprofiile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
