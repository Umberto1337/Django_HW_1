from django.http import JsonResponse
from .crud import create_client, create_product, create_order
# Импортируйте другие функции CRUD по необходимости


def create_client_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        client = create_client(name, email, phone_number, address)
        return JsonResponse({'id': client.id, 'name': client.name})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def create_product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product = create_product(name, description, price, quantity)
        return JsonResponse({'id': product.id, 'name': product.name})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def create_order_view(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        product_ids = request.POST.getlist('product_ids[]')
        order = create_order(client_id, product_ids)
        return JsonResponse({'id': order.id, 'total_amount': order.total_amount})
    else:
        return JsonResponse({'error': 'Invalid request method'})