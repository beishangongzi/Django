from django.urls import path
from engTV.views import engtv

urlpatterns = [
        path('', engtv),
        path('<int:tvno>/', engtv, name='engtv-url'),
        ]
