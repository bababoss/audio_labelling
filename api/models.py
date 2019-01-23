from django.db import models

# Create your models here.


class MediaFileUpload(models.Model):

    media_file=models.FileField(upload_to='uploaded_media',blank=True,null=True)
    is_label=models.BooleanField(default=False)
    text=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Uploaded media file history'
        verbose_name_plural = 'Uploaded media file history'
        ordering = ['created']

    def __str__(self):
        return 'media_file:  %s ' % (self.media_file)


