# Generated by Django 3.2.4 on 2021-06-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
