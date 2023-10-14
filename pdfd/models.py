from django.db import models

class notices(models.Model):
    title = models.CharField(max_length=255)
    pdf_content = models.BinaryField()
    downloaded_timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title