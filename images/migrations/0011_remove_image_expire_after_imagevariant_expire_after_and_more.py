# Generated by Django 4.2.5 on 2023-10-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0010_alter_image_seconds"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="expire_after",
        ),
        migrations.AddField(
            model_name="imagevariant",
            name="expire_after",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="imagevariant",
            name="variant_name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]