from django.urls import path 
from . import views

app_name = 'firstapp' #appの名前空間を表す（画面の遷移を指定する場合に用いる）
urlpatterns={
    path('index/',views.index,name='index'),#/helloでアクセスした場合にviewsファイル内のindex関数を表す
    path('page/<str:user_name>',views.user_page,name='user_page'),
    path('number_page/<str:user_name>/<int:number>',views.number_page, name = 'number_page'),
    path('home',views.home, name = 'home')
}