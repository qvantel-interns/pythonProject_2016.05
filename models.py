from django.db import models
class SignUp(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(max_length=20)
