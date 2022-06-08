from django.urls import path
from Game_warframe_1 import views

urlpatterns = [
    #path(route, view, kwargs=None, name=None
    path('index/', views.index,name='index'),


    path('name/', views.name,name='name'),
    path('<int:question_id>',views.vote,name='vote'),
    path('add_user/',views.add_user,name = 'add_user'),
    path('select_user/',views.select_user,name = 'select_user')
]