from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# django는 기본적으로 admin페이지에 로그인 하기 위해 기본적으로 User모델을 사용하고 있기 때문에
# 사용자 정의 User모델로 대체를 해야된다.
# AUTH_USER_MODEL = "myapp.MyUser"

class User(AbstractUser):
    pass
    # article_set = 장고가 자동으로 추가해주는 컬럼
    # comment_set = 장고가 자동으로 추가해주는 컬럼