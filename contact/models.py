from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact'
        ordering = ('name',)

    def __str__(self):
        return self.name