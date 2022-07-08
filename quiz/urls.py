from django.urls import path
from . import views

urlpatterns=[
    path('start',views.start_quiz,name='start'),
    path('autocad',views.index,name='index'),
    path('matlab',views.index1,name='index1'),
    path('cloudcomputing',views.index2,name='index2'),
    path('CyberSecurity',views.index3,name='index3'),
    path('PCBdesigning',views.index4,name='index4'),
    path('python',views.index5,name='index5')
]