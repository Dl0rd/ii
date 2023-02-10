# Generated by Django 4.1.5 on 2023-02-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(verbose_name='Текст для предсказаний')),
            ],
            options={
                'verbose_name': 'Предсказание',
                'verbose_name_plural': 'Предсказания',
            },
        ),
    ]
