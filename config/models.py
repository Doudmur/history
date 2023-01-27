from django.db import models

class news_list(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

