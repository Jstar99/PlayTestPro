# Generated by Django 4.0.5 on 2023-04-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devSide', '0003_project_max_user_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'favicon',
            },
        ),
    ]
