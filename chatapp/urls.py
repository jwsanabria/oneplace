from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatapp/<int:id>/', views.chatapp, name='chatapp'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('accounts/social/login/cancelled/', views.login_cancelled, name='login_cancelled'),

]