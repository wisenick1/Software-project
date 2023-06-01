from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from common.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import Movie
from django.views.decorators.csrf import csrf_exempt


# 임시 맵핑


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


# @login_required(login_url='/common/login/')
def preference(request):
    # 유저가 로그인했는지 확인
    # if request.user.is_authenticated:
    #     visit = request.user.visit
    # else:
    #     return redirect('common:login')
    visit = request.user.visit

    movies = Movie.objects.all()
    visit = False
    if visit:
        # 추천 페이지로 바로 진행
        return redirect('sgv:preference')
    else:
        # print(visit)
        request.user.visit = False
        request.user.save()
        return render(request, 'sgv/selection.html', {'movies': movies})

@csrf_exempt
def toggle_choice(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        movie.choice = not movie.choice
        movie.save()
        return JsonResponse({'success': True})
    except Movie.DoesNotExist:
        return JsonResponse({'success': False})

def recommend(request):
    return render(request, 'sgv/recommend.html')
