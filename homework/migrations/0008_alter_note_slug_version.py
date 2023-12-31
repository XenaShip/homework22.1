# Generated by Django 4.2.2 on 2023-07-09 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0007_note_alter_product_change_alter_product_made_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.CharField(max_length=255, unique_for_date='made', verbose_name='слаг'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(max_length=20, verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=100, verbose_name='название версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
