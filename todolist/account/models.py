# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from .managers import CustomUserManager
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("email addres"), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     # date_joined = models.DateTimeField(default=timezone.now)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     is_verified = models.BooleanField(default=False)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     # for manager
#     object = CustomUserManager()
#
#     def __str__(self) -> str:
#         return self.email
#
#
# # create profile models
# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     image_profile = models.ImageField(upload_to="images/profile", null=True, blank=True)
#
#     def __str__(self):
#         return self.user.email
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
