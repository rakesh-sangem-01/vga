from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('registercall/', views.registercall, name='registercall'),
    path('registerlogic/', views.registerlogic, name='registerlogic'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('logout/', views.logout, name='logout'),
    #path('base/', views.base, name='base'),
]