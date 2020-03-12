from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updateroom/',views.updateroom),
    path('getroom/',views.get_room),
    path('getlog/',views.getlog),
    path('map/', views.map),
    path('', views.index),
    # path('ajaxupdate/',views.ajaxupdate),
]
