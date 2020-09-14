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
    prob_p = models.FloatField(default = 0)
    prob_dp = models.FloatField(default = 0)
    prob_n = models.FloatField(default = 0)
    temperature = models.FloatField(default = 0)


def __str__(self):
    return self.id