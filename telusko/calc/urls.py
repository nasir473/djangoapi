from django.urls import path

from . import views,time

urlpatterns = [
    path('',views.home,name='home'),
    path('nasir/',views.nasir,name='nasir'),
    path('add', views.add, name='add'),
    path('q1', views.q1, name='q1'),
    path('travello/', views.travello, name='q1'),
    path('restapi', views.restapi, name='restapi'),
    path('table/', views.table, name='table'),
    path('camera/', views.camera, name='camera'),
    path('time/', views.time, name='time')
    #path('time/', time, name='time')
]

