from django.db import models


# Project model:
class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Project'
        ordering = ('title',)

    def __str__(self):
        return f"{self.title}"



# Image upload model:
class Upload(models.Model):
    image = models.ImageField(upload_to='')



# Category model:
class Category(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Category'
        ordering = ('name',)

    def __str__(self):
        return self.name