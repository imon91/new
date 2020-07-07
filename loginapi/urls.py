from django.contrib import admin
from django.urls import path, include
from loginapi import views
from .views import userView, UserCreate, taskView, taskDetail, taskEdit, taskDelete, taskCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', userView.as_view(), name='list'),
    # path('<str:section_name>/', BlogDetail.as_view(), name='detail'),
    path('<int:pk>/detail', taskDetail.as_view(), name='taskDetail'),
    path('<int:pk>/taskEdit', taskEdit.as_view(), name='taskEdit'),
    # path('<int:pk>/delete', BlogDelete.as_view(), name='delete'),
    # path('create', BlogCreate.as_view(), name='create'),
    # path('c', BlogSearch.as_view(), name='search'),
    # path('fetch', BlogFetch.as_view(), name='fetch'),
    path('userCreate', UserCreate.as_view(), name='UserCreate'),
    path('taskView', taskView.as_view(), name='taskView'),
    path('taskCreate', taskCreate.as_view(), name='taskCreate'),
    path('<int:pk>/taskDelete', taskDelete.as_view(), name='taskDelete'),
     #path('', UserCreate.as_view(), name='UserCreate'),
    # path('UserLogin', UserLogin.as_view(), name='UserLogin'),

]

