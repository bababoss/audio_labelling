from django.db import models

# Create your models here.


class Audio(models.Model):
     audio_file= models.FileField(max_length=200)
    
    pub_date = models.DateTimeField('date published')


