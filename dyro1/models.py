from django.db import models

# Create your models here.
class Contact(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name