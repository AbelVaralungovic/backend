from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from ckeditor.fields import RichTextField

def get_default_pisac():
    return get_user_model().objects.first().id

class Objava(models.Model):
    naslov = models.CharField(max_length=50)
    slika = models.ImageField(upload_to='images/', default='/images/default.jpg')
    sadrzaj = models.TextField()
    kreirano = models.TimeField(auto_now_add=True)
    azurirano = models.TimeField(auto_now=True)
    pisac = models.ForeignKey(User, on_delete=models.DO_NOTHING, default = get_default_pisac)

    def __str__(self):
        return self.naslov
    
    class Meta:
        ordering = ['-kreirano']