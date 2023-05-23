from django.contrib import admin
from django.urls import path, include
# from sgv import views
# from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sgv/', include('sgv.urls')),
    path('common/', include('common.urls')),
]
