# Generated by Django 4.0.3 on 2022-03-30 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_artiles_articles_alter_articles_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='full_tex',
            new_name='full_text',
        ),
    ]
