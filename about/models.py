from django.db import models


# Company information model:
class CompanyInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    mission_statement = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'CompanyInfo'
        ordering = ('title', )

    def __str__(self):
        return f'{self.title}'



# Teammembers model:
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Teammember'
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}'