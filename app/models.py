from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class SUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.CharField(max_length=15,null=True)
    gender= models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.user.username
    
class UploadData(models.Model):
    suser = models.ForeignKey(SUser,on_delete=models.CASCADE)
    file= models.FileField()
    postdate = models.DateField()

class UploadDoc(models.Model):
    suser = models.ForeignKey(SUser,on_delete=models.CASCADE)
    file= models.FileField()
    postdate = models.DateField()