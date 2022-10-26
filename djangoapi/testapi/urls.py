from django.urls import path
from . import views
urlpatterns = [
    path('insdata', views.ins_data),
    path('deldata', views.del_data),
    path('putdata', views.update_data),
    path('getdata/', views.get_data),
]
