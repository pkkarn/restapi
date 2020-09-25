# Generated by Django 3.1.1 on 2020-09-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
