from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage.as_view(), name='mainpage'),   
    path('search', search.as_view(), name='search'),     
    path('books/', include('books.urls')),
]
