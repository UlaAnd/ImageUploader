# Generated by Django 4.2.5 on 2023-10-01 16:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_userprofile_tier"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tier",
            old_name="originally_uploaded_image",
            new_name="allow_originally_size_image",
        ),
    ]
