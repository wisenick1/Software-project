from django.shortcuts import render


# Create your views here.

import csv

from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

data = None
file_dir = 'movie_csv_file_directory'


def read_data(table_name):
    with open(file_dir + f'{table_name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def open_table(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(file_dir + f'{table_name}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_movies(request):
    read_data('movies')
    if not data:
        return HttpResponse('Nothing to update')

    arr = []
    for row in data:
        arr.append(Movie(
            item_name=row[0],
            genre1=row[1],
            genre2=row[2],
            description=row[3]
        ))

    open_table('movies', Movie, arr)
    return HttpResponse('Movie table updated')

###영화 추천 알고리즘
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


