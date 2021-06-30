from django.db.models.query import ValuesIterable
from django.urls import path     
from . import views
urlpatterns = [
    
    path('', views.home),
    path('main',views.index),
    path('main/create',views.create),
    path('main/<int:id>/confirmar',views.confirmar),
    path('main/<int:id>/destroy', views.destroy),
    ]