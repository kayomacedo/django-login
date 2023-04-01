from django.urls import path 
from . import views

urlpatterns =[
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/',views.login, name='login'),
    path('plataforma/',views.plataforma, name='plataforma'),
    path('home/',views.home, name='home'),
    path('quests/',views.perguntas, name='perguntas'),
    path('logout/',views.logout_view, name='logout'),
    path('about/',views.about, name='about'),
    path('users/',views.usuarios, name='usuarios'),
 
    
    
     
]