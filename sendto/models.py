from django.db import models

# Create your models here.
class Sendto(models.Model):
    email_to = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)