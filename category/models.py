from django.db import models
from audioop import reverse

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length = 40)
    description = models.TextField(max_length = 200, null=True)
    status = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
