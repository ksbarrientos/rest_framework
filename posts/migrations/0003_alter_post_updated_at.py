# Generated by Django 4.1.7 on 2023-04-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
