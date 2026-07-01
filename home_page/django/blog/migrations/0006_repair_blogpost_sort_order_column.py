# Generated manually to repair schema drift on 2026-06-28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blogpost_options_blogpost_sort_order_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                "ALTER TABLE blog_blogpost "
                "ADD COLUMN IF NOT EXISTS sort_order integer NOT NULL DEFAULT 0;"
            ),
            reverse_sql=("ALTER TABLE blog_blogpost DROP COLUMN IF EXISTS sort_order;"),
        ),
        migrations.RunSQL(
            sql=(
                "CREATE INDEX IF NOT EXISTS blog_blogpost_sort_order_8dbf1f84 "
                "ON blog_blogpost (sort_order);"
            ),
            reverse_sql=("DROP INDEX IF EXISTS blog_blogpost_sort_order_8dbf1f84;"),
        ),
    ]
