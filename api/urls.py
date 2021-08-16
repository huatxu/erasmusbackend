from django.urls import path
from api import views


urlpatterns = [
    path('comida/', views.ComidaList.as_view()),
    path('cerveza/', views.CervezaList.as_view()),
]