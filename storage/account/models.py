from django.db import models

# Create your models here.
class UserDetails(models.Model):
    Username=models.TextField()
    UserID=models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    email_id =models.EmailField()
    password=models.TextField()

