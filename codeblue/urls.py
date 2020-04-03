from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updateroom/',views.updateroom),
    path('getroom/',views.get_room),
    path('getlog/',views.getlog),
    path('map/', views.index),
    path('', views.map),
    path('loadroom/', views.loadroom),
    # path('ajaxupdate/',views.ajaxupdate),
]
