from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=100)
    song_durection=models.IntegerField()

def get(self):
    return ','.join([str(i) for i in self.user.all()])