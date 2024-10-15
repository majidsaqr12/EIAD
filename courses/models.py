from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, default='MAD')
    course_outline = models.TextField(help_text="Course Outline, separate each item with a newline", null=True, blank=True)
    includes = models.TextField(help_text="This course includes, separate each item with a newline", null=True, blank=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    whatsapp_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"{self.name} - {self.course.title}"