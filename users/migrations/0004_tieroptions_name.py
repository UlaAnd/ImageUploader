# Generated by Django 4.2.5 on 2023-10-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "users",
            "0003_rename_originally_uploaded_image_tier_allow_originally_size_image",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="tieroptions",
            name="name",
            field=models.CharField(default="height", max_length=200),
        ),
    ]
