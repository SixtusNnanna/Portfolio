from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('portfolio', views.projectList, name='project-list' ),
    path('portfolio/<int:project_id>/', views.projectDetail, name='project_detail'),
    path('blog', views.postList, name='post-list'),
    path('blog/<int:post_id>/', views.postDetail, name='post_detail' ),
    path('blog/<category>/', views.categoryPost, name ="category_post"),

]