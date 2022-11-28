from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'bunks'
urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('<str:username>/', views.UserFeedView.as_view(), name='user_feed'),
    path('<str:username>/bunk', views.bunk, name='bunk')
]
