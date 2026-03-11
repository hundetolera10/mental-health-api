from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    AGE_GROUP_CHOICES = [
        ("teen", "Teen"),
        ("young_adult", "Young Adult"),
        ("adult", "Adult"),
    ]
    age = models.IntegerField(blank=True, null=True)
    age_group = models.CharField(
        max_length=20, 
        choices=AGE_GROUP_CHOICES,
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        if self.age is not None:
            if self.age < 18:
                self.age_group = "teen"
            elif 18 <= self.age < 30:
                self.age_group = "young_adult"
            else:
                self.age_group = "adult"
        super().save(*args, **kwargs)
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username