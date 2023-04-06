from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cport(models.Model):
    cmp=models.TextField()
    img=models.FileField(upload_to="com/",blank=True,null=True)
    email=models.EmailField(max_length=200,null=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.cmp
    
