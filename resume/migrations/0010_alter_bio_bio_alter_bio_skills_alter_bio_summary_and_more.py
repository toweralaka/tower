# Generated by Django 4.1 on 2024-02-28 12:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0009_project_repository"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bio",
            name="bio",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="bio",
            name="skills",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="bio",
            name="summary",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="education",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="experience",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="experience",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="skill",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
