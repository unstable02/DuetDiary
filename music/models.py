from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to="songs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
