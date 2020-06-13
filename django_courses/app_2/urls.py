from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:year>/', views.year_archive),
    path('home/', views.home, name='home-view'),
    path('book/<chapter>/',views.book,name = 'book'),

    # path('index/', views.index, name='index-view'),
    # path('bio/<username>/', views.bio, name='bio'),
]
