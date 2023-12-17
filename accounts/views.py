import hashlib
import random
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import auth
from django.core.mail import send_mail
from django.views import View
from accounts.forms import LoginForm,RegistForm
from django.contrib.sites.shortcuts  import get_current_site

from accounts.models import User
# Create your views here.

# 회원가입
def regist(request):
    # POST로 접근 : 정상적인 접근
    if request.method == 'POST':
        # 현재 경로값
        path = request.POST.get('path',"")
        # 로그인 되어있는 상태라면 메인 페이지로 돌아감
        if request.user.is_authenticated:
            return redirect('/')    
        else:
            # 회원가입 폼으로부터 값 전달받음
            forms = RegistForm(request.POST) 
            # 회원가입 폼이 올바르다면
            if forms.is_valid():
                user = forms.save(commit=False) 
                user.type = "nomal"   
                if (send_activate_email(request,user)):  
                    user.set_password(forms.password)
                    user.save()     
                    context = {"success":path}
                else:
                    context = {"email":"이메일 전송에 실패했습니다."}
            else:
                context = forms.errors
            return JsonResponse(context)    
    # GET으로 접근 : 비정상적인 접근
    else :
        return redirect('/')    
    

# 로그인
def login(request):
    # POST로 접근 : 정상적인 접근
    if request.method == 'POST':
        # 현재 경로값
        path = request.POST.get('path',"")
         # 로그인 되어있는 상태라면 메인 페이지로 돌아감
        if request.user.is_authenticated:
            return redirect('/')
        else:
             # 로그인 폼으로부터 값 전달받음
            forms = LoginForm(request.POST)
             # 회원가입 폼이 올바르다면
            if forms.is_valid():
                auth.login(request,forms.user)
                context = {"success":path}
            else:
                context = forms.errors
            return JsonResponse(context)
        return redirect('/')
    # GET으로 접근 : 비정상적인 접근
    else :
        return redirect('/')    
    

# 로그아웃
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')


# ____ 계정 활성화 요청 링크 발송 기능  ____
def send_activate_email(request,user):
    user.hash = getHash()
    domain = get_current_site(request).domain #현재 도메인 주소를 받아옴
    email_contents = f"반갑습니다! {user.name}님\n\n아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n회원가입 링크 : http://{domain}/accounts/activate/{user.name}/{user.hash}\n\n감사합니다."            
    mail = send_mail(subject='Bookmmelier Account Check', message=email_contents, from_email='dltmdgus@dippingai.com', recipient_list=[user.email]) #메일 작성 후 발송 실행
    return mail

# 해쉬 생성
def getHash():
    enc = hashlib.md5()      
    enc.update(str(random.randint(1000,10000)).encode('utf-8')) #사용자 이메일의 임의 해시값을 생성함
    hash = enc.hexdigest()
    return hash

# 사용자 계정 활성화
class activate(View):
    context = {}
    template_name = 'activate.html'
    def get(self,request):
        self.context = {'result' : '올바르지 않은 접근입니다.'}
        return render(request,self.template_name,self.context)
    
    def get(self,request,name,hash):
        if not id or not hash :
            self.context = {'result' : '올바르지 않은 접근입니다.'}
        else :            
            # 존재하는 ID일 경우
            if User.objects.filter(name = name).exists():
                user = User.objects.get(name = name) #사용자 정보 확인
                if user.is_active:
                    self.context = {'result' : '이미 활성화된 계정입니다!'}
                else:
                    if user.hash == hash: #사용자의 해시 값이 일치할 경우
                        user.is_active = 1 #사용 가능 계정으로 설정
                        user.save()
                        self.context = {'result' : '계정이 활성화되었습니다! 페이지를 종료해주세요!'}
                    else :
                        self.context = {'result' : '잘못된 활성화 값이 입력되었습니다!'}
            else:
                self.context = {'result' : '존재하지 않는 계정입니다.'}
        return render(request,self.template_name ,self.context)