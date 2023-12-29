from django.urls import path
from .views import *

app_name = "books"

urlpatterns = [
    # path('', list.as_view(), name='list'),
    path('detail',detail.as_view(), name='detail'),    
    path('author', author.as_view(), name='author'),    
    path('subject', subject.as_view(), name='subject'),    
    path('search/book',search_books.as_view(), name='search_books'),  
    path('search/author', search_authors.as_view(), name='search_authors'),  
    path('search/publisher', search_publishers.as_view(), name='search_publishers'), 
    
]
