from django.db import models
from django.utils import  timezone

# Create your models here.
class Post(models.Model):
    # 이건 아직 잘모름 : 다른 모델에 대한 링크라고 한다. DB의 ForeignKey 같음
    author = models.ForeignKey('auth.User')
    # 최대 200자까지
    title = models.CharField(max_length=200)
    text = models.TextField()
    # 디폴트 현재시간으로
    created_date = models.DateTimeField(default=timezone.now)
    # BLANK, NULL 허용
    published_date = models.DateTimeField(blank = True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
