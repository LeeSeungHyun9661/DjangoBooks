from django.contrib.auth import authenticate
from django import forms
import re
from accounts.models import User

# 로그인 폼
class LoginForm(forms.Form):
    name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'id':'login_name'}),label="아이디")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'login_password'}),label="비밀번호")
    class Meta:
        model= User
        fields = ['name','password']
    # 로그인 확인
    def clean(self): 
        cleaned_data = super().clean() 
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        try:
            user = authenticate(name = name, password = password)
            if user is not None:             
                if user.is_active:
                    self.user = user
                else:
                    self.add_error('name', '이메일을 통한 인증을 완료해주세요.')
        except Exception as e:
            if e.args[0] == 'Wrong Name':
                self.add_error('name', '존재하지 않는 아이디입니다.')
            elif e.args[0] == 'Wrong Password':
                self.add_error('name', '비밀번호가 일치하지 않습니다.')
            else :
                self.add_error('name',e)

# 회원가입 폼
class RegistForm(forms.ModelForm):
    name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'id':'regist_name'}),label="Name")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'regist_password'}),label="Password")
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={'id':'regist_password_check'}),label="password_check")
    email = forms.CharField(label="Email")
    gender = forms.ChoiceField(label='Gender',widget=forms.RadioSelect,choices=(('M','Male'),('F','Femail')))
    age = forms.IntegerField(label='Age')
    class Meta:
        model= User
        fields = ['name','password','password_check','email','gender','age']

    # 회원가입 확인
    def clean(self): 
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')
        email = cleaned_data.get('email')
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')

        if re.search(r'^[A-Za-z0-9_]{8,20}$',name): 
            if re.search(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$',password):       
                if password == password_check:   
                    if re.search(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
                        if not User.objects.filter(name = name).exists():                      
                            if not User.objects.filter(email = email).exists():                                
                                self.password = password 
                                self.email = email
                                self.name = name
                                self.gender = gender
                                self.age = age
                            else:
                                self.add_error('email','이미 사용중인 이메일입니다.')   
                        else: 
                            self.add_error('name','이미 사용중인 아이디입니다.')
                    else:
                        self.add_error('email','올바른 이메일 주소를 입력해주세요.')
                else:
                    self.add_error('password_check','비밀번호가 일치하지 않습니다.')
            else:
                self.add_error('password','올바른 비밀번호를 입력해주세요. (영문, 숫자, 특수문자 - 8~20자)')
        else:                 
            self.add_error('name','올바른 아이디를 입력해주세요. (영문, 숫자, 언더바, 8~15자)')