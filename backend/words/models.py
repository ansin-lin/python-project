from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=128, unique=True)
    meaning = models.CharField(max_length=255)
    example = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
