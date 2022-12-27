from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    address=models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    image = models.FileField(upload_to= 'uploads/%Y/%m/%d',null=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        abstract = True


