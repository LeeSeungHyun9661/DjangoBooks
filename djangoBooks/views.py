from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from datetime import datetime

class CachingPaginator(Paginator):
    def _get_count(self):

        if not hasattr(self, "_count"):
            self._count = None

        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)

            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)


# Create your views here.
class books_list(View):
    context = {}
    template_name = 'books_list.html'

    def get(self,request):    
        books = Book.objects.all()
        page = int(request.GET.get('page', 1)) 
        perpage = int(request.GET.get('perpage',)) 
        sort = int(request.GET.get('sort', 0)) 
        search_input = request.GET.get('search_input',"")

        # ajax로 통신 : 페이지네이션 또는 검색
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  
            self.template_name = 'books_table.html'
            if search_input != "":
                books = books.filter( Q(TITLE_NM__icontains = search_input) | Q(AUTHR_NM__icontains = search_input) | Q(PUBLISHER_NM__icontains = search_input));
              
            if sort == 0:
                books = books
            elif sort == 1:
                books = books 
            elif sort == 2:
                books = books.order_by('PBLICTE_DE') 
            elif sort == 3:
                books = books.order_by('-PBLICTE_DE') 
            else :
                books = books.order_by('TITLE_NM') 
        # 페이지 선택                
        paginator = CachingPaginator(books, perpage)        
        books_list = paginator.get_page(page)

        left_index = int(page) - 2
        if left_index < 2 :
            left_index=1

        right_index = int(page) + 2
        if right_index > paginator.num_pages :
            right_index = paginator.num_pages

        page_range = range(left_index,right_index+1)

        self.context = {"books_list":books_list,"perpage":perpage,"sort":sort,"search_input":search_input,"page_range":page_range}
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