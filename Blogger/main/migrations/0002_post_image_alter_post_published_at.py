# Generated by Django 5.2.4 on 2025-07-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.jpeg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(),
        ),
    ]
