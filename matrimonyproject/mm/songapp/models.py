from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Song(models.Model):
    title=models.TextField()
    artist=models.TextField()
    image=models.ImageField(upload_to ='uploads/')
    audio_file=models.FileField(blank=True,null=True,upload_to='media/')
    duration=models.CharField(max_length=20)

    def __str__(self):
        return self.title
class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False,null=True)


