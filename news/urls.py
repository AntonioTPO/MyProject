from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('/news/', views.Page.as_view(), name='news_home'),
    path('create', views.NewsCreateArticles.as_view(), name='create'),
    path('/news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('/news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('/news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('login', views.TestWebLoginViews.as_view(), name='login_page'),
    path('register', views.RegUserView.as_view(), name='register_page'),
    path('logout', views.UserLogout.as_view(), name='logout_page'),
]
