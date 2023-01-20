from django.db import models

# Create your models here.


class Privacy(models.Model):
    """
    Create privacy policy
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    privacy_policy = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
