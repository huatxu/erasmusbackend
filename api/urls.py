from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('comida/', csrf_exempt(views.ComidaList.as_view())),
    path('cerveza/', csrf_exempt(views.CervezaList.as_view())),
]