# Generated by Django 4.2.5 on 2023-10-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0008_image_seconds_alter_imagevariant_option"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="expire_after",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
