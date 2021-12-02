from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(max_length=500)
    is_responsed = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.email} just sent message with "{self.subject}" subject'
