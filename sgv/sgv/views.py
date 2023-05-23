from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.models import CustomUser
# 임시 맵핑


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def preference(request):
    # 유저가 로그인했는지 확인
    if request.user.is_authenticated:
        visit = request.user.visit
    else:
        return redirect('common:login')
    if visit:
        # 추천 페이지로 바로 진행
        return redirect('sgv:preference')
    else:
        print(visit)
        request.user.visit = False
        request.user.save()
        return render(request, 'sgv/selection.html')
def recommend(request):
    return render(request, 'sgv/recommend.html')