# Generated by Django 3.2.18 on 2023-05-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.IntegerField(null=True, verbose_name='олень'),
        ),
    ]
