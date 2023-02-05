from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='default.png', upload_to='Profile_images')

    def __str__(self):
        return f'{self.user.username}-Profile'


