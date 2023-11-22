from django.shortcuts import render,redirect
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

        paginator = Paginator(books, 10)
        # 페이지 선택
        books_list = paginator.get_page(page)
        self.context = {"books_list":books_list}
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)

# 도서 상세 페이지
class books_detail(View):
    context={}
    template_name = 'books_detail_modal.html'

    def get(self,request): 
        
        # 도서 isbn13 받아오기
        SEQ_NO = request.GET.get('SEQ_NO', '') 
        if Book.objects.filter(SEQ_NO = SEQ_NO).exists(): 
            book = Book.objects.get(SEQ_NO = SEQ_NO) # 도서 객채 추가
            self.context["book"] = book

            return render(request, self.template_name ,self.context)
        else:
            # 도서를 찾을 수 없습니다!
            return redirect("books:list"),

    def post(self,request):
        return redirect("books:list")