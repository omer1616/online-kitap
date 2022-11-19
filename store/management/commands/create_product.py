from django.core.management import BaseCommand
from store.models.product import Product
import requests


class Command(BaseCommand):

    
    def handle(self, *args , **options):
        url = "https://dummyjson.com/products"

        response = requests.get(url)
        print(response.json())
        products = response.json()
        
        for product in products:
            print("--"*100)
            print(product.title)
            print("--"*100)





        

