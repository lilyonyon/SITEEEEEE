# Generated by Django 4.2.11 on 2024-04-25 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_blog_id_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 4, 25, 14, 55, 0, 660984), verbose_name='Опубликована'),
        ),
    ]