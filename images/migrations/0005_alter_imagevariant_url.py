# Generated by Django 4.2.5 on 2023-10-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0004_alter_image_thumbnail_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagevariant",
            name="url",
            field=models.ImageField(blank=True, upload_to="thumbnail/"),
        ),
    ]
