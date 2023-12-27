from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from datetime import datetime
from operator import itemgetter, attrgetter
import operator

# Create your views here.
class books_list(View):
    context = {}
    template_name = 'books_list.html'

    def get(self,request):    
        books = Book.objects.all()
        page = int(request.GET.get('page', 1)) 
        perpage = int(request.GET.get('perpage',10)) 
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
    template_name = 'books_detail.html'

    def get(self,request):         
        # 도서 isbn13 받아오기
        isbn = request.GET.get('isbn')
        print(isbn)
        if isbn :
            if Book.objects.filter(isbn = isbn).exists(): 
                book = Book.objects.get(isbn = isbn) # 도서 객채 추가
                self.context["book"] = book
                return render(request, self.template_name ,self.context)
            else :
            # 도서를 찾을 수 없습니다!
                return redirect("/")
        else :
            return redirect("/")
    def post(self,request):
        return redirect("books:list")
    
# 도서 상세 페이지
class books_author(View):
    context={}
    template_name = 'books_author.html'
    def get(self,request):         
        # 도서 isbn13 받아오기
        author_id = request.GET.get('author_id')
        if author_id :
            self.context = {"author_id":author_id}
            return render(request, self.template_name ,self.context)
        else :
            return redirect("/")
    def post(self,request):
        return redirect("books:list")
    
    
# 도서 상세 페이지
class books_subject(View):
    context={}
    template_name = 'books_subject.html'
    def get(self,request):         
        # 도서 isbn13 받아오기
        subject = request.GET.get('subject')
        if subject :
            self.context = {"subject":subject}
            return render(request, self.template_name ,self.context)
        else :
            return redirect("/")
    def post(self,request):
        return redirect("books:list")
    
  
# 검색 클래스
class books_search(View):
    context = {}
    template_name = 'books_search.html'
    def get(self,request):
        page = int(request.GET.get('page', 1)) 
        perpage = int(request.GET.get('perpage',10)) 
        sort = int(request.GET.get('sort', 0)) 
        mod = int(request.GET.get('mod', 0)) 
        search_input = request.GET.get('search_input')
        applied_subjects = request.GET.getlist('applied_subjects')

        #검색어가 있을 경우 - 해당 검색어로 필터링
        if search_input: 
            books = Book.objects.filter(Q(title__icontains = search_input) | Q(authors__icontains = search_input) | Q(publishers__icontains = search_input))
        else :
            books = Book.objects.all()

        subject_count = {}
        for book in books:
            for subject,subject_name in book.subjects.items():
                if subject_name in subject_count:
                    subject_count[subject_name] = subject_count[subject_name]+1
                else:
                    subject_count[subject_name] = 1
                    
        subject_count = sorted(
            subject_count.items(), 
            key = operator.itemgetter(1), 
            reverse = True
        )

        # Ajax 요청인지 확인
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  
            self.template_name = 'books_search_table.html'
            # 아이템 정렬 기준 선택 
            if sort == 0:
                books = books
            elif sort == 1:
                books = books 
            elif sort == 2:
                books = books
            elif sort == 3:
                books = books
            else :
                books = books   

            if(applied_subjects):
                for book in books:
                    if(not any(item in book.subjects.values() for item in applied_subjects)):
                        books = books.exclude(isbn = book.isbn) 

        paginator = Paginator(books, perpage)
        books_list = paginator.get_page(page)

        left_index = int(page) - 2
        if left_index < 2 :
            left_index=1

        right_index = int(page) + 2
        if right_index > paginator.num_pages :
            right_index = paginator.num_pages
        page_range = range(left_index,right_index+1)

        self.context = {
            "books_list":books_list,
            "perpage":perpage,
            "sort":sort,
            "mod":mod,
            "search_input":search_input,
            "page_range":page_range,
            "count":len(books),
            "subject_count" : subject_count,
        }
        return render(request, self.template_name, self.context)        
    def post(self,request):
        return render(request, self.template_name, self.context)
    