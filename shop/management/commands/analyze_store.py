from decimal import Decimal
from django.db.models import DecimalField,  ExpressionWrapper, Count
from typing import Any
from django.db.models import FloatField
from django.core.management.base import BaseCommand
from shop.models import Tag, Category, Item
from django.db.models import (
    Sum,
    Avg,
    Count,
    Min,
    Max,
    Q,
    F,
)

class Command(BaseCommand):
    def handle(self, *args:Any, **options:Any):
        
        # categories = Category.objects.aggregate(total_count=Count('id'))
        # print(f"Total Items: {categories['total_count']}") #aggregate გამოყენებით თითოეული ვერ დავითვალე ეს ხო ერთ კონრეტულს ითვლის და annotate ით გავაკეთებ ამას
        
        # categories1 = Category.objects.annotate(items_count=Count('items'))
        # for category in categories1:
            # print(f"category:{category.name}, count of items:{category.items_count}")
        
        # categories2 = Category.objects.annotate(max_price=Max('items__price'),min_price=Min('items__price'),avg_price=Avg('items__price'))
        # for category in categories2:
            # print(f"Category: {category.name},Max Price: {category.max_price},Min Price: {category.min_price},Avg Price: {category.avg_price}")

        # ------------------

        # categories4 = Category.objects.annotate(item_count=Count('items'))
        # for category in categories4:
        #     print(f"Category: {category.name}")
        #     print(f"  Category Items Count: {category.item_count}")# პროდუქტის საერთო რაოდენობა (Category Items Count). es zemot gavakete ukve

        # categories3 = Category.objects.annotate(total_sum=Sum('items__price'))
        # for category in categories3:
        #     print(f"category>{category.name} :sum-->{category.total_sum}")

        # --------------------
        # items = Item.objects.select_related('category')
        # for item in items:
        #     print(f"f item:{item.name}  //is from:{item.category.name}/category")

        tags= Tag.objects.prefetch_related('items').all()
        for tag in tags:
            print(tag.name, [item.name for item in tag.items.all()])
