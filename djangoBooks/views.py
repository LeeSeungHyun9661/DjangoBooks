from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# 메인 페이지 뷰 클래스
class mainpage(View):
    context = {}
    template_name = 'mainpage.html'
    def get(self,request):
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)

class search(View):
    context = {}
    template_name = 'search.html'

    def get(self,request):
        page = int(request.GET.get('page', 1)) 
        perpage = int(request.GET.get('perpage',10)) 
        sort = int(request.GET.get('sort', 0)) 
        search_input = request.GET.get('search_input')
        self.context = {
            # "books_list":books_list,
            "perpage":perpage,
            "sort":sort,
            "search_input":search_input,
            # "page_range":page_range
            }
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)