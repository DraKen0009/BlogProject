from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    profile_user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default="default.png",upload_to='profile_pics')
    # profile_image=ResizedImageField(size=[300,300],default='default.png',upload_to='profile_pics')

    def __str__(self):
        return self.profile_user.username

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()  # saving image first

        img = Image.open(self.profile_image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.profile_image.path)  # saving image at the same path

