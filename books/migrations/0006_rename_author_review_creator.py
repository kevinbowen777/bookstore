# Generated by Django 4.1.2 on 2022-10-21 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_book_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="author",
            new_name="creator",
        ),
    ]