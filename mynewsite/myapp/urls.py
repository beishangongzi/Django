from django.urls import path

from myapp.views import about, listing, disp_detail, index

urlpatterns = [
    path('about/', about),
    path("list/", listing),
    path("list/<int:sku>", disp_detail),
    path("", index)
]