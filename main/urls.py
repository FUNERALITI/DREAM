from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('register', views.register, name='register'),
    path('home', views.index, name='home'),
    path('sending', views.sending_post, name='sending'),
    path('blog', views.PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/comments', views.post_detail, name='comments'),
    path('like_post/<int:pk>/', views.like_post, name='like_post')

]