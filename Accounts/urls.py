from django.urls import path
from . import views
urlpatterns=[
        path('register',views.register,name="register"),
        path('registeration',views.registration),
        path('logout',views.userlogout,name="logout"),
        
        	]

