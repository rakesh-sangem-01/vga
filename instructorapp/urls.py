from django.urls import path, include
from . import views
app_name = 'instructorapp'
urlpatterns = [
    path('instructorhomepage/', views.instructorhomepage, name='instructorhomepage'),
    path('sharegardeningtips/', views.sharegardeningtips, name='sharegardeningtips'),
    path('contactsupport/', views.contactsupport, name='contactsupport'),
]

