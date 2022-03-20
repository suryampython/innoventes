from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
from django.utils import timezone

class Company(models.Model):
    CompanyName=models.CharField(blank=False,validators=[MinLengthValidator(5)], max_length=100)
    emailId=models.EmailField(blank=False,max_length=100)
    alpha = RegexValidator(r'[a-zA-Z]{2}[0-9]{2}(N|E)', 'Length should be 5 characters \n1st & 2nd characters should be alphabets \n3rd & 4th characters should be numbers \n5th character should be E or N')
    CompanyCode=models.CharField(unique=True,blank=True,validators=[MinLengthValidator(5),alpha],max_length=5)
    Strength=models.PositiveIntegerField(blank=True)
    webSite=models.URLField(blank=True)
    createdTime = models.DateTimeField(default=timezone.now)

