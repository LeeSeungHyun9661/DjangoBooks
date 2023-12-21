from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DeleteView
from accounts.forms import LoginForm,RegistForm
from books.models import Bestseller,Book, NewRelease
from django.db.models import Q
from django.core.paginator import Paginator
import json

# 메인 페이지 뷰 클래스
class mainpage(View):
    template_name = 'mainpage.html'
    def get(self,request):
        register_form = RegistForm()
        login_form = LoginForm()

        # 베스트셀러 불러오기
        bestsellers = Book.objects.filter(isbn__in=Bestseller.objects.values_list("isbn",flat=True))

        # 새로운 출간 도서 불러오기
        newReleases = Book.objects.filter(isbn__in=NewRelease.objects.values_list("isbn",flat=True))

        self.context = {
            'register_form':register_form,
            'login_form':login_form,
            'bestsellers' : bestsellers,
            'newReleases' : newReleases,
        }
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        return render(request, self.template_name, self.context)