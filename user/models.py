from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum

class User(AbstractUser):
    # keep username as the identifier; no email required
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    ELEMENT_CHOICES = [
        ('fire','Fire'),
        ('water','Water'),
        ('earth','Earth'),
        ('air','Air'),
    ]
    ANIMAL_CHOICES = [
        ('owl','Owl'),
        ('centipede','Centipede'),
        ('dragon','Dragon'),
        ('wolf','Wolf'),
        ('lion','Lion'),
        ('eagle','Eagle'),
        ('butterfly','Butterfly'),
        ('shark','Shark'),
        ('jaguar','Jaguar'),
        ('ant','Ant'),
    ]

    element = models.CharField(max_length=10, choices=ELEMENT_CHOICES, blank=True, null=True)
    animal = models.CharField(max_length=10, choices=ANIMAL_CHOICES, blank=True, null=True)