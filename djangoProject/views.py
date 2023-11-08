from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# 메인 페이지 뷰 클래스

def mainpage(request):
   return render(request, "mainpage.html")
