# Generated by Django 3.2.16 on 2023-01-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20230124_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staf',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='superuser'),
        ),
    ]
