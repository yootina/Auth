from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 1. 유저 모델을 참조하는 경우 (권장x)
    # user = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 2. settings.AUTH_USER_MODEL == 'accounts.User' 권장(o)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 3. 권장(o)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # comment_set = 장고가 자동으로 추가해주는 컬럼
    # user_id = 장고가 자동으로 추가해주는 컬럼


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 장고가 자동으로 추가해주는 컬럼
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id = 장고가 자동으로 추가해주는 컬럼