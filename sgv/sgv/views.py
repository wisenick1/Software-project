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
    Movie.objects.create(
        id=1,
        title="영화1",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=2,
        title="영화2",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=3,
        title="영화3",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=4,
        title="영화4",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=5,
        title="영화5",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=6,
        title="영화6",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=7,
        title="영화7",
        genre="드라마",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    Movie.objects.create(
        id=8,
        title="영화8",
        genre="액션",
        poster_path="https://image.tmdb.org/t/p/w500/xoqr4dMbRJnzuhsWDF3XNHQwJ9x.jpg"
    )
    movies = Movie.objects.all()
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
        movie.save()
        print(movie.title)
        print(movie.choice)
        return JsonResponse({'success': True, 'choice': movie.choice})
    except Movie.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Movie not found'})
@csrf_exempt
def toggle_choice(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    print(movie.id)
    movie.choice = not movie.choice
    print(movie.choice)
    movie.save()
    return redirect('sgv:preference')

@csrf_exempt
def update_movie_choice(request):
    if request.method == "POST" and request.is_ajax():
        movie_id = request.POST.get("movie_id")
        movie_choice = request.POST.get("movie_choice")
        print(movie_choice)
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.choice = not movie_choice
            print(movie.choice)
            movie.save()
            return JsonResponse({"success": True})
        except Movie.DoesNotExist:
            return JsonResponse({"success": False, "error": "Movie not found"})

    return JsonResponse({"success": False, "error": "Invalid request"})
