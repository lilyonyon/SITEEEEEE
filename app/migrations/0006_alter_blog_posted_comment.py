# Generated by Django 4.2.11 on 2024-05-11 15:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 5, 11, 18, 54, 46, 636158), verbose_name='Опубликована'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2024, 5, 11, 18, 54, 46, 636158), verbose_name='Дата комментария')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog', verbose_name='Статья комментария')),
            ],
            options={
                'verbose_name': 'Комментарии к статье блога',
                'verbose_name_plural': 'Комментарии к статьям блога',
                'db_table': 'Comment',
                'ordering': ['-date'],
            },
        ),
    ]
