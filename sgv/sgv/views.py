from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from common.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import Movie
from django.views.decorators.csrf import csrf_exempt


# 임시 맵핑


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


# Movie값 초기화
def set_all_Movie(movies):
    for movie in movies:
        movie.choice =False
        movie.save()

#@login_required(login_url='/common/login/')
def preference(request):
    #visit = request.user.visit
    movies = Movie.objects.all()
    visit = False
    if visit:
        # 추천 페이지로 바로 진행 현재는 예시
        return redirect('common:login')
    else:
        set_all_Movie(movies)
        # visit값을 선호도 조사가 끝나는 form에서 변화하게끔 변화
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

    #알고리즘 돌리는 부분
    #유저 선호도 가져오고, 이거를 매개변수로 넣으면 알고리즘 돌아가고 webtoon 리턴
    #웹툰 값으로 렌더링
    
    # 최초방문자의 경우 visit값이 False일거라서 Truue
    if request.user.visit:
       print("방문")
    else:
        request.user.visit = True
        request.user.save()
    return render(request, 'sgv/recommend.html')
