from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from common.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import Movie
from django.views.decorators.csrf import csrf_exempt

# 임시 맵핑


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


@login_required(login_url='/common/login/')
def preference(request):
    # 유저가 로그인했는지 확인
    # if request.user.is_authenticated:
    #     visit = request.user.visit
    # else:
    #     return redirect('common:login')
    visit = request.user.visit
    movie1 = Movie(
        id=1,
        title="영화1",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie2 = Movie(
        id=2,
        title="영화2",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie3 = Movie(
        id=3,
        title="영화3",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie4 = Movie(
        id=4,
        title="영화4",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie5 = Movie(
        id=5,
        title="영화5",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie6 = Movie(
        id=6,
        title="영화6",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie7 = Movie(
        id=7,
        title="영화7",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie8 = Movie(
        id=8,
        title="영화8",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie9 = Movie(
        id=9,
        title="영화9",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie10 = Movie(
        id=10,
        title="영화10",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie11 = Movie(
        id=11,
        title="영화11",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movie12 = Movie(
        id=12,
        title="영화12",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11]
    visit = False
    if visit:
        # 추천 페이지로 바로 진행
        return redirect('sgv:preference')
    else:
        #print(visit)
        request.user.visit = False
        request.user.save()
        return render(request, 'sgv/selection.html', {'movies': movies})


def recommend(request):
    return render(request, 'sgv/recommend.html')

@csrf_exempt
def toggle_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        movie.choice = not movie.choice
        print("True")
        movie.save()
        return JsonResponse({'success': True})
    except Movie.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Movie not found'})

