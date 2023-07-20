from django.contrib import admin
from homework.models import Product, Category, Note, Version
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name_product', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category')
    list_filter = ('name_category',)
    search_fields = ('name_category', 'description',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'the_text', 'image', 'made', 'published', 'views',)
    list_filter = ('name',)
    search_fields = ('name', 'made',)

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active',)
    list_filter = ('product',)
    search_fields = ('version_name', 'product',)