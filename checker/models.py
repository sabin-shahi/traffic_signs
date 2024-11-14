from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return False
    
    groups = models.ManyToManyField(Group,
        related_name='custom_user_groups',
        blank=True,
    )


    user_permissions = models.ManyToManyField(Permission,
        related_name='custom_user_permissions',
        blank=True,
    )

    serial_permissions = models.ManyToManyField(Permission,
        related_name='serial_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     def has_perm(self, perm, obj=None):
#         if self.is_superuser:
#             return True
#         return False

#     def has_module_perms(self, app_label):
#         if self.is_superuser:
#             return True
#         return False

# class UserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     website = models.URLField(blank=True)
#     # Add more fields as needed

# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     def has_perm(self, perm, obj=None):
#         if self.is_superuser:
#             return True
#         return False

#     def has_module_perms(self, app_label):
#         if self.is_superuser:
#             return True
#         return False
    
#     groups = models.ManyToManyField(Group,
#         related_name='custom_user_groups',
#         blank=True,
#     )


#     user_permissions = models.ManyToManyField(Permission,
#         related_name='custom_user_permissions',
#         blank=True,
#     )

#     serial_permissions = models.ManyToManyField(Permission,
#         related_name='serial_permissions',
#         blank=True,
#     )
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission

# class CustomUser(AbstractUser):
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     def has_perm(self, perm, obj=None):
#         if self.is_superuser:
#             return True
#         return False

#     def has_module_perms(self, app_label):
#         if self.is_superuser:
#             return True
#         return False
    
#     groups = models.ManyToManyField(Group,
#         related_name='custom_user_groups',
#         blank=True,
#     )


#     user_permissions = models.ManyToManyField(Permission,
#         related_name='custom_user_permissions',
#         blank=True,
#     )

#     serial_permissions = models.ManyToManyField(Permission,
#         related_name='serial_permissions',
#         blank=True,
#     )

#     # Add a foreign key
#     company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.username