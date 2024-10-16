from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
    
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    course_outline = models.TextField(help_text="Course Outline, separate each item with a newline", null=True, blank=True)
    includes = models.TextField(help_text="This course includes, separate each item with a newline", null=True, blank=True)

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
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])


class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    whatsapp_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.course.title}"