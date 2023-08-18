from django.db import models

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.title
