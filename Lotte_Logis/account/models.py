from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    permission = models.IntegerField()
    
    def __str__(self):
        result = self.user.username + " - " + self.name
        return result
