# Generated by Django 4.2.5 on 2023-09-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="file_upload",
            fields=[
                ("ids", models.AutoField(primary_key=True, serialize=False)),
                ("file_name", models.CharField(max_length=255)),
                ("my_file", models.FileField(upload_to="")),
            ],
        ),
    ]
