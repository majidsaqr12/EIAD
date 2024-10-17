# Generated by Django 5.1.2 on 2024-10-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='og_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='seo_images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='og_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='og_type',
            field=models.CharField(default='website', max_length=50),
        ),
    ]