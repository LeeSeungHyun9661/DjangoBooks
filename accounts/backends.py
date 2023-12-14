from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class MyUserBackend(ModelBackend):
    def authenticate(self,request, **kwargs):
        name = kwargs.get('name')
        password = kwargs.get('password')
        try:
            user = get_user_model().objects.get(name=name)            
            print(name, " | " , password)
        except Exception as e:
            print(e)
            raise Exception('Wrong Name')
        if user.check_password(password):
            return user
        else:
            raise Exception('Wrong Password')
