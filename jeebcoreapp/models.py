from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Core(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'core') #Core belongs to One Owner / on_delete (delete Care belong User)
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='core_logo', blank=False)

    # functin in database
    def __str__(self):
        return self.name
