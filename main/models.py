from django.db import models

class NewsletterSubscriber(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__ (self):
        return self.email