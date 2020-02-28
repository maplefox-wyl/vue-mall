from . import views
from django.urls import path,re_path

urlpatterns = [
    path('index', views.index_shop),
    path('add_shop', views.add_shop),
    path("search_shop",views.search_shop),
    re_path(r"mod/(\d+)$",views.mod_shop),
    re_path(r"del/(\d+)$",views.del_shop),
    path("all_shop",views.all_shop),
    path("test",views.test),
]
