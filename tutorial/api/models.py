from django.db import models

# Create your models here.
class UserDetails(models.Model):
    UserID=models.AutoField(unique=True, primary_key=True)
    Username=models.CharField(max_length=100)
    date_added = models.DateField(auto_now = True)
    email_id =models.EmailField()
    password=models.TextField()

    def __str__(self):
        return self.Username