# Generated by Django 2.2.5 on 2019-12-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]