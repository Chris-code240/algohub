from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home),
    path('start/',views.start_page),
    path('analyze/',views.analyze_code)
]