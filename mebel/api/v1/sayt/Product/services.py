from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from mebel.settings import PER_PAGE
from sayt.models import Product


def format_pro(data):
    return OrderedDict([
        ('name', data.name),
        ('price', data.price),
        ('ctg', data.ctg.content if data.ctg else None),
        ('gabarit_uzun', data.gabarit_eni),
        ('gabarit_eni', data.gabarit_eni),
        ('gabarit_baland', data.gabarit_baland),
        ('is_spalni', data.is_spalni),
        ("spalni_uzun", data.spalni_uzun),
        ('spalni_eni', data.spalni_eni),
        ('spalni_baland', data.spalni_baland),
        ('color', data.color)
    ])


def paginated_ctg(requests):
    page = int(requests.GET.get('page', 1))
    ctg = Product.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        result.append(format_pro(ctg[x]))

    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
