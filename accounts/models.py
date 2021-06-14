from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from config import settings



#createsuperuser作成時のクラスのオーバーライド
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
 
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザー", max_length=30)
    phone_number = models.CharField(default='電話番号', max_length=11)
    hourly_wage = models.IntegerField(verbose_name='時給', null=True, blank=False)

    def __str__(self):
        return self.username


    
