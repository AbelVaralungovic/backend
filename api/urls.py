from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetAllPosts.as_view(), name='get_all_posts'),
    path('<int:pk>/', views.GetPostDetial.as_view(), name='get_detail')
]
