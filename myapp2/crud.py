from .models import Client, Product, Order


# Создание
def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client


def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product


def create_order(client_id, product_ids):
    client = Client.objects.get(id=client_id)
    products = Product.objects.filter(id__in=product_ids)
    total_amount = sum(product.price for product in products)
    order = Order(client=client, total_amount=total_amount)
    order.save()
    order.products.set(products)
    return order


# Чтение
def get_clients(client_id):
    return Client.objects.all(id=client_id)


def get_products(product_id):
    return Product.objects.all(id=product_id)


def get_orders(order_id):
    return Order.objects.all(id=order_id)


# Обновление
def update_client(client_id, name=None, email=None, phone_number=None, address=None):
    client = Client.objects.get(id=client_id)
    if name:
        client.name = name
    if email:
        client.email = email
    if phone_number:
        client.phone_number = phone_number
    if address:
        client.address = address
    client.save()
    return client


def update_product(product_id, name=None, description=None, price=None, quantity=None):
    product = Product.objects.get(id=product_id)
    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if quantity:
        product.quantity = quantity
    product.save()
    return product


def update_order(order_id, client_id=None, product_ids=None):
    order = Order.objects.get(id=order_id)
    if client_id:
        order.client_id = Client.objects.get(id=client_id)
    if product_ids:
        products = Product.objects.filter(id__in=product_ids)
        order.products.set(products)
        order.total_amount = sum([product.price for product in products])
    order.save()
    return order


# Удаление
def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()


def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()


def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()

