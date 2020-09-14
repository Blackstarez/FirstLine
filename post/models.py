from django.db import models
from member.models import MemberInfo
# Create your models here.
class Post(models.Model):
    object = models.Manager()
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 20)
    content = models.TextField(max_length = 1000)
    user_id = models.name = models.ForeignKey(MemberInfo, on_delete=models.CASCADE)
    date_time= models.DateTimeField(auto_now=False)
    num_like = models.IntegerField(max_length = 5)
    num_read = models.IntegerField(max_length = 5)
    num_reply = models.IntegerField(max_length = 5)
    is_blind = models.BooleanField(default = False)
    is_public = models.BooleanField(default = True)
    p_dp = models.FloatField(max_length= 5)
    a_da = models.FloatField(max_length= 5)
    temp = models.FloatField(max_length= 5)
    prob_slang = models.FloatField(max_length= 5)



def __str__(self):
    return self.id