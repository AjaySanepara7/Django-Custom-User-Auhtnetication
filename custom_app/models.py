from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import BaseUserManager, AbstractUser


class MyUserManager(BaseUserManager):
    def create_user(self, username, password, first_name, last_name, email, date_of_birth, gender, hobby):
    
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender = gender,
            hobby = hobby
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, first_name, last_name, email, date_of_birth, gender, hobby):
        
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            hobby=hobby
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractUser):
    person_gender = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others")
    ]

    hobbies = [
        ("S", "Sports"),
        ("T", "Travelling"),
        ("R", "Reading"),
        ("P", "Painting"),
        ("W", "Writing")
    ]

    gender = models.CharField(max_length=100, choices=person_gender)
    date_of_birth = models.DateField()
    hobby = MultiSelectField(choices=hobbies)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'hobby']

    def __str__(self):
        return self.username