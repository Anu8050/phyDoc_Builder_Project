# Generated by Django 4.0.1 on 2022-07-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phyDoc_app', '0006_rename_templateid_document_details_template_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]