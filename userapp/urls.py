from django.urls import path, include
from . import views
app_name = 'userapp'
urlpatterns = [
    path('userhomepage/', views.userhomepage, name='userhomepage'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('gardeningtips/', views.gardeningtips, name='gardeningtips'),
    path('contactsupport/', views.contactsupport, name='contactsupport'),
    path('gardeningplanning/', views.gardeningplanning, name='gardeningplanning'),
]