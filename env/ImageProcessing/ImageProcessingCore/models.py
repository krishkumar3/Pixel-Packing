from django.db import models
# Create your models here.
class Core(models.Model):
    message = models.TextField(default='')
    inputImage = models.ImageField(upload_to ='uploads/')
    outputImage = models.ImageField(upload_to ='outputs/',default= 'frontend/src/default.jpg')
