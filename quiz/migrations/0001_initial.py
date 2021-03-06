# Generated by Django 2.2.2 on 2019-09-07 18:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(blank=True, max_length=5000)),
                ('possible_answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5000), size=None)),
                ('correct_answer', models.CharField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000)),
                ('questions', models.ManyToManyField(to='quiz.Question')),
            ],
        ),
    ]
