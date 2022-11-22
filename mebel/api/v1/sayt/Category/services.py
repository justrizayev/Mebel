from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from mebel.settings import PER_PAGE
from sayt.models import Category


def format_ctg(data):
    return OrderedDict([
        ('id', data.id),
        ('content', data.content),
        ('slug', data.slug)
    ])


def paginated_ctg(requests):
    page = int(requests.GET.get('page', 1))
    ctg = Category.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        result.append(format_ctg(ctg[x]))

    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
