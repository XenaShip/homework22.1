# Generated by Django 4.2.2 on 2023-07-16 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0010_alter_product_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('version_number',), 'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AddField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Признак версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='homework.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.PositiveIntegerField(verbose_name='Номер версии'),
        ),
    ]
