from django.shortcuts import render
from django.utils.timezone import now, timedelta
from .models import Order


def ordered_products(request):
    user = request.user
    week_ago = now() - timedelta(days=7)
    month_ago = now() - timedelta(days=30)
    year_ago = now() - timedelta(days=365)

    week_orders = Order.objects.filter(user=user, created_at__gte=week_ago)
    month_orders = Order.objects.filter(user=user, created_at__gte=month_ago)
    year_orders = Order.objects.filter(user=user, created_at__gte=year_ago)

    week_products = set(product for order in week_orders for product in order.products.all())
    month_products = set(product for order in month_orders for product in order.products.all())
    year_products = set(product for order in year_orders for product in order.products.all())

    context = {
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products,
    }

    return render(request, 'orders/ordered_products.html', context)
