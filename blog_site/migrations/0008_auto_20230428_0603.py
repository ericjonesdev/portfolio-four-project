# Generated by Django 3.2.18 on 2023-04-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0007_alter_userprofiile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiile',
            name='github',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiile',
            name='twitter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
