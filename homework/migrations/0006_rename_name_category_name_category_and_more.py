# Generated by Django 4.2.1 on 2023-06-07 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_category_id_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='name_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name_product',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homework.category'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
