from django.urls import path
from myapp import views
urlpatterns = [
        path('', views.index, name='view-index'),
        path('<int:pid>/<str:del_pass>/', views.index, name='view_del')
            ]
