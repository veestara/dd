from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('sunpac_view/', views.sunpac_view, name='sunpac_view'),
    path('test/',views.test, name='test')
]
