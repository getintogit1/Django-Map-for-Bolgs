from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None): # we add all our required variables
        if not email:
            raise ValueError("User must have an Email adress")
        if not username:
            raise ValueError("User must have an Username")
        
        user = self.model(
            email = self.normalize_email(email) ,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email) ,
            username = username,
            password = password
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    


class Account(AbstractBaseUser):
    #neccesary variables
    email                   = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
    username                = models.CharField(max_length = 30, unique = True)
    date_joined             = models.DateTimeField(verbose_name = "date_joined", auto_now_add = True)
    last_login              = models.DateTimeField(verbose_name = "last_login", auto_now = True)
    is_admin                = models.BooleanField(default = False)
    is_active               = models.BooleanField(default = True)
    is_staff                = models.BooleanField(default = False)
    is_superuser            = models.BooleanField(default = False)
    #firstname
    #lastname
    #birth

    #whatever you want to be able to login with  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # i wnat to tell my acc obj where the manager is, how to use the manager
    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email

    # these functions are required if you wnat to use a custom user
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label): #they can do stuff if they are admin
        return True

    ### we need to go to settings and set an Porperty "AUTH_USER_MODELL = 'account.Account' " ist overwrites that build in django for default user objects 

# Create your models here.
