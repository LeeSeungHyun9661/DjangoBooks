from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
   path('login', login, name='login'),     
   path('logout', logout, name='logout'),     
   path('regist', regist, name='regist'),   
   path('activate/<str:name>/<str:hash>', activate.as_view(), name='activate'), 
]
     