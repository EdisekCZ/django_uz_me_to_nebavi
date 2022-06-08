from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.GenshinListView.as_view(), name='characters'),
    path('characters/<int:pk>/', views.GenshinDetailView.as_view(), name='character_detail'),
    path('region/', views.RegionListView.as_view(), name='region'),
    path('region/<int:pk>/', views.RegionDetailView.as_view(), name='region_detail'),
]

