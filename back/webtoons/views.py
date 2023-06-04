from django.shortcuts import render

# Create your views here.

import csv

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Webtoon

data = None
file_dir = './'

def read_data(table_name):
    with open(file_dir + f'{table_name}.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def open_table(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(file_dir + f'{table_name}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for item in bulk_list:
            writer.writerow([
                item.item_name,
                item.story_author,
                item.image_author,
                item.type,
                item.genre,
                item.description,
                item.thumbnail,
                item.item_id
            ])
    return

@login_required
def add_webtoon(request):
    read_data('webtoon')
    if not data:
        return HttpResponse('Nothing to update')

    arr = []
    for row in data:
        arr.append(Webtoon(
            user=request.user,
            item_name=row[0],
            story_author=row[1],
            image_author=row[2],
            type=row[3],
            genre=row[4],
            description=row[5],
            thumbnail=row[6],
            item_id=row[7]
        ))

    open_table('webtoon', Webtoon, arr)
    return HttpResponse('Webtoon table updated')
