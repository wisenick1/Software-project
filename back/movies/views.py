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
from .models import Movie
from webtoons.models import Webtoon

def preprocess_text(text):
    # 텍스트 전처리 함수: 소문자 변환, 특수 문자 제거 등
    text = text.lower()  # 소문자 변환
    text = re.sub(r'[^가-힣\s]', '', text)  # 특수 문자 제거
    return text

def analyze_webtoon_genre(webtoon_descriptions):
    file = open('stopword.txt', 'r', encoding='utf-8')
    stop_words = file.read().splitlines()
    
    # 텍스트 전처리
    preprocessed_descriptions = [preprocess_text(desc) for desc in webtoon_descriptions]
    
    # TF-IDF 벡터화 객체를 생성합니다.
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    
    # 웹툰 설명을 벡터화합니다.
    X = vectorizer.fit_transform(webtoon_descriptions)
    
    # K-means 클러스터링을 수행합니다.
    kmeans = KMeans(n_clusters = 25)  # 장르를 n개로 클러스터링하도록 설정합니다.
    kmeans.fit(X)
    
    # 각 웹툰에 대한 클러스터 할당 결과를 가져옵니다.
    labels = kmeans.labels_
    
    return labels

def recommend(movie1, movie2, movie3, movie1_p = 10, movie2_p = 10, movie3_p = 10):
    webtoon_count = 10 # 추천할 웹툰 수
    movie_count = 3 # 선호하는 영화 수
    
    # data = pd.read_csv('webtoon_articles.csv') # db에서 웹툰 가져오기
    web = Webtoon.objects.all()

    # Django 쿼리셋을 리스트로 변환
    web_list = list(web)

    # 쿼리셋의 각 인스턴스에서 필드 값을 추출하여 딕셔너리로 저장
    data_web = {
        'user': [w.user for w in web_list],
        'item_name': [w.item_name for w in web_list],
        'story_author': [w.story_author for w in web_list],
        'image_author': [w.image_author for w in web_list],
        'type': [w.type for w in web_list],
        'genre': [w.genre for w in web_list],
        'description': [w.description for w in web_list],
        'thumbnail': [w.thumbnail for w in web_list],
        'item_id': [w.item_id for w in web_list]
    }

    # 딕셔너리를 Pandas DataFrame으로 변환
    data = pd.DataFrame(data_web)
    
    # mdata = pd.read_csv('movie.csv') # db에서 영화 가져오기
    mov = Movie.objects.all()

    # Django 쿼리셋을 리스트로 변환
    mov_list = list(mov)

    # 쿼리셋의 각 인스턴스에서 필드 값을 추출하여 딕셔너리로 저장
    data_mov = {
        'user': [m.user for m in mov_list],
        'item_name': [m.item_name for m in mov_list],
        'genre': [m.genre1 for m in mov_list],
        'genre2': [m.genre2 for m in mov_list],
        'description': [m.description for m in mov_list]
    }

    # 딕셔너리를 Pandas DataFrame으로 변환
    data = pd.DataFrame(data_web)
    mdata = pd.DataFrame(data_mov)
    
    wdata = data[['item_name', 'genre', 'description']]
    wdata['check'] = 'w'
    mdata['check'] = 'm'
    wdata['genre2'] = ''
    fdata = pd.concat([mdata, wdata])

    # Description으로 장르 분석
    webtoon_descriptions = fdata['description']
    genre_labels = analyze_webtoon_genre(webtoon_descriptions)
    fdata['descriptionPoint'] = genre_labels

    # 원-핫 인코딩
    incoded = pd.get_dummies(fdata, columns = ['descriptionPoint'])

    # genre1에 대한 원-핫 인코딩
    oneHot_genre1 = pd.get_dummies(fdata['genre'])

    # genre2를 genre1의 값으로 대체하여 원-핫 인코딩
    fdata['genre2'] = fdata['genre'].where(fdata['genre2'] == '', fdata['genre2'])
    oneHot_genre2 = pd.get_dummies(fdata['genre2'].apply(lambda x:x))

    # 영화 장르1, 장르2 백터 합치기
    for i in range(len(movie_data)):
        movie_oneHot = oneHot_genre1 + oneHot_genre2
    movie_oneHot = movie_oneHot/2

    # 원-핫 인코딩된 장르와 줄거리 concat
    oneHotIncoded = pd.concat([incoded, movie_oneHot], axis=1)

    # 영화 웹툰 분리
    groups = oneHotIncoded.groupby(oneHotIncoded.check)
    movie = groups.get_group("m")
    webtoon = groups.get_group("w")

    # 백터 생성
    userMovie = np.zeros(len(movie.columns) - 5, dtype = float)

    # movie 입력 형식에 따라 수정, 현재는 index
    userMovie = userMovie + movie1_p*movie.iloc[int(movie1), 5:].values
    userMovie = userMovie + movie2_p*movie.iloc[int(movie2), 5:].values
    userMovie = userMovie + movie3_p*movie.iloc[int(movie3), 5:].values

    cosSim = pd.DataFrame([0])

    for i in range(len(webtoon)):
        # 벡터를 NumPy 배열로 변환
        vector1 = np.array(userMovie)
        vector2 = np.array(webtoon.iloc[i, 5:].values)

        # 내적 계산
        dot_product = np.dot(vector1, vector2)

        # 각 벡터의 크기 계산
        magnitude1 = np.linalg.norm(vector1)
        magnitude2 = np.linalg.norm(vector2)

        # 코사인 유사도 계산
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
        cosSim.loc[i] = [cosine_similarity]

    # 코사인 유사도에 따라 웹툰 인덱스와 코사인 유사도 값 저장
    top_values = cosSim[0].nlargest(webtoon_count)

    # array형식으로 이름 return
    return webtoon['item_name'][top_values.index].values
