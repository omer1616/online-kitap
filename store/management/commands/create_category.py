from django.core.management import BaseCommand
from store.models.category import Category
import requests


class Command(BaseCommand):

    
    def handle(self, *args , **options):
        url = "https://dummyjson.com/products/categories"

        response = requests.get(url)
        print(response.json())
        categories = response.json()
        for category_name in categories:
            Category.objects.create(name=category_name)
            print("oluşturuldu")





        

