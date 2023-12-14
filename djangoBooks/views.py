from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DeleteView
from accounts.forms import LoginForm,RegistForm


# 메인 페이지 뷰 클래스
class mainpage(View):
    template_name = 'mainpage.html'
    def get(self,request):
        register_form = RegistForm()
        login_form = LoginForm()
        self.context = {
            'register_form':register_form,
            'login_form':login_form
        }
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)
    
# 검색 클래스
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