from django.db import models



class Document(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
