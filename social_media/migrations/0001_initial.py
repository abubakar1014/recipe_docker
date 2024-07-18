# Generated by Django 5.0 on 2024-07-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('founder', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.TextField(default='n/a')),
                ('description', models.TextField(default='n/a')),
            ],
            options={
                'verbose_name_plural': 'Recipe',
            },
        ),
    ]
