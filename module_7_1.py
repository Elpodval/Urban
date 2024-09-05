
# -*- coding: utf-8 -*-

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read().strip()
            return products
        except FileNotFoundError:
            return ''

    def add(self, *products):
        current_products = self.get_products().split('\n')
        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = f"{product.name}, {product.weight}, {product.category}"
                if product_str not in current_products:
                    file.write(product_str + '\n')
                else:
                    print(f"Продукт {product_str} уже есть в магазине")
        file.close()

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())