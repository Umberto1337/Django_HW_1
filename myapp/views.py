from django.http import HttpResponse
from django.shortcuts import render
import logging

# Настройка логирования
logger = logging.getLogger(__name__)


def home(request):
    html = """
    <html>
    <head><title>Главная</title></head>
    <body>
    <h1>Добро пожаловать на мой первый сайт</h1>
    <p>Это моя домашняя страница</p>
    </body>
    </html>
    """
    logger.info("Главная страница")
    return HttpResponse(html)


def about(request):
    html = """
    <html>
    <head><title>О нас</title></head>
    <body>
    <h1>О нас</h1>
    <p>Это моя страница о нас</p>
    </body>
    </html>
    """
    logger.info("Страница о нас")
    return HttpResponse(html)