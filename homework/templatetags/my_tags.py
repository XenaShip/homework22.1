from django import template

register = template.Library()


@register.simple_tag
def media_path(image):
    path_image = '/media/' + image.name
    return path_image


@register.filter(name='mediapath')
def filter_media_path(image):
    path_image = '/media/' + image.name
    return path_image
