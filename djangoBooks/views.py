from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator

# Create your views here.
class books_list(View):
    context = {}
    template_name = 'books_list.html'

    def get(self,request):    
        books = Book.objects.all()
        page = int(request.GET.get('page', 1)) 

        # ajax로 통신 : 페이지네이션 또는 검색
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            self.template_name = 'books_table.html'

        paginator = Paginator(books, 5)
        # 페이지 선택
        books_list = paginator.get_page(page)
        self.context = {"books_list":books_list}
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)

# 도서 상세 페이지
class books_detail(View):
    context = {}
    template_name = 'books_detail.html'

    def get(self,request): 
        return render(request, self.template_name, self.context)

    def post(self,request):
        return render(request, self.template_name, self.context)