from django.db import models
from member.models import MemberInfo
# Create your models here.
class Post(models.Model):
    object = models.Manager()
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 20, null=False)
    content = models.TextField(max_length = 1000, null=False)
    user_id = models.name = models.ForeignKey(MemberInfo, on_delete=models.CASCADE, null=False)
    date_time= models.DateTimeField(auto_now=True, null=False)
    num_like = models.IntegerField(default=0)
    num_read = models.IntegerField(default=0)
    num_reply = models.IntegerField(default=0)
    is_blind = models.BooleanField(default = False)
    is_public = models.BooleanField(default = True)
    p_dp = models.FloatField(default = 0)
    a_da = models.FloatField(default = 0)
    temp = models.FloatField(default = 0)
    prob_slang = models.FloatField(default = 0)



def __str__(self):
    return self.id