from django.db import models

# Create your models here.
class MemberInfo(models.Model):
    object = models.Manager()
    id = models.CharField(max_length = 20, primary_key = True)
    pw = models.CharField(max_length = 16)
    name = models.CharField(max_length = 10)
    age = models.IntegerField()           
    sex = models.IntegerField()            # 1: 남성 0: 여성
    email = models.CharField(max_length = 30)
    phoneNumber = models.CharField(max_length = 13)
    address = models.CharField(max_length = 100)
    offerInfoAgree = models.IntegerField() # 1: 동의  0: 비동의
    offerInfoAgreeDay = models.CharField(max_length = 14)# 년월일시분초  20201116232211
    creationDate = models.CharField(max_length =14)      # 년월일시분초
    classification = models.IntegerField() # 관리자 회원 구분

def __str__(self):
    return self.id