from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


# Post --> Django Model (models.Model)
class Post(models.Model):
    # ForeignKey --> links to another Model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # CharField --> text w/ limited number of characters
    title = models.CharField(max_length=200)

    # TextField --> text w/ unlimited number of characters
    text = models.TextField()

    # DateTimeField --> date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
