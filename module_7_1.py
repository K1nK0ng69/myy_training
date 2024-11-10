class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products = self.get_products().splitlines()
        current_product_info = {line for line in current_products}

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str not in current_product_info:
                    file.write(product_str + '\n')
                    current_product_info.add(product_str)
                else:
                    print(f"Продукт {product_str} уже есть в магазине")


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Проверка вывода продукта
print(p2)  # Spaghetti, 3.4, Groceries

# Добавление продуктов в магазин
s1.add(p1, p2, p3)

# Получение всех продуктов из файла
print(s1.get_products())
