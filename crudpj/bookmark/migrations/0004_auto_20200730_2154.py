# Generated by Django 3.0.5 on 2020-07-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_bookmark_pavicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='pavicon',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='favicon',
            field=models.ImageField(null=True, upload_to='favi'),
        ),
    ]