# Generated by Django 4.0.1 on 2022-07-13 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phyDoc_app', '0005_alter_document_templates_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document_details',
            old_name='templateid',
            new_name='template_name',
        ),
    ]
