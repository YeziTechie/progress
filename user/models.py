from django.db.models.functions import Lower
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\-]+$',
        message='Username may contain only letters, numbers, and hyphens (no spaces).'
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )

    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    ELEMENT_CHOICES = [
        ('Fire','Fire'),
        ('Void','Void'),
        ('Tornado','Tornado'),
        ('Lightning','Lightning'),
        ('Volcano','Volcano'),
        ('Earth','Earth'),
        ('Water','Water'),
        ('Air','Air'),
    ]
    ANIMAL_CHOICES = [
        ('Owl','Owl'),
        ('Centipede','Centipede'),
        ('Dragon','Dragon'),
        ('Wolf','Wolf'),
        ('Lion','Lion'),
        ('Eagle','Eagle'),
        ('Butterfly','Butterfly'),
        ('Shark','Shark'),
        ('Jaguar','Jaguar'),
        ('Ant','Ant'),
    ]

    element = models.CharField(max_length=10, choices=ELEMENT_CHOICES, blank=True, null=True)
    animal = models.CharField(max_length=10, choices=ANIMAL_CHOICES, blank=True, null=True)

    def clean(self):
        super().clean()
        if User.objects.exclude(pk=self.pk).filter(username__iexact=self.username).exists():
            raise ValidationError({'username': 'A user with that username already exists (case-insensitive).'})

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('username'),
                name='unique_username_case_insensitive'
            )
        ]


