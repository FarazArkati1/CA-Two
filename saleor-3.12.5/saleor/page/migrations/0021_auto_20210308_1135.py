# Generated by Django 3.1.7 on 2021-03-08 11:35

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0020_update_content_fields"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="page",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["private_metadata"], name="page_p_meta_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="page",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["metadata"], name="page_meta_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pagetype",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["private_metadata"], name="pagetype_p_meta_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pagetype",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["metadata"], name="pagetype_meta_idx"
            ),
        ),
    ]
