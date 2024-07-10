from django.db import models

# Create your models here.

class List(models.Model):
    Title=models.CharField(max_length=50)
    Detail=models.CharField(max_length=200)
    On_Date=models.DateField( auto_now_add=True)

    def __str__(self):
        return self.Title
    