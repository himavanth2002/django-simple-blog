from django.urls import path
from . import views
urlpatterns=[ 
    path('',views.iindex,name='iindex'),
    path('post/<str:pk>',views.post,name='post')
]