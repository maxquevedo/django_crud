from django.urls import path
from usuarios import views

urlpatterns = [

    path('',views.user_list,name='user_list'),
    path('new',views.user_create,name='user_new'),
    path('edit/<int:pk>',views.user_update,name='user_update'),
    path('delete/<int:pk>',views.user_delete,name='user_delete'),

]