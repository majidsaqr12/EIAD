from django.db import models
from django.utils import timezone


class Program(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/programs/')

    def __str__(self):
        return self.title

class ProgramRegistration(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="registrations")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    whatsapp_number = models.CharField(max_length=15)


    # SEO Fields
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.CharField(max_length=255, null=True, blank=True)
    og_image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    og_type = models.CharField(max_length=50, default='website')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.program.title}'
