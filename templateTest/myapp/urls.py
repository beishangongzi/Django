from django.urls import path
from myapp.views import index

urlpatterns = [
        path('<int:tvno>/', index, name='tv-url'),
        path('', index),
        ]
