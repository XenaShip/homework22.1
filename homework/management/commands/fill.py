from django.core.management import BaseCommand
from homework.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()


        category_list = [
            {'pk': 1, 'name_category': 'молочные продукты', 'description': 'то, что сделано из молока'},
            {'pk': 2, 'name_category': 'бытовая техника', 'description': 'все для удобства в доме'},
            {'pk': 3, 'name_category': 'игрушки', 'description': 'то, чем дети играют'},
            {'pk': 4, 'name_category': 'зоотовары', 'description': 'товары для животных и ухода за ними'}
        ]
        category_objects = []
        for category_item in category_list:
            category_objects.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_objects)

        product_list = [
            {'name_product': 'кефир', 'description': 'то, что любит папа', 'preview': 'photo_2022-04-11_19-53-41.jpg',
             'category': Category.objects.get(pk=1), 'price': '20', 'made': '2023-06-05', 'change': '2023-06-05'},
            {'name_product': 'творог', 'description': 'то, что любит Лили', 'preview': 'photo_2022-04-11_19-53-41.jpg',
             'category': Category.objects.get(pk=1), 'price': '30', 'made': '2023-06-05', 'change': '2023-06-06'},
            {'name_product': 'холодильник', 'description': 'техника для хранения еды',
             'preview': 'photo_2022-04-11_19-53-41.jpg', 'category': Category.objects.get(pk=2), 'price': '15', 'made': '2023-06-08',
             'change': '2023-06-07'},
            {'name_product': 'кость', 'description': 'то, что грызет собака',
             'preview': 'photo_2022-04-11_19-53-41.jpg', 'category': Category.objects.get(pk=4), 'price': '20', 'made': '2023-06-05',
             'change': '2023-06-05'},
        ]

        product_objects = []
        for product_item in product_list:
            product_objects.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(product_objects)
