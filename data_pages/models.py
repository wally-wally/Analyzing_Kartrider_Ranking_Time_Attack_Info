from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class DataPage(models.Model):
    title = models.TextField() # 분석한 데이터 title
    nickname = models.TextField() # 유저의 닉네임
    speed = models.TextField() # 선택한 채널명(S0 = 보통, S1 = 빠름, S2 = 매우빠름, S3 = 가장빠름)
    img_url = models.TextField() # 데이터 이미지 url 경로
    created_at = models.DateTimeField(auto_now_add=True) # 데이터 분석 날짜

    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return f'{self.title} / 채널 : {self.speed}'

    def get_absolute_url(self):
        return reverse("data_pages:storage_detail", kwargs={"datapage_pk": self.pk})