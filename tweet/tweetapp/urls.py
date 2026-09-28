from django.urls import path
from . import views 

urlpatterns = [
     path('', views.tweet_list, name='list-all'),
     path('create/', views.create_tweet, name='create'),
     path('<int:tweet_id>/edit/', views.update_tweet, name='update'),
     path('<int:tweet_id>/delete/', views.delete_tweet, name='delete'),
     path('register/', views.register, name='register'),
] 