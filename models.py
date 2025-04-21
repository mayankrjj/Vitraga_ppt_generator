from django.db import models

class Presentation(models.Model):
    topic = models.CharField(max_length=255)
    slide_count = models.IntegerField()
    pptx_file = models.FileField(upload_to='presentations/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
