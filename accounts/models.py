from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    avatar = models.CharField(max_length=20 , verbose_name='Profile Picture' , null=True , blank=True)
    email_active_code = models.CharField(max_length=100 , verbose_name='Email Activation Code')

    def __str__(self) -> str:
        super(User , self).__str__()
        return self.get_full_name()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'