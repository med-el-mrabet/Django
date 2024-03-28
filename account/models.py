from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_enseignant= models.BooleanField('Is admin', default=False)
    is_etudiant = models.BooleanField('Is customer', default=False)
    is_entreprise = models.BooleanField('Is employee', default=False)