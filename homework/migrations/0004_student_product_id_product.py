# Generated by Django 4.2.1 on 2023-06-06 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_remove_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='фамилия')),
                ('is_active', models.BooleanField(default=True, verbose_name='учится')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='id_product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='homework.student'),
        ),
    ]