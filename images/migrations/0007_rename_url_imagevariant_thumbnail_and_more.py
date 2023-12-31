# Generated by Django 4.2.5 on 2023-10-01 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "users",
            "0003_rename_originally_uploaded_image_tier_allow_originally_size_image",
        ),
        ("images", "0006_alter_image_thumbnail_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagevariant",
            old_name="url",
            new_name="thumbnail",
        ),
        migrations.RemoveField(
            model_name="image",
            name="thumbnail_link",
        ),
        migrations.AddField(
            model_name="imagevariant",
            name="image",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="images.image",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imagevariant",
            name="option",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.tieroptions",
            ),
            preserve_default=False,
        ),
    ]
