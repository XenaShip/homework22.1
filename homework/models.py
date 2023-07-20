import uuid
from django.utils.text import slugify
from django.db import models
# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='цена')
    made = models.DateField(verbose_name='изготовлено', auto_now_add=True)
    change = models.DateField(verbose_name='изменено', auto_now=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.pk} {self.name_product} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name_category = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.pk} {self.name_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Note(models.Model):
    name = models.CharField(max_length=70, verbose_name='заголовок')
    slug = models.CharField(max_length=255, verbose_name='слаг', unique_for_date='made')
    the_text = models.CharField(max_length=200, verbose_name='текст')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', null=True)
    made = models.DateField(verbose_name='изготовлено', auto_now_add=True)
    published = models.BooleanField(verbose_name='опубликовано', default=False)
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0)

    def views_up(self):
        self.views += 1

    def __str__(self):
        return f'Статья: {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            title = str(self.name)
            string = title.translate(
                str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                              "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
            self.slug = slugify(string)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ('-made',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='version')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии', null=False, blank=False)
    version_name = models.CharField(max_length=50, verbose_name='Имя версии', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Признак версии')

    def __str__(self):
        return f'{self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)
