# Generated by Django 3.0.5 on 2020-06-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200608_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, default='./static/IU.jpg', upload_to='photos/%Y/%m/%d'),
        ),
    ]